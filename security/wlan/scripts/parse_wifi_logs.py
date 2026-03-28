#!/usr/bin/env python3
import argparse
import json
import re
from collections import Counter
from datetime import datetime

PATTERNS = {
    "deauth": re.compile(r"deauth|de-auth|disassoc", re.IGNORECASE),
    "auth_fail": re.compile(r"auth.*fail|failed authentication|invalid password", re.IGNORECASE),
    "rogue_indicator": re.compile(r"unknown bssid|rogue ap|evil twin", re.IGNORECASE),
}

def parse_log(path):
    counts = Counter()
    flagged_lines = {k: [] for k in PATTERNS.keys()}

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for idx, line in enumerate(f, start=1):
            for name, pattern in PATTERNS.items():
                if pattern.search(line):
                    counts[name] += 1
                    if len(flagged_lines[name]) < 20:
                        flagged_lines[name].append({"line": idx, "text": line.strip()})

    return counts, flagged_lines

def main():
    parser = argparse.ArgumentParser(description="Parse WLAN/AP logs for suspicious indicators.")
    parser.add_argument("--log", required=True, help="Path to log file")
    parser.add_argument("--deauth-threshold", type=int, default=10)
    parser.add_argument("--authfail-threshold", type=int, default=15)
    parser.add_argument("--output", default="", help="Optional output JSON report path")
    args = parser.parse_args()

    counts, flagged = parse_log(args.log)

    alerts = []
    if counts["deauth"] >= args.deauth_threshold:
        alerts.append(f"High deauth/disassoc volume: {counts['deauth']} (threshold {args.deauth_threshold})")
    if counts["auth_fail"] >= args.authfail_threshold:
        alerts.append(f"High auth failure volume: {counts['auth_fail']} (threshold {args.authfail_threshold})")
    if counts["rogue_indicator"] > 0:
        alerts.append(f"Rogue AP indicator occurrences: {counts['rogue_indicator']}")

    report = {
        "timestamp_utc": datetime.utcnow().isoformat() + "Z",
        "counts": dict(counts),
        "alerts": alerts,
        "flagged_examples": flagged,
    }

    print(json.dumps(report, indent=2))

    if args.output:
        with open(args.output, "w", encoding="utf-8") as out:
            json.dump(report, out, indent=2)
        print(f"\nSaved report to: {args.output}")

if __name__ == "__main__":
    main()