#!/usr/bin/env python3
import re

def parse_log(file_path):
    with open(file_path, "r") as f:
        logs = f.readlines()
    errors = [line for line in logs if "error" in line.lower()]
    return errors

if __name__ == "__main__":
    errors = parse_log("/var/log/syslog")
    print(f"Found {len(errors)} errors")
