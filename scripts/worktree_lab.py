#!/usr/bin/env python3
import argparse,json,re,subprocess
from common import ROOT,load_config,ensure_git_repo,git,default_base_ref
def slug(s): return re.sub(r'[^a-zA-Z0-9._-]+','-',s).strip('-').lower()
def prepare(feature,base):
    ensure_git_repo(); feature=slug(feature); wtroot=ROOT/'.worktrees'; wtroot.mkdir(exist_ok=True); manifest={'feature':feature,'base':base,'variants':{}}
    for variant in load_config()['worktree_variants']:
        branch=f'ai/{feature}/{variant}'; path=wtroot/f'{feature}-{variant}'; exists=git('show-ref','--verify','--quiet',f'refs/heads/{branch}',check=False).returncode==0
        if not path.exists():
            cmd=['worktree','add'];
            if not exists: cmd += ['-b',branch]
            cmd += [str(path),branch if exists else base]; p=git(*cmd,check=False)
            if p.returncode: raise SystemExit(p.stderr or p.stdout)
        manifest['variants'][variant]={'branch':branch,'path':str(path)}
    out=wtroot/f'{feature}.json'; out.write_text(json.dumps(manifest,indent=2),encoding='utf-8'); print(out)
def status(feature):
    manifest=json.loads((ROOT/'.worktrees'/f'{slug(feature)}.json').read_text())
    for variant,item in manifest['variants'].items():
        p=subprocess.run(['git','status','--short'],cwd=item['path'],text=True,capture_output=True); print(f"[{variant}] {item['branch']}: {p.stdout.strip() or 'clean'}")
ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='cmd',required=True); p=sub.add_parser('prepare'); p.add_argument('--feature',required=True); p.add_argument('--base'); s=sub.add_parser('status'); s.add_argument('--feature',required=True); a=ap.parse_args(); prepare(a.feature,a.base or default_base_ref()) if a.cmd=='prepare' else status(a.feature)
