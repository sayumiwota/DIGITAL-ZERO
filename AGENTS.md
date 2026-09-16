# AGENTS.md

## Mission
Make the smallest reversible change that solves a verified problem.

## Engineering Principles
1. Investigate impact before editing.
2. Preserve public behavior unless explicitly changed.
3. Prefer minimal dependencies.
4. Keep changes reversible.
5. Separate evidence from assumptions.
6. Never weaken or delete meaningful tests just to make CI pass.

## Forbidden Patterns
- hard-coded credentials, tokens, API keys, or passwords
- silent exception swallowing
- unchecked casts used only to bypass type errors
- unrelated refactoring inside a focused fix
- direct production mutation
- destructive migration without rollback
- duplicated domain/business logic
- disabling security checks to make a build green

## Required Checks
Before: dependency impact, API/schema contracts, tests, security surface, migration impact.
After: lint, typecheck where applicable, unit/integration tests, security scan, regression check, final diff review.

## Parallel Implementation
For high-impact work compare up to three variants: `minimal`, `maintainable`, `performance`.
A candidate is ineligible if a mandatory quality gate fails.

## Autonomous Changes Allowed
Branches, worktrees, isolated code edits, tests, static/dynamic analysis, benchmarks, docs, draft PRs, preview/staging deploys.

## Approval Required
Default-branch merge, production DB migration, IAM/permission changes, secret rotation/disclosure, destructive infrastructure deletion, irreversible data transformation, high-risk production rollout/rollback.

## PR Evidence
Problem, reproduction/evidence, files changed, commands, test results, security results, benchmark when relevant, remaining risks, rollback plan.
