#!/usr/bin/env python3
import argparse,json,subprocess,time,statistics
from common import ROOT,load_config
cfg=load_config()['benchmark']; ap=argparse.ArgumentParser(); ap.add_argument('--name',required=True); ap.add_argument('--command',required=True); ap.add_argument('--runs',type=int,default=cfg['runs']); ap.add_argument('--warmups',type=int,default=cfg['warmups']); ap.add_argument('--timeout',type=int,default=cfg['timeout_seconds']); args=ap.parse_args()
def run():
    t=time.perf_counter(); p=subprocess.run(args.command,cwd=ROOT,shell=True,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=args.timeout); return p.returncode,time.perf_counter()-t,p.stdout
for _ in range(args.warmups):
    code,_,_=run()
    if code: raise SystemExit('Warmup failed')
times=[]
for _ in range(args.runs):
    code,elapsed,_=run()
    if code: raise SystemExit('Benchmark failed')
    times.append(elapsed)
result={'name':args.name,'command':args.command,'runs':args.runs,'mean_sec':round(statistics.mean(times),6),'median_sec':round(statistics.median(times),6),'min_sec':round(min(times),6),'max_sec':round(max(times),6)}
(ROOT/'reports').mkdir(exist_ok=True); (ROOT/f'reports/benchmark-{args.name}.json').write_text(json.dumps(result,indent=2),encoding='utf-8'); print(json.dumps(result,indent=2))
