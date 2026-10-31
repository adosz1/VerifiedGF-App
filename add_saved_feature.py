import re

# Read current HTML
file_path = "c:/Users/kovia/Desktop/VerifiedGF-App/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. ADD CSS STYLES FOR SAVED FEATURE
saved_css = """
    /* ── Bookmark / Save Button on Cards ── */
    .card-save-btn {
      position: absolute;
      top: 10px;
      right: 10px;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: rgba(15, 23, 42, 0.72);
      backdrop-filter: blur(6px);
      border: 1px solid rgba(255, 255, 255, 0.25);
      color: #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 10;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .card-save-btn svg {
      width: 19px;
      height: 19px;
      transition: transform 0.2s, fill 0.2s;
    }
    .card-save-btn.saved {
      background: #FFFFFF;
      color: #EF4444;
      border-color: #EF4444;
      box-shadow: 0 4px 14px rgba(239, 68, 68, 0.4);
    }
    .card-save-btn.saved svg {
      fill: #EF4444;
      stroke: #EF4444;
    }
    .card-save-btn:active {
      transform: scale(0.85);
    }
    /* Reposition duration pill to the left of the bookmark button */
    .duration-pill {
      right: 52px !important;
    }
    /* Tab bar badge counter */
    .nav-tab-item {
      position: relative;
    }
    .nav-badge-pill {
      position: absolute;
      top: 2px;
      right: calc(50% - 18px);
      background: #EF4444;
      color: #fff;
      font-size: 9px;
      font-weight: 800;
      padding: 1px 5px;
      border-radius: 10px;
      min-width: 15px;
      text-align: center;
      line-height: 1.2;
      box-shadow: 0 2px 5px rgba(239, 68, 68, 0.5);
    }

    /* Saved View Layout */
    .saved-header-box {
      background: linear-gradient(150deg, #1E293B 0%, #0F172A 100%);
      color: #fff;
      padding: 24px 18px 26px;
      margin-bottom: 12px;
    }
    .saved-header-title {
      font-size: 24px;
      font-weight: 900;
      letter-spacing: -0.4px;
      margin-bottom: 4px;
    }
    .saved-header-sub {
      font-size: 13px;
      color: #94A3B8;
    }
    .saved-actions-bar {
      padding: 4px 16px 12px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .saved-clear-btn {
      font-size: 12px;
      font-weight: 700;
      color: #EF4444;
      background: none;
      border: none;
      cursor: pointer;
      text-decoration: underline;
    }
    .saved-empty-container {
      margin: 20px 16px;
      padding: 46px 20px;
      background: #fff;
      border: 1px dashed #CBD5E1;
      border-radius: 20px;
      text-align: center;
    }
    .saved-empty-icon {
      font-size: 52px;
      margin-bottom: 12px;
    }
    .saved-empty-heading {
      font-size: 17px;
      font-weight: 800;
      color: var(--text);
      margin-bottom: 6px;
    }
    .saved-empty-text {
      font-size: 13px;
      color: var(--muted);
      line-height: 1.5;
      margin-bottom: 18px;
    }
    .saved-detail-fav-btn {
      width: 100%;
      height: 48px;
      border-radius: 14px;
      border: 1px solid var(--border);
      background: #fff;
      color: var(--text);
      font-size: 14px;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: all 0.2s;
    }
    .saved-detail-fav-btn.is-saved {
      background: #FEF2F2;
      border-color: #FECACA;
      color: #EF4444;
    }
"""

if ".card-save-btn {" not in html:
    html = html.replace("</style>", f"{saved_css}\n  </style>")
    print("Injected Saved CSS styles successfully!")

