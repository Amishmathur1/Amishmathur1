import base64

with open("assets/img/coding_chalkboard.png", "rb") as f:
    chalk_b64 = base64.b64encode(f.read()).decode("utf-8")

def make_pill(x, y, name, w=None):
    if w is None:
        w = max(60, len(name) * 7.5 + 22)
    return f'''<g transform="translate({x}, {y})">
      <rect x="0" y="0" width="{w}" height="24" rx="12" fill="#0A0A0A" stroke="#262626" stroke-width="1"/>
      <text x="{w/2}" y="16" text-anchor="middle" fill="#CCCCCC" class="sans" font-size="10.5" font-weight="500">{name}</text>
    </g>'''

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
    <text x="18" y="15" text-anchor="middle" fill="#FFFFFF" class="mono" font-size="12" font-weight="700">04</text>
    <text x="44" y="15" fill="#AAAAAA" class="mono" font-size="11" font-weight="600" letter-spacing="1.5px">/ CODING</text>
    <line x1="130" y1="11" x2="680" y2="11" stroke="#1F1F1F" stroke-width="1"/>
    <text x="924" y="15" text-anchor="end" fill="#777777" class="mono" font-size="9" letter-spacing="1.5px">PRACTICE TODAY  •  STRONGER TOMORROW</text>
  </g>

  <!-- Left: Chalkboard Artwork -->
  <g transform="translate(20, 48)">
    <clipPath id="codingClip">
      <rect x="0" y="0" width="260" height="196" rx="6"/>
    </clipPath>
    <image href="data:image/png;base64,{chalk_b64}" width="260" height="196" preserveAspectRatio="xMidYMid slice" clip-path="url(#codingClip)"/>
  </g>

  <!-- Right: Platform Cards and Focus Areas -->
  <g transform="translate(300, 48)">
    <!-- LeetCode Card -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="198" height="60" rx="8" fill="#080808" stroke="#282828" stroke-width="1"/>
      <path fill="#FFFFFF" transform="translate(16, 18) scale(1.1)" d="M13.483 0a1.374 1.374 0 0 0-.961.438L7.116 6.226l-3.854 4.126a5.266 5.266 0 0 0-1.209 2.104 5.35 5.35 0 0 0-.125.513 5.527 5.527 0 0 0 .062 2.362 5.874 5.874 0 0 0 .349 1.017 5.938 5.938 0 0 0 4.818 3.564 5.923 5.923 0 0 0 2.457-.22 5.92 5.92 0 0 0 2.176-1.18l3.669-3.926a1.374 1.374 0 0 0-.064-1.936 1.374 1.374 0 0 0-1.936.064L9.757 16.71a3.17 3.17 0 0 1-1.166.632 3.18 3.18 0 0 1-1.319.118 3.19 3.19 0 0 1-2.59-1.916 3.15 3.15 0 0 1-.188-.546 2.97 2.97 0 0 1-.033-1.27 2.82 2.82 0 0 1 .65-1.13l3.853-4.125 5.405-5.788A1.374 1.374 0 0 0 13.483 0Zm-2.88 8.442a1.374 1.374 0 0 0-.97.402l-2.88 2.88a1.374 1.374 0 1 0 1.944 1.944l2.88-2.88a1.374 1.374 0 0 0-.974-2.346Z"/>
      <text x="54" y="27" fill="#FFFFFF" class="sans" font-size="13" font-weight="700">LeetCode</text>
      <text x="54" y="44" fill="#888888" class="sans" font-size="10">Problem Solving</text>
    </g>

    <!-- Codeforces Card -->
    <g transform="translate(216, 0)">
      <rect x="0" y="0" width="198" height="60" rx="8" fill="#080808" stroke="#282828" stroke-width="1"/>
      <path fill="#FFFFFF" transform="translate(16, 18) scale(1.1)" d="M4.5 7.5a1.5 1.5 0 0 1 1.5 1.5v12a1.5 1.5 0 0 1-3 0V9a1.5 1.5 0 0 1 1.5-1.5Zm7.5-6a1.5 1.5 0 0 1 1.5 1.5v18a1.5 1.5 0 0 1-3 0V3a1.5 1.5 0 0 1 1.5-1.5Zm7.5 9a1.5 1.5 0 0 1 1.5 1.5v9a1.5 1.5 0 0 1-3 0v-9a1.5 1.5 0 0 1 1.5-1.5Z"/>
      <text x="54" y="27" fill="#FFFFFF" class="sans" font-size="13" font-weight="700">Codeforces</text>
      <text x="54" y="44" fill="#888888" class="sans" font-size="10">Competitive Programming</text>
    </g>

    <!-- CodeChef Card -->
    <g transform="translate(432, 0)">
      <rect x="0" y="0" width="198" height="60" rx="8" fill="#080808" stroke="#282828" stroke-width="1"/>
      <path fill="#FFFFFF" transform="translate(16, 18) scale(1.1)" d="M12 2C8.5 2 5.5 4.2 4.5 7.2c-.3-.1-.7-.2-1-.2-1.9 0-3.5 1.6-3.5 3.5 0 1.7 1.2 3.1 2.8 3.4C2.9 15.8 4.2 17 6 17c.4 0 .7 0 1-.1 1.2 2 3.5 3.1 5.9 2.9 2.4.2 4.7-.9 5.9-2.9.3.1.6.1 1 .1 1.8 0 3.1-1.2 3.2-2.9 1.6-.3 2.8-1.7 2.8-3.4 0-1.9-1.6-3.5-3.5-3.5-.3 0-.7.1-1 .2C18.5 4.2 15.5 2 12 2Zm-5 17.5v2.5h10v-2.5H7Z"/>
      <text x="54" y="27" fill="#FFFFFF" class="sans" font-size="13" font-weight="700">CodeChef</text>
      <text x="54" y="44" fill="#888888" class="sans" font-size="10">Competitive Programming</text>
    </g>

    <!-- Focus Areas Header -->
    <text x="0" y="98" fill="#FFFFFF" class="sans" font-size="13" font-weight="700">Focus Areas</text>

    <!-- Focus Areas Pills -->
    {make_pill(0, 114, "Arrays")}
    {make_pill(72, 114, "Graphs")}
    {make_pill(144, 114, "Trees")}
    {make_pill(210, 114, "Dynamic Programming")}
    {make_pill(374, 114, "Algorithms")}
    {make_pill(472, 114, "Math")}
    {make_pill(532, 114, "Greedy")}

    {make_pill(0, 148, "Binary Search")}
    {make_pill(114, 148, "Heaps")}
    {make_pill(184, 148, "Strings")}
  </g>
</svg>'''

with open("assets/section_04_coding.svg", "w") as f:
    f.write(svg_content)

print("section_04_coding.svg generated!")
