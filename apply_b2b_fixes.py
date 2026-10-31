import json, re

file_path = "c:/Users/kovia/Desktop/VerifiedGF-App/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update hardcoded placeholder in HTML (Detail Modal template & initial state)
# Update category tag to INDEPENDENT GASTROPUB
html = html.replace(
    '<div class="detail-header-cuisine" id="detail-cuisine">Independent Gastropub</div>',
    '<div class="detail-header-cuisine" id="detail-cuisine">INDEPENDENT GASTROPUB</div>'
)

# Update restaurant name to The Dial
html = html.replace(
    '<h2 class="detail-header-title" id="detail-name">The Trentside Tavern</h2>',
    '<h2 class="detail-header-title" id="detail-name">The Dial</h2>'
)

# Update address to Station Street, Burton upon Trent, DE14 1BX
html = html.replace(
    '<span id="detail-address">27 Riverside Walk, Burton upon Trent, DE14 1RS</span>',
    '<span id="detail-address">Station Street, Burton upon Trent, DE14 1BX</span>'
)
html = html.replace(
    '<div style="font-weight: 700;" id="c-line-addr">27 Riverside Walk, Burton upon Trent</div>',
    '<div style="font-weight: 700;" id="c-line-addr">Station Street, Burton upon Trent, DE14 1BX</div>'
)

# Update distance text placeholder in contact card
html = html.replace(
    '<div style="font-size: 11.5px; color: var(--muted);" id="c-line-dist">0.4 miles from town centre</div>',
    '<div style="font-size: 11.5px; color: var(--muted);" id="c-line-dist">📍 0.3 miles away · 5 min walk</div>'
)

# Update Video modal placeholder title
html = html.replace(
    '<div class="vmb-title" id="audit-venue-title">The Trentside Tavern - Kitchen Tour</div>',
    '<div class="vmb-title" id="audit-venue-title">The Dial — Kitchen Video Audit</div>'
)
html = html.replace(
    '<div class="vmb-title" id="audit-venue-title">The Trentside Tavern — Kitchen Tour</div>',
    '<div class="vmb-title" id="audit-venue-title">The Dial — Kitchen Video Audit</div>'
)

# Update sheet placeholder
html = html.replace(
    '<div class="sheet-name" id="sheet-target-name">Restaurant Name</div>',
    '<div class="sheet-name" id="sheet-target-name">The Dial</div>'
)
html = html.replace(
    '<span id="sheet-target-cuisine">Gastropub</span>',
    '<span id="sheet-target-cuisine">INDEPENDENT GASTROPUB</span>'
)

# 2. Update venue 0 in restaurants_data.json and inside HTML
with open("c:/Users/kovia/Desktop/VerifiedGF-App/restaurants_data.json", "r", encoding="utf-8") as f:
    venues = json.load(f)

# Update venue 0
venues[0]["name"] = "The Dial"
venues[0]["type"] = "INDEPENDENT GASTROPUB"
venues[0]["address"] = "Station Street, Burton upon Trent, DE14 1BX"
venues[0]["shortLoc"] = "Station Street · 0.3 miles away"
venues[0]["distance"] = "0.3 miles away"
venues[0]["web"] = "thedial.co.uk"
venues[0]["phone"] = "01283 544 444"
venues[0]["ctaText"] = "Book Table"

# Also clean up all venue distances so none have clunky text like "London Central"
for v in venues:
    d = v.get("distance", "")
    if "London" in d or "Glasgow" in d or "Manchester" in d or "Leeds" in d:
        v["distance"] = "1.2 miles away"
    elif " mi" in d and "away" not in d:
        v["distance"] = f"{d} away"
    elif not d.endswith("away") and not d.endswith("walk"):
        v["distance"] = f"{d} away" if d else "0.5 miles away"
    
    # Set appropriate ctaText
    cats = v.get("categories", [])
    t = v.get("type", "").upper()
    if "CAFE" in cats or "BAKERY" in t or "CAFÉ" in t or "GELATO" in t or "PATISSERIE" in t:
        v["ctaText"] = "View Menu"
    elif "TAKEAWAY" in cats or "CHIPPER" in t or "STREET FOOD" in t or "TAQUERIA" in t:
        v["ctaText"] = "Get Directions"
    else:
        v["ctaText"] = "Book Table"

# Save updated dataset
with open("c:/Users/kovia/Desktop/VerifiedGF-App/restaurants_data.json", "w", encoding="utf-8") as f:
    json.dump(venues, f, indent=2)

print("Updated venues in JSON!")

# Replace RESTAURANTS in HTML
start_marker = "const RESTAURANTS = ["
end_marker = "/* ──────────────────────────────────────────────────\n   2. APP STATE & ROUTING"

idx_start = html.find(start_marker)
idx_end = html.find(end_marker)

if idx_start != -1 and idx_end != -1:
    restaurants_js = "const RESTAURANTS = " + json.dumps(venues, indent=2) + ";\n\n"
    html = html[:idx_start] + restaurants_js + html[idx_end:]
    print("Replaced RESTAURANTS array in index.html!")

