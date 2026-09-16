# DIGITAL ZERØ | Autonomous Software Engineering Factory v3

DIGITAL ZERØ の自律型ソフトウェア開発基盤。

## Core Flow
Detect → Analyze → Parallelize → Implement → Test → Security → Benchmark → PR → Human Gate → Deploy → Observe

## Included
- Git worktree 3方式比較（minimal / maintainable / performance）
- Nightly Bug Hunt
- Quality Gate
- Weekly Code Health
- Evidence-based PR generation
- AGENTS.md governance

## Safety Boundary
自動化は原則としてPR作成まで。`main`への自動マージ、本番DB破壊的変更、IAM/権限、Secret、不可逆マイグレーション、高リスク本番変更は承認ゲートを必須とする。