# 2. ADD SAVED VIEW SECTION HTML
saved_view_html = """
    <!-- ── TAB 3: SAVED RESTAURANTS VIEW ── -->
    <section id="view-saved-page" class="view-page">
      <div class="saved-header-box">
        <h1 class="saved-header-title">Saved Places</h1>
        <p class="saved-header-sub">Your personal bookmarked coeliac-safe kitchens.</p>
      </div>

      <div class="saved-actions-bar">
        <span class="section-title">Bookmarked Kitchens</span>
        <div style="display:flex;align-items:center;gap:10px;">
          <span class="section-counter" id="saved-header-counter">0 saved</span>
          <button class="saved-clear-btn" id="saved-clear-all-btn" onclick="clearAllSavedRestaurants()" style="display:none;">Clear All</button>
        </div>
      </div>

      <!-- Empty State -->
      <div id="saved-empty-state" class="saved-empty-container">
        <div class="saved-empty-icon">🔖</div>
        <h3 class="saved-empty-heading">No saved restaurants yet</h3>
        <p class="saved-empty-text">Tap the bookmark icon on any restaurant card to save it here for instant access whenever you're dining out.</p>
        <button class="btn-book-primary" style="max-width: 220px; margin: 0 auto;" onclick="switchView('discover')">
          Browse All 52 Places
        </button>
      </div>

      <!-- Saved Cards Container -->
      <div id="saved-cards-list" class="cards-container">
        <!-- Rendered via JS -->
      </div>
    </section>
"""

# Insert before </main>
if '<section id="view-saved-page"' not in html:
    html = html.replace("</main>", f"{saved_view_html}\n  </main>")
    print("Injected Saved View HTML section successfully!")

# 3. UPDATE BOTTOM NAV BAR (Saved tab button)
old_tab_saved = """    <button class="nav-tab-item" id="tab-btn-saved" onclick="showToast('Saved list synced to local device ★')">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>
      </svg>
      Saved
    </button>"""

new_tab_saved = """    <button class="nav-tab-item" id="tab-btn-saved" onclick="switchView('saved')">
      <span class="nav-badge-pill" id="nav-saved-badge" style="display:none;">0</span>
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/>
      </svg>
      Saved
    </button>"""

if old_tab_saved in html:
    html = html.replace(old_tab_saved, new_tab_saved)
    print("Updated bottom nav tab for Saved!")

# 4. UPDATE CARD TEMPLATE TO INCLUDE BOOKMARK BUTTON
# Look for card template in renderCardsList()
card_btn_placeholder = '<div class="live-verified-badge">✓ 100% GF VERIFIED</div>'
card_save_btn_html = """<div class="live-verified-badge">✓ 100% GF VERIFIED</div>
        <!-- Bookmark / Save Button -->
        <button class="card-save-btn ${isRestaurantSaved(r.id) ? 'saved' : ''}" onclick="event.stopPropagation(); toggleSaveRestaurant(${r.id});" aria-label="Save Restaurant">
          <svg viewBox="0 0 24 24" fill="${isRestaurantSaved(r.id) ? '#EF4444' : 'none'}" stroke="currentColor" stroke-width="2.2">
            <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/>
          </svg>
        </button>"""

if 'class="card-save-btn' not in html:
    html = html.replace(card_btn_placeholder, card_save_btn_html)
    print("Injected bookmark button into Card Template!")

# 5. UPDATE DETAIL MODAL ACTIONS (Add Save button in detail modal)
detail_action_marker = '<button class="btn-large-secondary" onclick="shareRestaurantLink()">'
detail_fav_btn = """<button class="saved-detail-fav-btn" id="detail-modal-fav-btn" onclick="toggleSaveFromModal()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
        <span id="detail-fav-btn-label">Save to Favourites</span>
      </button>
      <button class="btn-large-secondary" onclick="shareRestaurantLink()">"""

if "id=\"detail-modal-fav-btn\"" not in html:
    html = html.replace(detail_action_marker, detail_fav_btn)
    print("Injected Save button into Detail Modal!")

