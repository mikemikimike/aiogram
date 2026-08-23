from aiogram.types import MessageOriginHiddenUser, Update


def test_message_origin_hidden_user_allows_missing_sender_user_name() -> None:
    origin = MessageOriginHiddenUser.model_validate({"type": "hidden_user", "date": 1422450181})

    assert origin.sender_user_name is None


def test_update_with_legacy_hidden_user_origin_is_deserialized() -> None:
    update = Update.model_validate(
        {
            "update_id": 1143243230,
            "message": {
                "message_id": 1251,
                "from": {"id": 1, "is_bot": False, "first_name": "A"},
                "chat": {"id": -100262323, "type": "supergroup", "title": "Group"},
                "date": 1782327884,
                "reply_to_message": {
                    "message_id": 3,
                    "from": {"id": 2, "is_bot": False, "first_name": "B"},
                    "chat": {"id": -100262323, "type": "supergroup", "title": "Group"},
                    "date": 1422450181,
                    "forward_origin": {"type": "hidden_user", "date": 1422450181},
                    "forward_date": 1422450181,
                    "text": "x",
                },
                "text": "/purge",
            },
        }
    )

    assert isinstance(update.message.reply_to_message.forward_origin, MessageOriginHiddenUser)
    assert update.message.reply_to_message.forward_origin.sender_user_name is None
