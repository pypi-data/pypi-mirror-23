# BOTLIB - Framework to program bots.
#
# Copyright (C) 2016,2017 by Bart Thate <bthate@dds.nl>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES 
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF 
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE 
# FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY 
# DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER
# IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
# OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

""" select.epoll event loop, easily interrup_table esp. versus a blocking event loop. """

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
            try:
                handler(event)
            except Exception as ex:
                logging.error(get_exception())

    def select(self):
        stopped = False
        while self._state.status:
            if stopped:
                break
            for event in self.events():
                if not event:
                    stopped = True
                    break
                self._counter.events = self._counter.events + 1
                self.launch(self.dispatch, event, name=event._parsed.cmnd)
                self._time.latest = time.time()

    def events(self):
        try:
            fdlist = self._poll.poll()
        except ValueError:
            yield None
        for fd, event in fdlist:
            try:
                yield self.event()
            except ValueError:
                break
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
        #self._poll.register(fd, READ_ONLY)
        self._poll.register(fd)
        self._resume.fd = fd
        return fd

    def resume(self):
        logging.info("! resume on %s" % self._resume.fd)
        self._poll = select.epoll.fromfd(self._resume.fd)

    def start(self, *args, **kwargs):
        super().start()
        self.launch(self.select)

    def stop(self):
        self._status = ""
        try:
            self._poll.unregister(self._resume.fd)
        except:
            pass
        try:
            self._poll.close()
        except:
            pass
