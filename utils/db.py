import json, threading
from pathlib import Path

DATA_DIR=Path("data");DATA_DIR.mkdir(exist_ok=True)
_lock=threading.Lock()

def _load(p:Path):
 if not p.exists():return{}
 try:
  with open(p)as f:return json.load(f)
 except:return{}

def _save(p:Path,d:dict):
 try:
  t=p.with_suffix(".tmp")
  with open(t,"w")as f:json.dump(d,f,indent=2)
  t.rename(p);return True
 except:return False

def get(col:str,key:str,default=None):
 with _lock:
  p=DATA_DIR/f"{col}.json"
  d=_load(p);return d.get(key,default)

def setv(col:str,key:str,value):
 with _lock:
  p=DATA_DIR/f"{col}.json"
  d=_load(p);d[key]=value;return _save(p,d)

def remove(col:str,key:str):
 with _lock:
  p=DATA_DIR/f"{col}.json"
  d=_load(p);d.pop(key,None);return _save(p,d)
