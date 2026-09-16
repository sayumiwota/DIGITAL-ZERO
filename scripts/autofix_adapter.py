#!/usr/bin/env python3
import argparse,os,shlex,subprocess
from common import ROOT
ap=argparse.ArgumentParser(); ap.add_argument('--target',required=True); args=ap.parse_args()
prompt=f'''Inspect {args.target} for a concrete reproducible defect. Obey AGENTS.md. Make the smallest safe change. Add a regression test when possible. Never weaken tests. Leave the repository unchanged if no verified defect exists.'''
cmd=os.environ.get('AUTOFIX_COMMAND','').strip()
if not cmd:
    print('AUTOFIX_COMMAND not configured; analysis-only mode.'); print(prompt); raise SystemExit(0)
p=subprocess.run(shlex.split(cmd),cwd=ROOT,input=prompt,text=True); raise SystemExit(p.returncode)
