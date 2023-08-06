__version__ = '0.2.0'

# import os
# os.environ['RUST_LOG'] = 'async_tokio=debug'  # noqa

from asyncio.events import AbstractEventLoop
from asyncio.unix_events import DefaultEventLoopPolicy

from . import _tokio

__all__ = ('new_event_loop', 'EventLoopPolicy')


def new_event_loop():
    return _tokio.new_event_loop()


class EventLoopPolicy(DefaultEventLoopPolicy):
    """Event loop policy."""

    def _loop_factory(self):
        return new_event_loop()

    def set_event_loop(self, loop):
        """Set the event loop."""
        self._local._set_called = True
        assert loop is None or isinstance(
            loop, (AbstractEventLoop, _tokio.TokioEventLoop))
        self._local._loop = loop
