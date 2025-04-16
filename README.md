# 🧪 log-analyzer-python

This is a beginner-friendly cybersecurity lab that simulates log file triage for brute-force detection.  
It parses a fake log and alerts when suspicious login failures are detected.

## 🔍 Skills Practiced:
- Python scripting
- Regex filtering
- Basic detection logic

## 🧠 How it Works:
The script looks through `logfile.txt` and finds any lines that contain "failed login".  
If found, it flags the line as suspicious activity.

## 🚀 To Run (Locally):
1. Save the files to a folder  
2. Open terminal or command prompt  
3. Run: `python log_parser.py`

## 🆕 Additional Scripts:
- `log_brute_force_detector.py`: Flags IPs with 3+ failed logins and writes alerts to a file (`alerts.txt`)
