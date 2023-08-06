import re
from functools import singledispatch  # type: ignore


def snake_case(name: str) -> str:
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


@singledispatch
def decode(value):
    return value


@decode.register(bytes)
def decode_bytes(value):
    return value.decode()


@decode.register(list)
def decode_list(value):
    from amino import List
    return List.wrap(value).map(decode)


@decode.register(dict)
def decode_dict(value):
    from amino import Map
    return Map.wrap(value)\
        .keymap(decode)\
        .valmap(decode)


@decode.register(Exception)
def decode_exc(value):
    return decode_list(value.args).head | str(value)


def camelcaseify(name, sep='', splitter='_'):
    return sep.join([n.capitalize() for n in re.split(splitter, name)])


def safe_string(value):
    try:
        return str(value)
    except Exception:
        try:
            return repr(value)
        except Exception:
            return 'invalid'

__all__ = ('snake_case', 'decode', 'camelcaseify')
