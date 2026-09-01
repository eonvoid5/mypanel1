from http.server import BaseHTTPRequestHandler, HTTPServer
import json

SERVERS=[{"id":1,"name":"Survival SMP","status":"offline","players":0,"cpu":0,"memory":0},{"id":2,"name":"Creative","status":"offline","players":0,"cpu":0,"memory":0}]
class H(BaseHTTPRequestHandler):
 def send(self,code,data,ctype='application/json'):
  b=data.encode() if isinstance(data,str) else json.dumps(data).encode(); self.send_response(code); self.send_header('Content-Type',ctype); self.send_header('Content-Length',str(len(b))); self.end_headers(); self.wfile.write(b)
 def do_GET(self):
  if self.path=='/api/servers': self.send(200,SERVERS); return
  if self.path=='/':
   html='''<!doctype html><html><head><meta name="viewport" content="width=device-width"><title>VOID HOST</title><style>*{box-sizing:border-box}body{margin:0;min-height:100vh;color:#eafff0;font:15px system-ui;background:radial-gradient(circle at 20% 10%,#164b35,transparent 35%),linear-gradient(135deg,#06100d,#0b2118 55%,#020604)}main{max-width:1200px;margin:auto;padding:40px}.glass{background:#ffffff0d;border:1px solid #ffffff18;backdrop-filter:blur(22px);border-radius:24px;box-shadow:0 20px 70px #0008;padding:24px}.nav{display:flex;gap:12px;margin-bottom:24px}.nav button,button{border:1px solid #ffffff18;background:#ffffff0d;color:#eafff0;border-radius:14px;padding:12px 18px;cursor:pointer}.nav button:hover,button:hover{background:#ffffff18}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:18px}.status{color:#72ff9b}.big{font-size:30px;font-weight:700;margin:8px 0}</style></head><body><main><div class="nav"><button onclick="load('Dashboard')">Dashboard</button><button onclick="load('Servers')">Servers</button><button onclick="load('Console')">Console</button><button onclick="load('Files')">Files</button><button onclick="load('Admin')">Admin</button></div><section class="glass"><h1>VOID HOST</h1><p>Game server control panel</p><div id="app"></div></section></main><script>async function load(page){let a=document.getElementById('app');if(page==='Dashboard'||page==='Servers'){let s=await fetch('/api/servers').then(r=>r.json());a.innerHTML='<h2>'+page+'</h2><div class="grid">'+s.map(x=>`<div class="glass"><h2>${x.name}</h2><div class="status">${x.status}</div><div class="big">${x.players} players</div><p>CPU ${x.cpu}% · RAM ${x.memory} MB</p><button onclick="power(${x.id},'start')">Start</button> <button onclick="power(${x.id},'stop')">Stop</button></div>`).join('')+'</div>'}else a.innerHTML='<h2>'+page+'</h2><p>Module connected to the VoidHost application shell.</p>'}async function power(id,action){await fetch('/api/servers/'+id+'/'+action,{method:'POST'});load('Servers')}load('Dashboard')</script></body></html>'''
   self.send(200,html,'text/html'); return
  self.send(404,{"error":"Not found"})
 def do_POST(self):
  p=self.path.split('/');
  if len(p)==5 and p[1]=='api' and p[2]=='servers':
   try:s=next(x for x in SERVERS if x['id']==int(p[3])); s['status']='online' if p[4]=='start' else 'offline'; self.send(200,s)
   except StopIteration:self.send(404,{"error":"Server not found"})
   return
  self.send(404,{"error":"Not found"})
HTTPServer(('0.0.0.0',8080),H).serve_forever()
