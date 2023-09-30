import moviepy.editor as editor
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import TOKEN

def convert_video(path):
    editor.VideoFileClip(path).write_videofile(f'{path.split(".")[0]}.mp4')

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.message):
    await message.answer("Привет, я умею конвертировать видео в формат mp4.")

@dp.message()
async def video_handler(message: types.Video):
    file_id = message.document.file_id
    file = await bot.get_file(file_id)
    file_path = f'{file.file_path}'
    await message.answer("Идет конвератация видео.")
    await bot.download_file(file_path, file_path)
    convert_video(file_path)
    # строчка с ошибкой
    # await bot.send_video(message.chat.id, video=open(file_path, 'rb'), caption="Ваше видео сконвертировано.")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())