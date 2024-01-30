from pydantic import BaseModel
from pydantic_settings import BaseSettings


class HueConfig(BaseModel):
    hostname: str
    username: str
    clientkey: str


class Settings(BaseSettings):
    hue: HueConfig

    class Config:
        env_nested_delimiter = "__"


app_config = Settings()  # type: ignore
