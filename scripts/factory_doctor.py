#!/usr/bin/env python3
import json, shutil, sys
from common import ROOT
checks={'git':bool(shutil.which('git')),'python':bool(shutil.which('python') or shutil.which('python3')),'gh_optional':bool(shutil.which('gh')),'config':(ROOT/'factory.config.json').exists(),'agents_md':(ROOT/'AGENTS.md').exists(),'github_actions':(ROOT/'.github/workflows').exists()}
print(json.dumps(checks,indent=2))
if not all(checks[x] for x in ('git','python','config','agents_md')): sys.exit(1)
