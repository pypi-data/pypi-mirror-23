# botlib/log.py
#
#

""" log module to set standard format of logging. """

from .static import *

import logging.handlers
import logging
import socket
import os

homedir = os.path.expanduser("~")
curdir = os.getcwd()

try:
    hostname = socket.getfqdn()
except:
    hostname = "localhost"

logdir = homedir + os.sep + ".botlog" + os.sep
logcurdir = curdir + os.sep + ".botlog" + os.sep

datefmt = '%H:%M:%S'
format_large = "%(asctime)-8s %(message)-8s %(module)s.%(lineno)s %(threadName)-10s"
format_source = "%(message)-8s %(module)s.%(lineno)-15s"
format_time = "%(asctime)-8s %(message)s"
format = "%(message)s"

class DumpHandler(logging.StreamHandler):

    def emit(self, *args, **kwargs):
        pass

class Formatter(logging.Formatter):

    def format(self, record):
        target = str(record.msg)
        if not target: target = " "
        if target[0] in [">", ]:
            target = "%s%s%s%s%s" % (BOLD, GRAY, target[0], ENDC, target[1:])
        elif target[0] in ["<", ]:
            target = "%s%s%s%s%s" % (BOLD, GRAY, target[0], ENDC, target[1:])
        elif target[0] in ["!", ]:
            target = "%s%s%s%s%s" % (BOLD, BLA, target[0], ENDC, target[1:])
        elif target[0] in ["#", ]:
            target = "%s%s%s%s" % (RED, target[0], ENDC, target[1:])
        elif target[0] in ["^", ]:
            target = "%s%s%s%s%s" % (BOLD, BLUE, target[0], ENDC, target[1:])
        elif target[0] in ["-", ]:
            target = "%s%s%s%s" % (BOLD, target[0], ENDC, target[1:])
        elif target[0] in ["&", ]:
            target = "%s%s%s%s" % (RED, target[0], ENDC, target[1:])
        record.msg = target
        return logging.Formatter.format(self, record)

class FormatterClean(logging.Formatter):

    def format(self, record):
        target = str(record.msg)
        if not target:
            target = " "
        if target[0] in [">", "<", "!", "#", "^", "-", "&"]:
            target = target[2:]
        record.msg = target
        return logging.Formatter.format(self, record)

def cdir(path):
    res = "" 
    for p in path.split(os.sep):
        res += "%s%s" % (p, os.sep)
        padje = os.path.abspath(os.path.normpath(res))
        try:
            os.mkdir(padje)
        except (IsADirectoryError, NotADirectoryError, FileExistsError):
            pass
    return True

def log(level, error):
    l = LEVELS.get(str(level).lower(), logging.NOTSET)
    logging.log(l, error)

def loglevel(loglevel="error", dir=""):
    from .space import cfg
    if dir:
        global logdir
        logdir = dir
    logger = logging.getLogger("")
    formatter = Formatter(format, datefmt=datefmt)
    formatter_clean = FormatterClean(format, datefmt=datefmt)
    level = LEVELS.get(str(loglevel).lower(), logging.NOTSET)
    filehandler = None
    if not os.path.exists(logdir):
        cdir(logdir)
    if logger.handlers:
        for handler in logger.handlers:
            logger.removeHandler(handler)
    if cfg.verbose:
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    else:
        dhandler = DumpHandler()
        logger.addHandler(dhandler)        
        logger.setLevel(level)
    try:
        filehandler = logging.handlers.TimedRotatingFileHandler(os.path.join(logdir, "bot.log"), 'midnight')
    except Exception as ex:
        logging.error(ex)
    if filehandler:
        filehandler.setFormatter(formatter_clean)
        filehandler.setLevel(level)
        logger.addHandler(filehandler)
    global enabled
    enabled = True
    return logger
