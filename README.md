<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Space+Grotesk:wght@300;400;500;600&display=swap" rel="stylesheet">

<style>
  :root {
    --bg-primary: #0d0d0d;
    --bg-secondary: #161616;
    --bg-card: #1a1a1a;
    --bg-card-hover: #222222;
    --accent: #C4784A;
    --accent-hover: #d4895c;
    --accent-dim: rgba(196, 120, 74, 0.15);
    --text-primary: #f5f0e8;
    --text-secondary: #a8a19a;
    --text-muted: #6b6560;
    --border: #2a2a2a;
    --font-heading: 'Playfair Display', Georgia, serif;
    --font-body: 'Space Grotesk', -apple-system, sans-serif;
  }

  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  body {
    background: var(--bg-primary);
    color: var(--text-primary);
    font-family: var(--font-body);
    font-size: 16px;
    line-height: 1.7;
    min-height: 100vh;
  }

  a {
    color: var(--accent);
    text-decoration: none;
    transition: color 0.2s ease;
  }
  a:hover {
    color: var(--accent-hover);
  }

  .container {
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 24px;
  }

  /* ─── HERO ─── */
  .hero {
    padding: 120px 0 100px;
    text-align: center;
    position: relative;
  }
  .hero::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 60px;
    height: 1px;
    background: var(--accent);
  }

  .hero-eyebrow {
    font-family: var(--font-body);
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 28px;
  }

  .hero h1 {
    font-family: var(--font-heading);
    font-size: clamp(42px, 8vw, 80px);
    font-weight: 400;
    line-height: 1.1;
    margin-bottom: 24px;
    color: var(--text-primary);
  }
  .hero h1 em {
    font-style: italic;
    color: var(--accent);
  }

  .hero-tagline {
    font-size: 18px;
    color: var(--text-secondary);
    font-weight: 300;
    max-width: 500px;
    margin: 0 auto 48px;
    line-height: 1.8;
  }

  /* ─── SOCIAL LINKS ─── */
  .social-links {
    display: flex;
    justify-content: center;
    gap: 32px;
    flex-wrap: wrap;
  }
  .social-links a {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    color: var(--text-secondary);
    font-size: 13px;
    font-weight: 500;
    letter-spacing: 0.5px;
    padding: 10px 0;
    border-bottom: 1px solid transparent;
    transition: all 0.25s ease;
  }
  .social-links a:hover {
    color: var(--text-primary);
    border-bottom-color: var(--accent);
  }
  .social-links svg {
    width: 18px;
    height: 18px;
    flex-shrink: 0;
  }

  /* ─── SECTIONS ─── */
  section {
    padding: 100px 0;
    border-bottom: 1px solid var(--border);
  }
  section:last-child {
    border-bottom: none;
  }

  .section-label {
    font-family: var(--font-body);
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 5px;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 48px;
    display: flex;
    align-items: center;
    gap: 16px;
  }
  .section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
    max-width: 80px;
  }

  h2 {
    font-family: var(--font-heading);
    font-size: clamp(32px, 5vw, 48px);
    font-weight: 400;
    margin-bottom: 24px;
    color: var(--text-primary);
  }

  /* ─── ABOUT ─── */
  .about-content {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: start;
  }
  .about-bio {
    font-size: 17px;
    color: var(--text-secondary);
    line-height: 1.9;
  }
  .about-bio p + p {
    margin-top: 20px;
  }
  .about-bio strong {
    color: var(--text-primary);
    font-weight: 500;
  }

  .about-meta {
    background: var(--bg-card);
    border: 1px solid var(--border);
    padding: 36px;
  }
  .about-meta-item {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 14px 0;
    border-bottom: 1px solid var(--border);
    font-size: 14px;
  }
  .about-meta-item:last-child {
    border-bottom: none;
  }
  .about-meta-item svg {
    width: 18px;
    height: 18px;
    color: var(--accent);
    flex-shrink: 0;
  }
  .about-meta-item span {
    color: var(--text-secondary);
  }

  /* ─── TECH STACK ─── */
  .stack-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1px;
    background: var(--border);
  }
  .stack-category {
    background: var(--bg-card);
    padding: 36px 28px;
  }
  .stack-category h4 {
    font-family: var(--font-body);
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 20px;
  }
  .stack-category ul {
    list-style: none;
  }
  .stack-category li {
    font-size: 14px;
    color: var(--text-secondary);
    padding: 6px 0;
    font-weight: 400;
  }

  /* ─── PROJECTS ─── */
  .projects-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
  }
  .project-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    padding: 40px 32px;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
  }
  .project-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: var(--accent);
    transform: scaleX(0);
    transition: transform 0.3s ease;
  }
  .project-card:hover {
    background: var(--bg-card-hover);
    transform: translateY(-4px);
  }
  .project-card:hover::before {
    transform: scaleX(1);
  }

  .project-icon {
    width: 48px;
    height: 48px;
    background: var(--accent-dim);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 28px;
    font-size: 22px;
  }

  .project-card h3 {
    font-family: var(--font-heading);
    font-size: 24px;
    font-weight: 600;
    margin-bottom: 16px;
    color: var(--text-primary);
  }
  .project-card p {
    font-size: 14px;
    color: var(--text-secondary);
    line-height: 1.8;
    margin-bottom: 24px;
  }

  .project-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 24px;
  }
  .project-tag {
    font-size: 11px;
    font-weight: 500;
    color: var(--accent);
    background: var(--accent-dim);
    padding: 4px 10px;
    font-family: var(--font-body);
  }

  .project-link {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-size: 13px;
    font-weight: 500;
    color: var(--text-secondary);
    transition: color 0.2s ease;
  }
  .project-link:hover {
    color: var(--accent);
  }
  .project-link svg {
    width: 14px;
    height: 14px;
    transition: transform 0.2s ease;
  }
  .project-link:hover svg {
    transform: translateX(3px);
  }

  /* ─── FOOTER ─── */
  .footer {
    padding: 60px 0;
    text-align: center;
    border-top: 1px solid var(--border);
  }
  .footer p {
    font-size: 12px;
    color: var(--text-muted);
    letter-spacing: 2px;
    text-transform: uppercase;
  }
  .footer-accent {
    color: var(--accent);
  }

  /* ─── RESPONSIVE ─── */
  @media (max-width: 900px) {
    .about-content {
      grid-template-columns: 1fr;
      gap: 40px;
    }
    .stack-grid {
      grid-template-columns: repeat(2, 1fr);
    }
    .projects-grid {
      grid-template-columns: repeat(2, 1fr);
    }
  }
  @media (max-width: 600px) {
    .hero {
      padding: 80px 0 60px;
    }
    .stack-grid {
      grid-template-columns: 1fr;
    }
    .projects-grid {
      grid-template-columns: 1fr;
    }
    .social-links {
      flex-direction: column;
      align-items: center;
      gap: 16px;
    }
    section {
      padding: 60px 0;
    }
  }
