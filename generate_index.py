import json

with open('full_catalog.json', 'r', encoding='utf-8') as f:
    catalog = json.load(f)

# Build JSON-LD ItemList
json_ld_items = []
for idx, r in enumerate(catalog, start=1):
    item = {
        '@type': 'ListItem',
        'position': idx,
        'item': {
            '@type': 'SoftwareSourceCode',
            'name': r['title'],
            'alternateName': r['name'],
            'description': r['description'],
            'codeRepository': r['url'],
            'programmingLanguage': r['primaryLanguage'],
            'applicationCategory': r['category']
        }
    }
    if r['homepageUrl']:
        item['item']['url'] = r['homepageUrl']
    json_ld_items.append(item)

json_ld_data = {
    '@context': 'https://schema.org',
    '@type': 'ProfilePage',
    'mainEntity': {
        '@type': 'Person',
        'name': 'Md. Shifat',
        'alternateName': 'WebSmartBD',
        'jobTitle': 'Full-Stack Developer & Entrepreneur',
        'url': 'https://bmshifat.pro.bd/',
        'sameAs': [
            'https://github.com/websmartbd',
            'mailto:bmshifat0@gmail.com'
        ]
    },
    'hasPart': {
        '@type': 'ItemList',
        'name': 'Public Repositories of WebSmartBD',
        'description': 'Curated index of all public GitHub repositories and open-source projects by WebSmartBD.',
        'numberOfItems': len(catalog),
        'itemListElement': json_ld_items
    }
}

json_ld_str = json.dumps(json_ld_data, ensure_ascii=False, indent=2)
catalog_json_str = json.dumps(catalog, ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>WebSmartBD — Public Repositories & Open Source Directory</title>
  <meta name="description" content="Explore all public GitHub repositories and open-source projects by WebSmartBD (Md. Shifat). Fullstack web apps, AI tools, developer utilities, and backend systems." />
  <meta name="keywords" content="WebSmartBD, Md Shifat, GitHub public repositories, open source bangladesh, qresto, claude-switch, poselens, authia, clip-manager" />
  <meta name="author" content="Md. Shifat (WebSmartBD)" />
  <meta name="robots" content="index, follow" />

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website" />
  <meta property="og:title" content="WebSmartBD — Public Repositories & Open Source Directory" />
  <meta property="og:description" content="Comprehensive index of all public GitHub repositories, live projects, and tools created by WebSmartBD." />
  <meta property="og:url" content="https://websmartbd.github.io/websmartbd/" />
  <meta property="og:site_name" content="WebSmartBD Repository Hub" />

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="WebSmartBD — Public Repositories Index" />
  <meta name="twitter:description" content="Discover 24+ open source tools, web apps, and AI applications by WebSmartBD." />

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet" />

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace']
          },
          colors: {
            brand: {
              50: '#fffbeb',
              100: '#fef3c7',
              200: '#fde68a',
              300: '#fcd34d',
              400: '#fbbf24',
              500: '#f59e0b',
              600: '#d97706',
              700: '#b45309',
              800: '#92400e',
              900: '#78350f'
            }
          }
        }
      }
    };
  </script>

  <style>
    /* Custom scrollbars */
    ::-webkit-scrollbar {
      width: 7px;
      height: 7px;
    }
    ::-webkit-scrollbar-track {
      background: #f1f5f9;
    }
    ::-webkit-scrollbar-thumb {
      background: #cbd5e1;
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #f59e0b;
    }
    .modal-backdrop {
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
    }
    .line-clamp-3 {
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }
  </style>

  <!-- JSON-LD Structured Data for Search Engine Indexing -->
  <script type="application/ld+json">
""" + json_ld_str + """
  </script>
