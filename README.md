# edbfi-ci playground

Temporary integration fixture for [edbfi-ci](https://github.com/edbfi/edbfi-ci).
Older action, hook and Python lockfile pins intentionally produce real Dependabot updates.
The CI, PR policy and auto-merge workflows come from edbfi-ci templates.

Only disposable test data belongs here. `DEPENDENCY_AUTOMERGE_TOKEN` belongs only
in a Dependabot secret and must be scoped to this repository.

Test evidence and rollout decisions belong in the edbfi-ci S4 PR.
