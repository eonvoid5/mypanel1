from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import json, sqlite3
DB='voidhost.db'
conn=sqlite3.connect(DB,check_same_thread=False)
conn.execute('CREATE TABLE IF NOT EXISTS servers(id INTEGER PRIMARY KEY,name TEXT,status TEXT,cpu INTEGER,memory TEXT,address TEXT)')
if conn.execute('SELECT COUNT(*) FROM servers').fetchone()[0]==0:
 conn.executemany('INSERT INTO servers(name,status,cpu,memory,address) VALUES(?,?,?,?,?)',[('Survival SMP','online',38,'4.8 GB','play.voidhost.net:25565'),('Skyblock Network','online',17,'5.8 GB','sky.voidhost.net:25565'),('Modded Forge','online',41,'7.1 GB','forge.voidhost.net:25565')]);conn.commit()
class Handler(SimpleHTTPRequestHandler):
 def send_json(self,data,code=200):
  raw=json.dumps(data).encode();self.send_response(code);self.send_header('Content-Type','application/json');self.send_header('Content-Length',str(len(raw)));self.end_headers();self.wfile.write(raw)
 def do_GET(self):
  if self.path=='/api/servers':
   rows=conn.execute('SELECT id,name,status,cpu,memory,address FROM servers').fetchall();self.send_json([dict(zip(('id','name','status','cpu','memory','address'),r)) for r in rows]);return
  super().do_GET()
 def do_POST(self):
  if self.path.startswith('/api/servers/') and self.path.endswith('/power'):
   sid=int(self.path.split('/')[3]);n=int(self.headers.get('Content-Length',0));body=json.loads(self.rfile.read(n) or '{}');a=body.get('action','start');s={'start':'online','stop':'offline','kill':'offline','restart':'online'}.get(a,'online');conn.execute('UPDATE servers SET status=? WHERE id=?',(s,sid));conn.commit();self.send_json({'ok':True,'status':s});return
  if self.path=='/api/console':
   n=int(self.headers.get('Content-Length',0));body=json.loads(self.rfile.read(n) or '{}');self.send_json({'ok':True,'echo':body.get('command','')});return
  self.send_json({'error':'not found'},404)
print('VOID HOST API: http://0.0.0.0:8080')
ThreadingHTTPServer(('0.0.0.0',8080),Handler).serve_forever()
