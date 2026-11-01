"""Build the separately named Glass Home card without replacing upstream assets."""
from pathlib import Path
import build

build.VERSION = '3.5.1'
build.PARTS.insert(build.PARTS.index('aurora-app.js'), 'room-controls.js')
text = build.bundle('/aurora_glass/btn/')
text = text.replace('Aurora <em>Glass</em>', 'Glass <em>Home</em>')
text = text.replace('Aurora Glass v3', 'Glass Home')
text += '\nif (!customElements.get("glass-home-card")) customElements.define("glass-home-card", class extends customElements.get("aurora-glass-card-3-5-1") {});\n'
text += r'''
/* Styling scoped to the separately registered Glass Home card. */
'''
# The additional rules are inserted in the generated wrapper CSS.
css = '.gh-controls{grid-column:1/-1;display:grid;gap:10px;width:100%;margin-top:12px}.gh-control{padding:12px;border:1px solid var(--border);border-radius:16px;background:var(--surface)}.gh-control-title{display:flex;align-items:center;gap:8px;flex-wrap:wrap;font-size:.85rem}.gh-control-title>i{color:var(--acc-text)}.gh-cover-state,.gh-appliance-state{margin-left:auto;color:var(--dim);font-size:.78rem}.gh-actions{display:flex;gap:6px;flex-wrap:wrap;margin-top:10px}.gh-actions .btn{min-height:40px;padding:8px 14px;font-size:.8rem}.gh-actions button:disabled{opacity:.35;cursor:not-allowed}.motion-state{font-size:.75rem;margin-left:5px}'
css += '.gh-control{position:relative;overflow:hidden;background:linear-gradient(130deg,color-mix(in srgb,var(--room) 12%,transparent),var(--surface));box-shadow:inset 0 1px 0 rgba(255,255,255,.07)}.gh-cover-art{height:82px;position:relative;width:72px;margin:0 auto 12px;border:4px solid #515c82;border-radius:5px;background:linear-gradient(#111b41,#8f88bd);box-shadow:0 5px 25px #0005}.gh-cover-art:after{content:"";position:absolute;inset:0;border-left:2px solid #7a83ac;left:48%}.gh-slats{position:absolute;inset:0 0 auto;height:var(--blind-closed,100%);background:repeating-linear-gradient(0deg,#8f9bbd 0 5px,#495474 6px 8px);transition:height .5s}.gh-blanket-art{height:82px;display:grid;place-items:center;position:relative;margin-bottom:12px}.gh-blanket-art i{width:110px;height:62px;border-radius:14px;background:repeating-linear-gradient(90deg,#8c6eab 0 12px,#5d4584 13px 15px);transform:perspective(100px) rotateX(15deg);box-shadow:0 10px 22px #0005}.gh-blanket-art span{position:absolute;z-index:1;top:-10px;font-size:36px;opacity:.25;color:#f4b16c}.gh-active .gh-blanket-art span{opacity:1;animation:gh-warm 2s ease-in-out infinite alternate}.gh-active{border-color:#d99b6b99}.gh-people{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:24px}.gh-person{display:flex;align-items:center;flex-direction:column;gap:8px;min-width:125px;padding:18px 22px;cursor:pointer;color:var(--text);background:linear-gradient(130deg,color-mix(in srgb,var(--b1) 14%,transparent),var(--surface))}.gh-home{border-color:#34d39977;box-shadow:0 0 25px #34d39915}.gh-avatar{width:62px;height:62px;border-radius:50%;overflow:hidden;display:grid;place-items:center;background:var(--surface-2);font-size:30px;border:2px solid var(--border)}.gh-avatar img{width:100%;height:100%;object-fit:cover}.gh-home .gh-avatar{border-color:#34d399aa}.gh-person-state{font-size:.8rem;color:var(--dim)}.gh-home .gh-person-state{color:var(--ok)}@keyframes gh-warm{to{transform:translateY(-5px);opacity:.65}}@media(prefers-reduced-motion:reduce){.gh-active .gh-blanket-art span{animation:none}}@media(max-width:560px){.gh-people{display:grid;grid-template-columns:repeat(2,1fr)}.gh-person{min-width:0;padding:14px}.gh-cover-state,.gh-appliance-state{width:100%;margin-left:0}}'
text = text.replace('CSS + "\\n" + OVERRIDES', 'CSS + "\\n" + OVERRIDES + ' + __import__('json').dumps(css))
target = Path(__file__).resolve().parent.parent / 'custom_components/aurora_glass/frontend/glass-home.js'
target.write_text(text, encoding='utf-8', newline='\n')
print(f'Built {target.name}: {len(text)} characters')
