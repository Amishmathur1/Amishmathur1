import base64

with open("assets/img/mountain_wireframe.png", "rb") as f:
    mountain_b64 = base64.b64encode(f.read()).decode("utf-8")

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 250" width="100%" height="100%">
  <defs>
    <style>
      .mono {{ font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, Courier, monospace; }}
      .sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
    </style>
  </defs>

  <!-- Outer Frame -->
  <rect x="0.5" y="0.5" width="959" height="249" rx="8" fill="#000000" stroke="#222222" stroke-width="1"/>

  <!-- Section Header -->
  <g transform="translate(18, 14)">
    <rect x="0" y="0" width="36" height="22" rx="4" fill="#0D0D0D" stroke="#333333" stroke-width="1"/>
    <text x="18" y="15" text-anchor="middle" fill="#FFFFFF" class="mono" font-size="12" font-weight="700">02</text>
    <text x="44" y="15" fill="#AAAAAA" class="mono" font-size="11" font-weight="600" letter-spacing="1.5px">/ CURRENTLY BUILDING MYSELF</text>
    <line x1="280" y1="11" x2="740" y2="11" stroke="#1F1F1F" stroke-width="1"/>
    <text x="924" y="15" text-anchor="end" fill="#777777" class="mono" font-size="9" letter-spacing="1.5px">PROGRESS OVER PERFECTION</text>
  </g>

  <!-- 4 Cards Grid -->
  <!-- Card 1: AI / LLM -->
  <g transform="translate(20, 50)">
    <rect x="0" y="0" width="146" height="182" rx="8" fill="#080808" stroke="#262626" stroke-width="1"/>
    <!-- Icon: Brain / AI -->
    <circle cx="28" cy="28" r="14" fill="#141414"/>
    <path fill="#FFFFFF" transform="translate(19, 19) scale(0.75)" d="M12 2a4.5 4.5 0 0 0-4.5 4.5c0 .64.13 1.25.37 1.8A5.48 5.48 0 0 0 4 13.5C4 16.54 6.46 19 9.5 19h1v3h3v-3h1a4.5 4.5 0 0 0 4.5-4.5c0-.64-.13-1.25-.37-1.8A5.48 5.48 0 0 0 20 7.5C20 4.46 17.54 2 14.5 2h-2.5Zm-1 12H9.5A2.5 2.5 0 0 1 7 11.5c0-1.12.74-2.07 1.76-2.38l.8-.24-.26-.8A2.5 2.5 0 0 1 11 6.5V14Zm2 0V6.5a2.5 2.5 0 0 1 1.7 1.58l-.26.8.8.24A2.5 2.5 0 0 1 17 11.5a2.5 2.5 0 0 1-2.5 2.5H13Z"/>
    <text x="50" y="32" fill="#FFFFFF" class="sans" font-size="12" font-weight="700">AI / LLM</text>
    
    <text x="16" y="74" fill="#CCCCCC" class="sans" font-size="11.5">RAG</text>
    <text x="16" y="102" fill="#CCCCCC" class="sans" font-size="11.5">Embeddings</text>
    <text x="16" y="130" fill="#CCCCCC" class="sans" font-size="11.5">LLM Applications</text>
    <text x="16" y="158" fill="#CCCCCC" class="sans" font-size="11.5">Tool Calling</text>
  </g>

  <!-- Card 2: Backend -->
  <g transform="translate(178, 50)">
    <rect x="0" y="0" width="146" height="182" rx="8" fill="#080808" stroke="#262626" stroke-width="1"/>
    <!-- Icon: Server -->
    <circle cx="28" cy="28" r="14" fill="#141414"/>
    <path fill="#FFFFFF" transform="translate(20, 20) scale(0.66)" d="M4 3h16a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1Zm0 7h16a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1v-4a1 1 0 0 1 1-1Zm0 7h16a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1v-4a1 1 0 0 1 1-1Zm2-12v2h2V5H6Zm0 7v2h2v-2H6Zm0 7v2h2v-2H6Z"/>
    <text x="50" y="32" fill="#FFFFFF" class="sans" font-size="12" font-weight="700">Backend</text>
    
    <text x="16" y="74" fill="#CCCCCC" class="sans" font-size="11.5">FastAPI</text>
    <text x="16" y="102" fill="#CCCCCC" class="sans" font-size="11.5">REST APIs</text>
    <text x="16" y="130" fill="#CCCCCC" class="sans" font-size="11.5">SQL</text>
    <text x="16" y="158" fill="#CCCCCC" class="sans" font-size="11.5">Authentication</text>
  </g>

  <!-- Card 3: Problem Solving -->
  <g transform="translate(336, 50)">
    <rect x="0" y="0" width="154" height="182" rx="8" fill="#080808" stroke="#262626" stroke-width="1"/>
    <!-- Icon: Code -->
    <circle cx="28" cy="28" r="14" fill="#141414"/>
    <path fill="#FFFFFF" transform="translate(20, 20) scale(0.66)" d="M8.7 15.3 4.4 11 8.7 6.7a1 1 0 1 0-1.4-1.4l-5 5a1 1 0 0 0 0 1.4l5 5a1 1 0 1 0 1.4-1.4Zm6.6 0 4.3-4.3-4.3-4.3a1 1 0 1 1 1.4-1.4l5 5a1 1 0 0 1 0 1.4l-5 5a1 1 0 0 1-1.4-1.4Z"/>
    <text x="48" y="32" fill="#FFFFFF" class="sans" font-size="11.5" font-weight="700">Problem Solving</text>
    
    <text x="16" y="74" fill="#CCCCCC" class="sans" font-size="11.5">DSA</text>
    <text x="16" y="102" fill="#CCCCCC" class="sans" font-size="11.5">LeetCode</text>
    <text x="16" y="130" fill="#CCCCCC" class="sans" font-size="11.5">Algorithms</text>
    <text x="16" y="158" fill="#CCCCCC" class="sans" font-size="11.5">C++ / Python</text>
  </g>

  <!-- Card 4: Systems -->
  <g transform="translate(502, 50)">
    <rect x="0" y="0" width="146" height="182" rx="8" fill="#080808" stroke="#262626" stroke-width="1"/>
    <!-- Icon: CPU / Chip -->
    <circle cx="28" cy="28" r="14" fill="#141414"/>
    <path fill="#FFFFFF" transform="translate(20, 20) scale(0.66)" d="M6 4h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2Zm2 4v8h8V8H8Zm1-4v2h2V4H9Zm4 0v2h2V4h-2Zm-8 5v2h2V9H5Zm0 4v2h2v-2H5Zm14-4v2h2V9h-2Zm0 4v2h2v-2h-2Zm-10 7v2h2v-2H9Zm4 0v2h2v-2h-2Z"/>
    <text x="50" y="32" fill="#FFFFFF" class="sans" font-size="12" font-weight="700">Systems</text>
    
    <text x="16" y="74" fill="#CCCCCC" class="sans" font-size="11.5">System Design</text>
    <text x="16" y="102" fill="#CCCCCC" class="sans" font-size="11.5">Linux</text>
    <text x="16" y="130" fill="#CCCCCC" class="sans" font-size="11.5">Databases</text>
    <text x="16" y="158" fill="#CCCCCC" class="sans" font-size="11.5">Architecture</text>
  </g>

  <!-- Mountain Peak Artwork on Right -->
  <g transform="translate(660, 48)">
    <rect x="0" y="0" width="280" height="184" rx="8" fill="#000000"/>
    <clipPath id="mountClip">
      <rect x="0" y="0" width="280" height="184" rx="8"/>
    </clipPath>
    <image href="data:image/png;base64,{mountain_b64}" width="280" height="184" preserveAspectRatio="xMidYMid slice" clip-path="url(#mountClip)"/>
  </g>
</svg>'''

with open("assets/section_02_building.svg", "w") as f:
    f.write(svg_content)

print("section_02_building.svg generated!")
