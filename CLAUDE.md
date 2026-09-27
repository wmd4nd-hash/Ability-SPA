# Ability SPA & Wellness – Website Redesign

Project brief for Claude Code. Read this first in every session.
Everything below comes from an SEO/UI audit and design exploration done before this project started.
Items marked **[TO CONFIRM]** are unknown and must not be invented. Use visible placeholders like `[ЦЕНА]` or `[ТЕЛЕФОН]` until real data is provided.

---

## 1. The business

- **Name:** Ability SPA & Wellness (logo reads "ABILITY SPA", with a lotus mark)
- **Current site:** https://abilityspa.com (WordPress)
- **Type:** Urban day spa inside hotels, not a nature retreat.
- **Locations:**
  - **Burgas:** ul. "Aleksandrovska" 21, city center, inside the renovated Hotel Bulgaria. This is the main location.
  - **Varna:** inside Hotel "Cherno More" (newest location).
- **Burgas facilities:**
  - Thermal zone: herbal sauna, Finnish sauna, classic steam bath, hamam, relax zone
  - Heated indoor pool with relax zone and jacuzzi, plus a children's pool at 32–33 °C
  - Fitness hall with Technogym equipment and a protein bar by the pool
  - Salt relax room
- **Service categories:** osteopathy, massages, therapies, beauty/cosmetics (including microneedle mesotherapy)
- **Other offers:** gift vouchers ("подаръчни ваучери"), promotions, Multisport cards accepted on weekdays 07:00–22:00.
- **Booking:** external online booking system (subdomain linked from the "РЕЗЕРВИРАЙ" button). **[TO CONFIRM exact URL]**
- **Reputation:** Facebook shows 100% recommend (42 reviews), about 5,000 followers, and price range $$. Reviewers praise cleanliness, staff, the pool, the saunas, and value.
- **Language:** Bulgarian is primary. English (and possibly Russian) is needed for summer tourists; currently these exist only as PDF menus.
- **Unknown [TO CONFIRM]:** phone numbers, opening hours, full price list, Varna facilities, exact booking URL, owner's decision on platform.

---

## 2. Goals of the redesign

1. Make **booking** the obvious main action on every page and device.
2. Fix the **SEO** fundamentals so the site ranks for local searches in Burgas and Varna.
3. Modernize the look while **keeping the original brand colors** and the lotus logo.
4. Be **mobile-first**, fast, and readable.

---

## 3. SEO audit findings (current site)

### Critical
- The homepage has **no H1** and no H2s. The biggest headings are H3s ("ТЕРМАЛНА ЗОНА", "БАСЕЙН И ДЖАКУЗИ"), and "Вашето място за Релакс!" is an H4.
- The homepage title is **"Начало - Ability Spa"**, with no keywords or cities.
- Both location pages (Burgas and Varna) have the wrong title **"Insights - Ability Spa"**, which is a template error.
- There are **two conflicting meta descriptions** (Yoast plus one hard-coded in the theme header) and duplicate OG tags (og:title "Ability SPA" and "Начало", plus two og:image and two og:url).
- Hidden SVG `<title>` text "Change Image on Hover in CSS" is left over from the template in four service icons.

### Important
- There's no **LocalBusiness / DaySpa schema**, only generic Organization and WebSite. There's no address, phone, hours, or geo data.
- Prices and EN/RU content exist only as **PDFs**. Polylang is installed, but there are no language pages and no hreflang.
- The Varna URL is `/ability-spawellness/`, which doesn't describe the page. URLs mix Cyrillic and English slugs.
- The site is heavy: DFD Ronneby theme, WPBakery, Slider Revolution, and 4 web fonts.
- Some images lack alt text or have generic filenames like "Untitled-design-1.png". The OG image is a small logo.

### Already fine (keep)
- The page is indexable, the canonical is correct, `lang="bg-BG"` is set, it has a viewport meta tag and Yoast installed, and it's verified in Google Search Console.
- Service pages already exist (massages, therapies, hamam, cosmetics, osteopathy, "професионални-масажи-бургас").

### Search visibility
- The brand name ranks strongly.
- For "спа център Бургас" the site appears, but the Facebook page outranks the website. Competitors are hotel spas: Atlantis, Grand Hotel Primoretz (6th Sense), Hotel Natura, and Aqua. The directory spaburgas.com also ranks.
- For "масаж Бургас" the site is **not visible**. Booking platforms (studio24, Oink, alo.bg) and dedicated massage studios win there.
- For "спа център Варна" the site ranks weakly. The site is not on the official Varna tourism list of spa and wellness centers.

