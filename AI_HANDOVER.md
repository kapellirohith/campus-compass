# 🤖 AI Handover Document — Campus Compass

**Priority: HIGH**
**Target Audience: Future AI Agents / LLMs**

If you are an AI reading this, you are taking over the "Campus Compass" project. Read this entire document before making any changes. The user has explicitly directed you to understand the history and design philosophy of this project before proceeding.

---

## 1. Project Overview
- **Name:** Campus Compass
- **Target Audience:** Incoming freshers to Amrita Vishwa Vidyapeetham, Amaravati Campus (Class of 2030).
- **Core Concept:** A "Cinematic Digital Field Guide" written from the perspective of a senior. It is NOT a standard college information website, student dashboard, or SaaS landing page. It is a premium editorial experience.
- **Tech Stack:** Pure Vanilla HTML, CSS, and minimal JS.
  - **NO Frameworks:** Do not use React, Vue, Next.js.
  - **NO CSS Libraries:** Do not use TailwindCSS, Bootstrap, or any utility classes. Everything is custom CSS in `styles.css`.
  - **NO Backend:** Fully static site.

---

## 2. History & Design Philosophy (CRITICAL)

### The Journey (What NOT to do)
1. **Initial Version:** The site started as a standard, generic tech-bro landing page with emojis, glowing buttons, and grid cards.
2. **First Redesign (Rejected):** The AI attempted a "modern SaaS" look with chips, pills, accordions, and dashboard-style layouts. The user rejected this because it looked like an AI-generated template or a Notion dashboard, not a top 1% competition submission.
3. **Current Version (Cinematic Editorial):** The user mandated a complete **concept reset**. The current design is inspired by Apple's product storytelling and the NYT "Snow Fall" editorial style. 

### The Rules of the Current Design Language
- **Typography First:** Headers use `Instrument Serif` (elegant, never bold). Body uses `Inter`. Reference data uses `IBM Plex Mono`.
- **Zero Emojis:** Do NOT use emojis as design elements, icons, or bullet points anywhere on the site.
- **Zero Cards/Chips (Mostly):** Do not use grid-based cards, facility chips, or rounded pills. The only exception is the minimal Club section.
- **Cinematic Photography:** The site relies on massive, full-width photographs to set the emotional tone. It alternates between bright reading experiences (white/ivory backgrounds) and dark cinematic moments (`#0F1B2D` backgrounds).
- **Unique Layouts:** No two consecutive chapters share the same layout pattern. (e.g., Chapter 1 is a single narrow column, Chapter 2 is a two-column spread with a sticky image, Chapter 3 opens with a massive photo, etc.).
- **Voice:** The copy is written in a direct, slightly cynical but ultimately warm "senior" voice. Confessions are large, cinematic pull-quotes on dark backgrounds.

---

## 3. Architecture & File Structure

The project lives in `/Users/rohithkapelli/.gemini/antigravity-ide/scratch/campus-compass/`.

### `index.html`
Contains the entire narrative flow. 
- **Navigation:** Clean, minimal, sticky navbar (`#navbar`).
- **Hero:** Full-bleed background image with a dark overlay and large serif typography.
- **Chapter 1 (Before You Pack):** A single-column, multi-expand checklist (JavaScript handles the expansion, it is NOT a single-accordion).
- **Chapter 2 (Your First Week):** A two-column editorial spread (`.editorial-layout`) with text on the left and a sticky image on the right (`.editorial-image`). Includes a vertical timeline (`.timeline`) and a 30-day plan grid (`.thirty-grid`).
- **Chapter 3 (Inside the Classroom):** Opens with a massive photo banner (`.photo-opener`). Contains tables for Branches and Grades, and an Amrita Dictionary.
- **Chapter 4 (Beyond the Classroom):** Club section. Uses a simple tab system (Technical vs Cultural).
- **Chapter 5 (The Unwritten Rules):** An immersive dark-mode section (`.dark-section.has-bg`) that uses a night campus photo at low opacity in the background.
- **Chapter 6 (Your Digital Arsenal):** Compact reference list for tools like AUMS, Canva, etc.
- **Closing:** Cinematic dark section with a final emotional message.

### `styles.css`
Contains all design tokens and layouts.
- Look at the `:root` variables. The ONLY accent color is `var(--saffron)` (`#D97706`). Do not introduce green, blue, or red accents for aesthetics (only for semantic warnings like the FA grade callout).
- The CSS handles the complex layouts like `.editorial-layout` (CSS Grid) and `.photo-opener`.

### `script.js`
Handles minimal interactions:
- Sticky navbar styling on scroll.
- Scroll progress bar at the top of the screen.
- Scroll reveals (`.reveal` class) using Intersection Observer.
- Tab switching for the Clubs section.
- Multi-expand logic for the Packing Checklist.

### `/images/` Directory
The site maps exactly to 5 specific image filenames. If you add new images, ensure they are high-quality, real photos of the campus.
- `hero.jpg`: The massive background for the landing section.
- `hostel.jpg`: Used as a full-width photo break between Chapter 1 and 2.
- `students.jpg`: The sticky image that stays on screen during Chapter 2.
- `classroom.jpg`: The massive photo-opener at the start of Chapter 3.
- `night.jpg`: Used as a low-opacity background for Chapter 5 and the Closing.

## 4. Recent Updates
- **Broader Academic Scope:** Originally the "Your Branch" table (Chapter 3) only listed Computer Science branches. We have updated this to include other programs offered at the Amaravati campus, specifically 5-year Integrated M.Sc. (Physics/Data Science) and MBA (Management). 
- **Real Images:** The user has provided real campus images (`culture.jpg`, `podium image 2.jpg`, `quantum valley winners.jpg`, `sports.jpg`, `student at podium.jpg`) into the `/images/` directory. Future models should be aware that these real assets exist and are integrated into the aesthetic flow.
- **Campus Contacts & Location:** Added a new block at the end of Chapter 6 (Tools) containing a direct Google Maps navigation link, as well as the official `mailto:` links for Administrative queries (`adminoffice@av.amrita.edu`) and Academic queries (`acadcell.eng@av.amrita.edu`).

---

## 5. How to Continue Work

1. **Do not add new sections or features.** The site is feature-complete.
2. **Do not redesign the CSS.** The current cinematic editorial style is exactly what the user wants.
3. If the user asks for a "Final Polish" or "QA Audit," evaluate the site against standard competition rubrics (Performance, Mobile Responsiveness, Accessibility, Narrative flow) without changing the core aesthetic.

**End of Handover Document.**
