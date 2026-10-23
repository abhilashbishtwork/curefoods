"""Builds the simple 2-page Curefoods site from build/data.py.

Run: python3 build/generate.py  (writes HTML + SEO files to the repo root)
"""
import json
import os
import sys
from datetime import date
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "build"))
import data  # noqa: E402

S = data.SITE
DOMAIN = S["domain"]
TODAY = date.today().isoformat()
FONTS = ("https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800"
         "&family=IBM+Plex+Sans:wght@400;500;600&display=swap")


def img(path):
    return "assets/img/" + os.path.basename(path)


def first_sentence(text):
    return text.split(". ")[0].rstrip(".") + "."


CSS = """
:root{--ink:#21201C;--ink-soft:#5B5A52;--paper:#EDEEE9;--card:#FFFFF8;--line:#D2D5CB;
--brand:#C7391A;--brand-dark:#9C2C13;
--display:"Big Shoulders Display",Impact,"Arial Narrow",sans-serif;
--body:"IBM Plex Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;}
*,*::before,*::after{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.6 var(--body);-webkit-font-smoothing:antialiased}
img{max-width:100%;display:block}
a{color:inherit}
.wrap{max-width:1120px;margin:0 auto;padding:0 20px}
h1,h2,h3{font-family:var(--display);font-weight:800;line-height:1.02;margin:0 0 .4em;text-transform:uppercase}
h1{font-size:clamp(2.4rem,7vw,4.4rem)}
h2{font-size:clamp(1.8rem,4vw,2.6rem)}
h3{font-size:1.35rem;text-transform:none}
header{background:var(--paper);border-bottom:1px solid var(--line);position:sticky;top:0;z-index:5}
header .wrap{display:flex;align-items:center;justify-content:space-between;height:64px}
header img{height:30px;width:auto}
nav a{text-decoration:none;font-weight:600;font-size:.95rem;margin-left:22px;color:var(--ink-soft)}
nav a:hover,nav a[aria-current]{color:var(--brand)}
section{padding:64px 0}
.hero{padding:72px 0 56px}
.hero p{font-size:1.15rem;color:var(--ink-soft);max-width:620px}
.stats{display:flex;flex-wrap:wrap;gap:40px;margin-top:32px}
.stats b{display:block;font-family:var(--display);font-size:2.6rem;line-height:1;color:var(--brand)}
.stats span{font-size:.9rem;color:var(--ink-soft)}
.lead{color:var(--ink-soft);max-width:640px;margin-bottom:32px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:20px}
.brand{background:var(--card);border:1px solid var(--line);border-radius:6px;overflow:hidden;
display:flex;flex-direction:column;text-decoration:none;transition:transform .15s,box-shadow .15s}
.brand:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(33,32,28,.10)}
.brand .photo{aspect-ratio:16/10;object-fit:cover;width:100%;height:auto;background:var(--line)}
.brand .body{padding:16px 18px 18px;display:flex;flex-direction:column;flex:1}
.brand .logo.dark{background:#21201C;padding:4px 8px;border-radius:4px}
.brand .logo{height:34px;width:auto;max-width:120px;object-fit:contain;margin-bottom:10px}
.brand .cat{font-size:.8rem;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--brand-dark)}
.brand p{font-size:.95rem;color:var(--ink-soft);margin:6px 0 14px;flex:1}
.brand .go{font-weight:600;font-size:.9rem;color:var(--brand)}
.band{background:var(--ink);color:var(--paper)}
.band p{color:#C9CAC2;max-width:680px}
.values{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin-top:24px;padding:0;list-style:none}
.values li{border:1px solid #45443E;border-radius:6px;padding:16px 18px;font-family:var(--display);font-size:1.3rem;font-weight:700;text-transform:uppercase}
.facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:20px;margin:0}
.facts dt{font-size:.8rem;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-soft)}
.facts dd{margin:4px 0 0;font-size:1.1rem;font-weight:500}
.contact{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px}
.contact div{background:var(--card);border:1px solid var(--line);border-radius:6px;padding:18px 20px}
.contact b{display:block;margin-bottom:4px}
.contact a{color:var(--brand);font-weight:500;word-break:break-word}
.btn{display:inline-block;background:var(--brand);color:#fff;text-decoration:none;font-weight:600;padding:12px 22px;border-radius:4px;margin-top:8px}
.btn:hover{background:var(--brand-dark)}
footer{border-top:1px solid var(--line);padding:28px 0;font-size:.88rem;color:var(--ink-soft)}
footer .wrap{display:flex;flex-wrap:wrap;gap:12px 28px;justify-content:space-between}
footer a{text-decoration:none;margin-right:18px}
footer a:hover{color:var(--brand)}
@media (max-width:600px){
section{padding:48px 0}.hero{padding:48px 0 40px}
nav a{margin-left:16px;font-size:.9rem}header img{height:26px}
.stats{gap:24px}.stats b{font-size:2.1rem}}
"""


