from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

__all__ = ('register_handlers',)


async def on_studmanas_message(_: Client, message: Message) -> None:
    if not message.text:
        return

    text = message.text.lower()

    if message.from_user.username == 'iris_moon_bot':
        if 'работы на ферме' in text or 'зачёт' in text:
            await message.delete()
    else:
        if 'ферма' in text:
            await message.delete()


def register_handlers(client: Client) -> None:
    client.add_handler(
        MessageHandler(
            on_studmanas_message,
            filters.chat('@studmanas'),
        ),
    )
