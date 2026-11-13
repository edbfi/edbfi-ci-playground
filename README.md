# edbfi-ci playground

<p align="center">
  <a href="https://github.com/edbfi/edbfi-ci-playground/actions/workflows/ci.yml?query=branch%3Amain"><img src="https://img.shields.io/github/actions/workflow/status/edbfi/edbfi-ci-playground/ci.yml?branch=main&amp;event=push&amp;label=CI&amp;style=flat" alt="CI"></a>
</p>

Temporary integration fixture for [edbfi-ci](https://github.com/edbfi/edbfi-ci).
Older action, hook and Python lockfile pins intentionally produce real Dependabot updates.
The CI, PR policy and auto-merge workflows come from edbfi-ci templates.

Only disposable test data belongs here. `DEPENDENCY_AUTOMERGE_TOKEN` belongs only
in a Dependabot secret and must be scoped to this repository.

Test evidence and rollout decisions belong in edbfi-ci PRs.
