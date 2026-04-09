import requests
import json
import time
import os

def fetch_starnote_requests():
    # 2026 Direct Search URL: Searches r/StarNoteApp for the specific lightbulb flair
    # URL encoded "💡 Feature Request" = %F0%9F%92%A1%20Feature%20Request
    url = "https://www.reddit.com/r/StarNoteApp/search.json?q=flair:%22%F0%9F%92%A1%20Feature%20Request%22&restrict_sr=1&sort=top&t=month"
    
    # Enhanced Headers to avoid being flagged as a generic bot
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 StarNoteWikiBot/1.0',
        'Accept': 'application/json'
    }

    try:
        print(f"Connecting to Reddit: {url}")
        response = requests.get(url, headers=headers, timeout=15)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code != 200:
            return []
            
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        print(f"Successfully retrieved {len(posts)} posts.")
        return posts
        
    except Exception as e:
        print(f"Network error: {e}")
        return []

def aggregate_features(posts):
    # Dictionary to track cumulative upvotes for similar ideas
    groups = {
        "LaTeX & Math Support": 0,
        "Cloud Sync (Auto)": 0,
        "Object Grouping & Layers": 0,
        "Handwriting OCR Search": 0,
        "Audio Recording Sync": 0,
        "Windows/PC Version": 0,
        "Sticker Management": 0
    }
    
    found_any = False
    for post in posts:
        title = post['data']['title'].lower()
        upvotes = post['data']['score']
        
        # Simple keyword matching logic
        for key in groups:
            # We check for a subset of the key to be flexible
            keyword = key.split(' ')[0].lower() 
            if keyword in title:
                groups[key] += upvotes
                found_any = True
                
    # Return sorted list of tuples (Feature, Score)
    return sorted(groups.items(), key=lambda x: x[1], reverse=True), found_any

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
 
