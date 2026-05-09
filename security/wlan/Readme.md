# WLAN Defensive Security Lab (Authorized Use Only)

This project is for **defensive wireless security testing in an isolated, authorized lab**.

## Purpose
- Build a repeatable WLAN lab
- Audit AP configuration against a baseline
- Parse logs for suspicious events
- Generate scheduled security reports

## Raspberry Pi Role
A Raspberry Pi can serve as:
1. **Log collector** (syslog target)
2. **Script runner** (cron jobs for audits)
3. **Lightweight monitoring node** for WLAN-related telemetry

## Directory Layout
- `docs/` → topology, hardening checklist, runbook
- `data/samples/` → sample logs and config files
- `scripts/` → Python/Bash tooling
- `reports/` → generated audit reports

## Quick Start
1. Place AP config export (JSON) at `data/samples/ap_config.json`
2. Place AP/syslog sample at `data/samples/ap_logs_sample.log`
3. Run:
   - `python3 scripts/check_ap_config.py --config data/samples/ap_config.json`
   - `python3 scripts/parse_wifi_logs.py --log data/samples/ap_logs_sample.log`
   - `bash scripts/wifi_baseline_audit.sh`