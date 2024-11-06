import asyncio
import logging
import sys

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart, Command

P = True
My_IP = 1711818456
BOT_T = '6234328757:AAGv1HE4awNCqc12ZJ5XCDUNX-eq3D8alIo'

(P and print("Start"))

bot = Bot(token=BOT_T)
dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text=f"Hello, {message.from_user.full_name}!")
@dp.message(Command("help"))
async def handle_start(message: types.Message):
    await message.answer(text=f"I am a simple bot.\nSend me any message")
@dp.message(Command("exit"))
async def handle_start(message: types.Message):
    await message.answer(text=f"-_-")
    exit()
    

@dp.message()
async def echo_message(message: types.Message):
    
    await message.send_copy(chat_id=message.chat.id)

    # await bot.send_message(chat_id=message.chat.id, text="send_message with no id")
    # await bot.send_message(chat_id=message.chat.id, text="Reply_with_id", reply_to_message_id=message.message_id)
    # await message.reply(text="reply_without_id(last)")
    # if message.text:
    #     await message.answer(text=message.text)
    # elif message.sticker:
    #     await message.reply_sticker(sticker=message.sticker.file_id)
    # else:
    #     await message.reply(text="Its not a text")


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

(P and print("End"))
