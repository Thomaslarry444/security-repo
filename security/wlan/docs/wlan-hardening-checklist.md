# WLAN Hardening Checklist (Baseline)

## Encryption & Auth
- [ ] WPA3 enabled where supported
- [ ] Else WPA2-AES only (no TKIP)
- [ ] Strong passphrase (>= 16 chars)
- [ ] Default credentials changed

## Unsafe Features
- [ ] WPS disabled
- [ ] Remote admin disabled (or restricted)
- [ ] UPnP disabled (if not required)

## Network Segmentation
- [ ] Guest network isolated from internal LAN
- [ ] Management interface restricted (allowlist/VLAN)

## RF/Operational
- [ ] Firmware up to date
- [ ] Unused SSIDs disabled
- [ ] SSID naming avoids sensitive identifiers

## Logging & Monitoring
- [ ] Syslog enabled and forwarded to collector (Raspberry Pi)
- [ ] Time sync configured (NTP)
- [ ] Authentication/deauthentication events logged