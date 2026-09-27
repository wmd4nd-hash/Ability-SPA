# Ability SPA & Wellness – website redesign

Homepage prototype for the new abilityspa.com. See `CLAUDE.md` for the full brief.

## What's here

- `index.html` – homepage (Bulgarian), static HTML, mobile-first
- `css/styles.css` – all styles, brand colours as CSS variables
- `images/` – real photos (WebP, 640/960 px), logo variants, OG image
- `current-site/` – saved HTML of the current homepage (for content + redirect mapping)
- `docs/preview-*.png` – screenshots at 390 px (phone) and 1440 px (desktop)

**Live preview:** https://raw.githack.com/wmd4nd-hash/Ability-SPA/claude/new-session-bmiv3x/index.html
(always shows the latest push to this branch; may take a few minutes to refresh)

Or open `index.html` locally in a browser. No build step.

Links to pages that don't exist yet (`masazhi-burgas/`, `ceni/`, `vaucheri/` …) open simple
"coming soon" pages (`noindex`) so nothing is broken in the preview. Links whose target is still a
`[PLACEHOLDER]` show a short note instead – that script and `.proto-note` are **prototype-only**.

## Status

Prototype only – platform (WordPress / static / Wix) is still to be decided.

Everything in `[SQUARE BRACKETS]` is a placeholder waiting for real data:
phone numbers, opening hours, prices, Varna address, facilities and booking link,
social links.

- Booking link (Burgas) taken from the current site: `https://book.abilityspa.com/reservations/start?site=1`
- Photos: pool (hero), jacuzzi, fitness and OG image are 1080 px originals supplied by the team; pool shots have a gentle warm grade. Sauna and salt room are still the 960 px files from the current site.
- Note: the current site's file named `БАСЕЙН-...png` (and the supplied `pool-jacuzzi.png`) actually shows cacao pods.
- Service cards (massage, therapies, cosmetics, osteopathy) still need treatment photos.
- Logo is built from the low-res PNG; replace with SVG when the vector file arrives.
- Prices are in **€** (Bulgaria uses the euro since 1 Jan 2026).
- First-visit FAQ answers contain placeholders (towels/robes, kids' rules, duration, parking). Add FAQPage JSON-LD only once all answers are confirmed.
- Varna has no online booking on the current site (bookings by phone/Viber), so the Varna card offers call + Viber.
- Review cards are empty slots – fill only with real, attributed Google/Facebook reviews.
- Hero uses the 1080 px pool photo full-width; a ≥ 2400 px original would look sharper on large desktops.

## Motion

Subtle, CSS-driven animations with no library: slow settle-in zoom and staggered fade-up in the
hero, fade/rise reveal on scroll (IntersectionObserver), soft wipe on facility photos, header
shadow on scroll. Hidden-before-reveal only applies when JS runs (`html.js`), and all motion is
disabled for `prefers-reduced-motion`.

## Layout notes

Layout takes cues from competitor thermanumera.com (full-bleed hero, key-facts band,
numbered sections, text-on-image service cards, entry prices on the homepage, reviews,
contact strip) and from AIRE, Vabali and Therme Bucharest (quick tiles for prices / first visit /
vouchers, first-visit FAQ). The hero follows Therma Numera's minimal pattern: photo,
tag line, big H1, two buttons, short caption – nothing else on the photo while keeping Ability's colours and readable type. Arches were dropped at the owner's request.
Deliberately avoided from that site: auto-opening chat widget, full-width cookie banner,
ultra-thin grey text, brand-only English H1.
