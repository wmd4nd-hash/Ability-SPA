# Sitemap – new abilityspa.com (proposal)

**61 pages + 27 blog posts.** 35 pages move from an old address (301 redirect), 2 keep their address, 24 are new – mostly to cover the target keywords in the brief, give Varna its own pages, and replace the PDF-only prices with real HTML pages. English mirrors the main pages under `/en/`; Russian is optional.

Rules behind it: short Latin slugs with keyword + city · one H1 and one main keyword per page · every service reachable in max. 2 clicks from the homepage · nothing hidden (every page in the menu, the footer or a hub page) · no page for template parts · vouchers and prices are pages, not blog posts or PDFs.

## Navigation

**Header:** Услуги ▾ (Масажи · Терапии · Козметика · Остеопатия) · Цени · Бургас · Варна · Ваучери · Контакти · BG / EN · Резервирай (бутон)

**Footer:** Бургас и Варна: адрес, часове, телефони, Viber/WhatsApp, соц. мрежи · Пакети · Промоции · Първо посещение · За нас · Блог · Общи условия · Поверителност · Бисквитки

## Structure

```
abilityspa.com/
├── Начало
│   └── /  –  Начало – СПА център в Бургас и Варна  [запазена]
├── Бургас · Ability Spa
│   ├── /spa-burgas/  –  СПА център в Бургас – хотел „България“  [преместена]
│   ├── /spa-burgas/termalna-zona/  –  Термална зона: сауни, парна баня  [преместена]
│   ├── /spa-burgas/hamam/  –  Хамам – турска баня  [преместена]
│   ├── /spa-burgas/basein/  –  Басейн, джакузи и детски басейн  [нова]
│   ├── /spa-burgas/solna-staya/  –  Солна стая  [нова]
│   └── /fitnes-burgas/  –  Фитнес Technogym  [преместена]
├── Варна · Ability Spa&Wellness
│   ├── /spa-varna/  –  СПА център във Варна – хотел „Черно море“  [преместена]
│   ├── /spa-varna/termalna-zona/  –  Термална зона и инфрачервена пейка  [нова]
│   ├── /spa-varna/fitnes/  –  Фитнес Technogym  [нова]
│   ├── /spa-varna/grupovi-trenirovki/  –  Групови тренировки: йога, пилатес, kango jumps, табата  [преместена]
│   └── /masazhi-varna/  –  Масажи във Варна  [нова]
├── Масажи
│   ├── /masazhi-burgas/  –  Масажи в Бургас  [преместена]
│   ├── /masazhi-burgas/klasicheski-masazh/  –  Класически масаж  [преместена]
│   ├── /masazhi-burgas/dalbokotaken-masazh/  –  Дълбокотъканен масаж  [нова]
│   ├── /masazhi-burgas/antitseluliten-masazh/  –  Антицелулитен масаж  [преместена]
│   ├── /masazhi-burgas/sporten-masazh/  –  Спортен масаж  [преместена]
│   ├── /masazhi-burgas/aromaterapevtichen-masazh/  –  Ароматерапевтичен масаж  [преместена]
│   ├── /masazhi-burgas/limfodrenazhen-masazh/  –  Лимфодренажен масаж  [преместена]
│   ├── /masazhi-burgas/refleksoterapiya/  –  Рефлексотерапия  [преместена]
│   ├── /masazhi-burgas/terapevtichen-masazh/  –  Терапевтичен масаж  [нова]
│   └── /masazhi-burgas/presoterapiya/  –  Пресотерапия  [нова]
├── Остеопатия
│   └── /osteopatiya-burgas/  –  Остеопатия – Петър Дамянов  [преместена]
├── СПА терапии
│   ├── /terapii/  –  СПА терапии за тяло (Бургас и Варна)  [преместена]
│   ├── /terapii/vulkanichni-kamani/  –  Масаж с вулканични камъни  [преместена]
│   ├── /terapii/plodova-terapiya-ability-spa/  –  Плодова терапия „Ability SPA“  [преместена]
│   ├── /terapii/chocolate-dream/  –  Chocolate Dream  [преместена]
│   ├── /terapii/coffee-time/  –  Coffee Time  [преместена]
│   ├── /terapii/fitness-nuts/  –  Fitness Nuts  [преместена]
│   ├── /terapii/sea-kissed/  –  Sea Kissed  [преместена]
│   ├── /terapii/gold-amber/  –  Gold Amber (Варна)  [преместена]
│   ├── /terapii/bulgarian-rose/  –  Bulgarian Rose (Варна)  [преместена]
│   └── /terapii/lavender-touch/  –  Lavender Touch (Варна)  [преместена]
├── Козметика
│   ├── /kozmetika-burgas/  –  Козметични процедури в Бургас  [преместена]
│   ├── /kozmetika-burgas/terapii-za-litse/  –  Терапии за лице (почистване, дермабразио, кислородна…)  [преместена]
│   ├── /kozmetika-burgas/spetsialni-terapii-za-litse/  –  Специални терапии (Gold, витамин C, микронидлинг…)  [преместена]
│   ├── /kozmetika-burgas/pdt-lazer/  –  Апаратни процедури с PDT лазер  [преместена]
│   ├── /kozmetika-burgas/mezoterapiya/  –  Мезотерапия (микроиглена и безиглена)  [нова]
│   └── /kozmetika-burgas/mikroblejding/  –  Микроблейдинг и вежди  [нова]
├── Цени, пакети, ваучери
│   ├── /ceni/  –  Цени – всички услуги в HTML (+ PDF за изтегляне)  [нова]
│   ├── /paketi/  –  СПА пакети  [нова]
│   ├── /paketi/spa-za-dvama/  –  СПА пакет за двама  [нова]
│   ├── /vaucheri/  –  Подаръчни ваучери  [преместена]
│   ├── /promocii/  –  Промоции  [нова]
│   ├── /promocii/burgas/  –  Промоции – Бургас  [преместена]
│   └── /promocii/varna/  –  Промоции – Варна  [преместена]
├── Информация
│   ├── /parvo-poseshtenie/  –  Първо посещение: какво да взема, правила, СПА етикет, деца, Multisport  [нова]
│   ├── /za-nas/  –  За нас и екипът  [нова]
│   ├── /kontakti/  –  Контакти – Бургас и Варна  [преместена]
│   └── /blog/  –  Блог (27 статии, адресите остават)  [запазена]
├── Правни
│   ├── /obshti-usloviya/  –  Общи условия  [преместена]
│   ├── /poveritelnost/  –  Поверителност  [преместена]
│   └── /biskvitki/  –  Бисквитки  [нова]
└── English (/en/)
    ├── /en/  –  Home – Spa in Burgas & Varna  [нова]
    ├── /en/spa-burgas/  –  Ability Spa Burgas  [нова]
    ├── /en/spa-varna/  –  Ability Spa&Wellness Varna  [нова]
    ├── /en/massages/  –  Massages  [нова]
    ├── /en/prices/  –  Prices  [нова]
    ├── /en/vouchers/  –  Gift vouchers  [нова]
    ├── /en/promotions/varna/  –  Promotions – Varna  [преместена]
    └── /en/contact/  –  Contact  [нова]
```

