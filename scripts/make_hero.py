import base64

with open("assets/img/hero_astronaut.png", "rb") as f:
    hero_b64 = base64.b64encode(f.read()).decode("utf-8")

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 290" width="100%" height="100%">
  <defs>
    <linearGradient id="fadeLeft" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#000000" stop-opacity="1"/>
      <stop offset="25%" stop-color="#000000" stop-opacity="0.8"/>
      <stop offset="60%" stop-color="#000000" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="fadeBottom" x1="0" y1="1" x2="0" y2="0">
      <stop offset="0%" stop-color="#000000" stop-opacity="1"/>
      <stop offset="20%" stop-color="#000000" stop-opacity="0"/>
    </linearGradient>
    <style>
      .mono {{ font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, Courier, monospace; }}
      .sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
    </style>
  </defs>

  <!-- Outer Frame -->
  <rect x="0.5" y="0.5" width="959" height="289" rx="8" fill="#000000" stroke="#222222" stroke-width="1"/>

  <!-- Top Nav Bar -->
  <line x1="0" y1="38" x2="960" y2="38" stroke="#1F1F1F" stroke-width="1"/>
  <text x="24" y="24" fill="#FFFFFF" class="mono" font-size="13" font-weight="700">&lt;/&gt;</text>
  
  <text x="140" y="24" fill="#777777" class="mono" font-size="10" letter-spacing="1.5px">01. ABOUT</text>
  <text x="245" y="24" fill="#777777" class="mono" font-size="10" letter-spacing="1.5px">02. CURRENTLY</text>
  <text x="375" y="24" fill="#777777" class="mono" font-size="10" letter-spacing="1.5px">03. TECHNOLOGY</text>
  <text x="515" y="24" fill="#777777" class="mono" font-size="10" letter-spacing="1.5px">04. CODING</text>
  <text x="630" y="24" fill="#777777" class="mono" font-size="10" letter-spacing="1.5px">05. EDUCATION</text>
  
  <text x="936" y="24" text-anchor="end" fill="#777777" class="mono" font-size="11" letter-spacing="1px">// AMISH MATHUR</text>

  <!-- Astronaut Image Background (Masked on Left and Bottom) -->
  <g transform="translate(420, 39)">
    <image href="data:image/png;base64,{hero_b64}" width="430" height="250" preserveAspectRatio="xMidYMid slice"/>
    <rect x="0" y="0" width="180" height="250" fill="url(#fadeLeft)"/>
    <rect x="0" y="200" width="430" height="50" fill="url(#fadeBottom)"/>
  </g>

  <!-- Left Content -->
  <text x="32" y="78" fill="#777777" class="mono" font-size="9.5" letter-spacing="3.5px">BUILD  &gt;  LEARN  &gt;  IMPROVE  &gt;  REPEAT</text>
  
  <text x="32" y="128" fill="#FFFFFF" class="sans" font-size="40" font-weight="900" letter-spacing="1.5px">AMISH MATHUR</text>
  <text x="32" y="152" fill="#AAAAAA" class="sans" font-size="11.5" font-weight="600" letter-spacing="3px">ELECTRONICS &amp; COMPUTER ENGINEERING</text>

  <!-- Quote Callout -->
  <line x1="32" y1="184" x2="32" y2="236" stroke="#FFFFFF" stroke-width="2.5"/>
  <text x="46" y="204" fill="#FFFFFF" class="sans" font-size="14" font-weight="500" font-style="italic">"Building AI-powered software</text>
  <text x="46" y="226" fill="#FFFFFF" class="sans" font-size="14" font-weight="500" font-style="italic">with curiosity and intent."</text>

  <!-- Right Sidebar Manifesto -->
  <line x1="850" y1="52" x2="850" y2="270" stroke="#1F1F1F" stroke-width="1"/>
  
  <text x="864" y="80" fill="#777777" class="mono" font-size="8" font-weight="600" letter-spacing="1.5px">IDEAS</text>
  <text x="864" y="96" fill="#777777" class="mono" font-size="8" font-weight="600" letter-spacing="1.5px">CODE</text>
  <text x="864" y="112" fill="#777777" class="mono" font-size="8" font-weight="600" letter-spacing="1.5px">SYSTEMS</text>
  <text x="864" y="128" fill="#777777" class="mono" font-size="8" font-weight="600" letter-spacing="1.5px">PEOPLE</text>
  <text x="864" y="144" fill="#777777" class="mono" font-size="7.5" font-weight="600" letter-spacing="0.5px">A BETTER TOMORROW</text>
  
  <line x1="864" y1="160" x2="894" y2="160" stroke="#333333" stroke-width="1.5"/>
  
  <text x="864" y="188" fill="#FFFFFF" font-size="15">✦</text>
  
  <text x="864" y="210" fill="#CCCCCC" class="mono" font-size="8.5" font-weight="700" letter-spacing="1.5px">TURNING</text>
  <text x="864" y="224" fill="#CCCCCC" class="mono" font-size="8.5" font-weight="700" letter-spacing="1.5px">IDEAS</text>
  <text x="864" y="238" fill="#CCCCCC" class="mono" font-size="8.5" font-weight="700" letter-spacing="1.5px">INTO</text>
  <text x="864" y="252" fill="#CCCCCC" class="mono" font-size="8.5" font-weight="700" letter-spacing="1.5px">IMPACT.</text>
</svg>'''

with open("assets/hero.svg", "w") as f:
    f.write(svg_content)

print("Updated hero.svg generated!")
