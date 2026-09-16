#!/usr/bin/env python3
import argparse,json,random,secrets
from common import ROOT,load_config
cfg=load_config(); exts=set(cfg['source_extensions']); excluded=set(cfg['exclude_dirs'])
items=[]
for p in ROOT.rglob('*'):
    if p.is_file() and p.suffix in exts and not any(part in excluded for part in p.parts): items.append(p)
ap=argparse.ArgumentParser(); ap.add_argument('--seed',type=int); ap.add_argument('--json',action='store_true'); args=ap.parse_args()
seed=args.seed if args.seed is not None else secrets.randbits(32)
if not items:
    payload={'seed':seed,'path':'','candidate_count':0}
else:
    chosen=random.Random(seed).choice(sorted(items)); payload={'seed':seed,'path':str(chosen.relative_to(ROOT)),'candidate_count':len(items)}
print(json.dumps(payload,ensure_ascii=False) if args.json else payload['path'])
