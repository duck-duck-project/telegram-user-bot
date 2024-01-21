import pathlib

from pyrogram import Client

import handlers
from config import load_config

config_path = pathlib.Path(__file__).parent.parent / 'config.toml'
config = load_config(config_path)

client = Client(
    name='.session',
    api_id=config.api_id,
    api_hash=config.api_hash,
)

handlers.register_handlers(client)

client.run()
