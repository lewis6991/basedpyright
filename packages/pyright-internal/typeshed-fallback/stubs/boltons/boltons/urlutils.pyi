from _typeshed import Incomplete

from boltons.dictutils import OrderedMultiDict

SCHEME_PORT_MAP: Incomplete
NO_NETLOC_SCHEMES: Incomplete

class URLParseError(ValueError): ...

DEFAULT_ENCODING: str

def to_unicode(obj: object) -> str: ...
def find_all_links(text, with_text: bool = False, default_scheme: str = "https", schemes=()): ...
def quote_path_part(text, full_quote: bool = True): ...
def quote_query_part(text, full_quote: bool = True): ...
def quote_fragment_part(text, full_quote: bool = True): ...
def quote_userinfo_part(text, full_quote: bool = True): ...
def unquote(string, encoding: str = "utf-8", errors: str = "replace"): ...
def unquote_to_bytes(string): ...
def register_scheme(text, uses_netloc: Incomplete | None = None, default_port: Incomplete | None = None) -> None: ...
def resolve_path_parts(path_parts): ...

class cachedproperty:
    __doc__: Incomplete
    func: Incomplete
    def __init__(self, func) -> None: ...
    def __get__(self, obj, objtype: Incomplete | None = None): ...

class URL:
    scheme: Incomplete
    username: Incomplete
    password: Incomplete
    family: Incomplete
    host: Incomplete
    port: Incomplete
    path_parts: Incomplete
    fragment: Incomplete
    def __init__(self, url: str = "") -> None: ...
    @classmethod
    def from_parts(
        cls,
        scheme: Incomplete | None = None,
        host: Incomplete | None = None,
        path_parts=(),
        query_params=(),
        fragment: str = "",
        port: Incomplete | None = None,
        username: Incomplete | None = None,
        password: Incomplete | None = None,
    ): ...
    query_params: Incomplete
    qp: Incomplete
    @property
    def path(self): ...
    @path.setter
    def path(self, path_text) -> None: ...
    @property
    def uses_netloc(self): ...
    @property
    def default_port(self): ...
    def normalize(self, with_case: bool = True) -> None: ...
    def navigate(self, dest): ...
    def get_authority(self, full_quote: bool = False, with_userinfo: bool = False): ...
    def to_text(self, full_quote: bool = False): ...
    def __unicode__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

def parse_host(host): ...
def parse_url(url_text): ...

DEFAULT_PARSED_URL: Incomplete

def parse_qsl(qs, keep_blank_values: bool = True, encoding="utf8"): ...

PREV: Incomplete
NEXT: Incomplete
KEY: Incomplete
VALUE: Incomplete
SPREV: Incomplete
SNEXT: Incomplete

OMD = OrderedMultiDict

class QueryParamDict(OrderedMultiDict[Incomplete, Incomplete]):
    @classmethod
    def from_text(cls, query_string): ...
    def to_text(self, full_quote: bool = False): ...
