#!/usr/bin/env bash
#
# ws01_debug_playbook.sh
#
# A documented command playbook for:
#   Google Project 6 – Debugging a Cloud Web Server (ws01)
#
# NOTE:
# - This is **not** meant to be fully automated.
# - It captures the main commands & reasoning steps used during the lab.
#

echo "=== 1) Check Apache status ==="
echo "sudo systemctl status apache2"
# Look for:
#  - Active: failed
#  - Errors like: Address already in use, could not bind to address [::]:80

echo
echo "=== 2) Try restarting Apache (to confirm failure) ==="
echo "sudo systemctl restart apache2"
echo "# If this fails, re-check status:"
echo "sudo systemctl status apache2"

echo
echo "=== 3) Check which process is using port 80 ==="
echo "sudo netstat -nlp | grep ':80 '"
# Example output:
# tcp 0 0 0.0.0.0:80 0.0.0.0:* LISTEN 1356/python3

echo
echo "=== 4) Identify the python3 process ==="
echo "ps -ax | grep python3"
# Look for the PID that matches the one shown in netstat.
# Example:
# 1371 ? Ss 0:00 python3 /usr/local/bin/jimmytest.py

echo
echo "=== 5) Inspect the offending script (jimmytest.py) ==="
echo "sudo cat /usr/local/bin/jimmytest.py"
# Confirm this is a developer test script and not a production component.

echo
echo "=== 6) Kill the current process (temporary fix) ==="
echo "sudo kill <PID_FROM_NETSTAT>"
echo "ps -ax | grep python3"
# If it respawns with a new PID, it is likely started by a systemd service.

echo
echo "=== 7) Look for a related systemd service (e.g., jimmytest.service) ==="
echo "sudo systemctl --type=service | grep jimmy"
# Example:
# jimmytest.service loaded active running Jimmy python test service

echo
echo "=== 8) Stop and disable the rogue service ==="
echo "sudo systemctl stop jimmytest"
echo "sudo systemctl disable jimmytest"

echo
echo "=== 9) Confirm nothing is listening on port 80 now ==="
echo "sudo netstat -nlp | grep ':80 ' || echo 'No process on port 80'"

echo
echo "=== 10) Start Apache and verify ==="
echo "sudo systemctl start apache2"
echo "sudo systemctl status apache2"
echo "# Then refresh the website in the browser – it should show the Apache default page."
