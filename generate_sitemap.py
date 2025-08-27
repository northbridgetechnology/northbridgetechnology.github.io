import os
from pathlib import Path
from datetime import datetime

BASE_URL = "https://northbridgetechnology.com"  # 🔹 change to your domain
IGNORE = {"sitemap.html"}  # don't list sitemap itself

# Define categories
CATEGORIES = {
    "core": {
        "title": "Core Pages",
        "icon": "fa-earth-americas",
        "meta": "On-page sections match the navigation.",
        "files": [
            ("index.html", "Home"),
            ("index.html#services", "Services"),
            ("index.html#whitepapers", "Whitepapers"),
            ("index.html#about", "About"),
            ("index.html#contact", "Contact"),
        ],
    },
    "whitepapers": {
        "title": "Whitepapers",
        "icon": "fa-file-lines",
        "meta": "Long-form resources and guides.",
        "files": [
            ("whitepapers/northbridge_7_costly_it_mistakes.html",
             "7 Costly IT Mistakes That Stunt Business Growth"),
            ("whitepapers/northbridge_cybersecurity_smb_framework.html",
             "Cybersecurity Framework for SMBs"),
            (None, "Cloud Migration Strategy Guide (Coming Soon)"),
        ],
    },
    "utility": {
        "title": "Utility & Legal",
        "icon": "fa-screwdriver-wrench",
        "meta": "Helpful administrative pages.",
        "files": [
            ("contact_form.html", "Contact Form"),
            ("privacy_policy.html", "Privacy Policy"),
            ("terms_and_conditions.html", "Terms and Conditions"),
        ],
    },
    "external": {
        "title": "External Profiles",
        "icon": "fa-brands fa-linkedin",
        "meta": "These open in a new tab depending on browser settings.",
        "files": [
            ("mailto:info@northbridgetechnology.com", "Email: info@northbridgetechnology.com"),
            ("https://www.linkedin.com/company/northbridge-technology", "LinkedIn Company Page"),
        ],
    },
}

def get_html_files():
    """Return list of all HTML files for sitemap.xml"""
    files = []
    for root, _, filenames in os.walk("."):
        for f in filenames:
            if f.endswith(".html") and f not in IGNORE:
                files.append(Path(root, f).as_posix().lstrip("./"))
    return sorted(files)

def generate_xml(files):
    """Build sitemap.xml for SEO"""
    today = datetime.utcnow().strftime("%Y-%m-%d")
    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for f in files:
        url = f"{BASE_URL}/{f}"
        xml.append(f"  <url><loc>{url}</loc><lastmod>{today}</lastmod></url>")
    xml.append("</urlset>")
    return "\n".join(xml)

def build_card(category):
    """Generate one <section class='card'> block"""
    title = category["title"]
    icon = category["icon"]
    meta = category["meta"]
    links = []
    for f, label in category["files"]:
        if f:
            links.append(f'<li><a href="{f}">{label}</a></li>')
        else:
            links.append(f'<li><span title="Coming soon">{label}</span></li>')
    return f"""
      <section class="card">
        <h3><i class="fa-solid {icon}" aria-hidden="true"></i> {title}</h3>
        <ul>
          {''.join(links)}
        </ul>
        <div class="meta">{meta}</div>
      </section>
    """

