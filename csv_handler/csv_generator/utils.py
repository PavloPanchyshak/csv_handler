from enum import Enum


class HeaderTypes(Enum):
    STRING = 'string'
    INTEGER = 'integer'
    DOUBLE = 'double'
    BOOLEAN = 'boolean'


def validate_header_types(header_types: list[str]) -> None:
    invalid_header_types = []
    for header_type in header_types:
        try:
            HeaderTypes(header_type)
        except KeyError:
            invalid_header_types.append(header_type)

    if invalid_header_types:
        raise KeyError(f'Not support {invalid_header_types} types')
