#!/bin/bash
# OpenClaw Daily State Sync Script
# Runs daily at midnight to update system-state

WORKSPACE="/home/itsaslamautomations/.openclaw/workspace/Daily-Working-Space"
DATE=$(date +%Y-%m-%d)

echo "=== OpenClaw Daily State Sync - $DATE ==="

# Navigate to workspace
cd "$WORKSPACE" || exit 1

# Pull latest from remote
echo "Pulling latest..."
git pull origin main

# Update daily-state.json with today's date
echo "Updating today's updates..."
jq --arg date "$DATE" '.todaysUpdates.date = $date' system-state/daily-state.json > system-state/daily-state.tmp.json
mv system-state/daily-state.tmp.json system-state/daily-state.json

# Add new entries to today's updates
echo "Checking for new implementations..."

# Commit and push
echo "Committing changes..."
git add system-state/
git commit -m "Daily state sync - $DATE" || echo "No changes to commit"
git push origin main

echo "=== Sync Complete ==="
