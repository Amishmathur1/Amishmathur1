import os

os.makedirs("assets/buttons", exist_ok=True)

buttons = [
    {
        "name": "btn_linkedin.svg",
        "label": "LinkedIn",
        "svg_icon": '''<path fill="#FFFFFF" d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 10.9v8.37H9.2V10.9H6.46M7.83 6.45a1.62 1.62 0 1 0 0 3.24 1.62 1.62 0 0 0 0-3.24Z"/>'''
    },
    {
        "name": "btn_leetcode.svg",
        "label": "LeetCode",
        "svg_icon": '''<path fill="#FFFFFF" d="M13.483 0a1.374 1.374 0 0 0-.961.438L7.116 6.226l-3.854 4.126a5.266 5.266 0 0 0-1.209 2.104 5.35 5.35 0 0 0-.125.513 5.527 5.527 0 0 0 .062 2.362 5.874 5.874 0 0 0 .349 1.017 5.938 5.938 0 0 0 4.818 3.564 5.923 5.923 0 0 0 2.457-.22 5.92 5.92 0 0 0 2.176-1.18l3.669-3.926a1.374 1.374 0 0 0-.064-1.936 1.374 1.374 0 0 0-1.936.064L9.757 16.71a3.17 3.17 0 0 1-1.166.632 3.18 3.18 0 0 1-1.319.118 3.19 3.19 0 0 1-2.59-1.916 3.15 3.15 0 0 1-.188-.546 2.97 2.97 0 0 1-.033-1.27 2.82 2.82 0 0 1 .65-1.13l3.853-4.125 5.405-5.788A1.374 1.374 0 0 0 13.483 0Zm-2.88 8.442a1.374 1.374 0 0 0-.97.402l-2.88 2.88a1.374 1.374 0 1 0 1.944 1.944l2.88-2.88a1.374 1.374 0 0 0-.974-2.346Z"/>'''
    },
    {
        "name": "btn_github.svg",
        "label": "GitHub",
        "svg_icon": '''<path fill="#FFFFFF" d="M12 2A10 10 0 0 0 2 12c0 4.42 2.87 8.17 6.84 9.5.5.08.66-.23.66-.5v-1.69c-2.77.6-3.36-1.34-3.36-1.34-.46-1.16-1.11-1.47-1.11-1.47-.91-.62.07-.6.07-.6 1 .07 1.53 1.03 1.53 1.03.87 1.52 2.34 1.07 2.91.83.1-.65.35-1.09.63-1.34-2.22-.25-4.55-1.11-4.55-4.92 0-1.11.38-2 1.03-2.71-.1-.25-.45-1.29.1-2.64 0 0 .84-.27 2.75 1.02.79-.22 1.65-.33 2.5-.33.85 0 1.71.11 2.5.33 1.91-1.29 2.75-1.02 2.75-1.02.55 1.35.2 2.39.1 2.64.65.71 1.03 1.6 1.03 2.71 0 3.82-2.34 4.66-4.57 4.91.36.31.69.92.69 1.85V21c0 .27.16.59.67.5C19.14 20.16 22 16.42 22 12A10 10 0 0 0 12 2Z"/>'''
    },
    {
        "name": "btn_x.svg",
        "label": "X (Twitter)",
        "svg_icon": '''<path fill="#FFFFFF" d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>'''
    }
]

for b in buttons:
    width = 135 if len(b["label"]) > 8 else 115
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="32" viewBox="0 0 {width} 32">
  <rect x="0.5" y="0.5" width="{width - 1}" height="31" rx="4" fill="#080808" stroke="#333333" stroke-width="1"/>
  <g transform="translate(12, 8) scale(0.66)">
    {b["svg_icon"]}
  </g>
  <text x="36" y="20" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="12" font-weight="600" letter-spacing="0.3px">{b["label"]}</text>
</svg>'''
    with open(f"assets/buttons/{b['name']}", "w") as f:
        f.write(svg)

print("Social buttons created successfully!")

extra_buttons = [
    {
        "name": "btn_codeforces.svg",
        "label": "Codeforces",
        "svg_icon": '''<path fill="#FFFFFF" d="M4.5 7.5a1.5 1.5 0 0 1 1.5 1.5v12a1.5 1.5 0 0 1-3 0V9a1.5 1.5 0 0 1 1.5-1.5Zm7.5-6a1.5 1.5 0 0 1 1.5 1.5v18a1.5 1.5 0 0 1-3 0V3a1.5 1.5 0 0 1 1.5-1.5Zm7.5 9a1.5 1.5 0 0 1 1.5 1.5v9a1.5 1.5 0 0 1-3 0v-9a1.5 1.5 0 0 1 1.5-1.5Z"/>'''
    },
    {
        "name": "btn_codechef.svg",
        "label": "CodeChef",
        "svg_icon": '''<path fill="#FFFFFF" d="M12 2C8.5 2 5.5 4.2 4.5 7.2c-.3-.1-.7-.2-1-.2-1.9 0-3.5 1.6-3.5 3.5 0 1.7 1.2 3.1 2.8 3.4C2.9 15.8 4.2 17 6 17c.4 0 .7 0 1-.1 1.2 2 3.5 3.1 5.9 2.9 2.4.2 4.7-.9 5.9-2.9.3.1.6.1 1 .1 1.8 0 3.1-1.2 3.2-2.9 1.6-.3 2.8-1.7 2.8-3.4 0-1.9-1.6-3.5-3.5-3.5-.3 0-.7.1-1 .2C18.5 4.2 15.5 2 12 2Zm-5 17.5v2.5h10v-2.5H7Z"/>'''
    }
]

for b in extra_buttons:
    width = 125
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="32" viewBox="0 0 {width} 32">
  <rect x="0.5" y="0.5" width="{width - 1}" height="31" rx="4" fill="#080808" stroke="#333333" stroke-width="1"/>
  <g transform="translate(10, 8) scale(0.66)">
    {b["svg_icon"]}
  </g>
  <text x="34" y="20" fill="#FFFFFF" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="12" font-weight="600" letter-spacing="0.3px">{b["label"]}</text>
</svg>'''
    with open(f"assets/buttons/{b['name']}", "w") as f:
        f.write(svg)

print("Extra buttons created!")
