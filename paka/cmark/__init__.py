import sys

from paka.cmark._cmark import ffi, lib


_PY2 = sys.version_info.major == 2


class LineBreaks(object):
    soft = "soft"
    hard = "hard"


def get_version():
    result = ffi.string(lib.cmark_version_string())
    if _PY2:  # pragma: no cover
        return result
    return result.decode("ascii")


def to_html(text, breaks=False, safe=False):
    encoding = "utf-8"
    text_bytes = text.encode(encoding)
    opts = lib.CMARK_OPT_DEFAULT
    if breaks:
        if breaks == "hard":
            opts |= lib.CMARK_OPT_HARDBREAKS
    else:
        opts |= lib.CMARK_OPT_NOBREAKS
    if safe:
        opts |= lib.CMARK_OPT_SAFE
    return ffi.string(
        lib.cmark_markdown_to_html(
            text_bytes, len(text_bytes), opts)).decode(encoding)