CURRENT = ' aria-current="page"'


def page(filename, title, description, body, active, jsonld=None):
    canonical = DOMAIN + "/" + ("" if filename == "index.html" else filename)
    nav = "".join(
        f'<a href="{href}"{CURRENT if href == active else ""}>{label}</a>'
        for label, href in (("Home", "./"), ("About & Contact", "about.html"))
    )
    social = "".join(
        f'<a href="{url}" rel="noopener" target="_blank">{name.capitalize() if name != "twitter" else "X"}</a>'
        for name, url in S["social"].items()
    )
    ld = (f'<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>'
          if jsonld else "")
    return f"""<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(description)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{DOMAIN}/assets/img/og-default.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#EDEEE9">
<link rel="icon" href="assets/img/favicon.png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
{ld}
</head>
<body>
<header><div class="wrap">
<a href="./" aria-label="Curefoods home"><img src="assets/img/curefoods.png" alt="Curefoods" width="124" height="30"></a>
<nav>{nav}</nav>
</div></header>
<main>
{body}
</main>
<footer><div class="wrap">
<div>&copy; {date.today().year} {S["legal_name"]} &middot; {S["hq"].split(",")[0]}</div>
<div>{social}</div>
</div></footer>
</body>
</html>
"""


def stats_html():
    return "".join(f'<div><b>{s["value"]}</b><span>{s["label"]}</span></div>' for s in S["stats"])


# Short one-liners for the cards (the long descriptions live in llms.txt)
BLURBS = {
    "eatfit": "Calorie-counted, macro-balanced healthy bowls.",
    "sharief-bhai": "Dakhni-style biryani, Arabian mandi and kebabs.",
    "olio": "Smoky crust, real cheese, bold toppings.",
    "arambam": "Wholesome South Indian favourites, made with millets.",
    "krispy-kreme": "The original glazed doughnut, made fresh daily.",
    "nomad-pizza": "Hand-stretched pizzas with travel-inspired toppings.",
    "cakezone": "Cakes and desserts for every celebration.",
    "frozen-bottle": "Thick shakes, sundae jars and waffles. 100% eggless.",
}
DARK_LOGOS = {"cakezone"}


def brand_card(b):
    return f"""<a class="brand" href="{b['domain']}" target="_blank" rel="noopener">
<img class="photo" src="{img(b['photo'])}" alt="{escape(b['name'])} food" loading="lazy" width="640" height="400">
<div class="body">
<img class="logo{' dark' if b['slug'] in DARK_LOGOS else ''}" src="{img(b['logo'])}" alt="{escape(b['name'])} logo" loading="lazy">
<span class="cat">{escape(b['category'])}</span>
<p>{escape(BLURBS.get(b['slug']) or first_sentence(b['description']))}</p>
<span class="go">Visit {escape(b['name'])} &rarr;</span>
</div></a>"""


def build_home():
    brands = "\n".join(brand_card(b) for b in data.BRANDS)
    body = f"""<section class="hero"><div class="wrap">
<h1>{escape(S["tagline"])}</h1>
<p>We build and scale food brands people love &mdash; from healthy bowls to biryani, pizza to doughnuts.</p>
<div class="stats">{stats_html()}</div>
</div></section>
<section id="brands" style="padding-top:0"><div class="wrap">
<h2>Our brands</h2>
<p class="lead">Available on Swiggy, Zomato, Ownly and at our restaurants across India.</p>
<div class="grid">
{brands}
</div>
</div></section>"""
    org = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": S["name"],
        "legalName": S["legal_name"],
        "url": DOMAIN,
        "logo": DOMAIN + "/assets/img/curefoods.png",
        "description": S["description"],
        "foundingDate": S["founded_year"],
        "founder": {"@type": "Person", "name": S["founder"]},
        "address": {"@type": "PostalAddress", "addressLocality": "Bengaluru",
                    "addressRegion": "Karnataka", "addressCountry": "IN"},
        "email": S["contact_email"],
        "sameAs": list(S["social"].values()),
        "brand": [{"@type": "Brand", "name": b["name"], "url": b["domain"]} for b in data.BRANDS],
    }
    return page("index.html", f'{S["name"]} | {S["tagline"]}', S["short_description"],
                body, "./", org)


