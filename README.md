<!-- Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Space+Grotesk:wght@300;400;500;600&display=swap" rel="stylesheet">

<!-- Inline Fonts & Color Tokens -->
<style>
  :root {
    --accent:    #C4784A;
    --bg:        #0d0d0d;
    --text:      #f5f0e8;
    --muted:     #a8a19a;
    --border:    #2a2a2a;
    --card-bg:   #161616;
    --card-hover:#1e1e1e;
    --font-head: 'Playfair Display', Georgia, serif;
    --font-body: 'Space Grotesk', -apple-system, sans-serif;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { background: var(--bg); color: var(--text); font-family: var(--font-body); line-height: 1.7; }
  a { color: var(--accent); text-decoration: none; transition: color .2s; }
  a:hover { color: #d4895c; }

  /* Hero card */
  .hero-card {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 64px 48px;
    text-align: center;
    margin: 80px auto 60px;
    max-width: 680px;
  }
  .hero-card .eyebrow {
    font-family: var(--font-body);
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 5px;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 20px;
  }
  .hero-card h1 {
    font-family: var(--font-head);
    font-size: clamp(38px, 7vw, 68px);
    font-weight: 400;
    line-height: 1.1;
    margin-bottom: 16px;
  }
  .hero-card h1 em { font-style: italic; color: var(--accent); }
  .hero-card .tagline {
    font-size: 15px;
    color: var(--muted);
    font-weight: 300;
    margin-bottom: 40px;
  }

  /* Social links row */
  .social-row {
    display: flex;
    justify-content: center;
    gap: 28px;
    flex-wrap: wrap;
  }
  .social-row a {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    color: var(--muted);
    font-size: 13px;
    font-weight: 500;
    padding: 8px 0;
    border-bottom: 1px solid transparent;
    transition: all .25s;
  }
  .social-row a:hover { color: var(--text); border-bottom-color: var(--accent); }
  .social-row svg { width: 16px; height: 16px; flex-shrink: 0; }

  /* Section headings (Markdown ## backed) */
  h2 {
    font-family: var(--font-head);
    font-size: clamp(26px, 4vw, 38px);
    font-weight: 400;
    margin-bottom: 8px;
    color: var(--text);
  }
  .section-eyebrow {
    font-family: var(--font-body);
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 36px;
    display: flex;
    align-items: center;
    gap: 14px;
  }
  .section-eyebrow::after {
    content: '';
    height: 1px;
    background: var(--border);
    flex: 1;
    max-width: 60px;
  }

  /* Markdown lists */
  ul { list-style: none; }
  li { padding: 4px 0; color: var(--muted); font-size: 14px; }

  /* Project cards — blockquote-backed with inline style */
  .projects-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-top: 40px;
  }
  .project-card {
    background: var(--card-bg);
    border: 1px solid var(--border);
    padding: 36px 28px;
    position: relative;
    transition: background .3s, transform .3s;
  }
  .project-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: var(--accent);
    transform: scaleX(0);
    transition: transform .3s;
  }
  .project-card:hover { background: var(--card-hover); transform: translateY(-3px); }
  .project-card:hover::before { transform: scaleX(1); }
  .project-card .icon { font-size: 20px; margin-bottom: 20px; }
  .project-card h3 {
    font-family: var(--font-head);
    font-size: 22px;
    font-weight: 600;
    margin-bottom: 12px;
    color: var(--text);
  }
  .project-card p { font-size: 13px; color: var(--muted); line-height: 1.8; margin-bottom: 20px; }
  .tag-list {
    display: flex; flex-wrap: wrap; gap: 6px;
    margin-bottom: 20px;
  }
  .tag {
    font-size: 10px;
    font-weight: 500;
    color: var(--accent);
    background: rgba(196,120,74,.12);
    padding: 3px 9px;
    font-family: var(--font-body);
  }
  .project-link {
    display: inline-flex; align-items: center; gap: 6px;
    font-size: 12px; font-weight: 500; color: var(--muted);
    transition: color .2s;
  }
  .project-link:hover { color: var(--accent); }

  /* Footer */
  .footer {
    text-align: center;
    padding: 48px 0;
    border-top: 1px solid var(--border);
    margin-top: 80px;
  }
  .footer p { font-size: 11px; color: #6b6560; letter-spacing: 2px; text-transform: uppercase; }
  .footer span { color: var(--accent); }

  /* Responsive */
  @media (max-width: 800px) {
    .projects-grid { grid-template-columns: 1fr; }
    .hero-card { padding: 48px 28px; margin: 40px 16px 40px; }
  }
  @media (max-width: 600px) {
    .projects-grid { grid-template-columns: 1fr; }
    .social-row { flex-direction: column; align-items: center; gap: 12px; }
  }
</style>

<!-- ═══════════════════════════════════════════════════
     HERO  (Markdown link + HTML card)
════════════════════════════════════════════════════ -->
<div class="hero-card">

  <p class="eyebrow">Portfolio — 2024</p>

  <h1>Henry <em>Chen</em></h1>

  <p class="tagline">Fullstack Developer &nbsp;·&nbsp; Photographer &nbsp;·&nbsp; Sydney, Australia</p>

  <nav class="social-row">
    <a href="https://misoto22.com" target="_blank" rel="noopener">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="10"/>
        <path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
      </svg>
      misoto22.com
    </a>
    <a href="https://www.linkedin.com/in/henry-misoto22" target="_blank" rel="noopener">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/>
        <rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/>
      </svg>
      LinkedIn
    </a>
    <a href="https://www.instagram.com/hry.photography" target="_blank" rel="noopener">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <rect x="2" y="2" width="20" height="20" rx="5" ry="5"/>
        <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/>
        <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/>
      </svg>
      Instagram
    </a>
    <a href="mailto:henrycxw@gmail.com">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
        <polyline points="22,6 12,13 2,6"/>
      </svg>
      Email
    </a>
  </nav>

</div>

---

## About

> CS grad from **UWA** with a Master's in IT, based in Sydney. I gravitate toward the full picture — from React front-ends to Docker pipelines, from database schema design to CI/CD automation.
>
> Currently open to **fullstack** and **DevOps** roles where I can build things that matter.

**Location:** Sydney, NSW, Australia &nbsp;·&nbsp; **Resume:** [misoto22.com/files/resume.pdf](https://misoto22.com/files/resume.pdf)

---

## Tech Stack

Languages: `Python` · `TypeScript` · `Rust` · `SQL`

Web: `React` · `Next.js` · `Django` · `Node.js`

DevOps: `Docker` · `AWS` · `GitHub Actions` · `Linux`

Data: `PostgreSQL` · `SQL Server` · `Firebase` · `Cloudflare`

---

## Featured Work

> Selected projects — click through for the full story.

<div class="projects-grid">

  <article class="project-card">
    <div class="icon">🚗</div>
    <h3>Dealer Portal</h3>
    <p>Solo-built a full replacement for a legacy C#/.NET 4.8 dealer portal — both systems running on the same production database, processing live orders, with zero downtime and zero schema changes.</p>
    <div class="tag-list">
      <span class="tag">React</span>
      <span class="tag">TypeScript</span>
      <span class="tag">Vite</span>
      <span class="tag">Ant Design</span>
      <span class="tag">Django</span>
      <span class="tag">DRF</span>
      <span class="tag">SQL Server</span>
      <span class="tag">AWS Lightsail</span>
      <span class="tag">Docker</span>
    </div>
    <a href="https://misoto22.com/projects/dealer-portal" target="_blank" class="project-link">
      View project →
    </a>
  </article>

  <article class="project-card">
    <div class="icon">💎</div>
    <h3>Lumia Crystal</h3>
    <p>A headless e-commerce storefront for crystal jewelry — custom Next.js 15 frontend powered by Shopify Storefront API, with a 4-layer caching architecture delivering sub-second page loads across 60+ products.</p>
    <div class="tag-list">
      <span class="tag">Next.js 15</span>
      <span class="tag">TypeScript</span>
      <span class="tag">Tailwind CSS 4</span>
      <span class="tag">Shopify GraphQL</span>
    </div>
    <a href="https://misoto22.com/projects/lumia-crystal" target="_blank" class="project-link">
      View project →
    </a>
  </article>

  <article class="project-card">
    <div class="icon">🌐</div>
    <h3>misoto22.com</h3>
    <p>A bilingual developer portfolio that treats personal infrastructure as seriously as production — privacy-first analytics, WCAG AAA accessibility, 37 automated tests, and a full CI pipeline with Lighthouse audits.</p>
    <div class="tag-list">
      <span class="tag">Next.js 16</span>
      <span class="tag">TypeScript</span>
      <span class="tag">Tailwind CSS 4</span>
      <span class="tag">Framer Motion</span>
      <span class="tag">Supabase</span>
    </div>
    <a href="https://misoto22.com/projects/personal-website" target="_blank" class="project-link">
      View project →
    </a>
  </article>

</div>

---

<footer class="footer">
  <p>Henry Chen &nbsp;·&nbsp; <span>Sydney, Australia</span></p>
</footer>
