# Changelog

## [0.3.0](https://github.com/yedeya-labs/kanon-sandbox/compare/candidate-v0.2.0...candidate-v0.3.0) (2026-10-31)


### Features

* third feature, for the first candidate ([0864b06](https://github.com/yedeya-labs/kanon-sandbox/commit/0864b069c162ba0828ccb5456c05a3b57a1af22d))


### Bug Fixes

* **build:** fail the build hook when release or output is empty ([#22](https://github.com/yedeya-labs/kanon-sandbox/issues/22)) ([3dd9fab](https://github.com/yedeya-labs/kanon-sandbox/commit/3dd9fab43f1b6a081e05d2aff1cf6b8f3bf355b2))
* **n12:** quote the own hook's description and run, so the file parses ([#13](https://github.com/yedeya-labs/kanon-sandbox/issues/13)) ([9be16e6](https://github.com/yedeya-labs/kanon-sandbox/commit/9be16e664eb1f20176a4548cdfc782ed99bd2f4b))
* **reusable:** pass github.workflow_ref to the run script through env ([#16](https://github.com/yedeya-labs/kanon-sandbox/issues/16)) ([0dda6bb](https://github.com/yedeya-labs/kanon-sandbox/commit/0dda6bbb31ffc4d692295e8bfafb5fe7ba0b3c75))
* the reusable workflow names its version ([043815a](https://github.com/yedeya-labs/kanon-sandbox/commit/043815a3847001bdfbebeeb16aecb0d3fc7a56d3))


### CI

* a dispatch-only probe of tag creation under the ruleset (S0 probe) ([7356b63](https://github.com/yedeya-labs/kanon-sandbox/commit/7356b639ec8a442752788919f7923048347d14c0))
* an adopter-side caller pinned to v1.0.0, and Dependabot (S0 probe) ([477993a](https://github.com/yedeya-labs/kanon-sandbox/commit/477993ad9fa140be65c80996b9106898b41f8bde))
* ask Dependabot to run again after promoting v1.1.0 (S0 probe) ([119db23](https://github.com/yedeya-labs/kanon-sandbox/commit/119db23239ef35542c330c63b056fccae2cea6de))
* call Kanon's full pipeline lanes for the fork-PR probe (kanon[#368](https://github.com/yedeya-labs/kanon-sandbox/issues/368)) ([#11](https://github.com/yedeya-labs/kanon-sandbox/issues/11)) ([5e60b90](https://github.com/yedeya-labs/kanon-sandbox/commit/5e60b90e5e45106b85b9b62c5ccfbf8b9c2dc4b9))
* move Kanon's pins to candidate-v0.42.0 for the N12 live run ([#10](https://github.com/yedeya-labs/kanon-sandbox/issues/10)) ([484a34f](https://github.com/yedeya-labs/kanon-sandbox/commit/484a34ff27391911a586ae6f8ab771e1101992eb))
* N12 live posts at Kanon candidate-v0.41.0 (digest lanes, Slack hook, test hooks) ([#9](https://github.com/yedeya-labs/kanon-sandbox/issues/9)) ([b131ecf](https://github.com/yedeya-labs/kanon-sandbox/commit/b131ecf268fceb64930ea6bbec8fcd2a4810cf64))
* pin the caller to v0.2.0 so a Dependabot run must propose a newer tag (S0 probe) ([af33f66](https://github.com/yedeya-labs/kanon-sandbox/commit/af33f664b96bb19b619a1e58511c410ea9270e5d))
* probe how a called workflow's environment job reads an environment secret ([9105e22](https://github.com/yedeya-labs/kanon-sandbox/commit/9105e2218af2232caaf7d45ba2545120cd6ceea3))
* rehearse the deploy secret at Kanon v0.40.1 (kanon[#1049](https://github.com/yedeya-labs/kanon-sandbox/issues/1049)) ([5e57379](https://github.com/yedeya-labs/kanon-sandbox/commit/5e57379601b06e3f9321755fe0a62397bca52a40))
* remove the secret probe (kanon[#1049](https://github.com/yedeya-labs/kanon-sandbox/issues/1049) holds its results) ([692ebee](https://github.com/yedeya-labs/kanon-sandbox/commit/692ebeed709226dc9d2c1f106a9a890d1a5f0aa6))
* set up plan 0010's D12 rehearsal of the deploy lane at Kanon v0.40.0 ([#6](https://github.com/yedeya-labs/kanon-sandbox/issues/6)) ([076abf2](https://github.com/yedeya-labs/kanon-sandbox/commit/076abf2cb92ef202d1e722e3931e699316073f17))
* the rehearsal's smoke fails on attempt 1 only; a composite action can't read vars ([f932807](https://github.com/yedeya-labs/kanon-sandbox/commit/f932807ed8bbdc3b0d70c468a2edd64268914f16))
* the secret probe maps constants too ([506dc6e](https://github.com/yedeya-labs/kanon-sandbox/commit/506dc6e6c2e063b11843a3540918dd831c7b83f0))
* throwaway probe of artifact download on a re-run of failed jobs (plan 0010 D5) ([3b2a898](https://github.com/yedeya-labs/kanon-sandbox/commit/3b2a89830033744a95cd080e2d28ae38946a6477))
* throwaway probes of environment jobs in called workflows (plan 0010 D0) ([e1a3b04](https://github.com/yedeya-labs/kanon-sandbox/commit/e1a3b040b8a0954fc820e6465f0c17c2cba273f8))


### Chores

* bound the first candidate's changelog at v0.2.0 with last-release-sha (S0 probe) ([5aa4e5b](https://github.com/yedeya-labs/kanon-sandbox/commit/5aa4e5b953bf6d3107288dbfe4841a0dd576314b))
* cut each release as a candidate, candidate-vX.Y.Z (S0 probe) ([13ba371](https://github.com/yedeya-labs/kanon-sandbox/commit/13ba37196ab28ef095204b32a430d04a74866524))

## 0.2.0 (fixture)

Hand-made fixture release for the S0 probe.

# Changelog

## 0.1.0 (fixture)

Hand-made fixture release for the S0 probe.
