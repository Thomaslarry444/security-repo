#!/usr/bin/env python3
import argparse
import json
import re
import subprocess
from collections import Counter, defaultdict
from datetime import datetime, UTC
from pathlib import Path


BEACON_RE = re.compile(r"Beacon \((.*?)\).*(?:CH:\s*(\d+))?")
PROBE_RESP_RE = re.compile(r"Probe Response \((.*?)\).*(?:CH:\s*(\d+))?")
SSID_IN_PARENS_RE = re.compile(r"\((.*?)\)")


def run_tcpdump_read(pcap_path: str):
    cmd = ["tcpdump", "-r", pcap_path, "-nn"]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode not in (0, 1):
        raise RuntimeError(proc.stderr.strip() or "tcpdump failed")
    return proc.stdout.splitlines()


def main():
    parser = argparse.ArgumentParser(description="Summarize WLAN capture defensively")
    parser.add_argument("--pcap", required=True, help="Path to capture file")
    parser.add_argument("--out", default=None, help="Optional JSON output path")
    args = parser.parse_args()

    pcap = Path(args.pcap)
    if not pcap.exists():
        raise FileNotFoundError(f"PCAP not found: {pcap}")

    lines = run_tcpdump_read(str(pcap))

    counts = Counter()
    ssid_counts = Counter()
    channel_counts = Counter()
    examples = defaultdict(list)

    for idx, line in enumerate(lines, start=1):
        low = line.lower()

        if "beacon" in low:
            counts["beacon"] += 1
            m = BEACON_RE.search(line)
            if m:
                ssid = m.group(1).strip()
                ch = m.group(2)
                if ssid:
                    ssid_counts[ssid] += 1
                    if len(examples["beacon"]) < 5:
                        examples["beacon"].append({"line": idx, "text": line.strip()})
                if ch:
                    channel_counts[ch] += 1

        if "probe response" in low:
            counts["probe_response"] += 1
            m = PROBE_RESP_RE.search(line)
            if m:
                ssid = m.group(1).strip()
                ch = m.group(2)
                if ssid:
                    ssid_counts[ssid] += 1
                if ch:
                    channel_counts[ch] += 1
            if len(examples["probe_response"]) < 5:
                examples["probe_response"].append({"line": idx, "text": line.strip()})

        if "deauth" in low or "deauthentication" in low:
            counts["deauth"] += 1
            if len(examples["deauth"]) < 5:
                examples["deauth"].append({"line": idx, "text": line.strip()})

        if "disassoc" in low or "disassociation" in low:
            counts["disassoc"] += 1
            if len(examples["disassoc"]) < 5:
                examples["disassoc"].append({"line": idx, "text": line.strip()})

        if "auth" in low and "fail" in low:
            counts["auth_fail"] += 1
            if len(examples["auth_fail"]) < 5:
                examples["auth_fail"].append({"line": idx, "text": line.strip()})

    result = {
        "timestamp_utc": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
        "pcap": str(pcap),
        "summary": {
            "total_lines": len(lines),
            "beacon": counts["beacon"],
            "probe_response": counts["probe_response"],
            "deauth": counts["deauth"],
            "disassoc": counts["disassoc"],
            "auth_fail": counts["auth_fail"],
        },
        "top_ssids": ssid_counts.most_common(10),
        "top_channels": channel_counts.most_common(10),
        "examples": examples,
        "notes": [
            "This script is for defensive lab analysis only.",
            "Review counts for unusual management-frame activity.",
        ],
    }

    output = json.dumps(result, indent=2)

    if args.out:
        Path(args.out).write_text(output + "\n", encoding="utf-8")
    else:
        print(output)


if __name__ == "__main__":
    main()