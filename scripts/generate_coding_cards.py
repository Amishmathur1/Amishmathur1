import os

os.makedirs("assets/buttons", exist_ok=True)

coding_platforms = [
    {
        "name": "card_leetcode.svg",
        "title": "LeetCode",
        "subtitle": "Problem Solving",
        "icon": '''<path fill="#FFFFFF" d="M13.483 0a1.374 1.374 0 0 0-.961.438L7.116 6.226l-3.854 4.126a5.266 5.266 0 0 0-1.209 2.104 5.35 5.35 0 0 0-.125.513 5.527 5.527 0 0 0 .062 2.362 5.874 5.874 0 0 0 .349 1.017 5.938 5.938 0 0 0 4.818 3.564 5.923 5.923 0 0 0 2.457-.22 5.92 5.92 0 0 0 2.176-1.18l3.669-3.926a1.374 1.374 0 0 0-.064-1.936 1.374 1.374 0 0 0-1.936.064L9.757 16.71a3.17 3.17 0 0 1-1.166.632 3.18 3.18 0 0 1-1.319.118 3.19 3.19 0 0 1-2.59-1.916 3.15 3.15 0 0 1-.188-.546 2.97 2.97 0 0 1-.033-1.27 2.82 2.82 0 0 1 .65-1.13l3.853-4.125 5.405-5.788A1.374 1.374 0 0 0 13.483 0Zm-2.88 8.442a1.374 1.374 0 0 0-.97.402l-2.88 2.88a1.374 1.374 0 1 0 1.944 1.944l2.88-2.88a1.374 1.374 0 0 0-.974-2.346Z"/>'''
    },
    {
        "name": "card_codeforces.svg",
        "title": "Codeforces",
        "subtitle": "Competitive Programming",
        "icon": '''<path fill="#FFFFFF" d="M4.5 7.5a1.5 1.5 0 0 1 1.5 1.5v12a1.5 1.5 0 0 1-3 0V9a1.5 1.5 0 0 1 1.5-1.5Zm7.5-6a1.5 1.5 0 0 1 1.5 1.5v18a1.5 1.5 0 0 1-3 0V3a1.5 1.5 0 0 1 1.5-1.5Zm7.5 9a1.5 1.5 0 0 1 1.5 1.5v9a1.5 1.5 0 0 1-3 0v-9a1.5 1.5 0 0 1 1.5-1.5Z"/>'''
    },
    {
        "name": "card_codechef.svg",
        "title": "CodeChef",
        "subtitle": "Competitive Programming",
        "icon": '''<path fill="#FFFFFF" d="M12 2C8.5 2 5.5 4.2 4.5 7.2c-.3-.1-.7-.2-1-.2-1.9 0-3.5 1.6-3.5 3.5 0 1.7 1.2 3.1 2.8 3.4C2.9 15.8 4.2 17 6 17c.4 0 .7 0 1-.1 1.2 2 3.5 3.1 5.9 2.9 2.4.2 4.7-.9 5.9-2.9.3.1.6.1 1 .1 1.8 0 3.1-1.2 3.2-2.9 1.6-.3 2.8-1.7 2.8-3.4 0-1.9-1.6-3.5-3.5-3.5-.3 0-.7.1-1 .2C18.5 4.2 15.5 2 12 2Zm-5 17.5v2.5h10v-2.5H7Z"/>'''
    }
]

w, h = 186, 62
for c in coding_platforms:
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="8" fill="#080808" stroke="#2B2B2B" stroke-width="1"/>
  <g transform="translate(14, 18) scale(1.1)">
    {c["icon"]}
  </g>
  <text x="50" y="28" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="13" font-weight="700">{c["title"]}</text>
  <text x="50" y="44" fill="#888888" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="9" font-weight="400" letter-spacing="0.2px">{c["subtitle"]}</text>
</svg>'''
    with open(f"assets/buttons/{c['name']}", "w") as f:
        f.write(svg)

print("Coding platform cards generated!")
