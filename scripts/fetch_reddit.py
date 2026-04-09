import requests
import json
import time

def fetch_starnote_requests():
    # 2026 Best Practice: Be specific with your User-Agent to avoid 429 errors
    url = "https://www.reddit.com/r/StarNoteApp/search.json"
    params = {
        'q': 'flair:"💡 Feature Request"',
        'sort': 'top',
        't': 'month',
        'limit': 100
    }
    headers = {'User-Agent': 'Stellenbosch_Student_Wiki_Bot/1.0 (Educational Project)'}

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data['data']['children']
    except Exception as e:
        print(f"Error fetching data: {e}")
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