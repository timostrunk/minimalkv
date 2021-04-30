from minimalkv.constants import (
    FOREVER,
    NOT_SET,
    VALID_KEY_RE,
    VALID_KEY_REGEXP,
    VALID_NON_NUM,
)
from minimalkv.key_value_store import KeyValueStore, UrlKeyValueStore
from minimalkv.mixins import CopyMixin, TimeToLiveMixin, UrlMixin
from minimalkv.storefact._store_creation import create_store
from minimalkv.storefact._store_decoration import decorate_store
from minimalkv.storefact._urls import url2dict
from minimalkv.storefact.access import get_store, get_store_from_url

try:
    import pkg_resources

    __version__ = pkg_resources.get_distribution(__name__).version
except Exception:  # pragma: no cover
    __version__ = "unknown"

__all__ = [
    "CopyMixin",
    "create_store",
    "decorate_store",
    "FOREVER",
    "get_store_from_url",
    "get_store",
    "KeyValueStore",
    "NOT_SET",
    "TimeToLiveMixin",
    "url2dict",
    "UrlKeyValueStore",
    "UrlMixin",
    "VALID_KEY_RE",
    "VALID_KEY_REGEXP",
    "VALID_NON_NUM",
]