# 6. JAVASCRIPT LOGIC FOR SAVED FEATURE
saved_js = """
/* ──────────────────────────────────────────────────
   SAVED RESTAURANTS LOGIC (Persistent LocalStorage)
────────────────────────────────────────────────── */
let savedRestaurantIds = [];

function loadSavedRestaurants() {
  try {
    const raw = localStorage.getItem("verifiedgf_saved_ids");
    if (raw) {
      savedRestaurantIds = JSON.parse(raw);
    } else {
      // Default with first 2 favourites for a great initial experience
      savedRestaurantIds = [0, 10];
      saveSavedRestaurantsToStorage();
    }
  } catch(e) {
    savedRestaurantIds = [0, 10];
  }
  updateSavedBadges();
}

function saveSavedRestaurantsToStorage() {
  try {
    localStorage.setItem("verifiedgf_saved_ids", JSON.stringify(savedRestaurantIds));
  } catch(e) {}
  updateSavedBadges();
}

function isRestaurantSaved(id) {
  return savedRestaurantIds.includes(id);
}

function toggleSaveRestaurant(id) {
  const r = RESTAURANTS.find(item => item.id === id);
  const name = r ? r.name : "Place";
  
  if (isRestaurantSaved(id)) {
    savedRestaurantIds = savedRestaurantIds.filter(itemId => itemId !== id);
    showToast(`Removed "${name}" from Saved`);
  } else {
    savedRestaurantIds.push(id);
    showToast(`Saved "${name}" to your list ★`);
  }
  
  saveSavedRestaurantsToStorage();
  renderCardsList();
  if (currentActiveView === "saved") {
    renderSavedCardsList();
  }
  updateDetailModalFavBtn(id);
}

function toggleSaveFromModal() {
  toggleSaveRestaurant(currentSelectedRestaurantId);
}

function updateDetailModalFavBtn(id) {
  const btn = document.getElementById("detail-modal-fav-btn");
  const label = document.getElementById("detail-fav-btn-label");
  if (!btn || !label) return;
  
  const saved = isRestaurantSaved(id);
  const svg = btn.querySelector("svg");
  if (saved) {
    btn.classList.add("is-saved");
    label.textContent = "Saved to Favourites ★";
    if (svg) svg.setAttribute("fill", "#EF4444");
  } else {
    btn.classList.remove("is-saved");
    label.textContent = "Save to Favourites";
    if (svg) svg.setAttribute("fill", "none");
  }
}

function updateSavedBadges() {
  const count = savedRestaurantIds.length;
  const navBadge = document.getElementById("nav-saved-badge");
  const headerCounter = document.getElementById("saved-header-counter");
  const clearBtn = document.getElementById("saved-clear-all-btn");

  if (navBadge) {
    navBadge.textContent = count;
    navBadge.style.display = count > 0 ? "block" : "none";
  }
  if (headerCounter) {
    headerCounter.textContent = `${count} saved`;
  }
  if (clearBtn) {
    clearBtn.style.display = count > 0 ? "block" : "none";
  }
}

function clearAllSavedRestaurants() {
  if (confirm("Remove all saved restaurants from your list?")) {
    savedRestaurantIds = [];
    saveSavedRestaurantsToStorage();
    renderCardsList();
    renderSavedCardsList();
    showToast("Cleared all saved places");
  }
}

function renderSavedCardsList() {
  const container = document.getElementById("saved-cards-list");
  const emptyState = document.getElementById("saved-empty-state");
  if (!container || !emptyState) return;

  const savedList = RESTAURANTS.filter(r => savedRestaurantIds.includes(r.id));
  updateSavedBadges();

  if (savedList.length === 0) {
    container.innerHTML = "";
    emptyState.style.display = "block";
    return;
  }

  emptyState.style.display = "none";
  container.innerHTML = savedList.map(r => `
    <article class="restaurant-card" onclick="openDetailModal(${r.id})">
      <div class="card-media">
        <div class="kitchen-mock-bg" style="background: ${r.bg};">
          <div class="grid-lines"></div>
          <span class="kitchen-mock-emoji">${r.art}</span>
          <div class="kitchen-spec-tag">AUDITED 4K CAM · SPOTLESS PREP</div>
        </div>
        <div class="live-verified-badge">✓ 100% GF VERIFIED</div>
        <div class="duration-pill">${r.duration}</div>

        <!-- Remove / Toggle Save -->
        <button class="card-save-btn saved" onclick="event.stopPropagation(); toggleSaveRestaurant(${r.id});" aria-label="Remove from Saved">
          <svg viewBox="0 0 24 24" fill="#EF4444" stroke="#EF4444" stroke-width="2.2">
            <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/>
          </svg>
        </button>

        <div class="play-video-overlay" onclick="event.stopPropagation(); launchVideoAudit(${r.id});">
          <div class="play-circle-btn">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
          </div>
          <span class="play-btn-label">Play Video Audit</span>
        </div>
      </div>

      <div class="card-body">
        <div class="card-cuisine">${r.city} • ${r.type}</div>
        <div class="card-name-row">
          <h3 class="card-restaurant-name">${r.name}</h3>
          <span class="card-distance">${r.distance}</span>
        </div>
        <div class="card-address-row">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>
          </svg>
          ${r.address}
        </div>

        <div class="safety-badges-row">
          ${r.badges.map(b => `<span class="safety-badge ${b.cls}">${b.text}</span>`).join('')}
        </div>

        <div class="card-actions-row">
          <button class="btn-book-primary" onclick="event.stopPropagation(); bookRestaurantTable(${r.id});">
            Book Table
          </button>
          <button class="btn-map-action" onclick="event.stopPropagation(); showRestaurantOnMap(${r.id});">
            📍 Map
          </button>
          <button class="btn-safety-details" onclick="event.stopPropagation(); openDetailModal(${r.id});">
            View Safety
          </button>
        </div>
      </div>
    </article>
  `).join('');
}
"""

