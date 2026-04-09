import requests
import json
import time

def fetch_starnote_requests():
    # Use the direct subreddit JSON endpoint + the specific flair search string
    # We use %20 for spaces and %22 for quotes to ensure the URL is clean
    url = "https://www.reddit.com/r/StarNoteApp/search.json?q=flair:%22%F0%9F%92%A1%20Feature%20Request%22&restrict_sr=1&sort=top&t=month"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 StellenboschStudentProject/1.0',
        'Accept': 'application/json'
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)
        
        # Log the status to the GitHub Action console so we can see what happened
        print(f"Reddit API Status Code: {response.status_code}")
        
        if response.status_code != 200:
            print(f"Error: Received status {response.status_code}")
            return []
            
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        print(f"Found {len(posts)} potential feature posts.")
        return posts
        
    except Exception as e:
        print(f"Scraper crashed with error: {e}")
        return []

def aggregate_features(posts):
    # Mapping common keywords to group requests
    groups = {
        "LaTeX Support": 0,
        "Cloud Sync": 0,
        "Object Grouping": 0,
        "Handwriting Search": 0,
        "Audio Notes": 0
    }
    
    for post in posts:
        title = post['data']['title'].lower()
        upvotes = post['data']['score']
        
        for key in groups:
            if key.lower() in title:
                groups[key] += upvotes
                
    return sorted(groups.items(), key=lambda x: x[1], reverse=True)

def generate_wiki_table(sorted_data):
    header = "| Feature Group | Total Community Upvotes | Status |\n| :--- | :---: | :--- |\n"
    rows = ""
    for feature, score in sorted_data:
        rows += f"| {feature} | {score} | ⏳ Pending Dev Review |\n"
    return header + rows

# Main Execution
raw_posts = fetch_starnote_requests()
if raw_posts:
    aggregated = aggregate_features(raw_posts)
    markdown_table = generate_wiki_table(aggregated)
    
    with open("docs/features.md", "w") as f:
        f.write("# 🚀 Live Feature Tracker\n\n")
        f.write(f"*Last updated: {time.strftime('%Y-%m-%d %H:%M:%S')}*\n\n")
        f.write(markdown_table)
    print("Wiki table updated successfully!")
