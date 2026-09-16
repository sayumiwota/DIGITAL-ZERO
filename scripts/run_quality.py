#!/usr/bin/env python3
import argparse,json,subprocess,time
from common import ROOT,load_config
ap=argparse.ArgumentParser(); ap.add_argument('--allow-empty',action='store_true'); args=ap.parse_args(); results=[]
for group,commands in load_config()['quality_commands'].items():
    for cmd in commands:
        t=time.time(); p=subprocess.run(cmd,cwd=ROOT,shell=True,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        results.append({'group':group,'command':cmd,'returncode':p.returncode,'duration_sec':round(time.time()-t,3),'output':p.stdout[-20000:]})
(ROOT/'reports').mkdir(exist_ok=True); (ROOT/'reports/quality.json').write_text(json.dumps(results,indent=2,ensure_ascii=False),encoding='utf-8')
if not results and not args.allow_empty: raise SystemExit('No quality commands configured.')
if any(r['returncode']!=0 for r in results): raise SystemExit(1)