if "SAVED RESTAURANTS LOGIC" not in html:
    # Insert right before switchView
    html = html.replace('function switchView(viewName) {', f"{saved_js}\n\nfunction switchView(viewName) {{")
    print("Injected Saved JavaScript functions!")

# 7. UPDATE switchView TO HANDLE "saved"
old_switch = """  } else if (viewName === "map") {
    document.getElementById("view-map-page").classList.add("active");
    document.getElementById("tab-btn-map").classList.add("active");
    updateMapPins();
    renderMapQuickCards();
  }
}"""

new_switch = """  } else if (viewName === "map") {
    document.getElementById("view-map-page").classList.add("active");
    document.getElementById("tab-btn-map").classList.add("active");
    updateMapPins();
    renderMapQuickCards();
  } else if (viewName === "saved") {
    document.getElementById("view-saved-page").classList.add("active");
    document.getElementById("tab-btn-saved").classList.add("active");
    renderSavedCardsList();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
}"""

if old_switch in html:
    html = html.replace(old_switch, new_switch)
    print("Updated switchView to handle 'saved' view!")

# 8. UPDATE openDetailModal TO UPDATE THE MODAL FAV BUTTON
old_open_detail = "switchDetailTab(document.querySelector(\".detail-tab-btn\"), \"protocols\");"
new_open_detail = """switchDetailTab(document.querySelector(".detail-tab-btn"), "protocols");
  updateDetailModalFavBtn(id);"""

if old_open_detail in html and "updateDetailModalFavBtn(id);" not in html:
    html = html.replace(old_open_detail, new_open_detail)
    print("Updated openDetailModal to refresh modal fav button!")

# 9. UPDATE INITIALIZATION TO LOAD SAVED RESTAURANTS
old_init = "initMapPins();\nrenderCardsList();"
new_init = "loadSavedRestaurants();\ninitMapPins();\nrenderCardsList();"

if old_init in html:
    html = html.replace(old_init, new_init)
    print("Updated initialization to call loadSavedRestaurants()!")

# Write out updated index.html
with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

# Also write to brain verifiedgf.html
with open(r"C:\Users\kovia\.gemini\antigravity\brain\3adaafdb-e0af-4a64-a056-3893d3825ecf\verifiedgf.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Saved feature integrated successfully in both files!")
