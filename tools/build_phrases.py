"""Build shift-prep/phrases.html (copy sheet for loading dot phrases into Epic) from shift-prep/SMARTPHRASES.md."""
import html, json, pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent
md = (root / "shift-prep/SMARTPHRASES.md").read_text()
sections, cur = [], None
lines = md.splitlines()
i = 0
while i < len(lines):
    ln = lines[i]
    if ln.startswith("## "):
        cur = {"title": re.sub(r"\s*\(.*\)$", "", ln[3:]).strip(), "items": []}
        sections.append(cur)
    elif ln.startswith("### ") and cur is not None:
        m = re.match(r"### `(\.[A-Z]+)`:?\s*(.*)", ln)
        name, desc = m.group(1), m.group(2).strip()
        desc = re.sub(r"\s*\(see `MDM-GUIDE.md`.*\)", "", desc)
        j = i + 1
        while not lines[j].startswith("```"): j += 1
        k = j + 1
        while not lines[k].startswith("```"): k += 1
        cur["items"].append({"name": name, "desc": desc, "text": "\n".join(lines[j + 1:k])})
        i = k
    i += 1
sections = [s for s in sections if s["items"]]
total = sum(len(s["items"]) for s in sections)

def card(it):
    n, d, t = it["name"], it["desc"], it["text"]
    return f'''<article class="ph" data-name="{html.escape(n)}" data-search="{html.escape((n+' '+d+' '+t).lower())}">
  <header class="ph-h">
    <label class="done"><input type="checkbox" id="done-{n[1:]}" data-key="{n}"><span class="sr">Loaded in Epic</span></label>
    <div class="ph-id"><code class="nm">{html.escape(n)}</code>{f'<span class="ds">{html.escape(d)}</span>' if d else ''}</div>
    <div class="acts"><button type="button" class="b ghost" data-copy="name">Copy name</button><button type="button" class="b" data-copy="text">Copy text</button></div>
  </header>
  <pre class="tx">{html.escape(t)}</pre>
</article>'''

body = "\n".join(
    f'<section class="grp"><h2>{html.escape(s["title"])} <span class="ct">{len(s["items"])}</span></h2>\n' + "\n".join(card(it) for it in s["items"]) + "</section>"
    for s in sections)

