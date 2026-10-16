# edbfi-ci playground

Temporary integration fixture for [edbfi-ci](https://github.com/edbfi/edbfi-ci).
Older action, hook and Python lockfile pins intentionally produce real Dependabot updates.
The CI, PR policy and auto-merge workflows come from edbfi-ci templates.

Only disposable test data belongs here. `DEPENDENCY_AUTOMERGE_TOKEN` belongs only
in a Dependabot secret and must be scoped to this repository.

Test evidence and rollout decisions belong in the edbfi-ci S4 PR.

## Temporary T3 Code watcher reproduction

This disposable PR tests notifications for a failed required check, Pullfrog
review activity, and recovery to passing checks. Its initial commit deliberately
omits the DCO sign-off so the existing `pr-policy` check fails. A later revision
will add the sign-off without changing the file contents.

Do not merge this fixture. Record watcher registration, GitHub event timestamps,
and any watcher errors before closing the test PR.
