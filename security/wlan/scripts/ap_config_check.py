#!/usr/bin/env python3
import argparse
import json
from datetime import datetime

BASELINE_RULES = {
    "wpa_mode": ["WPA3", "WPA2-AES"],
    "wps_enabled": [False],
    "firmware_up_to_date": [True],
    "passphrase_min_length": 16,
    "default_admin_changed": [True],
}

def evaluate_config(cfg):
    results = []

    # Rule: WPA mode
    wpa_mode = cfg.get("wpa_mode")
    pass_rule = wpa_mode in BASELINE_RULES["wpa_mode"]
    results.append({
        "rule": "wpa_mode_allowed",
        "status": "PASS" if pass_rule else "FAIL",
        "actual": wpa_mode,
        "expected": BASELINE_RULES["wpa_mode"],
        "remediation": "Use WPA3 or WPA2-AES only."
    })

    # Rule: WPS disabled
    wps_enabled = cfg.get("wps_enabled")
    pass_rule = wps_enabled in BASELINE_RULES["wps_enabled"]
    results.append({
        "rule": "wps_disabled",
        "status": "PASS" if pass_rule else "FAIL",
        "actual": wps_enabled,
        "expected": BASELINE_RULES["wps_enabled"],
        "remediation": "Disable WPS."
    })

    # Rule: Firmware current
    fw = cfg.get("firmware_up_to_date")
    pass_rule = fw in BASELINE_RULES["firmware_up_to_date"]
    results.append({
        "rule": "firmware_up_to_date",
        "status": "PASS" if pass_rule else "FAIL",
        "actual": fw,
        "expected": BASELINE_RULES["firmware_up_to_date"],
        "remediation": "Update AP firmware to latest stable release."
    })

    # Rule: Passphrase length
    passphrase = cfg.get("wifi_passphrase", "")
    pass_rule = isinstance(passphrase, str) and len(passphrase) >= BASELINE_RULES["passphrase_min_length"]
    results.append({
        "rule": "passphrase_length",
        "status": "PASS" if pass_rule else "FAIL",
        "actual": len(passphrase) if isinstance(passphrase, str) else None,
        "expected": f">= {BASELINE_RULES['passphrase_min_length']}",
        "remediation": "Use a passphrase with at least 16 characters."
    })

    # Rule: Default admin changed
    admin_changed = cfg.get("default_admin_changed")
    pass_rule = admin_changed in BASELINE_RULES["default_admin_changed"]
    results.append({
        "rule": "default_admin_changed",
        "status": "PASS" if pass_rule else "FAIL",
        "actual": admin_changed,
        "expected": BASELINE_RULES["default_admin_changed"],
        "remediation": "Change default admin credentials."
    })

    return results

def summarize(results):
    total = len(results)
    passed = sum(1 for r in results if r["status"] == "PASS")
    failed = total - passed
    compliance = round((passed / total) * 100, 2) if total else 0.0
    return {"total": total, "passed": passed, "failed": failed, "compliance_percent": compliance}

def main():
    parser = argparse.ArgumentParser(description="Check AP config against WLAN baseline.")
    parser.add_argument("--config", required=True, help="Path to AP config JSON")
    parser.add_argument("--output", default="", help="Optional output JSON report path")
    args = parser.parse_args()

    with open(args.config, "r", encoding="utf-8") as f:
        cfg = json.load(f)

    results = evaluate_config(cfg)
    summary = summarize(results)

    report = {
        "timestamp_utc": datetime.utcnow().isoformat() + "Z",
        "summary": summary,
        "results": results
    }

    print(json.dumps(report, indent=2))

    if args.output:
        with open(args.output, "w", encoding="utf-8") as out:
            json.dump(report, out, indent=2)
        print(f"\nSaved report to: {args.output}")

if __name__ == "__main__":
    main()