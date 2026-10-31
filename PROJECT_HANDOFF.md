# CoeliSafe (VerifiedGF) — Project Handoff

## 1. Exact Local Paths
- **Project Root Folder:** `c:\Users\kovia\Desktop\VerifiedGF-App`
- **Primary Application File (Single-File SPA):** `c:\Users\kovia\Desktop\VerifiedGF-App\index.html`
- **SPA Routing Config:** `c:\Users\kovia\Desktop\VerifiedGF-App\_redirects`
- **Google Sheet CSV Cache/Template:** `c:\Users\kovia\Desktop\VerifiedGF-App\coelisafe-google-sheet-template.csv`
- **1-Click Sync & Packaging Scripts:**
  - `c:\Users\kovia\Desktop\VerifiedGF-App\Publish-CoeliSafe-Live.bat`
  - `c:\Users\kovia\Desktop\VerifiedGF-App\Sync-And-Publish.ps1`
- **Legal & B2B Contracts:** `c:\Users\kovia\Desktop\VerifiedGF-App\CoeliSafe-Legal-Contracts.md`
- **Cloudflare Upload Bundle:** `c:\Users\kovia\Desktop\CoeliSafe-Cloudflare-Deploy.zip`

---

## 2. Tech Stack & Architecture
- **Frontend:** Vanilla HTML5, CSS3 (2026 Modern Minimalist design system with dark/light mode variables), and Vanilla ES6+ JavaScript — self-contained inside `index.html` with zero build step required.
- **Typography:** `Plus Jakarta Sans` (headings/brand) + `Inter` (body/UI).
- **Interactive Map & Geolocation:**
  - **Leaflet.js (`v1.9.4`)** + free **OpenStreetMap** tiles (`#leaflet-map-container`).
  - **Live User GPS (`locateUserOnMap` & `renderUserBlueDotOnMap`):** HTML5 Geolocation (`getCurrentPosition` + `watchPosition`) rendering a draggable pulsing blue marker (`.user-gps-marker`), accuracy halo (`L.circle`), and real-time Haversine distance (`calculateDistanceKm` / `updateDistancesFromUserLocation`).
- **Localization (i18n):**
  - Default language is **Hungarian (`hu`)** via an instant zero-lag built-in DOM text-node dictionary (`BUILTIN_HU_DICTIONARY` + `applyBuiltInLanguage`), with smart region/timezone detection (`detectSmartRegionLanguage`) and 1-tap `🇭🇺 HU ↔ 🇬🇧 EN` header toggle.
- **Hosting & Deployment:**
  - **Cloudflare Pages:** Project `coelisafe-app` (`https://coelisafe-app.pages.dev`, transitioning custom domain `coelisafe.com` via Name.com nameservers `ishaan.ns.cloudflare.com` and `stella.ns.cloudflare.com`).
  - **Live Data Backend:** Published Google Sheets CSV (`COELISAFE_LIVE_SHEET_CSV_URL`) synced client-side on page load (`syncLiveGoogleSheetRestaurants`) and embedded at build time (`COELISAFE_EMBEDDED_CSV`).

---

## 3. Data Structure (`RESTAURANTS` Array)
All venues live in the `const RESTAURANTS = [...]` array inside `index.html`.
- **`id === 0`** (or any item with `verified: true`, or `status: "verified"`): Rendered as a **100% Verified GF Kitchen** with full safety protocols, 4K video audit modal, booking/directions CTA, and live map pin (`isVenueVerified(r)`).
- **`id > 0`** (without `verified: true`): Rendered as a **Pending Video Audit** waitlist card (`⏳ Pending Video Audit`).

### Restaurant Object Schema:
```js
{
  id: 0,                                  // Unique integer ID (0 = Showcase Verified Venue)
  verified: true,                         // Boolean flag for verified status
  name: "Tisza Bistro Szeged (Showcase)", // Venue display name
  type: "HUNGARIAN & MODERN BISTRO",      // Uppercase category/cuisine subtitle
  category: "fine-dining",                // Filter key: "szeged" | "budapest" | "debrecen" | "pecs" | "uk" | "bakery" | "fine-dining" | "asian" | "takeaway"
  city: "Szeged",                         // City name for search & filtering
  distance: "0.2 km away",                // Dynamically updated via Haversine when user GPS is active
  address: "Kárász utca 12., 6720 Szeged, Hungary",
  phone: "+36 62 555 019",                // Clickable tel: link in details modal
  website: "https://tiszabistroszeged.hu",// External venue website or menu URL
  bookingUrl: "https://...",              // Direct table reservation URL
  coords: [46.2530, 20.1414],             // [lat, lng] for Leaflet map marker & GPS distance math
  duration: "0:45 4K AUDIT",              // Video audit badge label
  videoUrl: "https://...",                // MP4/WebM URL for the 4K kitchen audit player
  art: "🍲",                              // Emoji icon for card & map strip
  bg: "linear-gradient(135deg, #0A2E36 0%, #0F4C5C 100%)",
  badges: [
    { text: "✓ Separate GF Prep Area", cls: "badge-green" },
    { text: "✓ Dedicated Fryer", cls: "badge-green" },
    { text: "✓ CoeliSafe Video Audited", cls: "badge-blue" }
  ],
  protocols: [
    { title: "Dedicated Prep Surface", desc: "..." }
  ],
  menuHighlights: [
    { item: "Szegedi Halászlé (GF)", price: "4 490 Ft", note: "100% GF" }
  ]
}
```

---

## 4. How to Add New Restaurants or UI Updates

### A. Adding or Updating Restaurants (No Code Edit Needed)
1. **Via Google Sheets (Instant Live Sync):**
   - Add a row to the connected Google Sheet (columns: `name, city, category, type, address, phone, website, bookingUrl, videoUrl, lat, lng, status, badges, menuHighlights`).
   - Set `status` to `verified` to publish as a live verified venue (with map pin and video audit) or `pending` for waitlist.
   - `syncLiveGoogleSheetRestaurants()` automatically fetches and merges new rows in visitors' browsers on page load.
2. **Via In-App Founder Admin Panel (`#admin`):**
   - Open `index.html#admin` (or click the hidden founder trigger in Settings) to add a venue via form, sync the Google Sheet URL, or export updated HTML.

### B. Making UI / Code Updates
1. Edit `c:\Users\kovia\Desktop\VerifiedGF-App\index.html` directly.
   - *Note on File Line Endings:* `index.html` uses Windows `CRLF` (`\r\n`) line endings. When using automated file-editing tools, target single unique lines to avoid multi-line newline mismatches.
   - If adding new English UI strings, add their Hungarian translation key-value pair to `BUILTIN_HU_DICTIONARY` inside `index.html`.
2. **Local Testing (0 Credits):**
   - Open `c:\Users\kovia\Desktop\VerifiedGF-App\index.html` directly in any browser and press `F5` to test.
3. **Deploying to Production (Cloudflare Pages):**
   - Double-click `c:\Users\kovia\Desktop\VerifiedGF-App\Publish-CoeliSafe-Live.bat` to embed the latest Google Sheet CSV into `index.html` and generate `c:\Users\kovia\Desktop\CoeliSafe-Cloudflare-Deploy.zip`.
   - In Cloudflare Pages (`Workers & Pages -> coelisafe-app -> Create new deployment`), drag-and-drop the `VerifiedGF-App` folder (or `CoeliSafe-Cloudflare-Deploy.zip`) and click **Save and Deploy**.
