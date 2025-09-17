### 📄 python/disk_monitor.py

#!/usr/bin/env python3
import shutil
import sys

def check_disk_usage(path="/", threshold=80):
    total, used, free = shutil.disk_usage(path)
    percent_used = (used / total) * 100
    if percent_used > threshold:
        print(f"WARNING: Disk usage at {percent_used:.2f}%")
        sys.exit(1)
    else:
        print(f"OK: Disk usage at {percent_used:.2f}%")
        sys.exit(0)

if __name__ == "__main__":
    check_disk_usage()