</style>

<!-- HERO -->
<section class="hero">
  <div class="container">
    <p class="hero-eyebrow">Portfolio — 2024</p>
    <h1>Henry <em>Chen</em></h1>
    <p class="hero-tagline">Fullstack Developer &nbsp;·&nbsp; Photographer &nbsp;·&nbsp; Sydney, Australia</p>

    <nav class="social-links">
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
          <rect x="2" y="9" width="4" height="12"/>
          <circle cx="4" cy="4" r="2"/>
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
    </nav>
  </div>
</section>

<!-- ABOUT -->
<section>
  <div class="container">
    <p class="section-label">About</p>
    <div class="about-content">
      <div class="about-bio">
        <p>CS grad from UWA with a Master's in IT, based in Sydney. I gravitate toward the full picture — from React front-ends to Docker pipelines, from database schema design to CI/CD automation.</p>
        <p>Currently open to <strong>fullstack</strong> and <strong>DevOps</strong> roles where I can build things that matter.</p>
      </div>
      <div class="about-meta">
        <div class="about-meta-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
            <circle cx="12" cy="10" r="3"/>
          </svg>
          <span>Sydney, NSW, Australia</span>
        </div>
        <div class="about-meta-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
            <polyline points="22,6 12,13 2,6"/>
          </svg>
          <a href="mailto:henrycxw@gmail.com">henrycxw@gmail.com</a>
        </div>
        <div class="about-meta-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
            <polyline points="14 2 14 8 20 8"/>
            <line x1="16" y1="13" x2="8" y2="13"/>
            <line x1="16" y1="17" x2="8" y2="17"/>
            <polyline points="10 9 9 9 8 9"/>
          </svg>
          <a href="https://misoto22.com/files/resume.pdf" target="_blank">View Resume</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- TECH STACK -->
