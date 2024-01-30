from pydantic import BaseModel
from pydantic.fields import FieldInfo
from pydantic_settings import BaseSettings
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
)
from typing import Any, Type
from appdirs import user_config_dir
from lambo import __name__
from pathlib import Path
import yaml

class HueConfig(BaseModel):
    hostname: str
    username: str
    clientkey: str


class YamlConfigSettingsSource(PydanticBaseSettingsSource):
    
    def get_field_value(self, field: FieldInfo, field_name: str) -> tuple[Any, str, bool]:
        return super().get_field_value(field, field_name)
    
    def __call__(self):
        try:
            pth = Path(user_config_dir()) / __name__ / "config.yaml"
            assert pth.exists()
            data = yaml.full_load(Path(pth).read_text())
            return data
        except AssertionError:
            return {}

class Settings(BaseSettings):
    hue: HueConfig

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            YamlConfigSettingsSource(settings_cls),
            env_settings,
        )


    class Config:
        env_nested_delimiter = "__"


app_config = Settings()  # type: ignore
