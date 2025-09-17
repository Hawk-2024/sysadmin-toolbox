#!/bin/bash
echo "User Accounts Report"
echo "---------------------"
awk -F: '{ print $1 " -> " $6 }' /etc/passwd