<section>
  <div class="container">
    <p class="section-label">Tech Stack</p>
    <div class="stack-grid">
      <div class="stack-category">
        <h4>Languages</h4>
        <ul>
          <li>Python</li>
          <li>TypeScript</li>
          <li>Rust</li>
          <li>SQL</li>
        </ul>
      </div>
      <div class="stack-category">
        <h4>Web</h4>
        <ul>
          <li>React</li>
          <li>Next.js</li>
          <li>Django</li>
          <li>Node.js</li>
        </ul>
      </div>
      <div class="stack-category">
        <h4>DevOps</h4>
        <ul>
          <li>Docker</li>
          <li>AWS</li>
          <li>GitHub Actions</li>
          <li>Linux</li>
        </ul>
      </div>
      <div class="stack-category">
        <h4>Data</h4>
        <ul>
          <li>PostgreSQL</li>
          <li>SQL Server</li>
          <li>Firebase</li>
          <li>Cloudflare</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- FEATURED WORK -->
<section>
  <div class="container">
    <p class="section-label">Featured Work</p>
    <h2>Selected Projects</h2>
    <br>
    <div class="projects-grid">

      <article class="project-card">
        <div class="project-icon">🚗</div>
        <h3>Dealer Portal</h3>
        <p>Solo-built a full replacement for a legacy C#/.NET 4.8 dealer portal — both systems running on the same production database, processing live orders, with zero downtime and zero schema changes.</p>
        <div class="project-tags">
          <span class="project-tag">React</span>
          <span class="project-tag">TypeScript</span>
          <span class="project-tag">Vite</span>
          <span class="project-tag">Ant Design</span>
          <span class="project-tag">Django</span>
          <span class="project-tag">DRF</span>
          <span class="project-tag">SQL Server</span>
          <span class="project-tag">AWS Lightsail</span>
          <span class="project-tag">Docker</span>
        </div>
        <a href="https://misoto22.com/projects/dealer-portal" target="_blank" class="project-link">
          View project
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="5" y1="12" x2="19" y2="12"/>
            <polyline points="12 5 19 12 12 19"/>
          </svg>
        </a>
      </article>

      <article class="project-card">
        <div class="project-icon">💎</div>
        <h3>Lumia Crystal</h3>
        <p>A headless e-commerce storefront for crystal jewelry — custom Next.js 15 frontend powered by Shopify Storefront API, with a 4-layer caching architecture delivering sub-second page loads across 60+ products.</p>
        <div class="project-tags">
          <span class="project-tag">Next.js 15</span>
          <span class="project-tag">TypeScript</span>
          <span class="project-tag">Tailwind CSS 4</span>
          <span class="project-tag">Shopify GraphQL</span>
        </div>
        <a href="https://misoto22.com/projects/lumia-crystal" target="_blank" class="project-link">
          View project
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="5" y1="12" x2="19" y2="12"/>
            <polyline points="12 5 19 12 12 19"/>
          </svg>
        </a>
      </article>

      <article class="project-card">
        <div class="project-icon">🌐</div>
        <h3>misoto22.com</h3>
        <p>A bilingual developer portfolio that treats personal infrastructure as seriously as production — privacy-first analytics, WCAG AAA accessibility, 37 automated tests, and a full CI pipeline with Lighthouse audits.</p>
        <div class="project-tags">
          <span class="project-tag">Next.js 16</span>
          <span class="project-tag">TypeScript</span>
          <span class="project-tag">Tailwind CSS 4</span>
          <span class="project-tag">Framer Motion</span>
          <span class="project-tag">Supabase</span>
        </div>
        <a href="https://misoto22.com/projects/personal-website" target="_blank" class="project-link">
          View project
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="5" y1="12" x2="19" y2="12"/>
            <polyline points="12 5 19 12 12 19"/>
          </svg>
        </a>
      </article>

    </div>
  </div>
</section>

<!-- FOOTER -->
<footer class="footer">
  <div class="container">
    <p>Henry Chen &nbsp;·&nbsp; <span class="footer-accent">Sydney, Australia</span></p>
  </div>
</footer>
