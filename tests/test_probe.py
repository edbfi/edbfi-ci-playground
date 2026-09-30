# SPDX-License-Identifier: AGPL-3.0-only
from playground_probe import ready


def test_ready() -> None:
    assert ready("ready: true")


def test_not_ready() -> None:
    assert not ready("ready: false")
