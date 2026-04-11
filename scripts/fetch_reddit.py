import json
import glob
import os
import time
import csv

def aggregate_local_data():
    # Look for any JSON files you've manually uploaded to this folder
    raw_folder = "data/raw_json/*.json"
    files = glob.glob(raw_folder)
    
    unique_posts = {} 
    print(f"📂 Found {len(files)} manual data drops to process.")
    
    if not files:
        print("⚠️ Warning: No JSON files found in data/raw_json/. Wiki will be empty.")
        return []

    for file in files:
        try:
            with open(file, "r", encoding="utf-8") as f:
                batch = json.load(f)
                # Check if this is a Reddit JSON or just an error page
                if 'data' not in batch:
                    print(f"❌ {file} contains invalid data (possibly a block message). Skipping.")
                    continue
                    
                posts = batch.get('data', {}).get('children', [])
                for post in posts:
                    p_data = post['data']
                    post_id = p_data['name']
                    unique_posts[post_id] = {
                        "id": post_id,
                        "title": p_data.get('title', 'No Title'),
                        "url": f"https://reddit.com{p_data.get('permalink', '')}",
                        "created_utc": p_data.get('created_utc', 0),
                        "score": p_data.get('score', 0)
                    }
        except Exception as e:
            print(f"⚠️ Error reading {file}: {e}")

    return list(unique_posts.values())

def generate_outputs(posts):
    # 1. CATEGORIZATION (Update keywords as needed)
    categories = {
        "LaTeX / Math Support": ["latex", "math", "formula", "equation"],
        "Cloud Sync (Drive/Dropbox)": ["sync", "cloud", "backup", "drive"],
        "Windows / Desktop Version": ["windows", "pc", "desktop", "exe"],
        "Infinite Canvas / Grouping": ["canvas", "infinite", "group", "layers"],
        "Handwriting to Text (OCR)": ["ocr", "handwriting", "text", "conversion"]
    }
    
    feature_counts = {cat: 0 for cat in categories}
    
    # 2. SAVE THE CSV
    os.makedirs('data', exist_ok=True)
    with open("data/cleaned_feature_data.csv", mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["id", "title", "url", "created_utc", "score"])
        writer.writeheader()
        for p in posts:
            writer.writerow(p)
            title_lower = p['title'].lower()
            for cat, keywords in categories.items():
                if any(kw in title_lower for kw in keywords):
                    feature_counts[cat] += 1

    # 3. SAVE THE WIKI PAGE (features.md)
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    md = f"# 🚀 Live Feature Tracker\n\n"
    md += f"!!! info \"Audit Status\"\n    **Last Sync:** {timestamp} (SAST)  \n"
    md += f"    **Unique Posts Analyzed:** {len(posts)}  \n\n"
    
    if posts:
        md += "| Feature Suggestion | Link |\n| :--- | :--- |\n"
        for p in posts[:20]: # Show the 20 most recent in the list
            md += f"| {p['title']} | [View]({p['url']}) |\n"
    else:
        md += "!!! warning \"No Data\"\n    Please upload valid JSON to `data/raw_json/`."

    os.makedirs('docs', exist_ok=True)
    with open("docs/features.md", "w", encoding="utf-8") as f:
        f.write(md)

if __name__ == "__main__":
    all_posts = aggregate_local_data()
    generate_outputs(all_posts)
    print("✅ Process Complete.")
