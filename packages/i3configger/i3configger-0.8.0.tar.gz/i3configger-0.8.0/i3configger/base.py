import logging
import os
import sys
import tempfile
from pathlib import Path

from i3configger import exc

log = logging.getLogger(__name__)
DEBUG = os.getenv('DEBUG', 0)
COMMENT_MARK = '#'
MESSAGES_NAME = '.messages.json'
VAR_MARK = '$'
SET_MARK = 'set'
SUFFIX = '.conf'
I3BAR = "i3bar"
"""reserved key for status bar template files"""
DEL = 'del'
"""signal to delete a key in shadow or set"""


# FIXME this is wrong - based on assumption that config always resides
# in partialsPath -> either make this a necessity or make it configurable
class Paths:
    def __init__(self, configPath):
        path = Path(configPath)
        assert path.exists() and path.is_file(), path
        self.root = path.parent
        self.config = configPath
        self.messages = self.root / MESSAGES_NAME


def configure_logging(verbosity: int, logPath: str, isDaemon=False):
    rootLogger = logging.getLogger()
    if logPath:
        logPath = Path(logPath).expanduser()
    else:
        name = 'i3configger-daemon.log' if isDaemon else 'i3configger.log'
        logPath = Path(tempfile.gettempdir()) / name
    if DEBUG:
        print('logging to %s' % logPath)
        level = 'DEBUG'
    else:
        level = logging.getLevelName(
            {0: 'ERROR', 1: 'WARNING', 2: 'INFO'}.get(verbosity, 'DEBUG'))
    fmt = ('%(asctime)s %(name)s:%(funcName)s:%(lineno)s '
           '%(levelname)s: %(message)s')
    if not rootLogger.handlers:
        logging.basicConfig(format=fmt, level=level)
        log.debug("logging initialized: %s", rootLogger.handlers)
    fileHandler = logging.FileHandler(logPath)
    fileHandler.setFormatter(logging.Formatter(fmt))
    fileHandler.setLevel(level)
    rootLogger.addHandler(fileHandler)


def i3configger_excepthook(type_, value, traceback):
    if DEBUG or not isinstance(value, exc.I3configgerException):
        _REAL_EXCEPTHOOK(type_, value, traceback)
    else:
        sys.exit("%s: %s" % (value.__class__.__name__, value))


def get_version():
    """hide behind a wrapped function (slow and not a catastrophe if fails)"""
    try:
        from pkg_resources import get_distribution
        return get_distribution('i3configger').version
    except:
        log.exception("fetching version failed")
        return 'unknown'


_REAL_EXCEPTHOOK = sys.excepthook
sys.excepthook = i3configger_excepthook
