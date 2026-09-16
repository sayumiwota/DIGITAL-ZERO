from pathlib import Path
import json, subprocess
ROOT = Path(__file__).resolve().parents[1]
def load_config(): return json.loads((ROOT/'factory.config.json').read_text(encoding='utf-8'))
def git(*args, check=True): return subprocess.run(['git',*args],cwd=ROOT,check=check,text=True,capture_output=True)
def ensure_git_repo():
    p=git('rev-parse','--is-inside-work-tree',check=False)
    if p.returncode!=0 or p.stdout.strip()!='true': raise SystemExit('Run this inside a Git repository.')
def default_base_ref():
    for ref in ('origin/main','origin/master','main','master'):
        if git('rev-parse','--verify',ref,check=False).returncode==0: return ref
    return 'HEAD'
