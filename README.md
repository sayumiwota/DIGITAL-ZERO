# DIGITAL ZERØ | Autonomous Software Engineering Factory v3

DIGITAL ZERØ の自律型ソフトウェア開発基盤と Engineering Control Center。

## Runtime
- Next.js 16.3.3 (Active LTS security patch line)
- React 19.3
- Node.js 24 LTS
- TypeScript 6

## Core Flow
Detect → Analyze → Parallelize → Implement → Test → Security → Benchmark → PR → Human Gate → Deploy → Observe

## App
- `/` Engineering Control Center
- `/api/health` machine-readable health endpoint

## Quality
`npm run verify` executes lint, typecheck, unit test, and production build. The factory adds npm security audit as a separate gate.

## Automation
- Quality Gate: every PR/push
- Nightly Bug Hunt: 02:00 JST
- Weekly Code Health: Monday 05:00 JST
- Worktree Lab: minimal / maintainable / performance

## Safety Boundary
Automation is designed to stop at PR creation. Default-branch auto-merge, production DB destructive changes, IAM/permissions, secrets, irreversible migrations, and high-risk production changes remain approval-gated.
