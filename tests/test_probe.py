# SPDX-License-Identifier: AGPL-3.0-only
from playground_probe import ready
import pytest


def test_ready() -> None:
    assert ready("ready: true")


def test_not_ready() -> None:
    assert not ready("ready: false")


@pytest.mark.parametrize("document", ["", "{}", "ready: null", "ready: no-thanks", "ready: false\nextra: 1"])
def test_non_ready_documents(document: str) -> None:
    assert not ready(document)
