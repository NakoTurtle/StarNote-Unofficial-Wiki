import requests
import json
import time
import os

def fetch_starnote_requests():
    # Searching for 'StarNote' to ensure we find SOMETHING, even if not a feature request
    url = "https://old.reddit.com/r/StarNoteApp/search.json?q=Feature&restrict_sr=1&sort=top&t=month"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) StarNoteDiagnostic/1.1 (Stellenbosch University Project)',
        'Accept': 'application/json'
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)
        status = response.status_code
        
        if status != 200:
            return [], f"Error: Status Code {status}", response.text[:500]
            
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        
        # Capture the raw keys of the first post for debugging
        debug_sample = ""
        if posts:
            debug_sample = str(posts[0]['data'].keys())
        else:
            debug_sample = f"Full JSON Response: {json.dumps(data)[:500]}"
            
        return posts, f"Success (Status {status})", debug_sample
        
    except Exception as e:
        return [], "Exception Occurred", str(e)

def generate_markdown(posts, status_msg, debug_text):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    content = f"# 🛠️ Wiki Diagnostic Page\n\n"
    content += f"!!! info \"System Internals\"\n"
    content += f"    **Last Attempt:** {timestamp} (SAST)  \n"
    content += f"    **API Status:** {status_msg}  \n"
    content += f"    **Post Count:** {len(posts)}\n\n"

    content += "## 🔍 Raw Debug Output\n"
    content += "If the table below is empty, this raw data explains why:\n"
    content += f"```text\n{debug_text}\n```\n\n"

    if posts:
        content += "## 🚀 Detected Features\n"
        content += "| Title | Upvotes |\n| :--- | :---: |\n"
        for post in posts[:10]: # Just show the first 10 for diagnostics
            content += f"| {post['data']['title']} | {post['data']['score']} |\n"
    else:
        content += "!!! danger \"Zero Results\"\n    Reddit returned a valid JSON but found no posts matching the query 'Feature'."

    return content

if __name__ == "__main__":
    posts, status, debug = fetch_starnote_requests()
    final_md = generate_markdown(posts, status, debug)
    
    os.makedirs('docs', exist_ok=True)
    with open("docs/features.md", "w", encoding="utf-8") as f:
        f.write(final_md)