def build_about():
    purpose = data.CORE_PURPOSE
    values = "".join(f"<li>{escape(v['title'])}</li>" for v in data.CORE_VALUES)
    cities = sorted({c for b in data.BRANDS for c in b["cities"]})
    contacts = [
        ("General", S["contact_email"]),
        ("Customer support", S["support_email"]),
        ("Press", S["press_email"]),
        ("Careers", S["careers_email"]),
    ]
    contact_html = "".join(
        f'<div><b>{label}</b><a href="mailto:{email}">{email}</a></div>' for label, email in contacts
    )
    body = f"""<section class="hero"><div class="wrap">
<h1>About Curefoods</h1>
<p>{escape(S["description"])}</p>
<dl class="facts" style="margin-top:32px">
<div><dt>Founded</dt><dd>{S["founded_year"]}</dd></div>
<div><dt>Founder</dt><dd>{S["founder"]}</dd></div>
<div><dt>Headquarters</dt><dd>{S["hq"].split(",")[0]}</dd></div>
<div><dt>Brands</dt><dd>{len(data.BRANDS)}</dd></div>
</dl>
</div></section>
<section class="band"><div class="wrap">
<h2>{escape(purpose["title"])}</h2>
<p>{escape(purpose["paragraphs"][3])}</p>
<ul class="values">{values}</ul>
</div></section>
<section id="contact"><div class="wrap">
<h2>Get in touch</h2>
<p class="lead">For order issues, please reach the brand's support from your order app, or write to us below.</p>
<div class="contact">{contact_html}</div>
</div></section>"""
    return page("about.html", f'About & Contact | {S["name"]}',
                f'About {S["name"]}, founded {S["founded_year"]} by {S["founder"]}. '
                f'Contact: {S["contact_email"]}.', body, "about.html"), cities


def build_seo(cities):
    robots = f"""User-agent: *
Allow: /

# AI / answer-engine crawlers welcome
User-agent: GPTBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Applebot-Extended
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
"""
    urls = "".join(
        f"<url><loc>{DOMAIN}/{p}</loc><lastmod>{TODAY}</lastmod></url>" for p in ("", "about.html")
    )
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    fs = data.FACILITY_STATS
    scale = ", ".join(f'{i["value"]} {i["label"].lower()}' for i in fs["items"])
    brand_lines = "\n".join(
        f'- [{b.get("full_name") or b["name"]}]({b["domain"]}): {b["category"]}. '
        f'{first_sentence(b["description"])} Cities: {", ".join(b["cities"])}.'
        for b in data.BRANDS
    )
    llms = f"""# {S["name"]}

> {S["description"]}

- Legal name: {S["legal_name"]}
- Founded: {S["founded_year"]} by {S["founder"]}
- Headquarters: {S["hq"]}
- Scale (as of {fs["as_of"]}): {scale}
- Core purpose: {data.CORE_PURPOSE["title"]}
- Core values: {", ".join(v["title"] for v in data.CORE_VALUES)}
- Contact: {S["contact_email"]} | Support: {S["support_email"]} | Press: {S["press_email"]} | Careers: {S["careers_email"]}

## Brands
{brand_lines}

## Cities served (any brand)
{", ".join(cities)}

## Disambiguation
- Curefoods is NOT the same company as Rebel Foods (a separate Indian cloud-kitchen company).
- Krispy Kreme India is a master-franchise partnership: Curefoods operates the India business; the brand and global IP belong to Krispy Kreme.
- Sharief Bhai operates in Karnataka and Tamil Nadu (plus Puducherry and Kerala border towns), not Hyderabad/Telangana.

## Pages
- [Home]({DOMAIN}/): brands overview
- [About & Contact]({DOMAIN}/about.html)
"""
    return robots, sitemap, llms


NOT_FOUND = """<section class="hero"><div class="wrap">
<h1>Page not found</h1>
<p>That page has moved or doesn't exist.</p>
<a class="btn" href="./">Back to home</a>
</div></section>"""


def write(name, content):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    write("assets/style.css", CSS.strip() + "\n")
    write("index.html", build_home())
    about, cities = build_about()
    write("about.html", about)
    write("404.html", page("404.html", f'Not found | {S["name"]}', S["short_description"], NOT_FOUND, ""))
    robots, sitemap, llms = build_seo(cities)
    write("robots.txt", robots)
    write("sitemap.xml", sitemap)
    write("llms.txt", llms)
    write(".nojekyll", "")
    print("Built index.html, about.html, 404.html, robots.txt, sitemap.xml, llms.txt")
