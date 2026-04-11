import json
import glob
import os
import time
import csv

def aggregate_all_data():
    raw_folder = "data/raw_json/*.json"
    files = glob.glob(raw_folder)
    
    unique_posts = {} 
    print(f"📂 Found {len(files)} JSON files to process.")
    
    for file in files:
        try:
            with open(file, "r", encoding="utf-8") as f:
                batch = json.load(f)
                posts = batch.get('data', {}).get('children', [])
                for post in posts:
                    p_data = post['data']
                    post_id = p_data['name'] # Unique ID (e.g., t3_xyz)
                    
                    # Store only the relevant fields to keep the CSV clean
                    unique_posts[post_id] = {
                        "id": post_id,
                        "title": p_data.get('title', 'No Title'),
                        "url": f"https://reddit.com{p_data.get('permalink', '')}",
                        "created_utc": p_data.get('created_utc', 0),
                        "score": p_data.get('score', 0)
                    }
        except Exception as e:
            print(f"⚠️ Error reading {file}: {e}")

    print(f"📊 Total unique posts after deduplication: {len(unique_posts)}")
    return list(unique_posts.values())

def generate_outputs(posts):
    # 1. CATEGORIZATION LOGIC
    categories = {
        "LaTeX / Math Support": ["latex", "math", "formula", "equation"],
        "Cloud Sync (Drive/Dropbox)": ["sync", "cloud", "backup", "drive"],
        "Windows / Desktop Version": ["windows", "pc", "desktop", "exe"],
        "Infinite Canvas / Grouping": ["canvas", "infinite", "group", "layers"],
        "Handwriting to Text (OCR)": ["ocr", "handwriting", "text", "conversion"]
    }
    
    feature_counts = {cat: 0 for cat in categories}
    
    # 2. SAVE THE CSV (The "Cleaned Data" artifact)
    csv_file = "data/cleaned_feature_data.csv"
    os.makedirs('data', exist_ok=True)
    
    with open(csv_file, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["id", "title", "url", "created_utc", "score"])
        writer.writeheader()
        for p in posts:
            writer.writerow(p)
            
            # While we are at it, update the category counts for the wiki
            title_lower = p['title'].lower()
            for cat, keywords in categories.items():
                if any(kw in title_lower for kw in keywords):
                    feature_counts[cat] += 1

    print(f"💾 CSV Saved: {csv_file}")

    # 3. SAVE THE WIKI PAGE
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    sorted_features = sorted(feature_counts.items(), key=lambda x: x[1], reverse=True)
    
    md = f"# 🏆 Most Wanted Features\n\n"
    md += f"!!! info \"Auditor Stats\"\n    **Last Audit:** {timestamp} (SAST)  \n"
    md += f"    **Total Unique Posts Scanned:** {len(posts)}  \n\n"
    md += f"[Download the Raw Cleaned Data (CSV)](https://github.com/NakoTurtle/StarNote-Unofficial-Wiki/blob/main/data/cleaned_feature_data.csv)  \n\n"
    
    md += "| Feature Category | Request Count | Priority |\n| :--- | :---: | :--- |\n"
    for feature, count in sorted_features:
        priority = "🔥 High" if count > 5 else "⏳ Medium" if count > 0 else "❄️ Low"
        md += f"| {feature} | {count} | {priority} |\n"
        
    os.makedirs('docs', exist_ok=True)
    with open("docs/most_wanted.md", "w", encoding="utf-8") as f:
        f.write(md)

if __name__ == "__main__":
    all_posts = aggregate_all_data()
    if all_posts:
        generate_outputs(all_posts)
        print("✅ Process Complete: CSV and Wiki updated.")
