import json
import glob
import os
import time
import csv
from collections import Counter

def aggregate_local_data():
    raw_folder = "data/raw_json/*.json"
    files = glob.glob(raw_folder)
    unique_posts = {} 
    
    if not files:
        return []

    for file in files:
        try:
            with open(file, "r", encoding="utf-8") as f:
                batch = json.load(f)
                posts = batch.get('data', {}).get('children', [])
                for post in posts:
                    p_data = post['data']
                    post_id = p_data['name']
                    unique_posts[post_id] = {
                        "id": post_id,
                        "title": p_data.get('title', 'No Title'),
                        "url": f"https://reddit.com{p_data.get('permalink', '')}",
                        "score": p_data.get('score', 0)
                    }
        except Exception as e:
            print(f"⚠️ Error reading {file}: {e}")

    return list(unique_posts.values())

def generate_outputs(posts):
    # 1. DEFINE FEATURE CATEGORIES & KEYWORDS
    # You can add more keywords here as you see them in the Reddit posts
    categories = {
        "LaTeX / Math Support": ["latex", "math", "formula", "equation", "symbol"],
        "Cloud Sync / Backup": ["sync", "cloud", "backup", "drive", "dropbox", "icloud"],
        "Windows / PC Version": ["windows", "pc", "desktop", "exe", "laptop"],
        "Infinite Canvas": ["canvas", "infinite", "zoom", "scrolling"],
        "Dark Mode": ["dark", "theme", "night", "black"],
        "Hyperlinks": ["link", "hyperlink", "url", "web"]
    }
    
    # 2. COUNT MENTIONS
    feature_mentions = {cat: 0 for cat in categories}
    for p in posts:
        title_lower = p['title'].lower()
        for cat, keywords in categories.items():
            if any(kw in title_lower for kw in keywords):
                feature_mentions[cat] += 1

    # Sort categories by highest count
    sorted_features = sorted(feature_mentions.items(), key=lambda x: x[1], reverse=True)

    # 3. GENERATE MARKDOWN (features.md)
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    md = f"# 🚀 Live Feature Tracker\n\n"
    md += f"!!! info \"Community Audit\"\n    **Last Sync:** {timestamp} (SAST)  \n"
    md += f"    **Total Unique Posts Analyzed:** {len(posts)}  \n\n"

    # Leaderboard Table
    md += "## 🏆 Most Requested Features\n"
    md += "| Feature Category | Request Count | Status |\n"
    md += "| :--- | :---: | :--- |\n"
    for feature, count in sorted_features:
        status = "🔥 Trending" if count > 5 else "⏳ Requested"
        md += f"| {feature} | {count} | {status} |\n"

    md += "\n---\n\n"
    
    # Raw Feed Table (Latest 20)
    md += "## 📂 Recent Discussions\n"
    md += "| Feature Suggestion | Community Link |\n| :--- | :--- |\n"
    for p in posts[:20]:
        md += f"| {p['title']} | [View on Reddit]({p['url Registrar}) |\n"

    # Save Markdown
    os.makedirs('docs', exist_ok=True)
    with open("docs/features.md", "w", encoding="utf-8") as f:
        f.write(md)

    # 4. SAVE CLEANED CSV
    os.makedirs('data', exist_ok=True)
    with open("data/cleaned_feature_data.csv", mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["id", "title", "url", "score"])
        writer.writeheader()
        writer.writerows(posts)

if __name__ == "__main__":
    all_posts = aggregate_local_data()
    if all_posts:
        generate_outputs(all_posts)
        print(f"✅ Wiki updated with {len(all_posts)} posts.")
