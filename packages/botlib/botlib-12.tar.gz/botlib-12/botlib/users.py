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

""" class to access user records. """

from .db import Db
from .object import Object
from .utils import userhost

import logging

class User(Object):

    pass


class Users(Db):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._userhosts = Object()

    def add(self, origin, perms):
        """ add a user to the store. """
        from .space import cfg
        user = self.fetch(origin)
        if not user:
            user = User()
            user.user = userhost(origin)
            user.perms = [x.upper() for x in perms]
            user.save()
        else:
            user.user = userhost(origin)
            user.perms = [x.upper() for x in perms]
            user.save()
        logging.warn("# user %s" % user)
        return user

    def allowed(self, origin, perm):
        """ check whether a user has a permission. """ 
        from .space import cfg, fleet
        if origin == cfg.owner:
            return True
        perm = perm.upper()
        user = self.fetch(origin)
        if user and perm in user.perms:
            return True
        logging.warn("# denied %s %s" % (origin, perm))
        return False

    def delete(self, origin, perms):
        """ add a user to the store. """
        user = self.fetch(origin)
        if user:
            user.perms.remove(perms)
            user.sync()
        return user

    def fetch(self, origin):
        """ return user data. """
        o = userhost(origin)
        return self.last("user", o)

    def set(self, origin, perms):
        """ set a permission of a user. """
        user = self.fetch(origin)
        if user:
           if perms.upper() not in user.perms:
               user.perms.append(perms.upper())
           user.sync()
        return user
