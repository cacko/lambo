from typing import Any, Optional
from python_hue_v2 import Hue as ApiHue
from .colors import Color

class ClientMeta(type):
    __instance: Optional["Hue"] = None

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        return type.__call__(cls, *args, **kwds)

    def register(cls, hostname: str, username: str):
        cls.__instance = cls(hostname=hostname, username=username)

    def signaling(cls, duration=2000, colors: Optional[list[str]] = None):
        light = cls.__instance.lights[0]
        try:
            assert colors
            xy_colors = list(map(lambda h: Color().hex_to_xy(h), colors))
            light._set("signaling", {"signal": "alternating", "duration": duration, "colors": xy_colors})
        except AssertionError:
            light._set("signaling", {"signal": "on_off", "duration": duration})


class Hue(ApiHue, metaclass=ClientMeta):
    def __init__(self, hostname: str, username: str) -> None:
        super().__init__(ip_address=hostname, hue_application_key=username)
