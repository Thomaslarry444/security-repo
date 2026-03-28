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

cat > "$MD_REPORT" <<EOF
# WLAN Audit Summary ($TS)

## Generated Reports
- Config audit JSON: \`$(basename "$CFG_REPORT")\`
- Log audit JSON: \`$(basename "$LOG_REPORT")\`

## Next Steps
1. Review failed baseline checks in config audit.
2. Review alert thresholds and flagged log examples.
3. Create remediation tasks and re-run audit.
EOF

echo "Audit complete."
echo "Config report: $CFG_REPORT"
echo "Log report:    $LOG_REPORT"
echo "Summary:       $MD_REPORT"