### Target keywords
- **Core:** спа център Бургас, спа Бургас, уелнес Бургас, басейн Бургас, сауна Бургас
- **Services (one page each):** масаж Бургас, релаксиращ масаж Бургас, класически масаж Бургас, дълбокотъканен масаж Бургас, антицелулитен масаж Бургас, козметични процедури Бургас, мезотерапия Бургас
- **Intent:** спа ваучер Бургас, спа цени Бургас, спа в центъра на Бургас, спа за двама Бургас, спа ден Бургас
- **Varna:** спа център Варна, спа хотел Черно море Варна, масаж Варна
- **English:** spa Burgas, massage Burgas, spa Varna, day spa Burgas city center

### SEO requirements for the new site
- Exactly one H1 per page, with a logical H2/H3 structure.
- Unique title (under 60 chars) and meta description (under 155 chars) per page, containing the keyword and city.
  - Homepage title suggestion: `СПА център в Бургас и Варна | Басейн, сауна, масажи – Ability SPA`
- Only one source of meta and OG tags, with no duplicates.
- LocalBusiness/DaySpa JSON-LD for **each** location (name, address, phone, hours, geo, priceRange, sameAs social links).
- Clean, descriptive, consistent slugs, e.g. `/spa-burgas/`, `/spa-varna/`, `/masazhi-burgas/`.
- **301 redirects from every old URL** to its new equivalent, so no rankings are lost. Map all old URLs before launch.
- HTML price and service content (not PDF-only). Keep the PDFs as optional downloads.
- Bulgarian primary plus an English version with hreflang. Russian is optional **[TO CONFIRM]**.
- Descriptive alt text and filenames for every image. Use a real spa photo as the OG image.
- Fast: minimal JS, optimized images (WebP/AVIF, lazy-loading below the fold), 2 fonts maximum.

### Off-site tasks (for the owner, not code)
- Complete and actively maintain the Google Business Profiles for both locations.
- Get listed on spaburgas.com, the official Varna tourism spa list, and studio24 (already present).

---

## 4. UI/UX audit findings (current site)

