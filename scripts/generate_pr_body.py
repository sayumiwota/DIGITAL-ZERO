#!/usr/bin/env python3
import argparse
ap=argparse.ArgumentParser(); ap.add_argument('--target',required=True); a=ap.parse_args()
print(f'''## Autonomous Engineering Factory\n\n### Target\n`{a.target}`\n\n### Policy\n- isolated branch/worktree\n- no automatic merge\n- AGENTS.md enforced\n\n### Evidence\nSee workflow logs and reports artifacts.\n\n### Risk\nAutomatically generated draft PR. Human review is required before merge.\n\n### Rollback\nRevert this PR if a regression is observed.\n''')
