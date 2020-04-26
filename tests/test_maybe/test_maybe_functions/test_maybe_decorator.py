from typing import Dict, Optional

import pytest

from returns.maybe import Nothing, Some, maybe


@maybe
def _function(hashmap: Dict[str, str], key: str) -> Optional[str]:
    return hashmap.get(key, None)


@maybe
async def _coroutine(hashmap: Dict[str, str], key: str) -> Optional[str]:
    return hashmap.get(key, None)


def test_maybe_some():
    """Ensures that maybe decorator works correctly for some case."""
    assert _function({'a': 'b'}, 'a') == Some('b')


def test_maybe_nothing():
    """Ensures that maybe decorator works correctly for nothing case."""
    assert _function({'a': 'b'}, 'c') == Nothing


@pytest.mark.anyio
async def test_async_maybe_some():
    """Ensures that maybe decorator works correctly for some case."""
    container = await _coroutine({'a': 'b'}, 'a')
    assert container == Some('b')


@pytest.mark.anyio
async def test_async_maybe_nothing():
    """Ensures that maybe decorator works correctly for nothing case."""
    container = await _coroutine({'a': 'b'}, 'c')
    assert container == Nothing