page = r'''<title>JMC Dot Phrases</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=JetBrains+Mono:wght@400;600&display=swap">
<style>
/* Layout: one reading column; sticky toolbar (progress + search); each phrase is a card with copy actions and a "loaded" checkbox. */
:root{
  --bg:#f3f6f7; --surface:#ffffff; --code:#eef3f4; --line:#d5e0e3; --fg:#13262b; --muted:#557077;
  --accent:#0b6c77; --on-accent:#ffffff; --accent-soft:rgba(11,108,119,.10); --ok:#1d7a4a;
  --f-body:"Atkinson Hyperlegible",-apple-system,"Segoe UI",system-ui,sans-serif;
  --f-mono:"JetBrains Mono",ui-monospace,"SF Mono",Consolas,monospace;
}
@media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){
  --bg:#0e171a; --surface:#152226; --code:#0b1316; --line:#26393e; --fg:#e3eef0; --muted:#8ea7ad;
  --accent:#5ec6d0; --on-accent:#06262a; --accent-soft:rgba(94,198,208,.13); --ok:#56cf8e; color-scheme:dark } }
:root[data-theme="dark"]{
  --bg:#0e171a; --surface:#152226; --code:#0b1316; --line:#26393e; --fg:#e3eef0; --muted:#8ea7ad;
  --accent:#5ec6d0; --on-accent:#06262a; --accent-soft:rgba(94,198,208,.13); --ok:#56cf8e; color-scheme:dark }
*{box-sizing:border-box}
body{background:var(--bg);color:var(--fg);font-family:var(--f-body);font-size:16px;line-height:1.5;
  padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--bg)}
.wrap{max-width:860px;margin:0 auto;padding-block:24px 64px;display:flex;flex-direction:column;gap:22px}
h1{font-size:28px;line-height:1.15;margin:0;text-wrap:balance}
h2{font-size:15px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:0;display:flex;gap:8px;align-items:center}
.ct{font-family:var(--f-mono);font-size:12px;letter-spacing:0;background:var(--accent-soft);color:var(--accent);padding:1px 8px;border-radius:99px}
p{margin:0}
.lead{color:var(--muted);max-width:65ch}
.how{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:16px 18px}
.how ol{margin:8px 0 0;padding-left:20px;display:flex;flex-direction:column;gap:6px}
.how code,.lead code{font-family:var(--f-mono);font-size:.9em;background:var(--code);padding:1px 5px;border-radius:5px}
.bar{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--bg);padding-block:10px;border-bottom:1px solid var(--line);display:flex;gap:12px;align-items:center;flex-wrap:wrap}
.bar input[type=search]{flex:1 1 220px;min-width:0;font:inherit;padding:10px 12px;border-radius:10px;border:1px solid var(--line);background:var(--surface);color:var(--fg)}
.prog{display:flex;align-items:center;gap:10px;font-family:var(--f-mono);font-size:13px;color:var(--muted);font-variant-numeric:tabular-nums}
.meter{width:110px;height:8px;border-radius:99px;background:var(--line);overflow:hidden}
.meter i{display:block;height:100%;width:0;background:var(--ok);transition:width .25s}
.grp{display:flex;flex-direction:column;gap:12px}
.ph{background:var(--surface);border:1px solid var(--line);border-radius:14px;overflow:hidden}
.ph.is-done{opacity:.62}
.ph-h{display:flex;gap:12px;align-items:center;padding:12px 14px;flex-wrap:wrap}
.ph-id{flex:1 1 200px;min-width:0;display:flex;flex-direction:column}
.nm{font-family:var(--f-mono);font-weight:600;font-size:16px;color:var(--accent)}
.ds{color:var(--muted);font-size:14px}
.acts{display:flex;gap:8px}
.b{font:inherit;font-size:14px;font-weight:700;padding:8px 12px;border-radius:9px;border:1px solid var(--accent);background:var(--accent);color:var(--on-accent);cursor:pointer;min-height:40px}
.b.ghost{background:transparent;color:var(--accent)}
.b.copied{background:var(--ok);border-color:var(--ok);color:var(--on-accent)}
.done{display:grid;place-items:center;width:28px;height:28px;flex:none;cursor:pointer}
.done input{width:22px;height:22px;accent-color:var(--ok);cursor:pointer;margin:0}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
.tx{margin:0;padding:12px 14px;background:var(--code);border-top:1px solid var(--line);font-family:var(--f-mono);font-size:13px;line-height:1.55;white-space:pre-wrap;overflow-wrap:anywhere}
.empty{color:var(--muted);text-align:center;padding:24px}
.foot{color:var(--muted);font-size:14px}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
@media (prefers-reduced-motion: reduce){.meter i{transition:none}}
</style>
<div class="wrap">
  <header style="display:flex;flex-direction:column;gap:8px">
    <h1>JMC Dot Phrases</h1>
    <p class="lead">Personal add-ons to the UCI department templates. Attestations always use UCI's approved versions. __TOTAL__ phrases, generated from <code>shift-prep/SMARTPHRASES.md</code>.</p>
  </header>
  <div class="how">
    <strong>Loading each phrase into Epic</strong>
    <ol>
      <li>Epic menu, then <strong>SmartPhrase Manager</strong>, then <strong>New</strong>.</li>
      <li>Tap <strong>Copy name</strong> and paste it as the phrase name (Epic drops the leading dot).</li>
      <li>Tap <strong>Copy text</strong> and paste into the editor.</li>
      <li>Check the <code>@TOKEN@</code> links resolve (they turn into fields). If one doesn't, delete it and type <code>@</code> to search for UCI's version.</li>
      <li>Options in <code>{a/b/c}</code> paste as plain text. Either build them into a SmartList, or leave them and delete the unused options each time you write.</li>
      <li>Accept, then tick the box on the card. Ticks are saved in this browser only.</li>
    </ol>
  </div>
  <div class="bar">
    <input type="search" id="q" placeholder="Search phrases (sepsis, MDM, foley...)" aria-label="Search phrases">
    <div class="prog"><div class="meter"><i id="mi"></i></div><span id="pc">0 of __TOTAL__ loaded</span></div>
  </div>
  __BODY__
  <p class="empty" id="none" hidden>No phrases match that search.</p>
  <p class="foot">For education. Confirm billing language with UCI coding and compliance.</p>
</div>
<script>
(function(){
  var KEY="jmc-phrases-loaded", saved={};
  try{saved=JSON.parse(localStorage.getItem(KEY)||"{}")||{}}catch(e){saved={}}
  var boxes=[].slice.call(document.querySelectorAll(".done input")), total=boxes.length;
  function save(){try{localStorage.setItem(KEY,JSON.stringify(saved))}catch(e){}}
  function prog(){var n=boxes.filter(function(b){return b.checked}).length;
    document.getElementById("pc").textContent=n+" of "+total+" loaded";
    document.getElementById("mi").style.width=(total?100*n/total:0)+"%"}
  boxes.forEach(function(b){var k=b.dataset.key; b.checked=!!saved[k];
    b.closest(".ph").classList.toggle("is-done",b.checked);
    b.addEventListener("change",function(){saved[k]=b.checked;b.closest(".ph").classList.toggle("is-done",b.checked);save();prog()})});
  prog();
  function selectText(el){var r=document.createRange();r.selectNodeContents(el);var s=getSelection();s.removeAllRanges();s.addRange(r)}
  document.addEventListener("click",function(e){var btn=e.target.closest("[data-copy]"); if(!btn)return;
    var card=btn.closest(".ph"), isName=btn.dataset.copy==="name";
    var val=isName?card.dataset.name.slice(1):card.querySelector(".tx").textContent;
    var label=btn.textContent;
    function ok(){btn.classList.add("copied");btn.textContent="Copied";setTimeout(function(){btn.classList.remove("copied");btn.textContent=label},1400)}
    function fail(){selectText(isName?card.querySelector(".nm"):card.querySelector(".tx"));btn.textContent="Selected, press Ctrl+C";setTimeout(function(){btn.textContent=label},2200)}
    try{navigator.clipboard.writeText(val).then(ok,fail)}catch(err){fail()}});
  var q=document.getElementById("q"), cards=[].slice.call(document.querySelectorAll(".ph"));
  q.addEventListener("input",function(){var t=q.value.trim().toLowerCase(), any=false;
    cards.forEach(function(c){var m=!t||c.dataset.search.indexOf(t)>-1;c.hidden=!m;if(m)any=true});
    document.querySelectorAll(".grp").forEach(function(g){g.hidden=!g.querySelector(".ph:not([hidden])")});
    document.getElementById("none").hidden=any});
})();
</script>
'''
page = page.replace("__TOTAL__", str(total)).replace("__BODY__", body)
(root / "shift-prep/phrases.html").write_text(page)
print("built", total, "phrases")
