from aiogram.client.session.middlewares.base import (
    BaseRequestMiddleware,
    NextRequestMiddlewareType,
    RequestMiddlewareType,
)


def test_request_middleware_types_return_method_result() -> None:
    assert NextRequestMiddlewareType.__call__.__annotations__["return"] == "TelegramType"
    assert RequestMiddlewareType.__call__.__annotations__["return"] == "TelegramType"
    assert BaseRequestMiddleware.__call__.__annotations__["return"] == "TelegramType"
