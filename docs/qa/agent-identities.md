# Agent identities

The App register (`K-LAYOUT-6`). The sandbox calls the Full pipeline's lanes (kanon#368): they run as
the organisation's existing Judge App (Reviewer, Merger) and Author App (Implementer, Explorer, Lead,
Overseer), and the release caller maps the existing Releaser App's secrets. No key is stored here
unless the Owner adds it; the deploy lane itself runs as no App.

| Role | App slug | Contents | Issues | Pull requests | Workflows | Actions | Other |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Reviewer | `yedeya-labs-judge` | Read & write | Read & write | Read & write | No access | Read & write | Checks: Read, Commit statuses: Read |
| Implementer | `yedeya-labs-author` | Read & write | Read & write | Read & write | Read & write | Read | Commit statuses: Read & write |
| Explorer | `yedeya-labs-author` | Read & write | Read & write | Read & write | Read & write | Read | Commit statuses: Read & write |
| Lead | `yedeya-labs-author` | Read & write | Read & write | Read & write | Read & write | Read | Commit statuses: Read & write |
| Overseer | `yedeya-labs-author` | Read & write | Read & write | Read & write | Read & write | Read | Commit statuses: Read & write |
| Merger | `yedeya-labs-judge` | Read & write | Read & write | Read & write | No access | Read & write | Checks: Read, Commit statuses: Read |
| Releaser | `yedeya-labs-releaser` | Read & write | No access | Read & write | No access | No access | None |

Every App also holds Metadata: Read (`K-ADOPT-8`).