1. **There's no Book button in the header** (the nav is: За нас, Спа менюта, Обекти, Услуги, Промоции, Блог, Контакти).
2. **The first mobile screen doesn't sell anything.** It shows the logo, menu, and slider, then a cookie banner covering about 25% of the screen. There's no booking, phone, or city.
3. **The four service icons stack with huge gaps on mobile** (about 1,600 px of scroll), rely on hover, and have no visible labels.
4. **Low contrast:** beige headings and links (#DDD3C0-ish) sit on white, so links look disabled.
5. **The footer is nearly empty** (only "© Ability Spa | Design by Design Depot"). There's no address, phone, hours, map, or socials.
6. **Two locations are confusing.** The facility sections describe only Burgas, and Varna gets one paragraph.
7. **There's no social proof** on the page despite excellent reviews.
8. The fonts and theme look dated and heavy.

What works: the professional photos (sauna, pool, gym, salt room), the brown/beige palette, and the alternating photo/text layout on desktop.

---

## 5. Design direction

### Colors – KEEP THE ORIGINAL ABILITY COLORS
Taken from the current site CSS:
| Token | Hex | Use |
|---|---|---|
| espresso | `#201A18` | primary dark: text, dark sections, footer, buttons |
| sand | `#DDD3C0` | brand beige: light sections, lines, text on dark |
| gold | `#C39F76` | accent: logo lotus, small details, hover |
| white | `#FFFFFF` | main background |

Contrast rules:
- **Never** put beige or gold text on white (that's the current site's main readability problem).
- Light backgrounds use `#201A18` text. Dark backgrounds use white or `#DDD3C0` text.
- Gold is for accents, lines, and large display text only, or use a darkened gold for text if needed. Check 4.5:1 contrast.

### References (inspiration only – do NOT copy logos or layouts)
1. **"Omra Spa" branding** (Behance, by Aiya Kerimova). This is the main structural reference.
   - Minimal, editorial, urban spa feel, which matches Ability's positioning
   - Small uppercase section labels with thin divider lines
   - Split panels (half text, half image), generous white space, strict grid
   - Dark text on light sand and light text on dark brown, which is readable
   - Useful assets: gift card, printed massage menu, loyalty card (stamps → free massage)
2. **"Velora" wellness retreat branding** (Behance, by Ishita Uniyal). This is the warmth reference.
   - ~~The arch motif~~ – **dropped by the owner's team (not a fan). Use clean rectangular photos and cards, as on thermanumera.com.**
   - Alternating dark-brown and cream sections for rhythm
   - Warm, calm, sunlit mood
   - Avoid its thin light text on dark/cream, because it fails contrast.

**Combined direction:** Omra's structure, typography, and readability, plus Velora's warmth (no arch shapes), all in Ability's original colors.

### Typography (proposal)
- Display: an elegant serif with **Cyrillic support** (e.g. Cormorant Garamond, which the current site already uses a Garamond family).
- Body/UI: a clean sans-serif with Cyrillic support (e.g. Jost or similar geometric sans). Avoid Inter, Roboto, and Arial.
- Use 2 fonts maximum. Body text should be at least 16 px and not in a light weight.

### Photography
- Use the real photos (sauna, pool, gym, salt room). **Higher-resolution originals are needed [TO CONFIRM]**, because the current files are about 960×720.
- The pool (blue LED wall) and gym (gray) are cool-toned. Either apply a gentle warm grade or frame them so they sit well with the warm palette.
- Add treatment and people photos if available (massage, beauty). **[TO CONFIRM]**

---

## 6. Homepage structure (target)

1. **Header:** logo, nav (Услуги, Цени, Бургас, Варна, Ваучери, Контакти), language switch BG/EN, and a **sticky "Резервирай" button**. On mobile, add a tap-to-call icon.
2. **Hero:** strong photo, an H1 like "СПА център в Бургас и Варна", one line of value, primary "Резервирай" and secondary "Виж услугите" buttons, and the city/address visible.
3. **Services:** 4 cards (Масажи, Терапии, Козметика, Остеопатия) in a 2×2 grid on mobile, each with a photo, label, "от [ЦЕНА] лв", and a link. No hover-dependent content.
4. **Facilities:** thermal zone, pool and jacuzzi, fitness, salt room, in split photo/text panels with rectangular photos.
5. **Locations:** two cards (Burgas and Varna), each with facilities, address, hours, phone, map link, and a Book button.
6. **Social proof:** rating summary (100% recommend on Facebook) plus real reviews **[TO CONFIRM]**. Don't invent quotes.
7. **Gift vouchers:** visual card and a CTA.
8. **Multisport and promotions:** short strip.
9. **Footer:** both addresses, phones, hours, map, socials (Facebook, Instagram, YouTube), quick links, and legal/cookies.
10. **Cookie banner:** a slim bottom bar, never covering the hero.

---

## 7. Technical decisions [TO CONFIRM with owner]

- **Platform:** (a) rebuild as a new custom WordPress theme (keeps the CMS and Yoast; lowest migration risk), (b) a modern static/JAMstack site, or (c) Wix (a connector exists). Decide before building.
- The booking system stays external. Just link it prominently.
- Whatever the platform, preserve SEO: redirect map, Search Console, and analytics/Facebook pixel carried over.

---

## 8. Working rules for Claude Code

- Don't invent facts, prices, phone numbers, hours, or reviews. Use `[PLACEHOLDER]`s.
- Write copy in Bulgarian first. Keep the tone calm, warm, and professional.
- Check accessibility on every component: real `<button>`/`<a>`, alt text, 4.5:1 contrast, 44 px touch targets.
- Build mobile first and test at 390 px and 1440 px.
- Keep performance lean: no slider plugins, optimized images, minimal JS.

---

## 9. Files in this project folder

LOOK AT THE REFERENCE IMAGES before designing anything. The colors must stay Ability's original colors (section 5), not the colors of the references.

```
CLAUDE.md                       <- this brief
references/
  omra-spa/omra-01..10.jpg      <- MAIN structural reference: layout, typography, section labels, readability
                                   (01 cover, 02 concept, 03 logotype, 04 clear space, 05 colour palette,
                                    06 gift certificates, 07 printed menu/price list, 08 loyalty card,
                                    09 social media, 10 closing)
  velora/velora-part-01..08.jpg <- WARMTH reference: arch motif, dark/cream section rhythm, mood
  velora/velora-full-board.jpg     (full board in one tall image)
assets/
  logo/ability-spa-logo.png     <- current logo (dark text + beige lotus, transparent PNG, low-res)
  photos/sauna-thermal-zone.png
  photos/salt-relax-room.png
  photos/pool-jacuzzi.png
  photos/fitness-technogym.jpg  <- real photos from the current site (about 960 px wide, low-res)
current-site/
  current-homepage-source.html  <- saved HTML of the current homepage (for SEO/content reference)
  current-homepage-snapshot.zip <- full snapshot with CSS/images (mobile version)
  screenshots/                  <- renders of the current homepage, desktop and mobile.
                                   Note: slider photos and web fonts did not load in these renders,
                                   so blank areas and the serif fallback font are rendering gaps, not real design.
```

Reference images are for inspiration only. Do not copy the Omra or Velora logos, names, or layouts one-to-one.

### Still missing [TO CONFIRM]
- Logo in vector format (SVG/AI/PDF)
- High-resolution original photos, plus treatment/people photos
- Texts, full price list, phone numbers, opening hours, Varna details
- Exact booking URL
- Platform decision (section 7)
