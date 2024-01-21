import pathlib
import tomllib
from dataclasses import dataclass

__all__ = (
    'Config',
    'load_config',
)


@dataclass(frozen=True, slots=True)
class Config:
    api_id: int
    api_hash: str


def load_config(file_path: pathlib.Path) -> Config:
    config_text = file_path.read_text(encoding='utf-8')
    config = tomllib.loads(config_text)

    return Config(
        api_id=config['api_id'],
        api_hash=config['api_hash'],
    )
