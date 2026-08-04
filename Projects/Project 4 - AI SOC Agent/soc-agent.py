#!/usr/bin/env python3
import os
import requests
import sys
import subprocess  # Added for automation

# 1. Fetch the Gemini API Key
API_KEY = os.environ.get('GEMINI_API_KEY')
if not API_KEY:
    print("❌ Error: GEMINI_API_KEY environment variable is not set!")
    sys.exit(1)

# 2. Safely load the playbook
try:
    with open('playbook.txt', 'r') as f:
        playbook = f.read()
except FileNotFoundError:
    print("❌ Error: 'playbook.txt' not found.")
    sys.exit(1)

# 3. AUTOMATION: Read the 20 most recent log entries automatically
# This reads directly from your newly created file for testing
print("📖 Reading local attack logs...")
log_entry = subprocess.getoutput('tail -n 20 attack_logs.txt')

# 4. Construct the prompt
prompt = f"""You are a junior SOC analyst.
Playbook rules:
{playbook}

Analyse this log:
{log_entry}

Respond strictly with:
- Threat type
- Severity
- Recommended action
"""

# 5. Connect to Gemini 3.5 Flash
url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key={API_KEY}'
headers = {'Content-Type': 'application/json'}
payload = {"contents": [{"parts": [{"text": prompt}]}]}

print("🔄 Sending live log data to Gemini 3.5 Flash...")
try:
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    result = response.json()
    ai_analysis = result['candidates'][0]['content']['parts'][0]['text']
    
    print("\n--- 🛡️ GEMINI 3.5 FLASH SOC ANALYST RESPONSE ---")
    print(ai_analysis)
    print("-----------------------------------------------")
except Exception as e:
    print(f"❌ An error occurred: {e}")
