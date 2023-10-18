from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
import datetime as dt

from dateutil.relativedelta import relativedelta

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    end = dt.datetime(2023, 1, 28, 20)
    n = dt.datetime.now()
    result = relativedelta(n, end)
    await msg.answer(f'Поздравляю, вы встречаетесь уже '
                     f'{result.months} месяцев,'
                     f' {result.days} дней,'
                     f' {result.hours} часов,'
                     f' {result.minutes} минут, '
                     f'{result.seconds} секунд и '
                     f'{result.microseconds} микросекунд')
