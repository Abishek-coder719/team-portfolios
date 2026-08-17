# Team QR Portfolio Kit

23 QR codes, each pointing to a permanent URL for one team member. Right now
every URL shows a shared "Portfolio coming soon" page. Later, you edit each
page's content — the QR code itself never has to change or be reprinted.

## What's in here
- `team_list.csv` — edit this first: put in real names (and slugs if you want nicer URLs)
- `pages/` — the 23 placeholder HTML pages (already built from team_list.csv)
- `qr_codes/` — the 23 QR code PNGs, ready to print (already built)
- `build_pages.py` — regenerates `pages/` from `team_list.csv`
- `build_qr_codes.py` — regenerates `qr_codes/` from `urls.csv`

## One-time setup (10 minutes)

1. **Edit names** (optional but recommended): open `team_list.csv` and replace
   `Team Member 1`, `Team Member 2`, etc. with real names. Keep the `slug`
   column as simple lowercase-with-dashes (e.g. `priya-sharma`).

2. **Create a free GitHub account** at github.com if you don't have one.

3. **Create a new repository** named `team-portfolios` (Settings → make it Public).

4. **Open `build_pages.py`** in this folder and change:
   ```python
   GITHUB_USERNAME = "yourusername"   # <- your real GitHub username
   REPO_NAME = "team-portfolios"      # <- only change if you named your repo differently
   ```

5. **Regenerate everything** with your real username and names:
   ```
   python3 build_pages.py
   python3 build_qr_codes.py
   ```

6. **Upload the `pages/` folder contents** to your GitHub repo (drag-and-drop
   works fine on github.com — no command line needed).

7. **Turn on GitHub Pages**: repo → Settings → Pages → set source to the
   main branch, root folder. GitHub will give you a live URL within a minute.

8. **Print the QR codes** from `qr_codes/` — each one is labeled with the
   person's slug and name.

## Updating a portfolio later (once it's ready)

1. Go to your repo on github.com
2. Open `pages/<their-slug>/index.html`
3. Click the pencil (edit) icon
4. Replace the placeholder content with their real portfolio, or a short
   redirect snippet pointing to their page on the college website once it's
   back online:
   ```html
   <meta http-equiv="refresh" content="0; url=https://college-site.edu/team/priya">
   ```
5. Commit the change

The printed QR code keeps working exactly as before — nothing to reprint.

## If you'd rather not deal with GitHub

Any free static host works the same way (Netlify, Vercel, Cloudflare Pages,
even a free Google Sites page per person). The key idea is the same either
way: pick a URL now, generate the QR code once, and only ever edit what's
*behind* that URL later.
