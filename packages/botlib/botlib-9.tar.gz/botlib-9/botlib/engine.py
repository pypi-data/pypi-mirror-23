# mad/engine.py
#
#

""" 
    a engine is select.epoll event loop, easily interrup_table
    esp. versus a blocking event loop.

"""

from .error import EDISCONNECT, ERESUME
from .launcher import Launcher
from .handler import Handler
from .object import Object
from .register import Register

import logging
import select
import queue
import time

READ_ONLY = select.POLLIN | select.POLLPRI | select.POLLHUP | select.POLLERR
READ_WRITE = READ_ONLY | select.POLLOUT

class Engine(Launcher):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._connected.clear()
        self._handlers = Register()
        self._queue = queue.Queue()
        self._poll = select.epoll()
        self._resume = Object()
        self._state.status = "running"
        self._time.start = time.time()

    def dispatch(self, event):
        event.parse()
        for handler in self._handlers.get(event._parsed.cmnd, []):
            handler(event)

    def select(self):
        while self._state.status:
            for event in self.events():
                if not event:
                    break
                self._counter.events = self._counter.events + 1
                self.launch(self.dispatch, event, name=event._parsed.cmnd)
                self._time.latest = time.time()

    def events(self):
        fdlist = self._poll.poll()
        for fd, event in fdlist:
            try:
                yield self.event()
            except (ConnectionResetError,
                    BrokenPipeError,
                    EDISCONNECT) as ex:
                        self.connect()

    def register_fd(self, f):
        try:
            fd = f.fileno()
        except:
            fd = f
        if not fd:
            return fd
        logging.warn("# engine on %s" % str(fd))
        self._poll.register(fd, READ_ONLY)
        self._resume.fd = fd
        return fd

    def resume(self):
        logging.info("# resume on %s" % self._resume.fd)
        self._poll = select.epoll.fromfd(self._resume.fd)

    def start(self, *args, **kwargs):
        super().start()
        self.launch(self.select)

    def stop(self):
        self._status = ""
        self._poll.unregister(self._resume.fd)
        #self._poll.close()
        