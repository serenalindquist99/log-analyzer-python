import re
from collections import defaultdict

# Dictionary to count failed logins by IP
failed_logins = defaultdict(int)

# Open and read log file
with open("logfile.txt", "r") as log:
    for line in log:
        # Search for failed login
        if re.search(r"failed login", line, re.IGNORECASE):
            # Extract the IP address at the end of the line
            ip_match = re.search(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", line)
            if ip_match:
                ip = ip_match.group()
                failed_logins[ip] += 1

# Write alerts to a file
with open("alerts.txt", "w") as alert_file:
    for ip, count in failed_logins.items():
        if count >= 3:
            alert = f"[ALERT] Brute-force suspected from {ip} - {count} failed attempts"
            print(alert)
            alert_file.write(alert + "\n")
