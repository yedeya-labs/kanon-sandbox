# Agent identities

The App register (`K-LAYOUT-6`). For plan 0010's D12 rehearsal: the sandbox's one lane caller, the
issue backstop, runs as the organisation's existing Author App, and the release caller maps the
existing Releaser App's secrets. Neither key is stored here unless the Owner adds it; the deploy
lane itself runs as no App.

| Role | App slug | Contents | Issues | Pull requests | Workflows | Actions | Other |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Implementer | `yedeya-labs-author` | Read & write | Read & write | Read & write | Read & write | Read | Commit statuses: Read & write |
| Explorer | `yedeya-labs-author` | Read & write | Read & write | Read & write | Read & write | Read | Commit statuses: Read & write |
| Lead | `yedeya-labs-author` | Read & write | Read & write | Read & write | Read & write | Read | Commit statuses: Read & write |
| Overseer | `yedeya-labs-author` | Read & write | Read & write | Read & write | Read & write | Read | Commit statuses: Read & write |
| Releaser | `yedeya-labs-releaser` | Read & write | No access | Read & write | No access | No access | None |

Every App also holds Metadata: Read (`K-ADOPT-8`).
