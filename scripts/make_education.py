import base64

with open("assets/img/srm_campus.png", "rb") as f:
    srm_b64 = base64.b64encode(f.read()).decode("utf-8")

def make_pill(x, y, name, w=None):
    if w is None:
        w = max(60, len(name) * 7.5 + 24)
    return f'''<g transform="translate({x}, {y})">
      <rect x="0" y="0" width="{w}" height="24" rx="12" fill="#0A0A0A" stroke="#262626" stroke-width="1"/>
      <text x="{w/2}" y="16" text-anchor="middle" fill="#CCCCCC" class="sans" font-size="10.5" font-weight="500">{name}</text>
    </g>'''

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 210" width="100%" height="100%">
  <defs>
    <style>
      .mono {{ font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, Courier, monospace; }}
      .sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
    </style>
  </defs>

  <!-- Outer Frame -->
  <rect x="0.5" y="0.5" width="959" height="209" rx="8" fill="#000000" stroke="#222222" stroke-width="1"/>

  <!-- Section Header -->
  <g transform="translate(18, 14)">
    <rect x="0" y="0" width="36" height="22" rx="4" fill="#0D0D0D" stroke="#333333" stroke-width="1"/>
    <text x="18" y="15" text-anchor="middle" fill="#FFFFFF" class="mono" font-size="12" font-weight="700">05</text>
    <text x="44" y="15" fill="#AAAAAA" class="mono" font-size="11" font-weight="600" letter-spacing="1.5px">/ EDUCATION</text>
    <line x1="140" y1="11" x2="680" y2="11" stroke="#1F1F1F" stroke-width="1"/>
    <text x="924" y="15" text-anchor="end" fill="#777777" class="mono" font-size="9" letter-spacing="1.5px">FOUNDATIONS FOR A BIGGER TOMORROW</text>
  </g>

  <!-- Left: SRM Campus Image -->
  <g transform="translate(20, 48)">
    <clipPath id="eduClip">
      <rect x="0" y="0" width="330" height="144" rx="6"/>
    </clipPath>
    <image href="data:image/png;base64,{srm_b64}" width="330" height="144" preserveAspectRatio="xMidYMid slice" clip-path="url(#eduClip)"/>
  </g>

  <!-- Right: Details -->
  <g transform="translate(375, 48)">
    <!-- Graduation Cap Icon -->
    <g transform="translate(0, 4)">
      <path fill="#FFFFFF" transform="scale(1.2)" d="M12 3 1 9l11 6 9-4.91V17h2V9L12 3zM5 13.18v4L12 21l7-3.82v-4L12 17l-7-3.82z"/>
    </g>

    <!-- Degree and College -->
    <text x="36" y="18" fill="#FFFFFF" class="sans" font-size="14.5" font-weight="700">B.Tech — Electronics &amp; Computer Engineering</text>
    <text x="36" y="38" fill="#AAAAAA" class="sans" font-size="12" font-weight="600">SRM Institute of Science and Technology</text>

    <!-- Line & Description -->
    <line x1="36" y1="56" x2="65" y2="56" stroke="#444444" stroke-width="2"/>
    <text x="75" y="60" fill="#888888" class="sans" font-size="11.5">Building a foundation in technology and real-world problem solving.</text>

    <!-- Specialization Pills -->
    {make_pill(36, 84, "Electronics")}
    {make_pill(134, 84, "Computer Science")}
    {make_pill(276, 84, "Software Engineering")}
    {make_pill(434, 84, "Hardware Systems")}
    
    {make_pill(36, 118, "Embedded Systems")}
  </g>
</svg>'''

with open("assets/section_05_education.svg", "w") as f:
    f.write(svg_content)

print("section_05_education.svg generated!")
