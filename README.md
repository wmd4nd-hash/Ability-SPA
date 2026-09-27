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

## Status

Prototype only – platform (WordPress / static / Wix) is still to be decided.

Everything in `[SQUARE BRACKETS]` is a placeholder waiting for real data:
phone numbers, opening hours, prices, Varna address, facilities and booking link,
social links.

- Booking link (Burgas) taken from the current site: `https://book.abilityspa.com/reservations/start?site=1`
- Photos: sauna, fitness and salt room are real but low-res (960 px). The gym photo has a gentle warm grade.
- **Pool photo is missing** – the supplied `pool-jacuzzi.png` actually shows cacao pods, so the pool slot is still a placeholder.
- Service cards (massage, therapies, cosmetics, osteopathy) still need treatment photos.
- Logo is built from the low-res PNG; replace with SVG when the vector file arrives.
