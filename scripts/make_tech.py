import base64

with open("assets/img/isometric_laptop.png", "rb") as f:
    iso_b64 = base64.b64encode(f.read()).decode("utf-8")

def make_badge(x, y, name, w=None):
    if w is None:
        w = max(60, len(name) * 8 + 24)
    # Return SVG group for a neat monochrome badge
    return f'''<g transform="translate({x}, {y})">
      <rect x="0" y="0" width="{w}" height="24" rx="4" fill="#0A0A0A" stroke="#262626" stroke-width="1"/>
      <circle cx="12" cy="12" r="3" fill="#FFFFFF"/>
      <text x="20" y="16" fill="#DDDDDD" class="sans" font-size="10.5" font-weight="500">{name}</text>
    </g>'''

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 270" width="100%" height="100%">
  <defs>
    <style>
      .mono {{ font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, Courier, monospace; }}
      .sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
    </style>
  </defs>

  <!-- Outer Frame -->
  <rect x="0.5" y="0.5" width="959" height="269" rx="8" fill="#000000" stroke="#222222" stroke-width="1"/>

  <!-- Section Header -->
  <g transform="translate(18, 14)">
    <rect x="0" y="0" width="36" height="22" rx="4" fill="#0D0D0D" stroke="#333333" stroke-width="1"/>
    <text x="18" y="15" text-anchor="middle" fill="#FFFFFF" class="mono" font-size="12" font-weight="700">03</text>
    <text x="44" y="15" fill="#AAAAAA" class="mono" font-size="11" font-weight="600" letter-spacing="1.5px">/ TECHNOLOGY</text>
    <line x1="160" y1="11" x2="740" y2="11" stroke="#1F1F1F" stroke-width="1"/>
    <text x="924" y="15" text-anchor="end" fill="#777777" class="mono" font-size="9" letter-spacing="1.5px">TOOLS THAT POWER MY IDEAS</text>
  </g>

  <!-- Left: Tech Stack Rows -->
  <g transform="translate(20, 50)">
    <!-- Row 1: Languages -->
    <text x="0" y="24" fill="#FFFFFF" class="sans" font-size="12.5" font-weight="700">Languages</text>
    {make_badge(130, 8, "Python")}
    {make_badge(210, 8, "C++")}
    {make_badge(270, 8, "C")}
    {make_badge(314, 8, "Java")}
    {make_badge(380, 8, "JavaScript")}
    {make_badge(476, 8, "TypeScript")}

    <line x1="0" y1="46" x2="660" y2="46" stroke="#191919" stroke-width="1"/>

    <!-- Row 2: Backend & Data -->
    <text x="0" y="74" fill="#FFFFFF" class="sans" font-size="12.5" font-weight="700">Backend &amp; Data</text>
    {make_badge(130, 58, "FastAPI")}
    {make_badge(212, 58, "Flask")}
    {make_badge(280, 58, "MySQL")}
    {make_badge(354, 58, "PostgreSQL")}
    {make_badge(454, 58, "MongoDB")}
    {make_badge(542, 58, "Redis")}

    <line x1="0" y1="96" x2="660" y2="96" stroke="#191919" stroke-width="1"/>

    <!-- Row 3: AI / ML -->
    <text x="0" y="124" fill="#FFFFFF" class="sans" font-size="12.5" font-weight="700">AI / ML</text>
    {make_badge(130, 108, "PyTorch")}
    {make_badge(216, 108, "TensorFlow")}
    {make_badge(316, 108, "OpenAI")}
    {make_badge(396, 108, "LangChain")}
    {make_badge(494, 108, "Hugging Face")}
    {make_badge(600, 108, "NumPy")}

    <line x1="0" y1="146" x2="660" y2="146" stroke="#191919" stroke-width="1"/>

    <!-- Row 4: Developer Tools -->
    <text x="0" y="174" fill="#FFFFFF" class="sans" font-size="12.5" font-weight="700">Developer Tools</text>
    {make_badge(130, 158, "Git")}
    {make_badge(185, 158, "GitHub")}
    {make_badge(260, 158, "Docker")}
    {make_badge(335, 158, "Linux")}
    {make_badge(405, 158, "VS Code")}
    {make_badge(488, 158, "Postman")}
    {make_badge(572, 158, "Figma")}
  </g>

  <!-- Vertical Divider -->
  <line x1="700" y1="50" x2="700" y2="250" stroke="#1F1F1F" stroke-width="1"/>

  <!-- Right: Isometric Visual and Tag -->
  <g transform="translate(712, 48)">
    <clipPath id="techClip">
      <rect x="0" y="0" width="230" height="155" rx="6"/>
    </clipPath>
    <image href="data:image/png;base64,{iso_b64}" width="230" height="155" preserveAspectRatio="xMidYMid slice" clip-path="url(#techClip)"/>
    
    <text x="10" y="182" fill="#777777" class="mono" font-size="8.5" font-weight="600" letter-spacing="1.5px">SAME TOOLS.</text>
    <text x="10" y="196" fill="#FFFFFF" class="mono" font-size="8.5" font-weight="700" letter-spacing="1.5px">BIGGER POSSIBILITIES.</text>
  </g>
</svg>'''

with open("assets/section_03_tech.svg", "w") as f:
    f.write(svg_content)

print("section_03_tech.svg generated!")
