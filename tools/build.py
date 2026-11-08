"""Build the installable (PWA) version of Plateau from src/index.html into docs/.
src/index.html is the same file published as the claude.ai artifact."""
import hashlib, json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / "src/index.html").read_text()
cut = src.index("</style>") + len("</style>")
head, body = src[:cut], src[cut:]
ver = hashlib.sha1(src.encode()).hexdigest()[:10]
pwa_head = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="192x192" href="icons/icon-192.png">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="theme-color" content="#0d1719">
<meta name="mobile-web-app-capable" content="yes">
<style>
html,body{margin:0}
[hidden]{display:none!important}
img{max-width:100%}
body{padding-top:env(safe-area-inset-top,0px);overscroll-behavior-y:none;-webkit-tap-highlight-color:transparent}
body::before{background:#0d1719}
</style>
"""
reg = f"""
<script>
try{{navigator.storage&&navigator.storage.persist&&navigator.storage.persist()}}catch(e){{}}
if("serviceWorker" in navigator){{window.addEventListener("load",()=>navigator.serviceWorker.register("sw.js").catch(()=>{{}}))}}
</script>
"""
html = "<!doctype html>\n<html lang=\"en\">\n<head>\n" + pwa_head + head + "\n</head>\n<body>\n" + body + reg + "</body>\n</html>\n"
out = root / "docs"
(out / "index.html").write_text(html)
manifest = {"name": "Plateau Vent Trainer", "short_name": "Plateau", "description": "Mechanical ventilation training: simulator, cases, questions, spaced review.",
  "start_url": "./", "scope": "./", "display": "standalone", "orientation": "portrait",
  "background_color": "#0d1719", "theme_color": "#0d1719",
  "icons": [{"src": "icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "icons/icon-512.png", "sizes": "512x512", "type": "image/png"},
            {"src": "icons/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]}
(out / "manifest.webmanifest").write_text(json.dumps(manifest, indent=2))
sw = """const CACHE="plateau-%s";
const SHELL=["./","index.html","manifest.webmanifest","icons/apple-touch-icon.png","icons/icon-192.png","icons/icon-512.png"];
self.addEventListener("install",e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(SHELL)).then(()=>self.skipWaiting()))});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener("fetch",e=>{
  const req=e.request;if(req.method!=="GET")return;
  const url=new URL(req.url);
  if(url.origin===location.origin){
    // Network first for the page so updates arrive; cache as offline fallback.
    e.respondWith(fetch(req).then(r=>{const cp=r.clone();caches.open(CACHE).then(c=>c.put(req,cp));return r}).catch(()=>caches.match(req).then(r=>r||caches.match("index.html"))));
  }else if(url.hostname.endsWith("fonts.googleapis.com")||url.hostname.endsWith("fonts.gstatic.com")){
    e.respondWith(caches.match(req).then(r=>r||fetch(req).then(res=>{const cp=res.clone();caches.open(CACHE).then(c=>c.put(req,cp));return res})));
  }
});
""" % ver
(out / "sw.js").write_text(sw)
(out / ".nojekyll").write_text("")
print("built", ver)