def generate_html():
    """Return the styled sitemap.html content"""
    # Build cards
    cards = "\n".join([
        build_card(CATEGORIES["core"]),
        build_card(CATEGORIES["whitepapers"]),
        build_card(CATEGORIES["utility"]),
        build_card(CATEGORIES["external"]),
    ])

    # Full page skeleton
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>NorthBridge Technology – Site Map</title>
  <meta name="description" content="HTML site map for NorthBridge Technology to help visitors and search engines quickly find pages." />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="{BASE_URL}/sitemap.html" />

  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Open+Sans:wght@300;400;500&display=swap">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <style>
    :root {{
      --primary: #1f2a44;
      --primary-light: #2f3b5c;
      --secondary: #162036;
      --accent: #4a7b9d;
      --text: #333;
      --text-light: #666;
      --background: #f8f9fb;
      --white: #ffffff;
      --shadow: 0 4px 12px rgba(0,0,0,0.08);
      --transition: all 0.3s ease;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: 'Open Sans', sans-serif; color: var(--text); background: var(--background); line-height: 1.6; }}

    header {{
      background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
      color: var(--white);
      padding: 3rem 2rem;
      text-align: center;
      position: relative;
      overflow: hidden;
    }}
    header::before {{
      content: '';
      position: absolute; inset: 0;
      background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 320'%3E%3Cpath fill='%23ffffff' fill-opacity='0.05' d='M0,224L48,213.3C96,203,192,181,288,160C384,139,480,117,576,122.7C672,128,768,160,864,170.7C960,181,1056,171,1152,165.3C1248,160,1344,160,1392,160L1440,160L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z'%3E%3C/path%3E%3C/svg%3E");
      background-size: cover; background-position: center;
    }}
    .logo {{ display: block; margin: 0 auto 1.25rem; width: 90px; height: 90px; background: var(--white); border-radius: 50%; padding: 18px; box-shadow: var(--shadow); }}
    header h1 {{ font-family: 'Montserrat', sans-serif; font-size: 2.4rem; font-weight: 700; }}
    header p {{ margin-top: .75rem; font-size: 1.1rem; opacity: 0.95; }}

    .breadcrumb {{ padding: 1rem 2rem; max-width: 1200px; margin: 0 auto; font-size: .9rem; color: var(--text-light); }}
    .breadcrumb a {{ color: var(--accent); text-decoration: none; }}
    .breadcrumb a:hover {{ text-decoration: underline; }}

    nav {{ background: var(--secondary); padding: 1rem; text-align: center; position: sticky; top: 0; z-index: 100; }}
    nav a {{ color: var(--white); margin: 0 1rem; text-decoration: none; font-weight: 500; font-family: 'Montserrat', sans-serif; position: relative; padding: .5rem 0; }}
    nav a:hover {{ color: var(--accent); }}

    main {{ max-width: 1100px; margin: 0 auto; padding: 3rem 1.5rem 4rem; }}
    h2 {{ color: var(--primary); font-family: 'Montserrat', sans-serif; font-size: 2rem; font-weight: 600; text-align: center; margin-bottom: 1.5rem; position: relative; padding-bottom: 1rem; }}
    h2::after {{ content: ''; position: absolute; bottom: 0; left: 50%; transform: translateX(-50%); width: 80px; height: 4px; background: var(--accent); border-radius: 2px; }}

    .sitemap-wrap {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.5rem; margin-top: 1.5rem; }}
    .card {{ background: var(--white); border-radius: 12px; box-shadow: var(--shadow); padding: 1.25rem 1.25rem 1rem; border-top: 4px solid var(--accent); }}
    .card h3 {{ font-family: 'Montserrat', sans-serif; font-size: 1.15rem; margin-bottom: .75rem; color: var(--primary); display: flex; align-items: center; gap: .5rem; }}
    .card ul {{ list-style: none; }}
    .card li + li {{ margin-top: .5rem; }}
    .card a {{ color: var(--text); text-decoration: none; }}
    .card a:hover {{ color: var(--accent); text-decoration: underline; }}

    .meta {{ font-size: .85rem; color: var(--text-light); margin-top: .75rem; }}

    footer {{ background: var(--primary); color: var(--white); text-align: center; padding: 2.5rem 1.5rem; }}
    footer a {{ color: #fff; }}
  </style>
</head>
<body>
  <div class="breadcrumb">
    <a href="index.html">Home</a> &gt; Site Map
  </div>

  <header>
    <div class="logo" aria-hidden="true"></div>
    <h1>Site Map</h1>
    <p>Quickly jump to any page or major section on the site.</p>
  </header>

  <nav aria-label="Primary">
    <a href="index.html">Home</a>
    <a href="index.html#services">Services</a>
    <a href="index.html#whitepapers">Whitepapers</a>
    <a href="index.html#about">About</a>
    <a href="index.html#contact">Contact</a>
  </nav>

  <main>
    <h2>All Pages & Sections</h2>
    <div class="sitemap-wrap">
      {cards}
    </div>

    <section class="card" style="margin-top:1.5rem">
      <h3><i class="fa-solid fa-circle-info" aria-hidden="true"></i> Tips</h3>
      <ul>
        <li>Looking for something specific? Use the site search in your browser (<kbd>Ctrl</kbd> + <kbd>F</kbd> / <kbd>Cmd</kbd> + <kbd>F</kbd>).</li>
        <li>Whitepapers may also be available as downloadable PDFs when published.</li>
      </ul>
    </section>
  </main>

  <footer>
    <p>&copy; {datetime.utcnow().year} NorthBridge Technology. All rights reserved.</p>
    <p><a href="privacy_policy.html">Privacy Policy</a> | <a href="terms_and_conditions.html">Terms and Conditions</a> | <a href="sitemap.html">Sitemap</a></p>
  </footer>
</body>
</html>
"""

REPO_ROOT = Path(__file__).parent.resolve()

if __name__ == "__main__":
    files = get_html_files()
    (REPO_ROOT / "sitemap.xml").write_text(generate_xml(files), encoding="utf-8")
    (REPO_ROOT / "sitemap.html").write_text(generate_html(), encoding="utf-8")
    print("✅ Generated sitemap.html and sitemap.xml in", REPO_ROOT)
