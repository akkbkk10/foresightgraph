from dataclasses import is_dataclass, fields
from datetime import datetime
from typing import Any, Type, get_origin, get_args, Union


def record_to_dict(record: Any) -> dict:
    """Serialize a dataclass record into a JSON-safe dict.

    Datetime fields are converted to ISO 8601 strings. Lists are preserved.
    Nested dataclasses are serialized recursively.
    """
    if not is_dataclass(record):
        raise TypeError("record must be a dataclass instance")

    result: dict = {}
    for f in fields(record):
        val = getattr(record, f.name)
        if isinstance(val, datetime):
            result[f.name] = val.isoformat()
        elif isinstance(val, list):
            out_list = []
            for item in val:
                if isinstance(item, datetime):
                    out_list.append(item.isoformat())
                elif is_dataclass(item):
                    out_list.append(record_to_dict(item))
                else:
                    out_list.append(item)
            result[f.name] = out_list
        elif is_dataclass(val):
            result[f.name] = record_to_dict(val)
        else:
            result[f.name] = val
    return result


def record_from_dict(record_type: Type[Any], data: dict) -> Any:
    """Deserialize a dict back into a dataclass record of type `record_type`.

    Expects datetime fields as ISO 8601 strings and list fields as lists.
    Raises TypeError when `record_type` is not a dataclass type.
    """
    if not isinstance(data, dict):
        raise TypeError("data must be a dict")

    # Quick check for dataclass type
    if not hasattr(record_type, "__dataclass_fields__"):
        raise TypeError("record_type must be a dataclass type")

    kwargs = {}
    for f in fields(record_type):
        name = f.name
        val = data.get(name)

        if val is None:
            kwargs[name] = None
            continue

        # Check if this is a datetime field (handles both datetime and Optional[datetime])
        is_datetime_field = (
            f.type is datetime or 
            getattr(f.type, "__name__", None) == "datetime" or
            (get_origin(f.type) is Union and any(arg is datetime for arg in get_args(f.type))) or
            (get_origin(f.type) is type(None) and get_args(f.type) and get_args(f.type)[0] is datetime)
        )

        if is_datetime_field:
            if isinstance(val, str):
                try:
                    kwargs[name] = datetime.fromisoformat(val)
                except Exception as exc:
                    raise ValueError(f"Invalid datetime value for field '{name}': {val}") from exc
            elif isinstance(val, datetime):
                kwargs[name] = val
            else:
                raise TypeError(f"Invalid type for datetime field '{name}': {type(val)}")

        # handle list (keep as-is)
        elif getattr(f.type, "__origin__", None) is list or f.type == list:
            kwargs[name] = val

        else:
            kwargs[name] = val

    return record_type(**kwargs)