</head>
<body class="bg-slate-50 text-slate-800 min-h-screen font-sans antialiased selection:bg-amber-200 selection:text-amber-900">

  <!-- Background Subtle Grid Pattern -->
  <div class="fixed inset-0 pointer-events-none opacity-40 bg-[linear-gradient(to_right,#e2e8f0_1px,transparent_1px),linear-gradient(to_bottom,#e2e8f0_1px,transparent_1px)] bg-[size:32px_32px]"></div>

  <!-- Main Container -->
  <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 flex flex-col min-h-screen">

    <!-- Top Navigation / Brand Bar -->
    <header class="flex flex-wrap items-center justify-between gap-4 pb-8 border-b border-slate-200/90">
      <div class="flex items-center gap-3.5">
        <div class="w-11 h-11 rounded-xl bg-gradient-to-tr from-amber-500 to-amber-400 p-0.5 shadow-md shadow-amber-500/10">
          <div class="w-full h-full bg-white rounded-[10px] flex items-center justify-center font-mono font-bold text-amber-600 text-lg">
            WS
          </div>
        </div>
        <div>
          <h1 class="text-xl font-bold tracking-tight text-slate-900 flex items-center gap-2">
            WebSmartBD
            <span class="px-2 py-0.5 text-xs font-mono font-semibold rounded-full bg-amber-100 text-amber-800 border border-amber-300">
              Open Source Index
            </span>
          </h1>
          <p class="text-xs text-slate-500 font-mono">by Md. Shifat • Bangladesh 🇧🇩</p>
        </div>
      </div>

      <!-- Social & Direct Profile Links -->
      <nav aria-label="External profiles" class="flex items-center flex-wrap gap-2 text-xs font-mono">
        <a href="https://github.com/websmartbd" target="_blank" rel="noopener noreferrer" class="px-3.5 py-1.5 rounded-lg bg-white hover:bg-slate-100 border border-slate-200 text-slate-700 shadow-sm transition-colors flex items-center gap-1.5 font-medium">
          <svg class="w-4 h-4 fill-slate-800" viewBox="0 0 24 24"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
          GitHub
        </a>
        <a href="https://bmshifat.pro.bd/" target="_blank" rel="noopener noreferrer" class="px-3.5 py-1.5 rounded-lg bg-white hover:bg-slate-100 border border-slate-200 text-slate-700 shadow-sm transition-colors flex items-center gap-1.5 font-medium">
          <svg class="w-4 h-4 fill-none stroke-current stroke-2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
          Website
        </a>
        <a href="mailto:bmshifat0@gmail.com" class="px-3.5 py-1.5 rounded-lg bg-white hover:bg-slate-100 border border-slate-200 text-slate-700 shadow-sm transition-colors flex items-center gap-1.5 font-medium">
          <svg class="w-4 h-4 fill-none stroke-current stroke-2" viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
          Email
        </a>
        <a href="https://buymeacha.com/bmshifat" target="_blank" rel="noopener noreferrer" class="px-3.5 py-1.5 rounded-lg bg-amber-50 hover:bg-amber-100 border border-amber-300 text-amber-900 shadow-sm transition-colors flex items-center gap-1.5 font-semibold">
          ☕ Buy me a cha
        </a>
      </nav>
    </header>

    <!-- Hero / Headline Section -->
    <section class="pt-8 pb-8">
      <div class="max-w-3xl">
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold tracking-tight text-slate-900 leading-tight">
          Public Repositories & <br />
          <span class="bg-clip-text text-transparent bg-gradient-to-r from-amber-600 via-amber-500 to-yellow-600">
            Open Source Index
          </span>
        </h2>
        <p class="mt-3.5 text-base sm:text-lg text-slate-600 leading-relaxed">
          A live catalog indexing all 24 public repositories by <span class="text-slate-900 font-semibold">WebSmartBD</span>. Synthesized directly from every repository's README file—complete with live demo links, architecture highlights, tech stacks, and source code.
        </p>
      </div>

      <!-- Quick Metrics Grid -->
      <div class="mt-7 grid grid-cols-2 sm:grid-cols-4 gap-3 sm:gap-4">
        <div class="p-4 rounded-xl bg-white border border-slate-200 shadow-sm">
          <div class="text-2xl sm:text-3xl font-extrabold text-amber-600 font-mono" id="stat-total-repos">24</div>
          <div class="text-xs text-slate-500 uppercase tracking-wider font-mono mt-1 font-semibold">Public Repositories</div>
        </div>
        <div class="p-4 rounded-xl bg-white border border-slate-200 shadow-sm">
          <div class="text-2xl sm:text-3xl font-extrabold text-emerald-600 font-mono">14</div>
          <div class="text-xs text-slate-500 uppercase tracking-wider font-mono mt-1 font-semibold">Live Deployed Apps</div>
        </div>
        <div class="p-4 rounded-xl bg-white border border-slate-200 shadow-sm">
          <div class="text-2xl sm:text-3xl font-extrabold text-sky-600 font-mono">6+</div>
          <div class="text-xs text-slate-500 uppercase tracking-wider font-mono mt-1 font-semibold">Languages & Stacks</div>
        </div>
        <div class="p-4 rounded-xl bg-white border border-slate-200 shadow-sm">
          <div class="text-2xl sm:text-3xl font-extrabold text-purple-600 font-mono">100%</div>
          <div class="text-xs text-slate-500 uppercase tracking-wider font-mono mt-1 font-semibold">Open Source</div>
        </div>
      </div>
    </section>

    <!-- Clean Sticky Category Tabs Bar (Top search & other filters removed as requested) -->
    <section class="sticky top-4 z-30 mb-8 p-2 sm:p-2.5 rounded-2xl bg-white/95 backdrop-blur-md border border-slate-200 shadow-sm flex items-center justify-between gap-3 flex-wrap">
      <div class="flex items-center gap-1.5 overflow-x-auto py-1 text-xs font-mono scrollbar-none" id="category-filters">
        <button class="category-btn px-3.5 py-2 rounded-xl font-bold whitespace-nowrap transition-all cursor-pointer bg-slate-900 text-white shadow-sm" data-category="all">
          All Projects (<span id="count-all">24</span>)
        </button>
        <button class="category-btn px-3.5 py-2 rounded-xl font-medium whitespace-nowrap transition-all cursor-pointer bg-slate-100 text-slate-600 hover:bg-slate-200 hover:text-slate-900" data-category="Web & Fullstack Apps">
          Web & Fullstack (<span id="count-web">7</span>)
        </button>
        <button class="category-btn px-3.5 py-2 rounded-xl font-medium whitespace-nowrap transition-all cursor-pointer bg-slate-100 text-slate-600 hover:bg-slate-200 hover:text-slate-900" data-category="AI & Machine Learning">
          AI & Machine Learning (<span id="count-ai">5</span>)
        </button>
        <button class="category-btn px-3.5 py-2 rounded-xl font-medium whitespace-nowrap transition-all cursor-pointer bg-slate-100 text-slate-600 hover:bg-slate-200 hover:text-slate-900" data-category="DevTools & CLI">
          DevTools & CLI (<span id="count-devtools">3</span>)
        </button>
        <button class="category-btn px-3.5 py-2 rounded-xl font-medium whitespace-nowrap transition-all cursor-pointer bg-slate-100 text-slate-600 hover:bg-slate-200 hover:text-slate-900" data-category="Backend & Security">
          Backend & Security (<span id="count-backend">3</span>)
        </button>
        <button class="category-btn px-3.5 py-2 rounded-xl font-medium whitespace-nowrap transition-all cursor-pointer bg-slate-100 text-slate-600 hover:bg-slate-200 hover:text-slate-900" data-category="Regional & Lifestyle">
          Regional & Lifestyle (<span id="count-regional">3</span>)
        </button>
        <button class="category-btn px-3.5 py-2 rounded-xl font-medium whitespace-nowrap transition-all cursor-pointer bg-slate-100 text-slate-600 hover:bg-slate-200 hover:text-slate-900" data-category="Others">
          Other Projects (<span id="count-others">3</span>)
        </button>
      </div>

      <div class="text-xs font-mono text-slate-500 px-2 flex items-center gap-1.5">
        <span>Showing:</span>
        <span id="active-result-count" class="font-bold text-amber-600">24</span>
        <span>repositories</span>
      </div>
    </section>

    <!-- Repository Cards Grid Container -->
    <main id="repo-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5" role="list" aria-label="Repositories list">
      <!-- Rendered dynamically by JavaScript -->
    </main>

    <!-- Empty State -->
    <div id="empty-state" class="hidden py-16 text-center flex-col items-center justify-center">
      <div class="w-16 h-16 rounded-2xl bg-white flex items-center justify-center text-slate-400 mb-4 border border-slate-200 shadow-sm">
        <svg class="w-8 h-8 stroke-current fill-none stroke-2" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
      </div>
      <h3 class="text-lg font-bold text-slate-800">No repositories found in this category</h3>
      <button onclick="resetCategory()" class="mt-4 px-4 py-2 rounded-xl bg-amber-500 text-slate-950 text-xs font-bold font-mono hover:bg-amber-400 transition-colors shadow-sm">
        View All Projects
      </button>
    </div>

    <!-- Repository Details Modal -->
    <div id="repo-modal" class="fixed inset-0 z-50 hidden modal-backdrop bg-slate-900/40 flex items-center justify-center p-4 sm:p-6 overflow-y-auto" role="dialog" aria-modal="true">
      <div class="relative w-full max-w-2xl bg-white border border-slate-200 rounded-2xl shadow-2xl p-6 sm:p-8 overflow-hidden text-left">
        <!-- Close button -->
        <button id="modal-close-btn" class="absolute top-5 right-5 w-8 h-8 rounded-lg bg-slate-100 text-slate-500 hover:text-slate-900 hover:bg-slate-200 flex items-center justify-center transition-colors cursor-pointer">
          <svg class="w-4 h-4 fill-none stroke-current stroke-2" viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
        </button>

        <div id="modal-content">
          <!-- Injected via JavaScript -->
        </div>
      </div>
    </div>

    <!-- Quick Toast Notification -->
    <div id="toast" class="fixed bottom-6 right-6 z-50 transform translate-y-12 opacity-0 transition-all duration-200 pointer-events-none bg-slate-900 text-white px-4 py-2.5 rounded-xl shadow-xl text-xs font-mono flex items-center gap-2">
      <svg class="w-4 h-4 text-emerald-400 fill-none stroke-current stroke-2" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>
      <span id="toast-message">Copied to clipboard</span>
    </div>

    <!-- Footer -->
    <footer class="mt-auto pt-16 pb-8 border-t border-slate-200 text-xs text-slate-500 font-mono flex flex-col sm:flex-row items-center justify-between gap-4">
      <div>
        Built for <a href="https://github.com/websmartbd/websmartbd" class="text-amber-600 hover:underline font-bold">websmartbd</a> repository • Indexed from public README files
      </div>
      <div class="flex items-center gap-4">
        <span class="font-medium text-slate-700">Md. Shifat (WebSmartBD)</span>
        <span>•</span>
        <a href="https://bmshifat.pro.bd/" target="_blank" rel="noopener" class="text-slate-600 hover:text-amber-600 font-medium transition-colors">bmshifat.pro.bd</a>
      </div>
    </footer>

  </div>

  <!-- JavaScript Client Engine -->
  <script>
    // Injected repository catalog data
    const repositories = """ + catalog_json_str + """;

    // State
    let selectedCategory = 'all';

    // DOM Elements
    const repoGrid = document.getElementById('repo-grid');
    const emptyState = document.getElementById('empty-state');
    const categoryContainer = document.getElementById('category-filters');
    const resultCount = document.getElementById('active-result-count');
    const repoModal = document.getElementById('repo-modal');
    const modalContent = document.getElementById('modal-content');
    const modalCloseBtn = document.getElementById('modal-close-btn');
    const toast = document.getElementById('toast');
    const toastMessage = document.getElementById('toast-message');

    // Language Light Badge Styling
    const langColors = {
      'JavaScript': 'bg-amber-50 text-amber-800 border-amber-200',
      'PHP': 'bg-indigo-50 text-indigo-800 border-indigo-200',
      'TypeScript': 'bg-sky-50 text-sky-800 border-sky-200',
      'Python': 'bg-emerald-50 text-emerald-800 border-emerald-200',
      'HTML': 'bg-rose-50 text-rose-800 border-rose-200',
      'CSS': 'bg-cyan-50 text-cyan-800 border-cyan-200',
      'Smali': 'bg-purple-50 text-purple-800 border-purple-200',
      'HTML/CSS': 'bg-rose-50 text-rose-800 border-rose-200'
    };

    // Category Counts
    function updateCategoryCounts() {
      const counts = {
        'all': repositories.length,
        'Web & Fullstack Apps': 0,
        'AI & Machine Learning': 0,
        'DevTools & CLI': 0,
        'Backend & Security': 0,
        'Regional & Lifestyle': 0,
        'Others': 0
      };

      repositories.forEach(r => {
        if (counts[r.category] !== undefined) {
          counts[r.category]++;
        } else {
          counts['Others']++;
        }
      });

      if (document.getElementById('count-all')) document.getElementById('count-all').innerText = counts['all'];
      if (document.getElementById('count-web')) document.getElementById('count-web').innerText = counts['Web & Fullstack Apps'];
      if (document.getElementById('count-ai')) document.getElementById('count-ai').innerText = counts['AI & Machine Learning'];
      if (document.getElementById('count-devtools')) document.getElementById('count-devtools').innerText = counts['DevTools & CLI'];
      if (document.getElementById('count-backend')) document.getElementById('count-backend').innerText = counts['Backend & Security'];
      if (document.getElementById('count-regional')) document.getElementById('count-regional').innerText = counts['Regional & Lifestyle'];
      if (document.getElementById('count-others')) document.getElementById('count-others').innerText = counts['Others'];
    }

    // Filter Logic
    function getFilteredRepositories() {
      return repositories.filter(repo => {
        if (selectedCategory === 'all') return true;
        if (selectedCategory === 'Others') {
          const mainCats = ['Web & Fullstack Apps', 'AI & Machine Learning', 'DevTools & CLI', 'Backend & Security', 'Regional & Lifestyle'];
          return !mainCats.includes(repo.category);
        }
        return repo.category === selectedCategory;
      }).sort((a, b) => {
        if (a.highlight && !b.highlight) return -1;
        if (!a.highlight && b.highlight) return 1;
        return b.stars - a.stars;
      });
    }

    // Render repository cards in clean light theme
    function render() {
      const filtered = getFilteredRepositories();
      resultCount.innerText = filtered.length;

      if (filtered.length === 0) {
        repoGrid.innerHTML = '';
        emptyState.classList.remove('hidden');
        emptyState.classList.add('flex');
        return;
      }

      emptyState.classList.add('hidden');
      emptyState.classList.remove('flex');

      repoGrid.innerHTML = filtered.map(repo => {
        const langBadgeClass = langColors[repo.primaryLanguage] || 'bg-slate-100 text-slate-700 border-slate-200';
        const hasLive = Boolean(repo.homepageUrl);

        return `
          <article class="group relative rounded-2xl bg-white hover:bg-amber-50/20 border border-slate-200/90 hover:border-amber-400/80 p-5 sm:p-6 flex flex-col justify-between transition-all duration-200 shadow-sm hover:shadow-md">
            <div>
              <!-- Header badges -->
              <div class="flex items-center justify-between gap-2 mb-3">
                <span class="text-[11px] font-mono px-2 py-0.5 rounded-md bg-slate-100 border border-slate-200 text-slate-600 font-medium">
                  ${repo.category}
                </span>
                <div class="flex items-center gap-1.5">
                  ${repo.stars > 0 ? `
                    <span class="text-[11px] font-mono px-2 py-0.5 rounded-md bg-amber-50 text-amber-700 border border-amber-200 flex items-center gap-1 font-semibold">
                      ★ ${repo.stars}
                    </span>
                  ` : ''}
                  <span class="text-[11px] font-mono px-2 py-0.5 rounded-md border font-semibold ${langBadgeClass}">
                    ${repo.primaryLanguage || 'Code'}
                  </span>
                </div>
              </div>

              <!-- Title & Repo Name -->
              <h3 class="text-base font-bold text-slate-900 group-hover:text-amber-600 transition-colors flex items-center justify-between">
                <a href="${repo.url}" target="_blank" rel="noopener noreferrer" class="hover:underline">
                  ${repo.title}
                </a>
              </h3>
              <p class="text-xs font-mono text-slate-500 mt-0.5">websmartbd/${repo.name}</p>

              <!-- Description -->
              <p class="mt-3 text-xs text-slate-600 leading-relaxed line-clamp-3">
                ${repo.description}
              </p>

              <!-- Tech Stack Chips -->
              <div class="mt-4 flex flex-wrap gap-1.5">
                ${repo.tech.slice(0, 4).map(t => `
                  <span class="px-2 py-0.5 rounded-md bg-slate-100 border border-slate-200 text-[10px] font-mono text-slate-600 font-medium">
                    ${t}
                  </span>
                `).join('')}
                ${repo.tech.length > 4 ? `
                  <span class="px-1.5 py-0.5 rounded-md bg-slate-100 text-[10px] font-mono text-slate-500 font-medium">
                    +${repo.tech.length - 4}
                  </span>
                ` : ''}
              </div>
            </div>

            <!-- Footer Actions -->
            <div class="mt-5 pt-4 border-t border-slate-100 flex items-center justify-between gap-2 text-xs font-mono">
              <div class="flex items-center gap-2">
                ${hasLive ? `
                  <a href="${repo.homepageUrl}" target="_blank" rel="noopener noreferrer" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white font-semibold flex items-center gap-1.5 transition-colors shadow-sm">
                    <span class="w-1.5 h-1.5 rounded-full bg-white animate-pulse"></span>
                    Live Demo
                  </a>
                ` : ''}
                <a href="${repo.url}" target="_blank" rel="noopener noreferrer" class="px-3 py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-white font-medium flex items-center gap-1.5 transition-colors shadow-sm">
                  GitHub
                  <svg class="w-3 h-3 stroke-current fill-none stroke-2" viewBox="0 0 24 24"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
                </a>
              </div>
              <button onclick="openDetailsModal('${repo.name}')" class="px-2.5 py-1.5 rounded-lg text-slate-500 hover:text-amber-700 hover:bg-slate-100 font-medium transition-colors cursor-pointer">
                Details →
              </button>
            </div>
          </article>
        `;
      }).join('');
    }

    // Modal Details Renderer
    window.openDetailsModal = function(repoName) {
      const repo = repositories.find(r => r.name === repoName);
      if (!repo) return;

      modalContent.innerHTML = `
        <div class="space-y-5">
          <div>
            <div class="flex items-center gap-2 mb-2">
              <span class="text-xs font-mono px-2 py-0.5 rounded bg-slate-100 text-amber-800 border border-amber-300 font-semibold">
                ${repo.category}
              </span>
              <span class="text-xs font-mono px-2 py-0.5 rounded bg-slate-100 text-slate-700 border border-slate-200 font-semibold">
                ${repo.primaryLanguage || 'Code'}
              </span>
              ${repo.stars > 0 ? `<span class="text-xs font-mono px-2 py-0.5 rounded bg-amber-50 text-amber-700 font-bold border border-amber-200">★ ${repo.stars} stars</span>` : ''}
            </div>
            <h2 class="text-2xl font-extrabold text-slate-900">${repo.title}</h2>
            <p class="text-xs font-mono text-slate-500 mt-1">Repository: websmartbd/${repo.name}</p>
          </div>

          <p class="text-sm text-slate-700 leading-relaxed">
            ${repo.description}
          </p>

          <div>
            <h4 class="text-xs uppercase font-mono tracking-wider text-amber-700 font-bold mb-2.5">Key Features (From README)</h4>
            <ul class="space-y-1.5 text-xs text-slate-600">
              ${repo.features.map(f => `
                <li class="flex items-start gap-2">
                  <span class="text-amber-500 font-bold">•</span>
                  <span>${f}</span>
                </li>
              `).join('')}
            </ul>
          </div>

          <div>
            <h4 class="text-xs uppercase font-mono tracking-wider text-slate-500 font-bold mb-2">Tech Stack & Tools</h4>
            <div class="flex flex-wrap gap-1.5">
              ${repo.tech.map(t => `
                <span class="px-2.5 py-1 rounded bg-slate-100 border border-slate-200 text-xs font-mono text-slate-700 font-medium">
                  ${t}
                </span>
              `).join('')}
            </div>
          </div>

          <!-- Quick Clone Command Box -->
          <div>
            <h4 class="text-xs uppercase font-mono tracking-wider text-slate-500 font-bold mb-1.5">Git Clone</h4>
            <div class="flex items-center justify-between px-3 py-2 bg-slate-50 border border-slate-200 rounded-xl font-mono text-xs text-slate-800">
              <code class="overflow-x-auto text-amber-700 font-semibold">git clone ${repo.url}.git</code>
              <button onclick="copyText('git clone ${repo.url}.git', 'Clone command copied!')" class="ml-2 px-3 py-1 rounded-lg bg-slate-200 hover:bg-slate-300 text-slate-800 text-[11px] font-bold cursor-pointer transition-colors">
                Copy
              </button>
            </div>
          </div>

          <!-- Links -->
          <div class="pt-4 border-t border-slate-200 flex items-center justify-between gap-3 text-xs font-mono">
            <a href="${repo.url}" target="_blank" rel="noopener noreferrer" class="px-4 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-medium flex items-center gap-2 transition-colors shadow-sm">
              Open GitHub Repo
              <svg class="w-3.5 h-3.5 stroke-current fill-none stroke-2" viewBox="0 0 24 24"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
            </a>
            ${repo.homepageUrl ? `
              <a href="${repo.homepageUrl}" target="_blank" rel="noopener noreferrer" class="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold flex items-center gap-2 transition-colors shadow-sm">
                Launch Live Demo
                <svg class="w-3.5 h-3.5 stroke-current fill-none stroke-2" viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg>
              </a>
            ` : ''}
          </div>
        </div>
      `;

      repoModal.classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    };

    function closeModal() {
      repoModal.classList.add('hidden');
      document.body.style.overflow = '';
    }

    modalCloseBtn.addEventListener('click', closeModal);
    repoModal.addEventListener('click', (e) => {
      if (e.target === repoModal) closeModal();
    });

    // Clipboard Copy Helper
    window.copyText = function(text, msg) {
      navigator.clipboard.writeText(text).then(() => {
        toastMessage.innerText = msg || 'Copied to clipboard';
        toast.classList.remove('translate-y-12', 'opacity-0');
        setTimeout(() => {
          toast.classList.add('translate-y-12', 'opacity-0');
        }, 2200);
      });
    };

    // Category button handling
    categoryContainer.addEventListener('click', (e) => {
      const btn = e.target.closest('.category-btn');
      if (!btn) return;

      document.querySelectorAll('.category-btn').forEach(b => {
        b.className = 'category-btn px-3.5 py-2 rounded-xl font-medium whitespace-nowrap transition-all cursor-pointer bg-slate-100 text-slate-600 hover:bg-slate-200 hover:text-slate-900';
      });

      btn.className = 'category-btn px-3.5 py-2 rounded-xl font-bold whitespace-nowrap transition-all cursor-pointer bg-slate-900 text-white shadow-sm';
      selectedCategory = btn.getAttribute('data-category');
      render();
    });

    window.resetCategory = function() {
      selectedCategory = 'all';
      document.querySelectorAll('.category-btn').forEach(b => {
        if (b.getAttribute('data-category') === 'all') {
          b.className = 'category-btn px-3.5 py-2 rounded-xl font-bold whitespace-nowrap transition-all cursor-pointer bg-slate-900 text-white shadow-sm';
        } else {
          b.className = 'category-btn px-3.5 py-2 rounded-xl font-medium whitespace-nowrap transition-all cursor-pointer bg-slate-100 text-slate-600 hover:bg-slate-200 hover:text-slate-900';
        }
      });
      render();
    };

    // Keyboard Shortcuts
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeModal();
      }
    });

    // Initial setup
    updateCategoryCounts();
    render();
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("SUCCESS: index.html generated with Light Mode and cleaned categories bar!")
