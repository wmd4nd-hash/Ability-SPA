# Sitemap – current abilityspa.com (live, 28.09.2026)

Built from the live site: the header menu, all **69 pages** in `page-sitemap.xml`, the links inside every page,
and where each of the **58 older addresses** still used in internal links ends up (checked one by one,
respecting the site's `Crawl-Delay: 20`). Raw data: `current-site/`. Redirect plan: `docs/redirect-map.md`.

Legend: **[M]** in the header menu · **[L]** reached only through links inside pages · **[H]** hidden – no menu entry
and no internal link (only via Google or the XML sitemap).

## Structure as a visitor finds it

```
abilityspa.com/  –  Начало  [M]
├── За нас  (anchor #WELCOME on the homepage)  [M]
├── СПА менюта  (6 PDF price lists)  [M]
│   ├── PDF: Ability Spa – Бургас (BG)
│   ├── PDF: Ability Spa – Burgas (EN)
│   ├── PDF: Ability Spa – Бургас (RU)
│   ├── PDF: Ability SPA&Wellness – Варна (BG)
│   ├── PDF: Ability Spa&Wellness – Варна (EN)
│   └── PDF: Ability Spa&Wellness – Варна (RU)
├── Обекти  [M]
│   ├── Ability Spa – Бургас (page title: "Insights")  /ability-spa-burgas/  [M]
│   │   ├── Хамам  /turska-banya-hamam/  [L]
│   │   ├── Tермална зона  /spa-zone/  [L]
│   │   └── Фитнес  /fitness-burgas/  [L]
│   └── Ability Spa&Wellness – Варна (page title: "Insights")  /ability-spawellness/  [M]
│       └── Групови тренировки  /massages/grupovi-trenirovki/  [L]
├── Услуги  (anchor #SERVICES on the homepage)  [M]
│   ├── Oстеопатия  /massages/osteopathy/  [M]
│   ├── Масажи  /massages/  [M]
│   │   ├── Антицелулитен масаж  /massages/anticellulite-massage/  [L]
│   │   ├── Ароматерапевтичен масаж  /massages/aromatherapy-massage/  [L]
│   │   ├── Класически масаж  /massages/classic-massage/  [L]
│   │   ├── Лимфодренажен масаж  /massages/limfodrenajen-massage/  [L]
│   │   ├── Рефлексотерапия  /massages/reflexology/  [L]
│   │   └── Спортен масаж  /massages/sport-massage/  [L]
│   ├── СПА процедури Бургас  /therapies/  [M]
│   │   ├── Терапия "Sea kissed"  /therapies/terapiya-s-morski-nutrienti/  [L]
│   │   ├── Терапия ‘’Fitness Nuts’’  /therapies/fitness-nuts-therapy/  [L]
│   │   ├── Терапия "Coffee Time"  /therapies/coffee-time-therapy/  [L]
│   │   ├── Терапия с вулканични камъни  /therapies/masaj-s-vulkanichni-kamyni/  [L]
│   │   ├── Плодова терапия "Ability SPA"  /therapies/therapy-ability-spa/  [L]
│   │   └── Терапия “Chocolate Dream”  /therapies/chocolate-dream-therapy/  [L]
│   ├── СПА процедури Варна  /spa-proceduri-varna/  [M]
│   │   ├── Терапия "Gold Amber"  /therapies/terapiya-golden-amber/  [L]
│   │   ├── Терапия "Bulgarian rose"  /therapies/terapiya-bulgarian-rose-2/  [L]
│   │   └── Терапия "Lavender Touch"  /therapies/terapiya-lavender-touch/  [L]
│   ├── Козметични процедури  /cosmetic-treatments/  [M]
│   │   ├── Aпаратни процедури с PDT лазер  /pdt-master-laser-procedures/  [L]
│   │   ├── Специални терапии за лице  /special-face-treatments/  [L]
│   │   └── Терапии за лице  /face-treatments/  [L]
│   └── Подаръчни ваучери и пакети от Ability SPA  /blog/spa-voucher/  [M]
├── Промоции  [M]
│   ├── Промоции в Ability SPA&Wellness, Варна  /promotions-varna/  [M]
│   │   └── Контакти Варна  /kontakti-varna/  [L]
│   └── Промоции в Ability SPA, Бургас  /promotions-burgas/  [M]
├── Блог  /blog/  (menu link goes through 2 redirects)  [M]
│   ├── 3 of 27 posts listed on the blog page: /blog/microblading/, /blog/masaj-polzi/, /blog/letni-trenirovki-kakvo-tribva-da-znaem/
│   └── the other 24 posts – see "Blog posts" below
├── Контакти  /contacts/  [M]
└── Footer (every page)
    └── links to Условия за ползване / Политика за поверителност use old addresses that return 404 – broken on all 69 pages
```

## Hidden pages (in the XML sitemap, but nothing links to them)

| Page | Address | Note |
|---|---|---|
| Условия за ползване | `/usloviya-za-polzvane/` |  |
| Политика за защита на личните данни и бисквитките | `/politika-za-zasthita-na-lichnite-danni-i-z/` |  |
| footer (theme template) | `/footer-ability-spa/` | Theme template page – should not be public |
| СПА Карта | `/spa-card/` | SPA card prices – no way to reach it |
| СПА етикет | `/spa-etiket/` | SPA etiquette |
| Promotions in Ability SPA&Wellness, Varna | `/promotions-ability-spawellness-varna-en/` | Only English page on the site; no language switch |

## Blog posts

27 posts. The blog page lists only **3**; the rest are reachable only if another page links to them.

| Post | Address | Listed on /blog/ | Linked from |
|---|---|---|---|
| Ретинолова терапия – Тайната на сияйната кожа | `/blog/retinolova-terapiq/` | no | – |
| Масаж през лятото – лукс или необходимост? | `/blog/masaj-prez-lyatoto/` | no | – |
| Водно дермабразио – тайната за свежа кожа през лятото | `/blog/vodno-dermabrazio-polzi/` | no | – |
| Gold терапия – златният път към сияйна кожа | `/blog/gold-therapy/` | no | – |
| Остеопатията: Естественият път към здравето | `/blog/osteopathy/` | no | – |
| Почистване на лице – първата стъпка към здрава и сияйна кожа | `/blog/pochistvane-na-lice/` | no | – |
| Кислородна терапия за лице – дълбока хидратация и подмладяване на клетъчно ниво | `/blog/kislorodna-terapia/` | no | – |
| Микроблейдинг – перфектните вежди, за които винаги сте мечтали | `/blog/microblading/` | yes | – |
| Защо спа процедурите са най-добрият избор през студените месеци | `/blog/spa-procedurite-nai-dobriat-izbor-zimata/` | no | – |
| Зимно СПА презареждане в Ability SPA ➜ един ден, посветен на вас | `/blog/zimno-spa-prezarejdane-v-ability-spa/` | no | – |
| 3 основни разлики между сауната и турската баня (хамам) | `/blog/sauna-hamam-razliki/` | no | – |
| 6 ползи за здравето от употребата на джакузи и топла вана | `/blog/djakuzi-topla-vana-polzi/` | no | – |
| Дневна СПА карта на цена от 35 лв. за незабравимо СПА преживяване | `/blog/spa-card-offer/` | no | – |
| Интервю с Илия Дамянов, управител на Ability SPA | `/blog/interview-iliya-damyanov/` | no | – |
| Лятото и грижата за кожата | `/blog/lyato-grija-za-kojata/` | no | – |
| Лятото и грижата за кожата: Защо козметичните процедури са особено важни през топлите месеци | `/blog/kozmetika-lyato/` | no | – |
| Масажът - история, ползи и препоръки | `/blog/masaj-polzi/` | yes | – |
| Петър Дамянов за Остеопатията | `/blog/petar-damyanov-osteopatia/` | no | – |
| СПА процедури с карта Multisport | `/blog/abilityspa-multisport/` | no | – |
| Що е то остеопатия и как помага? | `/blog/osteopatia-kak-pomaga/` | no | – |
| Билкова сауна – природна терапия за тялото и ума | `/blog/bilkova-sauna-prirodna-terapiya-za-tyaloto-i-uma/` | no | `/ability-spawellness/` |
| Финландска сауна - силата на топлината | `/blog/finlandska-sauna-polzi/` | no | `/ability-spawellness/` |
| Солна парна баня – дълбока грижа за дишането и кожата | `/blog/solna-parna-banya/` | no | `/ability-spawellness/` |
| Инфрачервена пейка – щадяща и изключително ефективна | `/blog/infrachervena-peika/` | no | `/ability-spawellness/` |
| Сауна, инфрачервена сауна и парна баня – ползи, разлики и как да изберем | `/blog/sauna-parna-banya-razliki-polzi/` | no | – |
| Летни тренировки: всичко, което трябва да знаем | `/blog/letni-trenirovki-kakvo-tribva-da-znaem/` | yes | – |
| Защо се чувстваме уморени през лятото? | `/blog/zashto-se-chuvstvame-umoreni-prez-lyatoto/` | no | – |

## Older addresses still used in internal links

58 addresses from earlier versions of the site (mostly Cyrillic) are still linked from pages. **29** redirect to a live page (13 of them through a chain of 2+ redirects), **29** are broken. All of them need a 301 in the new site.

| Old address | Result | Ends at | Linked from |
|---|---|---|---|
| `/therapies/терапия-с-морски-нутриенти/` | **broken (404)** | – | `/therapies/terapiya-s-morski-nutrienti/` |
| `/контакти/` | **broken (404)** | – | `/face-treatments/`, `/pdt-master-laser-procedures/`, `/special-face-treatments/` |
| `/красота/козметични-процедури-масаж-лице/` | **broken (404)** | – | `/blog/kozmetika-lyato/` |
| `/красота/козметични-терапии-за-лице/` | **broken (404)** | – | `/blog/kozmetika-lyato/` |
| `/масажи/остеопатия-2/` | **broken (404)** | – | `/blog/petar-damyanov-osteopatia/` |
| `/новини-и-събития-промоции/` | **broken (404)** | – | `/fitness-burgas/`, `/footer-ability-spa/` |
| `/новини-и-събития-промоции/abilityspa-карта-multisport-басейн-термална-зона/` | **broken (404)** | – | `/`, `/ability-spa-burgas/` |
| `/новини-и-събития-промоции/подаръчни-ваучери-от-ability-spa/` | **broken (404)** | – | `/`, `/ability-spa-burgas/`, `/blog/kozmetika-lyato/`, `/blog/masaj-prez-lyatoto/` +1 |
| `/новини-и-събития-промоции/що-е-то-остеопатия-и-как-помага/` | **broken (404)** | – | `/massages/osteopathy/` |
| `/политика-за-защита-на-личните-данни-и-з/` | **broken (404)** | – | `/footer-ability-spa/`, `/politika-za-zasthita-na-lichnite-danni-i-z/` |
| `/професионални-масажи-бургас-созопол/антицелулитен-масаж-отслабване/` | **broken (404)** | – | `/blog/masaj-polzi/` |
| `/професионални-масажи-бургас-созопол/ароматерапевтичен-масаж/` | **broken (404)** | – | `/blog/masaj-polzi/` |
| `/професионални-масажи-бургас-созопол/класически-масаж/` | **broken (404)** | – | `/blog/masaj-polzi/` |
| `/професионални-масажи-бургас-созопол/лимфодренажен-масаж/` | **broken (404)** | – | `/blog/masaj-polzi/` |
| `/професионални-масажи-бургас-созопол/масаж-на-ходила-рефлексотерапия/` | **broken (404)** | – | `/blog/masaj-polzi/` |
| `/професионални-масажи-бургас-созопол/спортен-масаж/` | **broken (404)** | – | `/blog/masaj-polzi/` |
| `/професионални-масажи-бургас/антицелулитен-масаж-отслабване/` | **broken (404)** | – | `/blog/masaj-prez-lyatoto/` |
| `/професионални-масажи-бургас/класически-масаж/` | **broken (404)** | – | `/blog/masaj-prez-lyatoto/`, `/massages/` |
| `/професионални-масажи-бургас/лимфодренажен-масаж/` | **broken (404)** | – | `/blog/masaj-prez-lyatoto/` |
| `/професионални-масажи-бургас/спортен-масаж/` | **broken (404)** | – | `/blog/masaj-prez-lyatoto/`, `/massages/` |
| `/терапии/` | **broken (404)** | – | `/`, `/footer-ability-spa/` |
| `/терапии/терапия-масаж-с-кафе/` | **broken (404)** | – | `/therapies/` |
| `/терапии/терапия-масаж-с-шоколад/` | **broken (404)** | – | `/spa-proceduri-varna/`, `/therapies/` |
| `/терапии/терапия-с-вулканични-камъни/` | **broken (404)** | – | `/blog/masaj-polzi/` |
| `/терапии/терапия-с-кафява-захар/` | **broken (404)** | – | `/therapies/` |
| `/терапии/терапия-с-морски-нутриенти/` | **broken (404)** | – | `/therapies/` |
| `/терапии/терапия-с-плодова-скраб/` | **broken (404)** | – | `/spa-proceduri-varna/`, `/therapies/` |
| `/условия-за-ползване/` | **broken (404)** | – | all 69 pages (footer/menu) |
| `/фитнес/` | **broken (404)** | – | `/spa-card/` |
| `/pdt-master-laser-лечебни-терапии/` | 1 redirect | `/pdt-master-laser-procedures/` | `/cosmetic-treatments/` |
| `/promotions/` | 1 redirect | `/promotions-ability-spawellness-varna-en/` | `/blog/spa-procedurite-nai-dobriat-izbor-zimata/` |
| `/terapiya-bulgarian-rose/` | 1 redirect | `/therapies/terapiya-bulgarian-rose-2/` | `/spa-proceduri-varna/` |
| `/terapiya-golden-amber/` | 1 redirect | `/therapies/terapiya-golden-amber/` | `/spa-proceduri-varna/` |
| `/terapiya-s-morski-nutrienti/` | 1 redirect | `/therapies/terapiya-s-morski-nutrienti/` | `/therapies/` |
| `/therapies/terapiya-bulgarian-rose/` | 1 redirect | `/therapies/terapiya-bulgarian-rose-2/` | `/spa-proceduri-varna/` |
| `/антицелулитен-масаж/` | 2 redirects | `/massages/anticellulite-massage/` | `/massages/` |
| `/ароматерапевтичен-масаж/` | 2 redirects | `/massages/aromatherapy-massage/` | `/massages/` |
| `/класически-масаж/` | 2 redirects | `/massages/classic-massage/` | `/massages/` |
| `/козметични-процедури-масаж-лице/` | 1 redirect | `/special-face-treatments/` | `/cosmetic-treatments/` |
| `/козметични-терапии-за-лице/` | 2 redirects | `/face-treatments/` | `/blog/pochistvane-na-lice/`, `/cosmetic-treatments/` |
| `/контакти-хотел-българия/` | 1 redirect | `/contacts/` | `/blog/djakuzi-topla-vana-polzi/`, `/blog/osteopathy/`, `/blog/osteopatia-kak-pomaga/`, `/blog/retinolova-terapiq/` +4 |
| `/красота/` | 1 redirect | `/cosmetic-treatments/` | `/`, `/ability-spa-burgas/`, `/blog/kozmetika-lyato/`, `/footer-ability-spa/` |
| `/лимфодренажен-масаж/` | 2 redirects | `/massages/limfodrenajen-massage/` | `/massages/` |
| `/масажи/масаж-на-ходила/` | 1 redirect | `/massages/reflexology/` | `/massages/` |
| `/масажи/остеопатия-остеопат/` | 1 redirect | `/massages/osteopathy/` | `/` |
| `/новини-и-събития-промоции/microblading/` | 1 redirect | `/blog/microblading/` | `/blog/` |
| `/новини-и-събития-промоции/spa-voucher/` | 1 redirect | `/blog/spa-voucher/` | all 69 pages (footer/menu) |
| `/новини-и-събития/` | 2 redirects | `/blog/` | all 69 pages (footer/menu) |
| `/професионални-масажи-бургас/` | 1 redirect | `/massages/` | `/`, `/ability-spa-burgas/`, `/blog/lyato-grija-za-kojata/`, `/footer-ability-spa/` |
| `/спортен-масаж/` | 2 redirects | `/massages/sport-massage/` | `/massages/` |
| `/терапия-масаж-с-кафе/` | 2 redirects | `/therapies/coffee-time-therapy/` | `/therapies/` |
| `/терапия-масаж-с-шоколад/` | 2 redirects | `/therapies/chocolate-dream-therapy/` | `/spa-proceduri-varna/`, `/therapies/` |
| `/терапия-с-вулканични-камъни/` | 2 redirects | `/therapies/masaj-s-vulkanichni-kamyni/` | `/spa-proceduri-varna/`, `/therapies/` |
| `/терапия-с-кафява-захар/` | 2 redirects | `/therapies/fitness-nuts-therapy/` | `/therapies/` |
| `/терапия-с-плодова-скраб/` | 2 redirects | `/therapies/therapy-ability-spa/` | `/spa-proceduri-varna/`, `/therapies/` |
| `/термална-зона/` | 1 redirect | `/spa-zone/` | `/ability-spa-burgas/` |
| `/фитнес-бургас/` | 2 redirects | `/fitness-burgas/` | `/ability-spa-burgas/`, `/blog/kozmetika-lyato/` |
| `/хамам-турска-баня/` | 1 redirect | `/turska-banya-hamam/` | `/` |

## Structural issues

1. **63 of 69 pages have no H1** heading.
2. **2 pages are titled "Insights"** – the Burgas and Varna location pages: `/ability-spa-burgas/`, `/ability-spawellness/`.
3. **6 pages are hidden** (no menu entry, no internal link), including the thermal zone and SPA card prices.
4. **29 broken internal links** and **13 redirect chains** from old Cyrillic addresses.
5. **Mixed URL logic:** osteopathy and Varna group training sit under `/massages/`; Varna therapies sit under `/therapies/` (the "СПА процедури Бургас" section); vouchers live under `/blog/`.
6. **Blog page lists only a few posts;** most articles are effectively orphaned.
7. **Prices only as PDFs** in the menu (6 files, 3 languages); no HTML price page.
8. **One English page** (Varna promotions) but no English site or language switch; no Russian pages.
9. **Template page `/footer-ability-spa/` is public** and listed in the sitemap.
