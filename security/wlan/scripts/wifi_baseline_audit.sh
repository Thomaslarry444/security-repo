#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPTS_DIR="$ROOT_DIR/scripts"
DATA_DIR="$ROOT_DIR/data/samples"
REPORTS_DIR="$ROOT_DIR/reports"

mkdir -p "$REPORTS_DIR"

TS="$(date -u +"%Y%m%dT%H%M%SZ")"
CFG_REPORT="$REPORTS_DIR/ap_config_audit_${TS}.json"
LOG_REPORT="$REPORTS_DIR/wifi_log_audit_${TS}.json"
MD_REPORT="$REPORTS_DIR/audit_summary_${TS}.md"

CONFIG_FILE="$DATA_DIR/ap_config.json"
LOG_FILE="$DATA_DIR/ap_logs_sample.log"

if [[ ! -f "$CONFIG_FILE" ]]; then
  echo "Missing config file: $CONFIG_FILE"
  exit 1
fi

if [[ ! -f "$LOG_FILE" ]]; then
  echo "Missing log file: $LOG_FILE"
  exit 1
fi

python3 "$SCRIPTS_DIR/check_ap_config.py" \
  --config "$CONFIG_FILE" \
  --output "$CFG_REPORT" >/dev/null

python3 "$SCRIPTS_DIR/parse_wifi_logs.py" \
  --log "$LOG_FILE" \
  --output "$LOG_REPORT" >/dev/null

# NEUE ERWEITERUNG: Live-Scan des Heimrouters
ROUTER_IP="10.10.87.1"  # Anpassen an Ihre Router-IP
WLAN_INTERFACE="wlan0"   # Anpassen an Ihr WLAN-Interface (prüfen mit 'iwconfig')
SCAN_REPORT="$REPORTS_DIR/live_scan_${TS}.txt"

echo "Starting live scan of router: $ROUTER_IP"
echo "Live Scan Report ($TS)" > "$SCAN_REPORT"

# 1. Nmap-Scan für offene Ports und Dienste
echo "=== Nmap Port Scan ===" >> "$SCAN_REPORT"
sudo nmap -sV -p- "$ROUTER_IP" >> "$SCAN_REPORT" 2>&1

# 2. WLAN-Scan mit airodump-ng (falls verfügbar, z.B. in Kali)
if command -v airodump-ng >/dev/null 2>&1; then
  echo "=== WLAN Scan ===" >> "$SCAN_REPORT"
  sudo airodump-ng --output-format csv -w /tmp/wlan_scan "$WLAN_INTERFACE" &
  SCAN_PID=$!
  sleep 15  # 15-Sekunden-Scan
  kill "$SCAN_PID" 2>/dev/null || true
  cat /tmp/wlan_scan-01.csv >> "$SCAN_REPORT" 2>/dev/null || echo "No WLAN data captured" >> "$SCAN_REPORT"
  rm -f /tmp/wlan_scan*
else
  echo "airodump-ng not found; install for WLAN scans (e.g., via apt in Kali)" >> "$SCAN_REPORT"
fi

# 3. Einfache Schwachstellen-Prüfung (z.B. auf veraltete Firmware)
echo "=== Basic Vulnerability Check ===" >> "$SCAN_REPORT"
ROUTER_MODEL=$(curl -s "http://$ROUTER_IP" | grep -i "model\|version" | head -1 || echo "Unknown")
echo "Router model/version: $ROUTER_MODEL" >> "$SCAN_REPORT"
if echo "$ROUTER_MODEL" | grep -qi "old\|wep\|wpa1"; then
  echo "WARNING: Potential weak encryption or outdated firmware detected." >> "$SCAN_REPORT"
fi

cat > "$MD_REPORT" <<EOF
# WLAN Audit Summary ($TS)

## Generated Reports
- Config audit JSON: \`$(basename "$CFG_REPORT")\`
- Log audit JSON: \`$(basename "$LOG_REPORT")\`
- Live scan TXT: \`$(basename "$SCAN_REPORT")\`

## Key Findings and Improvements
- **Ports/Services:** Review open ports in live scan (z.B. schließe unnötige wie Telnet/HTTP).
- **WLAN:** Prüfe Verschlüsselung (sollte WPA3 sein); aktiviere MAC-Filter, deaktiviere WPS.
- **Firmware:** Aktualisiere auf neueste Version; prüfe auf bekannte CVEs (z.B. via CVE-Datenbank).
- **Allgemein:** Verwende starke Passwörter (>12 Zeichen), aktiviere Firewall, segmentiere Netzwerk (Guest-WLAN).

## Next Steps
1. Review failed baseline checks in config audit.
2. Review alert thresholds and flagged log examples.
3. Create remediation tasks and re-run audit.
EOF

echo "Audit complete."
echo "Config report: $CFG_REPORT"
echo "Log report:    $LOG_REPORT"
echo "Live scan:     $SCAN_REPORT"
echo "Summary:       $MD_REPORT"