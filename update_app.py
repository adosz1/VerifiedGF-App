import json

# Read the compiled 52 restaurants
with open("c:/Users/kovia/Desktop/VerifiedGF-App/restaurants_data.json", "r", encoding="utf-8") as f:
    restaurants_data = json.load(f)

# Read the current index.html
with open("c:/Users/kovia/Desktop/VerifiedGF-App/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Update Hero text and counters
html = html.replace("7 Certified 100% GF Kitchens", "52 Certified 100% GF Kitchens Across the UK")
html = html.replace("7 verified", f"{len(restaurants_data)} verified")
html = html.replace("Map (7)", f"Map ({len(restaurants_data)})")
html = html.replace("Search Burton upon Trent...", "Search 50+ venues, cities (London, Manchester, Burton), or dishes...")

# Update the filter chips HTML
old_chips = """      <div class="filter-scroll" role="tablist">
        <button class="filter-chip active" data-category="all" onclick="applyFilterCategory(this)">All (7)</button>
        <button class="filter-chip" data-category="dedicated" onclick="applyFilterCategory(this)">Dedicated Only</button>
        <button class="filter-chip" data-category="cafe" onclick="applyFilterCategory(this)">Bakery & Café</button>
        <button class="filter-chip" data-category="fine" onclick="applyFilterCategory(this)">Fine Dining</button>
        <button class="filter-chip" data-category="asian" onclick="applyFilterCategory(this)">Asian Cuisine</button>
        <button class="filter-chip" data-category="takeaway" onclick="applyFilterCategory(this)">Takeaway Safe</button>
      </div>"""

new_chips = """      <div class="filter-scroll" role="tablist">
        <button class="filter-chip active" data-category="all" onclick="applyFilterCategory(this)">All UK (52)</button>
        <button class="filter-chip" data-category="midlands" onclick="applyFilterCategory(this)">Midlands & Burton (10)</button>
        <button class="filter-chip" data-category="london" onclick="applyFilterCategory(this)">London (16)</button>
        <button class="filter-chip" data-category="north" onclick="applyFilterCategory(this)">Manchester & North (10)</button>
        <button class="filter-chip" data-category="south" onclick="applyFilterCategory(this)">South & West (8)</button>
        <button class="filter-chip" data-category="scotland" onclick="applyFilterCategory(this)">Scotland (8)</button>
        <button class="filter-chip" data-category="cafe" onclick="applyFilterCategory(this)">Bakery & Café</button>
        <button class="filter-chip" data-category="fine" onclick="applyFilterCategory(this)">Fine Dining</button>
        <button class="filter-chip" data-category="asian" onclick="applyFilterCategory(this)">Asian & Latin</button>
        <button class="filter-chip" data-category="takeaway" onclick="applyFilterCategory(this)">Takeaway & Chipper</button>
      </div>"""

if old_chips in html:
    html = html.replace(old_chips, new_chips)

# Update Map Header Subtitle
html = html.replace('<div class="map-header-sub" id="map-subtitle">7 Certified 100% GF Kitchens</div>',
                    f'<div class="map-header-sub" id="map-subtitle">{len(restaurants_data)} Certified 100% GF Kitchens Across UK</div>')

# Update RESTAURANTS JS constant
start_marker = "const RESTAURANTS = ["
end_marker = "/* ──────────────────────────────────────────────────\n   2. APP STATE & ROUTING"

idx_start = html.find(start_marker)
idx_end = html.find(end_marker)

if idx_start != -1 and idx_end != -1:
    restaurants_js = "const RESTAURANTS = " + json.dumps(restaurants_data, indent=2) + ";\n\n"
    html = html[:idx_start] + restaurants_js + html[idx_end:]
    print("Replaced RESTAURANTS constant successfully!")
else:
    print("ERROR: Could not find RESTAURANTS markers in HTML!")

# Write updated index.html
with open("c:/Users/kovia/Desktop/VerifiedGF-App/index.html", "w", encoding="utf-8") as f:
    f.write(html)

# Also update the brain artifact verifiedgf.html
with open(r"C:\Users\kovia\.gemini\antigravity\brain\3adaafdb-e0af-4a64-a056-3893d3825ecf\verifiedgf.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated both index.html and verifiedgf.html with 52 restaurants!")
