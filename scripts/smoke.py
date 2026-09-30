# SPDX-License-Identifier: AGPL-3.0-only
from playground_probe import ready

assert ready("ready: true")
assert not ready("ready: false")
print("Installed package smoke check passed")
