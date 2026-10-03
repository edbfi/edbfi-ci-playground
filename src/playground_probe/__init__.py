# SPDX-License-Identifier: AGPL-3.0-only
"""Exercise the dependency that the playground installs."""

from typing import cast

import yaml


def ready(document: str) -> bool:
    return cast(object, yaml.safe_load(document)) == {"ready": True}