## Pages, keywords and where the old content comes from

| Address | Page | Main keyword | Status | Replaces (301 from) |
|---|---|---|---|---|
| **Начало** | | | | |
| `/` | Начало – СПА център в Бургас и Варна | спа център Бургас · спа Бургас · спа Варна | запазена | – |
| **Бургас · Ability Spa** | | | | |
| `/spa-burgas/` | СПА център в Бургас – хотел „България“ | спа център Бургас · спа в центъра на Бургас | преместена | `/ability-spa-burgas/` |
| `/spa-burgas/termalna-zona/` | Термална зона: сауни, парна баня | сауна Бургас | преместена | `/spa-zone/` |
| `/spa-burgas/hamam/` | Хамам – турска баня | хамам Бургас | преместена | `/turska-banya-hamam/` |
| `/spa-burgas/basein/` | Басейн, джакузи и детски басейн | басейн Бургас | нова | – |
| `/spa-burgas/solna-staya/` | Солна стая | солна стая Бургас | нова | – |
| `/fitnes-burgas/` | Фитнес Technogym | фитнес Бургас | преместена | `/fitness-burgas/` |
| **Варна · Ability Spa&Wellness** | | | | |
| `/spa-varna/` | СПА център във Варна – хотел „Черно море“ | спа център Варна · спа хотел Черно море Варна | преместена | `/ability-spawellness/`, `/spa-proceduri-varna/` |
| `/spa-varna/termalna-zona/` | Термална зона и инфрачервена пейка | сауна Варна | нова | – |
| `/spa-varna/fitnes/` | Фитнес Technogym | фитнес Варна | нова | – |
| `/spa-varna/grupovi-trenirovki/` | Групови тренировки: йога, пилатес, kango jumps, табата | йога Варна · пилатес Варна | преместена | `/massages/grupovi-trenirovki/` |
| `/masazhi-varna/` | Масажи във Варна | масаж Варна | нова | – |
| **Масажи** | | | | |
| `/masazhi-burgas/` | Масажи в Бургас | масаж Бургас · релаксиращ масаж Бургас | преместена | `/massages/` |
| `/masazhi-burgas/klasicheski-masazh/` | Класически масаж | класически масаж Бургас | преместена | `/massages/classic-massage/` |
| `/masazhi-burgas/dalbokotaken-masazh/` | Дълбокотъканен масаж | дълбокотъканен масаж Бургас | нова | – |
| `/masazhi-burgas/antitseluliten-masazh/` | Антицелулитен масаж | антицелулитен масаж Бургас | преместена | `/massages/anticellulite-massage/` |
| `/masazhi-burgas/sporten-masazh/` | Спортен масаж | спортен масаж Бургас | преместена | `/massages/sport-massage/` |
| `/masazhi-burgas/aromaterapevtichen-masazh/` | Ароматерапевтичен масаж | ароматерапия Бургас | преместена | `/massages/aromatherapy-massage/` |
| `/masazhi-burgas/limfodrenazhen-masazh/` | Лимфодренажен масаж | лимфодренаж Бургас | преместена | `/massages/limfodrenajen-massage/` |
| `/masazhi-burgas/refleksoterapiya/` | Рефлексотерапия | рефлексотерапия Бургас | преместена | `/massages/reflexology/` |
| `/masazhi-burgas/terapevtichen-masazh/` | Терапевтичен масаж | терапевтичен масаж Бургас | нова | – |
| `/masazhi-burgas/presoterapiya/` | Пресотерапия | пресотерапия Бургас | нова | – |
| **Остеопатия** | | | | |
| `/osteopatiya-burgas/` | Остеопатия – Петър Дамянов | остеопат Бургас | преместена | `/massages/osteopathy/` |
| **СПА терапии** | | | | |
| `/terapii/` | СПА терапии за тяло (Бургас и Варна) | спа процедури Бургас | преместена | `/therapies/` |
| `/terapii/vulkanichni-kamani/` | Масаж с вулканични камъни | масаж с горещи камъни Бургас | преместена | `/therapies/masaj-s-vulkanichni-kamyni/` |
| `/terapii/plodova-terapiya-ability-spa/` | Плодова терапия „Ability SPA“ | – | преместена | `/therapies/therapy-ability-spa/` |
| `/terapii/chocolate-dream/` | Chocolate Dream | шоколадова терапия | преместена | `/therapies/chocolate-dream-therapy/` |
| `/terapii/coffee-time/` | Coffee Time | – | преместена | `/therapies/coffee-time-therapy/` |
| `/terapii/fitness-nuts/` | Fitness Nuts | – | преместена | `/therapies/fitness-nuts-therapy/` |
| `/terapii/sea-kissed/` | Sea Kissed | – | преместена | `/therapies/terapiya-s-morski-nutrienti/` |
| `/terapii/gold-amber/` | Gold Amber (Варна) | – | преместена | `/therapies/terapiya-golden-amber/` |
| `/terapii/bulgarian-rose/` | Bulgarian Rose (Варна) | – | преместена | `/therapies/terapiya-bulgarian-rose-2/` |
| `/terapii/lavender-touch/` | Lavender Touch (Варна) | – | преместена | `/therapies/terapiya-lavender-touch/` |
| **Козметика** | | | | |
| `/kozmetika-burgas/` | Козметични процедури в Бургас | козметични процедури Бургас | преместена | `/cosmetic-treatments/` |
| `/kozmetika-burgas/terapii-za-litse/` | Терапии за лице (почистване, дермабразио, кислородна…) | почистване на лице Бургас | преместена | `/face-treatments/` |
| `/kozmetika-burgas/spetsialni-terapii-za-litse/` | Специални терапии (Gold, витамин C, микронидлинг…) | – | преместена | `/special-face-treatments/` |
| `/kozmetika-burgas/pdt-lazer/` | Апаратни процедури с PDT лазер | PDT лазер Бургас | преместена | `/pdt-master-laser-procedures/` |
| `/kozmetika-burgas/mezoterapiya/` | Мезотерапия (микроиглена и безиглена) | мезотерапия Бургас | нова | – |
| `/kozmetika-burgas/mikroblejding/` | Микроблейдинг и вежди | микроблейдинг Бургас | нова | – |
| **Цени, пакети, ваучери** | | | | |
| `/ceni/` | Цени – всички услуги в HTML (+ PDF за изтегляне) | спа цени Бургас | нова | `/spa-card/` |
| `/paketi/` | СПА пакети | спа ден Бургас | нова | – |
| `/paketi/spa-za-dvama/` | СПА пакет за двама | спа за двама Бургас | нова | – |
| `/vaucheri/` | Подаръчни ваучери | спа ваучер Бургас | преместена | `/blog/spa-voucher/` |
| `/promocii/` | Промоции | – | нова | – |
| `/promocii/burgas/` | Промоции – Бургас | – | преместена | `/promotions-burgas/` |
| `/promocii/varna/` | Промоции – Варна | – | преместена | `/promotions-varna/` |
| **Информация** | | | | |
| `/parvo-poseshtenie/` | Първо посещение: какво да взема, правила, СПА етикет, деца, Multisport | – | нова | `/spa-etiket/` |
| `/za-nas/` | За нас и екипът | – | нова | – |
| `/kontakti/` | Контакти – Бургас и Варна | – | преместена | `/contacts/`, `/kontakti-varna/` |
| `/blog/` | Блог (27 статии, адресите остават) | – | запазена | – |
| **Правни** | | | | |
| `/obshti-usloviya/` | Общи условия | – | преместена | `/usloviya-za-polzvane/` |
| `/poveritelnost/` | Поверителност | – | преместена | `/politika-za-zasthita-na-lichnite-danni-i-z/` |
| `/biskvitki/` | Бисквитки | – | нова | – |
| **English (/en/)** | | | | |
| `/en/` | Home – Spa in Burgas & Varna | spa Burgas · day spa Burgas city center | нова | – |
| `/en/spa-burgas/` | Ability Spa Burgas | spa Burgas | нова | – |
| `/en/spa-varna/` | Ability Spa&Wellness Varna | spa Varna | нова | – |
| `/en/massages/` | Massages | massage Burgas | нова | – |
| `/en/prices/` | Prices | – | нова | – |
| `/en/vouchers/` | Gift vouchers | – | нова | – |
| `/en/promotions/varna/` | Promotions – Varna | – | преместена | `/promotions-ability-spawellness-varna-en/` |
| `/en/contact/` | Contact | – | нова | – |

## Blog

All 27 existing posts keep their address under `/blog/`. The blog page lists **all** posts (today it shows 3), and each post links to the matching service page (e.g. sauna articles → `/spa-burgas/termalna-zona/`, osteopathy → `/osteopatiya-burgas/`), so no article stays orphaned.

## What changes compared with today

- **Burgas and Varna get separate sections** – Varna therapies, gym and group classes stop living under Burgas or `/massages/`.
- **Each keyword from the brief has its own page:** масаж Бургас, класически / дълбокотъканен / антицелулитен масаж, мезотерапия, басейн, сауна, спа цени, спа за двама, спа ваучер, масаж Варна, spa Burgas.
- **Prices become a page** (`/ceni/`); the PDFs stay as downloads.
- **Vouchers move out of the blog** to `/vaucheri/`; **SPA etiquette** becomes part of `/parvo-poseshtenie/`.
- **Hidden today → visible:** thermal zone, SPA card prices, legal pages, the English promotions page.
- **Removed:** `/footer-ability-spa/` (template part) – 301 to the homepage.
- **Old addresses:** every one of the 69 sitemap URLs and the 58 older internal addresses gets a direct 301 – see `docs/redirect-map.md`.
