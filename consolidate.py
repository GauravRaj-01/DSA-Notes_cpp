import os
import base64

# Define the source directory
source_dir = r"c:\Users\rajga\Downloads\DSA NOTES"
output_file = os.path.join(source_dir, "DSA-GAURAV.html")

# Order the files logically for the notebook
ordered_files = [
    {"filename": "dsa_array_patterns_notes.html", "title": "Array Patterns", "vol": "Volume 1", "icon": "array"},
    {"filename": "dsa_string_patterns_notes.html", "title": "String Patterns", "vol": "Volume 2", "icon": "string"},
    {"filename": "sorting_algorithms_notes.html", "title": "Sorting Algorithms", "vol": "Volume 3", "icon": "sorting"},
    {"filename": "dsa_linked_list_notes.html", "title": "Linked List Patterns", "vol": "Volume 4", "icon": "linkedlist"},
    {"filename": "dsa_stack_notes.html", "title": "Stack Patterns", "vol": "Volume 5", "icon": "stack"},
    {"filename": "dsa_hashmap_patterns_notes.html", "title": "HashMap Patterns", "vol": "Volume 6", "icon": "hashmap"},
    {"filename": "dsa_dp_patterns_notes.html", "title": "Dynamic Programming", "vol": "Volume 7", "icon": "dp"}
]

# SVG Icons Map for extreme premium visual fidelity
svg_icons = {
    "array": '<svg class="nav-icon" viewBox="0 0 24 24"><path d="M3 3h4v4H3V3zm6 0h4v4H9V3zm6 0h4v4h-4V3zM3 9h4v4H3V9zm6 0h4v4H9V9zm6 0h4v4h-4V9zM3 15h4v4H3v-4zm6 0h4v4H9v-4zm6 0h4v4h-4v-4z" fill="currentColor"/></svg>',
    "string": '<svg class="nav-icon" viewBox="0 0 24 24"><path d="M4 9h16v2H4V9zm0 4h10v2H4v-2zM4 5h16v2H4V5zm0 12h14v2H4v-2z" fill="currentColor"/></svg>',
    "sorting": '<svg class="nav-icon" viewBox="0 0 24 24"><path d="M3 18h6v-2H3v2zM3 6v2h18V6H3zm0 7h12v-2H3v2z" fill="currentColor"/></svg>',
    "linkedlist": '<svg class="nav-icon" viewBox="0 0 24 24"><path d="M16 6H8v2h8V6zm4 5h-4v2h4v-2zM4 11h4v2H4v-2zm12 5H8v2h8v-2z" fill="currentColor"/></svg>',
    "stack": '<svg class="nav-icon" viewBox="0 0 24 24"><path d="M19 17c0 .55-.45 1-1 1H6c-.55 0-1-.45-1-1v-2h14v2zm0-5c0 .55-.45 1-1 1H6c-.55 0-1-.45-1-1V9h14v3zm0-6c0 .55-.45 1-1 1H6c-.55 0-1-.45-1-1V3h14v3z" fill="currentColor"/></svg>',
    "hashmap": '<svg class="nav-icon" viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 14c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5z" fill="currentColor"/></svg>',
    "dp": '<svg class="nav-icon" viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-4 6h-4v2h4v2h-4v2h4v2H9V7h6v2z" fill="currentColor"/></svg>'
}

# Read and base64 encode all files
embedded_data = []
for file_info in ordered_files:
    filepath = os.path.join(source_dir, file_info["filename"])
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        b64_bytes = base64.b64encode(content.encode("utf-8"))
        b64_string = b64_bytes.decode("utf-8")
        
        embedded_data.append({
            "title": file_info["title"],
            "vol": file_info["vol"],
            "filename": file_info["filename"],
            "icon": file_info["icon"],
            "b64": b64_string
        })
        print(f"Successfully encoded {file_info['filename']} ({len(content)} chars)")
    else:
        print(f"Warning: {file_info['filename']} not found in directory!")

