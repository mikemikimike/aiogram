from aiogram.client.bot import Bot
from aiogram.client.session.middlewares.base import NextRequestMiddlewareType
from aiogram.methods import GetMe
from aiogram.types import User


async def middleware_result_is_method_result(
    make_request: NextRequestMiddlewareType[User],
    bot: Bot,
) -> User:
    return await make_request(bot, GetMe())
