import base64

with open("assets/img/about_coder.png", "rb") as f:
    coder_b64 = base64.b64encode(f.read()).decode("utf-8")

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 260" width="100%" height="100%">
  <defs>
    <style>
      .mono {{ font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, Courier, monospace; }}
      .sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
    </style>
  </defs>

  <!-- Outer Frame -->
  <rect x="0.5" y="0.5" width="959" height="259" rx="8" fill="#000000" stroke="#222222" stroke-width="1"/>

  <!-- Section Header -->
  <g transform="translate(18, 14)">
    <rect x="0" y="0" width="36" height="22" rx="4" fill="#0D0D0D" stroke="#333333" stroke-width="1"/>
    <text x="18" y="15" text-anchor="middle" fill="#FFFFFF" class="mono" font-size="12" font-weight="700">01</text>
    <text x="44" y="15" fill="#AAAAAA" class="mono" font-size="11" font-weight="600" letter-spacing="1.5px">/ ABOUT</text>
    <line x1="120" y1="11" x2="924" y2="11" stroke="#1F1F1F" stroke-width="1"/>
  </g>

  <!-- Left Column: Coder Image -->
  <g transform="translate(20, 52)">
    <rect x="0" y="0" width="260" height="192" rx="6" fill="#080808" stroke="#222222" stroke-width="1"/>
    <clipPath id="aboutClip">
      <rect x="1" y="1" width="258" height="190" rx="5"/>
    </clipPath>
    <image href="data:image/png;base64,{coder_b64}" width="258" height="190" preserveAspectRatio="xMidYMid slice" clip-path="url(#aboutClip)"/>
  </g>

  <!-- Middle Column: Info Table -->
  <g transform="translate(300, 52)">
    <!-- Row 1: Who I am -->
    <text x="0" y="24" fill="#FFFFFF" class="sans" font-size="12.5" font-weight="700">Who I am</text>
    <text x="130" y="20" fill="#AAAAAA" class="sans" font-size="12">I'm <tspan fill="#FFFFFF" font-weight="700">Amish Mathur</tspan>, a 4th-year Electronics &amp; Computer</text>
    <text x="130" y="38" fill="#AAAAAA" class="sans" font-size="12">Engineering student at <tspan fill="#FFFFFF" font-weight="700">SRM Institute of Science and Technology</tspan>.</text>
    
    <line x1="0" y1="52" x2="490" y2="52" stroke="#1A1A1A" stroke-width="1"/>

    <!-- Row 2: What I enjoy -->
    <text x="0" y="76" fill="#FFFFFF" class="sans" font-size="12.5" font-weight="700">What I enjoy</text>
    <text x="130" y="72" fill="#AAAAAA" class="sans" font-size="12">Building software around <tspan fill="#FFFFFF" font-weight="700">AI, backend engineering,</tspan></text>
    <text x="130" y="90" fill="#AAAAAA" class="sans" font-size="12"><tspan fill="#FFFFFF" font-weight="700">databases and algorithms</tspan>.</text>

    <line x1="0" y1="104" x2="490" y2="104" stroke="#1A1A1A" stroke-width="1"/>

    <!-- Row 3: How I learn -->
    <text x="0" y="128" fill="#FFFFFF" class="sans" font-size="12.5" font-weight="700">How I learn</text>
    <text x="130" y="128" fill="#AAAAAA" class="sans" font-size="12">Understand <tspan fill="#FFFFFF">→</tspan> build <tspan fill="#FFFFFF">→</tspan> break <tspan fill="#FFFFFF">→</tspan> debug <tspan fill="#FFFFFF">→</tspan> rebuild.</text>

    <line x1="0" y1="146" x2="490" y2="146" stroke="#1A1A1A" stroke-width="1"/>

    <!-- Row 4: Current direction -->
    <text x="0" y="168" fill="#FFFFFF" class="sans" font-size="12.5" font-weight="700">Current direction</text>
    <text x="130" y="166" fill="#AAAAAA" class="sans" font-size="12">Becoming a stronger software engineer by going deeper into</text>
    <text x="130" y="184" fill="#AAAAAA" class="sans" font-size="12"><tspan fill="#FFFFFF" font-weight="700">systems, AI and backend development</tspan>.</text>
  </g>

  <!-- Vertical Divider to Right Quote Column -->
  <line x1="810" y1="52" x2="810" y2="244" stroke="#1F1F1F" stroke-width="1"/>

  <!-- Right Column: Quote Card -->
  <g transform="translate(826, 68)">
    <text x="0" y="24" fill="#666666" class="sans" font-size="36" font-weight="900" font-family="Georgia, serif">“</text>
    
    <text x="0" y="60" fill="#AAAAAA" class="mono" font-size="9" font-weight="600" letter-spacing="1.5px">A CURIOUS</text>
    <text x="0" y="78" fill="#AAAAAA" class="mono" font-size="9" font-weight="600" letter-spacing="1.5px">MIND BUILDS</text>
    <text x="0" y="96" fill="#FFFFFF" class="mono" font-size="9" font-weight="700" letter-spacing="1.5px">EXTRAORDINARY</text>
    <text x="0" y="114" fill="#AAAAAA" class="mono" font-size="9" font-weight="600" letter-spacing="1.5px">THINGS.</text>
  </g>
</svg>'''

with open("assets/section_01_about.svg", "w") as f:
    f.write(svg_content)

print("section_01_about.svg generated!")
