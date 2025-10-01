<svg width="500" height="400" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="500" height="400" fill="#0d1117"/>
  
  <!-- Define the center point -->
  <defs>
    <radialGradient id="radarGlow" cx="50%" cy="50%">
      <stop offset="0%" style="stop-color:#30d158;stop-opacity:0.3"/>
      <stop offset="100%" style="stop-color:#30d158;stop-opacity:0"/>
    </radialGradient>
  </defs>
  
  <!-- Center point -->
  <g transform="translate(250, 200)">
    <!-- Grid circles -->
    <circle cx="0" cy="0" r="140" fill="none" stroke="#21262d" stroke-width="1"/>
    <circle cx="0" cy="0" r="105" fill="none" stroke="#21262d" stroke-width="1"/>
    <circle cx="0" cy="0" r="70" fill="none" stroke="#21262d" stroke-width="1"/>
    <circle cx="0" cy="0" r="35" fill="none" stroke="#21262d" stroke-width="1"/>
    
    <!-- Axis lines -->
    <line x1="0" y1="-140" x2="0" y2="140" stroke="#30d158" stroke-width="2"/>
    <line x1="-140" y1="0" x2="140" y2="0" stroke="#30d158" stroke-width="2"/>
    
    <!-- Filled area (Code review: 26%, Issues: 15%, Pull requests: 3%, Commits: 56%) -->
    <polygon points="0,-36.4 21,-0 0,4.2 -78.4,0" 
             fill="#30d158" 
             fill-opacity="0.4" 
             stroke="#30d158" 
             stroke-width="2"/>
    
    <!-- Glow effect -->
    <polygon points="0,-36.4 21,-0 0,4.2 -78.4,0" 
             fill="url(#radarGlow)" 
             stroke="none"/>
    
    <!-- Data points -->
    <circle cx="0" cy="-36.4" r="4" fill="#30d158"/>
    <circle cx="21" cy="0" r="4" fill="#30d158"/>
    <circle cx="0" cy="4.2" r="4" fill="#30d158"/>
    <circle cx="-78.4" cy="0" r="4" fill="#30d158"/>
    
    <!-- Labels -->
    <text x="0" y="-155" text-anchor="middle" fill="#8b949e" font-family="Arial, sans-serif" font-size="14" font-weight="500">Code review</text>
    <text x="0" y="-140" text-anchor="middle" fill="#8b949e" font-family="Arial, sans-serif" font-size="13">26%</text>
    
    <text x="155" y="5" text-anchor="start" fill="#8b949e" font-family="Arial, sans-serif" font-size="14" font-weight="500">Issues</text>
    <text x="155" y="20" text-anchor="start" fill="#8b949e" font-family="Arial, sans-serif" font-size="13">15%</text>
    
    <text x="0" y="170" text-anchor="middle" fill="#8b949e" font-family="Arial, sans-serif" font-size="14" font-weight="500">Pull requests</text>
    <text x="0" y="185" text-anchor="middle" fill="#8b949e" font-family="Arial, sans-serif" font-size="13">3%</text>
    
    <text x="-155" y="5" text-anchor="end" fill="#8b949e" font-family="Arial, sans-serif" font-size="14" font-weight="500">Commits</text>
    <text x="-155" y="20" text-anchor="end" fill="#8b949e" font-family="Arial, sans-serif" font-size="13">56%</text>
  </g>
</svg>
