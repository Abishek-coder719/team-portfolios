import csv
import os

GITHUB_USERNAME = "yourusername"   # <-- change this to your real GitHub username
REPO_NAME = "team-portfolios"      # <-- change this if you rename the repo

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{name} — Portfolio Coming Soon</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  body {{
    font-family: -apple-system, Segoe UI, Roboto, sans-serif;
    background: #0f1117;
    color: #f5f5f5;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    margin: 0;
    text-align: center;
  }}
  .card {{
    padding: 2.5rem 3rem;
    border-radius: 16px;
    background: #1a1d27;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
  }}
  h1 {{ margin: 0 0 0.5rem 0; font-size: 1.6rem; }}
  p {{ color: #a0a4b0; margin: 0; }}
</style>
</head>
<body>
  <div class="card">
    <h1>{name}</h1>
    <p>Portfolio coming soon 🚧</p>
  </div>
</body>
</html>
"""

INDEX_ROW = '<li><a href="{slug}/">{name}</a></li>'

def main():
    with open("team_list.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    os.makedirs("pages", exist_ok=True)
    index_rows = []
    urls = []

    for row in rows:
        slug = row["slug"].strip()
        name = row["name"].strip()
        folder = os.path.join("pages", slug)
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
            f.write(PAGE_TEMPLATE.format(name=name))
        url = f"https://{GITHUB_USERNAME}.github.io/{REPO_NAME}/{slug}/"
        urls.append((slug, name, url))
        index_rows.append(INDEX_ROW.format(slug=slug, name=name))

    # top-level index listing everyone (optional, handy for you)
    with open(os.path.join("pages", "index.html"), "w", encoding="utf-8") as f:
        f.write("<html><body><h1>Team</h1><ul>" + "".join(index_rows) + "</ul></body></html>")

    # write urls.csv for the QR generator to consume
    with open("urls.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["slug", "name", "url"])
        writer.writerows(urls)

    print(f"Built {len(urls)} placeholder pages in ./pages and wrote urls.csv")

if __name__ == "__main__":
    main()
