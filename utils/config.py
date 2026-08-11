import os, json
from pathlib import Path

CD=Path("config");CD.mkdir(exist_ok=True)

def getc(k:str,d=None):
 cf=CD/"settings.json"
 if not cf.exists():return d
 try:
  with open(cf)as f:return json.load(f).get(k,d)
 except:return d

def setc(k:str,v):
 cf=CD/"settings.json"
 data={}
 if cf.exists():
  try:
   with open(cf)as f:data=json.load(f)
  except:pass
 data[k]=v
 try:
  with open(cf,"w")as f:json.dump(data,f,indent=2)
  return True
 except:return False
