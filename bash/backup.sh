#!/bin/bash
# Backup /etc to ~/backups
DEST=~/backups/etc-$(date +%F).tar.gz
mkdir -p ~/backups
tar -czf $DEST /etc
echo "Backup saved to $DEST"
