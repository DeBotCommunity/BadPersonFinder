# Module by @DeBotMod
import time
import random

from telethon import events
from userbot import client
from telethon.errors import FloodWaitError

info = {'category': 'chat', 'pattern': '.lol', 'description': 'посиск плохого человека'}


@client.on(events.NewMessage(outgoing=True, pattern=".lol"))
async def lol_message(event):
    chat = await event.get_chat()
    sender = await event.get_sender()
    user_id = sender.id
    all_participants = await client.get_participants(chat)
    random_user = random.choice(all_participants)
    if user_id:
        x = 0
        emoji = ["❤️", "😳", "😀", "🥰", "😂", "😍", "🤣", "😊", "😁", "😘", "😆", "😎", "😃", "😋", "😄", "😜",
                 "😉", "😅", "😇", "🙂", "🙃", "😌", "🤪", "☺️", "😬", "🥳", "😏", "🤭", "🤩", "😙", "😛", "😝",
                 "😀", "🙊", "😻", "😹", "😸", "😺", "🌞", "🌼", "🌈", "🎉", "🎈", "🌺", "💕", "💖", "✨", "🍀",
                 "🌻", "🌹", "🌸"]
        while x < 100:
            try:
                await client.edit_message(event.message, f'{random.choice(emoji)} Поиск плохого человека... {x}%')
                x += random.randint(1, 3)
                time.sleep(0.1)
            except FloodWaitError as e:
                time.sleep(e.x)

        try:
            await client.edit_message(event.message, f'🟢 плохой человек найден - @{random_user.username}')
        except:
            await client.edit_message(event.message, f'🟢 плохой человек найден - {random_user.first_name}')