# 3. Add dynamic CTA helper function and B2B comment in JavaScript
b2b_cta_script = """
/* ==========================================================================
   B2B SALES PITCH / DYNAMIC CTA BUTTON CONFIGURATION
   --------------------------------------------------------------------------
   To customize the primary blue action button for different venue types:
   - Pubs & Gastropubs (e.g. The Dial): Set to "Book Table"
   - Walk-in venues (Bakeries & Cafes): Change to "Get Directions" or "View Menu"
   - Fast Casual & Takeaways: Change to "Order Online" or "Get Directions"
   ========================================================================== */
function getCtaButtonText(restaurant) {
  if (restaurant && restaurant.ctaText) {
    return restaurant.ctaText;
  }
  const type = (restaurant.type || "").toUpperCase();
  const cats = restaurant.categories || [];
  
  // Walk-in venues like bakeries or cafes
  if (cats.includes("cafe") || type.includes("BAKERY") || type.includes("CAFÉ") || type.includes("GELATO")) {
    return "View Menu"; /* <-- Change here to 'Get Directions' or 'View Menu' for walk-in venues */
  }
  
  // Takeaway and fast casual
  if (cats.includes("takeaway") || type.includes("TAKEAWAY") || type.includes("CHIP")) {
    return "Get Directions";
  }
  
  // Default for pubs, gastropubs, and dining restaurants
  return "Book Table";
}
"""

if "function getCtaButtonText(" not in html:
    html = html.replace("let currentCategoryFilter =", f"{b2b_cta_script}\nlet currentCategoryFilter =")
    print("Injected getCtaButtonText function!")

# 4. Update Card Template to use dynamic CTA and clean distance indicator
# Replace card distance line
old_dist_span = '<span class="card-distance">${r.distance}</span>'
new_dist_span = '<span class="card-distance">📍 ${r.distance}</span>'
html = html.replace(old_dist_span, new_dist_span)

# Replace card CTA button
old_card_btn = """        <!-- Action Row -->
        <div class="card-actions-row">
          <button class="btn-book-primary" onclick="event.stopPropagation(); bookRestaurantTable(${r.id});">
            Book Table
          </button>"""

new_card_btn = """        <!-- Action Row (Dynamic CTA for B2B Venue Pitch) -->
        <!-- Note: Change default text to 'Get Directions' or 'View Menu' for walk-in bakeries/cafes in getCtaButtonText() -->
        <div class="card-actions-row">
          <button class="btn-book-primary" onclick="event.stopPropagation(); bookRestaurantTable(${r.id});">
            ${getCtaButtonText(r)}
          </button>"""

html = html.replace(old_card_btn, new_card_btn)

# Also in saved cards template
old_saved_btn = """        <div class="card-actions-row">
          <button class="btn-book-primary" onclick="event.stopPropagation(); bookRestaurantTable(${r.id});">
            Book Table
          </button>"""
html = html.replace(old_saved_btn, new_card_btn)

# 5. Fix the clunky distance text in JS (openDetailModal & map pin click)
# In openDetailModal:
old_contact_dist = 'document.getElementById("c-line-dist").textContent = `${r.distance} from Burton railway station`;'
new_contact_dist = 'document.getElementById("c-line-dist").textContent = `📍 ${r.distance}`;'
html = html.replace(old_contact_dist, new_contact_dist)

# In openDetailModal detail-book-now-btn:
old_detail_cta = 'document.getElementById("detail-book-now-btn").onclick = () => bookRestaurantTable(r.id);'
new_detail_cta = """document.getElementById("detail-book-now-btn").textContent = `📅 ${getCtaButtonText(r)} (100% Free)`;
  document.getElementById("detail-book-now-btn").onclick = () => bookRestaurantTable(r.id);"""
html = html.replace(old_detail_cta, new_detail_cta)

# In onMapPinClicked:
old_route_label = 'document.getElementById("route-text-label").textContent = `${r.distance} walk from Burton Station (safe route)`;'
new_route_label = 'document.getElementById("route-text-label").textContent = `📍 ${r.distance} · Walking route displayed`;'
html = html.replace(old_route_label, new_route_label)

# In onMapPinClicked sheet-book-btn:
old_sheet_btn = 'document.getElementById("sheet-book-btn").onclick = () => bookRestaurantTable(r.id);'
new_sheet_btn = """document.getElementById("sheet-book-btn").textContent = `📅 ${getCtaButtonText(r)}`;
  document.getElementById("sheet-book-btn").onclick = () => bookRestaurantTable(r.id);"""
html = html.replace(old_sheet_btn, new_sheet_btn)

# Write out updated index.html
with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

# Also update brain verifiedgf.html
with open(r"C:\Users\kovia\.gemini\antigravity\brain\3adaafdb-e0af-4a64-a056-3893d3825ecf\verifiedgf.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Applied all B2B localization & dynamic CTA fixes successfully!")
