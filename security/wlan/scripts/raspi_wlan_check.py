#!/usr/bin/env python3
import argparse
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

def run(cmd):
    p = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    return p.returncode, p.stdout.strip(), p.stderr.strip()

def parse_link(output):
    data = {"connected": False}
    if "Not connected." in output:
        return data
    data["connected"] = True
    m = re.search(r"Connected to ([0-9a-f:]{17})", output, re.I)
    if m: data["bssid"] = m.group(1).upper()
    m = re.search(r"SSID: (.+)", output)
    if m: data["ssid"] = m.group(1).strip()
    m = re.search(r"freq: (\d+)", output)
    if m: data["freq_mhz"] = int(m.group(1))
    m = re.search(r"signal: (-?\d+) dBm", output)
    if m: data["signal_dbm"] = int(m.group(1))
    return data

def ping_ok(target):
    rc, _, _ = run(f"ping -c 1 -W 2 {target}")
    return rc == 0

def status_for(link, args):
    checks = []
    if not link.get("connected"):
        checks.append(("FAIL", "WLAN nicht verbunden"))
        return checks

    if args.expected_ssid and link.get("ssid") != args.expected_ssid:
        checks.append(("WARN", f"SSID abweichend: {link.get('ssid')} != {args.expected_ssid}"))
    else:
        checks.append(("PASS", f"SSID: {link.get('ssid', 'unbekannt')}"))

    if args.expected_bssid and link.get("bssid") != args.expected_bssid.upper():
        checks.append(("WARN", f"BSSID abweichend: {link.get('bssid')} != {args.expected_bssid.upper()}"))
    else:
        checks.append(("PASS", f"BSSID: {link.get('bssid', 'unbekannt')}"))

    sig = link.get("signal_dbm")
    if sig is None:
        checks.append(("WARN", "Signal unbekannt"))
    elif sig < args.min_signal_dbm:
        checks.append(("WARN", f"Schwaches Signal: {sig} dBm (< {args.min_signal_dbm} dBm)"))
    else:
        checks.append(("PASS", f"Signal: {sig} dBm"))

    if ping_ok(args.gateway):
        checks.append(("PASS", f"Gateway erreichbar: {args.gateway}"))
    else:
        checks.append(("FAIL", f"Gateway nicht erreichbar: {args.gateway}"))

    if ping_ok(args.internet_host):
        checks.append(("PASS", f"Internet erreichbar: {args.internet_host}"))
    else:
        checks.append(("WARN", f"Internet nicht erreichbar: {args.internet_host}"))

    return checks

def main():
    parser = argparse.ArgumentParser(description="Raspberry Pi WLAN Health Check")
    parser.add_argument("--iface", default="wlan0")
    parser.add_argument("--expected-ssid", default="")
    parser.add_argument("--expected-bssid", default="")
    parser.add_argument("--min-signal-dbm", type=int, default=-67)
    parser.add_argument("--gateway", default="192.168.1.1")
    parser.add_argument("--internet-host", default="1.1.1.1")
    parser.add_argument("--output", default="reports/raspi_wlan_check.json")
    args = parser.parse_args()

    rc, out, err = run(f"iw dev {args.iface} link")
    if rc != 0:
        result = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "iface": args.iface,
            "error": f"'iw' fehlgeschlagen: {err or out}",
            "checks": [["FAIL", "Interface-Check fehlgeschlagen"]]
        }
    else:
        link = parse_link(out)
        checks = status_for(link, args)
        result = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "iface": args.iface,
            "link": link,
            "checks": checks,
            "summary": {
                "pass": sum(1 for s, _ in checks if s == "PASS"),
                "warn": sum(1 for s, _ in checks if s == "WARN"),
                "fail": sum(1 for s, _ in checks if s == "FAIL"),
            }
        }

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()