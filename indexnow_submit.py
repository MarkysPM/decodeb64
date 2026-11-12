"""Envia todas las URLs de sitemap.xml a IndexNow (Bing, Yandex, etc.).
Uso: python indexnow_submit.py   (ejecutar DESPUES de desplegar el fichero de clave)"""
import json, re, urllib.request

HOST = "decodeb64.com"
KEY = "cb2f5c2c5d755f47a2ddc41a4ab55992"
xml = open("sitemap.xml", encoding="utf-8").read()
urls = sorted(set(re.findall(r"<loc>([^<]+)</loc>", xml)))
body = json.dumps({"host": HOST, "key": KEY,
                   "keyLocation": f"https://{HOST}/{KEY}.txt",
                   "urlList": urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
      headers={"Content-Type": "application/json; charset=utf-8"})
with urllib.request.urlopen(req) as r:
    print(r.status, len(urls), "URLs enviadas")
