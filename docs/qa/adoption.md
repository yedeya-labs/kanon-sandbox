# Adoption record

`yedeya-labs/kanon-sandbox` adopts Kanon. This is its adoption record (`K-LAYOUT-10`), started by `kanon init` on 2026-10-15. A section or choice it leaves out means its documented default.

## People

| Role | Who |
|---|---|
| Owner | `@yedeya` |
| Maintainer | `@yedeya` |
| Stakeholder | `@yedeya` |

## Plan

`yedeya-labs/kanon-sandbox` is a **public repository on an organisation** (`K-ADOPT-2`). Of the platform features of `K-ADOPT-3`:

- **Rulesets:** available.
- **Merge queue:** available.
- **Environments:** the deploy lane deploys to the ones ## Deploy declares, each a GitHub environment.

## Bootstrap

`in bootstrap since 2026-10-15`

## Choices

- **Feature:** `full`
- **Review trigger:** `labelled`
- **Overseer:** `installed`
- **Chat channel:** Slack, through Kanon's Slack hook (one secret per kind)

## Data

Whether this repository holds private or sensitive material, which nobody declared at install. The lanes read the files and diffs their work needs either way.

- **Private or sensitive material:** `not declared`

## Deploy

The deploy lane's environments, in deploy order: each deploys only after the one before it succeeded on the same release, and the last is production. `kanon init` writes the deploy caller from this list; the reference deploy is the first environment's (`K-PROJ-11`).

- **Environments:** `probe-staging`, `probe-production`
- **Reference environment:** `probe-staging`
- **Reference deploy workflow:** `deploy.yml`
- **Reference deploy job:** `probe-staging / deploy`