# Generate the beautiful consolidated master HTML with custom design and Linkedin integration
master_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DSA Notebook — Gaurav</title>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #03001e;
    --sidebar-bg: rgba(10, 12, 22, 0.7);
    --card-bg: rgba(21, 27, 38, 0.45);
    --border: rgba(255, 255, 255, 0.06);
    --text: #94a3b8;
    --text-white: #ffffff;
    --teal: #00f2fe;
    --purple: #9d4edd;
    --pink: #ff007f;
    --muted: #64748b;
    --glow-color: rgba(0, 242, 254, 0.25);
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Plus Jakarta Sans', sans-serif;
    background: radial-gradient(circle at 10% 20%, rgba(90, 24, 154, 0.15) 0%, rgba(13, 17, 28, 0) 50%),
                radial-gradient(circle at 90% 80%, rgba(0, 242, 254, 0.1) 0%, rgba(13, 17, 28, 0) 50%),
                #060814;
    color: var(--text);
    overflow: hidden;
    height: 100vh;
    display: flex;
  }

  /* GLASSMORPHIC SIDEBAR */
  .sidebar {
    width: 310px;
    background: var(--sidebar-bg);
    backdrop-filter: blur(25px) saturate(180%);
    -webkit-backdrop-filter: blur(25px) saturate(180%);
    border-right: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    flex-shrink: 0;
    height: 100%;
    z-index: 10;
    position: relative;
    box-shadow: 10px 0 35px rgba(0, 0, 0, 0.5);
  }

  .sidebar-logo {
    padding: 36px 28px 24px;
    border-bottom: 1px solid var(--border);
    position: relative;
  }

  .sidebar-logo-glow {
    position: absolute;
    top: -20px;
    left: 50%;
    transform: translateX(-50%);
    width: 140px;
    height: 60px;
    background: radial-gradient(circle, rgba(0, 242, 254, 0.2) 0%, transparent 70%);
    filter: blur(10px);
    pointer-events: none;
  }

  .sidebar-logo h1 {
    font-family: 'Outfit', sans-serif;
    font-size: 24px;
    font-weight: 800;
    color: var(--text-white);
    letter-spacing: -0.02em;
    background: linear-gradient(135deg, #00f2fe 0%, #4facfe 50%, #9d4edd 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
  }

  .sidebar-logo p {
    font-size: 10px;
    color: var(--muted);
    margin-top: 8px;
    text-transform: uppercase;
    letter-spacing: 0.18em;
    font-weight: 700;
    text-align: center;
  }

  .nav-list {
    flex: 1;
    overflow-y: auto;
    padding: 24px 20px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .nav-section-label {
    font-size: 10px;
    font-weight: 800;
    color: #475569;
    text-transform: uppercase;
    letter-spacing: 0.18em;
    padding-left: 14px;
    margin-bottom: 6px;
  }

  /* BUTTON STYLING & GLOW TRANSITIONS */
  .nav-btn {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 14px 18px;
    border-radius: 16px;
    color: #94a3b8;
    cursor: pointer;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    border: 1px solid rgba(255, 255, 255, 0.02);
    background: rgba(255, 255, 255, 0.02);
    width: 100%;
    text-align: left;
    position: relative;
    overflow: hidden;
  }

  .nav-btn::before {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 4px;
    background: linear-gradient(to bottom, #00f2fe, #4facfe);
    transform: scaleY(0);
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    border-radius: 0 8px 8px 0;
  }

  .nav-btn::after {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(circle at var(--x, 50%) var(--y, 50%), rgba(255, 255, 255, 0.08) 0%, transparent 60%);
    opacity: 0;
    transition: opacity 0.3s;
    pointer-events: none;
  }

  .nav-btn:hover::after {
    opacity: 1;
  }

  .nav-btn:hover {
    background: rgba(255, 255, 255, 0.05);
    color: #f1f5f9;
    border-color: rgba(255, 255, 255, 0.08);
    transform: translateX(6px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  }

  .nav-btn.active {
    background: rgba(0, 242, 254, 0.08);
    color: #ffffff;
    border-color: rgba(0, 242, 254, 0.25);
    font-weight: 600;
    box-shadow: 0 4px 20px rgba(0, 242, 254, 0.12), inset 0 1px 1px rgba(255, 255, 255, 0.1);
  }

  .nav-btn.active::before {
    transform: scaleY(1);
  }

  .nav-icon {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
    color: #64748b;
    transition: all 0.3s;
  }

  .nav-btn:hover .nav-icon {
    color: #00f2fe;
    transform: scale(1.1);
  }

  .nav-btn.active .nav-icon {
    color: #00f2fe;
    filter: drop-shadow(0 0 8px rgba(0, 242, 254, 0.8));
    transform: scale(1.1);
  }

  .btn-right {
    display: flex;
    flex-direction: column;
    gap: 3px;
  }

  .btn-vol {
    font-size: 9px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--muted);
    font-weight: 700;
  }

  .nav-btn.active .btn-vol {
    color: var(--teal);
  }

  .btn-title {
    font-size: 14px;
    font-weight: 500;
  }

  /* PREMIUM FOOTER WITH LINKEDIN BRANDING */
  .sidebar-footer {
    padding: 24px;
    border-top: 1px solid var(--border);
    background: rgba(10, 12, 22, 0.4);
    display: flex;
    flex-direction: column;
    gap: 12px;
    align-items: center;
  }

  .footer-copyright {
    font-size: 11px;
    color: var(--muted);
    text-align: center;
    letter-spacing: 0.02em;
    font-weight: 500;
  }

  .linkedin-link-wrap {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
  }

  .linkedin-badge {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    border-radius: 20px;
    background: rgba(0, 119, 181, 0.1);
    border: 1px solid rgba(0, 119, 181, 0.2);
    color: #0077b5;
    font-size: 12px;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }

  .linkedin-badge:hover {
    background: #0077b5;
    color: #ffffff;
    border-color: #0077b5;
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(0, 119, 181, 0.4);
  }

  .linkedin-badge svg {
    width: 16px;
    height: 16px;
    fill: currentColor;
    transition: fill 0.3s;
  }

  /* MAIN CONTENT AREA */
  .content-area {
    flex: 1;
    height: 100%;
    position: relative;
    background: #060814;
  }

  .tab-iframe {
    width: 100%;
    height: 100%;
    border: none;
    display: none;
  }

  .tab-iframe.active {
    display: block;
  }

  /* HIGH-FIDELITY LANDING PAGE */
  .landing-page {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 40px;
    overflow-y: auto;
    background: radial-gradient(circle at 80% 20%, rgba(0, 242, 254, 0.06) 0%, transparent 50%),
                radial-gradient(circle at 20% 80%, rgba(157, 78, 221, 0.06) 0%, transparent 50%);
  }

  .landing-card {
    max-width: 760px;
    width: 100%;
    background: var(--card-bg);
    backdrop-filter: blur(30px);
    -webkit-backdrop-filter: blur(30px);
    border: 1px solid var(--border);
    border-radius: 32px;
    padding: 64px 56px;
    text-align: center;
    box-shadow: 0 30px 70px rgba(0, 0, 0, 0.5),
                inset 0 1px 0 rgba(255, 255, 255, 0.05);
    position: relative;
    overflow: hidden;
  }

  .landing-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, #00f2fe, #4facfe, #9d4edd, #ff007f);
  }

  .landing-title {
    font-family: 'Outfit', sans-serif;
    font-size: 42px;
    font-weight: 800;
    color: var(--text-white);
    margin-bottom: 16px;
    letter-spacing: -0.03em;
    line-height: 1.1;
  }

  .landing-title span {
    background: linear-gradient(135deg, #00f2fe 0%, #4facfe 50%, #c084fc 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 0 10px rgba(0, 242, 254, 0.15));
  }

  .landing-subtitle {
    font-size: 16px;
    color: var(--text);
    margin-bottom: 44px;
    line-height: 1.8;
  }

  .stats-row {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 24px;
    margin-bottom: 48px;
  }

  .stat-box {
    background: rgba(255, 255, 255, 0.015);
    border: 1px solid rgba(255, 255, 255, 0.03);
    border-radius: 20px;
    padding: 24px 16px;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.02);
  }

  .stat-box:hover {
    border-color: rgba(0, 242, 254, 0.2);
    background: rgba(0, 242, 254, 0.02);
    transform: translateY(-5px);
    box-shadow: 0 10px 24px rgba(0, 0, 0, 0.2), inset 0 1px 0 rgba(255, 255, 255, 0.05);
  }

  .stat-val {
    font-size: 32px;
    font-weight: 800;
    color: var(--teal);
    margin-bottom: 6px;
    background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .stat-lbl {
    font-size: 10px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.15em;
    font-weight: 700;
  }

  .guide-box {
    background: rgba(0, 242, 254, 0.02);
    border: 1px solid rgba(0, 242, 254, 0.15);
    border-left: 4px solid var(--teal);
    border-radius: 8px 20px 20px 8px;
    padding: 24px 28px;
    text-align: left;
    font-size: 14.5px;
    line-height: 1.7;
    color: var(--text);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  }

  .guide-box b {
    color: var(--text-white);
  }

  /* SCROLLBAR */
  ::-webkit-scrollbar { width: 5px; }
  ::-webkit-scrollbar-track { background: transparent; }
  ::-webkit-scrollbar-thumb { background: var(--border); border-radius: 10px; }

  @media(max-width: 768px) {
    body { flex-direction: column; }
    .sidebar { width: 100%; height: auto; border-right: none; border-bottom: 1px solid var(--border); }
    .nav-list { max-height: 200px; }
  }
</style>
</head>
<body>

<!-- SIDEBAR -->
<nav class="sidebar">
  <div class="sidebar-logo">
    <div class="sidebar-logo-glow"></div>
    <h1>DSA Notebook</h1>
    <p>Consolidated Library · Gaurav</p>
  </div>
  
  <div class="nav-list">
    <div class="nav-section-label">Table of Contents</div>
    
    <!-- DYNAMIC SIDEBAR LINKS WITH PREMIUM ICONS -->
"""

# Append links dynamically to prevent hardcoding issues
for i, item in enumerate(embedded_data):
    master_html += f"""    <button class="nav-btn" onclick="activateTab({i}, '{item['title']}')" id="btn-{i}">
      {svg_icons[item['icon']]}
      <span class="btn-right">
        <span class="btn-vol">{item['vol']}</span>
        <span class="btn-title">{item['title']}</span>
      </span>
    </button>
"""

master_html += """  </div>
  
  <div class="sidebar-footer">
    <div class="footer-copyright">
      © 2026 Gaurav · All Rights Reserved
    </div>
    <div class="linkedin-link-wrap">
      <a href="https://www.linkedin.com/in/gaurav-raj-lakshkar-7772252b2" target="_blank" class="linkedin-badge">
        <svg viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.779-1.75-1.75s.784-1.75 1.75-1.75 1.75.779 1.75 1.75-.784 1.75-1.75 1.75zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
        Connect on LinkedIn
      </a>
    </div>
  </div>
</nav>

<!-- MAIN CONTENT AREA -->
<main class="content-area" id="content-area">

  <!-- LANDING PAGE -->
  <div class="landing-page" id="landing-page">
    <div class="landing-card">
      <div class="landing-title">DSA Master <span>Notebook</span></div>
      <div class="landing-subtitle">Welcome to your ultimate digital handbook. All your notes, C++ templates, visual dry-runs, and algorithm analyses are compiled into this single, high-performance workspace.</div>
      
      <div class="stats-row">
        <div class="stat-box">
          <div class="stat-val">7</div>
          <div class="stat-lbl">Core Volumes</div>
        </div>
        <div class="stat-box">
          <div class="stat-val">35+</div>
          <div class="stat-lbl">DSA Patterns</div>
        </div>
        <div class="stat-box">
          <div class="stat-val">100%</div>
          <div class="stat-lbl">Bilingual (Hi-En)</div>
        </div>
      </div>
      
      <div class="guide-box">
        👈 <b>Get Started:</b> Select any volume from the left sidebar to load its interactive notes, visual trace matrices, and code templates immediately with zero delay.
      </div>
    </div>
  </div>

  <!-- IFRAMES CONTAINER -->
</main>

<script>
  // Base64 Data Store
  const filesData = [
"""

# Output base64 data to Javascript array
for i, item in enumerate(embedded_data):
    master_html += f"""    {{
      index: {i},
      title: "{item['title']}",
      filename: "{item['filename']}",
      b64: "{item['b64']}"
    }},\n"""

master_html += """  ];

  const contentArea = document.getElementById('content-area');
  const landingPage = document.getElementById('landing-page');
  const loadedIframes = {};

  function activateTab(index, title) {
    // Hide landing page
    landingPage.style.display = 'none';

    // Remove active class from all buttons
    document.querySelectorAll('.nav-btn').forEach(btn => btn.classList.remove('active'));
    // Add active to clicked button
    document.getElementById(`btn-${index}`).classList.add('active');

    // Hide all iframes
    document.querySelectorAll('.tab-iframe').forEach(iframe => iframe.classList.remove('active'));

    // Lazy load the iframe if not already loaded
    if (!loadedIframes[index]) {
      const iframe = document.createElement('iframe');
      iframe.className = 'tab-iframe';
      iframe.id = `iframe-${index}`;
      
      // Decode base64 html to utf-8 safely
      const binaryString = atob(filesData[index].b64);
      const bytes = new Uint8Array(binaryString.length);
      for (let i = 0; i < binaryString.length; i++) {
        bytes[i] = binaryString.charCodeAt(i);
      }
      const utf8Decoder = new TextDecoder('utf-8');
      const htmlContent = utf8Decoder.decode(bytes);

      // Create Blob URL to bypass local iframe srcdoc path limits
      const blob = new Blob([htmlContent], { type: 'text/html;charset=utf-8' });
      const blobURL = URL.createObjectURL(blob);
      
      iframe.src = blobURL;
      contentArea.appendChild(iframe);
      loadedIframes[index] = iframe;
    }

    // Show the selected iframe
    loadedIframes[index].classList.add('active');
  }

  // Bind dynamic mouse glow dynamic hover effect to nav buttons
  window.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.nav-btn').forEach(btn => {
      btn.addEventListener('mousemove', e => {
        const rect = btn.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        btn.style.setProperty('--x', `${x}px`);
        btn.style.setProperty('--y', `${y}px`);
      });
    });
  });
</script>
</body>
</html>
"""

# Write the final file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(master_html)

index_file = os.path.join(source_dir, "index.html")
with open(index_file, "w", encoding="utf-8") as f:
    f.write(master_html)

print(f"SUCCESS! Created master consolidated notebook: {output_file} and index.html ({len(master_html)} bytes)")
