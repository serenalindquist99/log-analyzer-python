import re

with open("logfile.txt", "r") as log:
    for line in log:
        if re.search(r"failed login", line, re.IGNORECASE):
            print("[ALERT] Suspicious Activity Detected: ", line.strip())
