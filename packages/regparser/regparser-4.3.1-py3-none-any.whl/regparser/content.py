"""We need to modify content from time to time, e.g. image overrides and xml
macros. To provide flexibility in future expansion, we provide a layer of
indirection here.

TODO: Delete and replace with plugins."""
import itertools
import logging

from regparser.web.settings import parser as settings

logger = logging.getLogger(__name__)


def _try_to_load(path, ident='module'):
    module, obj = path.rsplit('.', 1)
    try:
        #   Note: we would use importlib, but it's not available to 2.6
        module = __import__(module, fromlist=[obj])
        if hasattr(module, obj):
            return getattr(module, obj)
    except ImportError:
        logger.warning("Could not load " + ident + " from " + path)


class Macros(object):
    def __iter__(self):
        iterators = []
        for source in settings.MACROS_SOURCES:
            macros = _try_to_load(source, 'macros')
            if macros:
                iterators.append(iter(macros))
        return itertools.chain(*iterators)


class ImageOverrides(object):
    @staticmethod
    def get(key, default=None):
        for source in settings.OVERRIDES_SOURCES:
            source = _try_to_load(source, 'overrides')
            if source and key in source:
                return source[key]
        return default
