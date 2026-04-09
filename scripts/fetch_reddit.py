import requests
import json
import time
import os

def fetch_starnote_requests():
    # We broaden the search to any post containing "Feature" or "Suggestion" in r/StarNoteApp
    # This ignores the tricky emoji flair entirely.
    url = "https://www.reddit.com/r/StarNoteApp/search.json?q=title:(Feature%20OR%20Request%20OR%20Suggestion)&restrict_sr=1&sort=top&t=month"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 StarNoteStudentProject/1.0',
        'Accept': 'application/json'
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)
        print(f"Reddit Search Status: {response.status_code}")
        
        if response.status_code != 200:
            return []
            
        data = response.json()
        return data.get('data', {}).get('children', [])
    except Exception as e:
        print(f"Error: {e}")
        return []

def aggregate_features(posts):
    # Expanded keywords to catch variations in how students write
    groups = {
        "LaTeX / Math Support": ["latex", "math", "formula", "equation"],
        "Cloud Sync (Auto)": ["sync", "cloud", "drive", "backup"],
        "Object Grouping": ["grouping", "group", "layers", "select"],
        "Handwriting Search": ["search", "ocr", "finding"],
        "Windows/PC Version": ["windows", "desktop", "laptop", "pc"],
        "Audio Sync": ["audio", "record", "voice"]
    }
    
    # Initialize counts
    scores = {key: 0 for key in groups}
    found_any = False

    for post in posts:
        title = post['data']['title'].lower()
        upvotes = post['data']['score']
        
        for feature_name, keywords in groups.items():
            if any(word in title for word in keywords):
                scores[feature_name] += upvotes
                found_any = True
                
    return sorted(scores.items(), key=lambda x: x[1], reverse=True), found_any

def generate_markdown(sorted_data, post_count, found_any):
    # Metadata and Status Admonitions
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    content = f"# 🚀 Live Feature Tracker\n\n"
    content += f"!!! info \"Status Check\"\n"
    content += f"    **Last Updated:** {timestamp} (SAST)  \n"
    content += f"    **Reddit Posts Scanned:** {post_count}\n\n"

    if post_count == 0:
        content += """
!!! danger "Empty Result Set"
    The scraper returned 0 posts from Reddit. This usually means the search query for the specific flair failed or Reddit is rate-limiting the request.
"""
    elif not found_any:
        content += """
!!! warning "No Matches Found"
    Posts were found, but none matched the current tracking keywords (LaTeX, Sync, etc.). The community might be discussing new topics!
"""
    else:
        # Table Header
        content += "| Feature Group | Community Upvotes | Status |\n"
        content += "| :--- | :---: | :--- |\n"
        
        for feature, score in sorted_data:
            # Add a status icon based on upvote heat
            status = ":material-fire: High Demand" if score > 50 else ":material-clock-outline: Pending Review"
            content += f"| {feature} | {score} | {status} |\n"

    return content

# Main Workflow
if __name__ == "__main__":
    raw_posts = fetch_starnote_requests()
    count = len(raw_posts)
    aggregated_data, matches_found = aggregate_features(raw_posts)
    
    final_markdown = generate_markdown(aggregated_data, count, matches_found)
    
    # Ensure the docs directory exists (relevant for local testing)
    os.makedirs('docs', exist_ok=True)
    
    with open("docs/features.md", "w", encoding="utf-8") as f:
        f.write(final_markdown)
        
    print("Done! features.md has been updated.")
 
