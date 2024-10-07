import json
from typing import Callable, List


def process_json(
    json_str: str,
    required_keys: List[str] | None = None,
    tokens: List[str] | None = None,
    callback: Callable[[str, str], None] | None = None,
) -> None:

    data = json.loads(json_str)

    required_keys = required_keys or []
    tokens = tokens or []

    for key, value in data.items():
        if key in required_keys:
            for token in tokens:
                if token.lower() in value.lower():
                    if callback:
                        callback(key, token)
