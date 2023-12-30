from abc import ABC, abstractmethod
from src.server.tgbot_app.my_stuff.factories.msg_creator import Msg_Creator

# common messages
common_msgs = []
common_msgs.append({
        "update_id": 424229028,
        "message": {
            "message_id": 1903,
            "from": {
                "id": 395578806,
                "is_bot": False,
                "first_name": "Ivan",
                "username": "shyrokyi_shershen",
                "language_code": "uk"
            },
            "chat": {
                "id": 395578806,
                "first_name": "Ivan",
                "username": "shyrokyi_shershen",
                "type": "private"
            },
            "date": 1703927601,
            "text": "/help",
            "entities": [
                {
                    "offset": 0,
                    "length": 5,
                    "type": "bot_command"
                }
            ]
        }
    })

common_msgs.append({
        "update_id": 424229029,
        "message": {
            "message_id": 1905,
            "from": {
                "id": 395578806,
                "is_bot": False,
                "first_name": "Ivan",
                "username": "shyrokyi_shershen",
                "language_code": "uk"
            },
            "chat": {
                "id": 395578806,
                "first_name": "Ivan",
                "username": "shyrokyi_shershen",
                "type": "private"
            },
            "date": 1703927662,
            "text": "/start",
            "entities": [
                {
                    "offset": 0,
                    "length": 6,
                    "type": "bot_command"
                }
            ]
        }
    })


# images2pdf messages
images2pdf_msgs = []
images2pdf_msgs.append({
        "update_id": 424229030,
        "message": {
            "message_id": 1907,
            "from": {
                "id": 395578806,
                "is_bot": False,
                "first_name": "Ivan",
                "username": "shyrokyi_shershen",
                "language_code": "uk"
            },
            "chat": {
                "id": 395578806,
                "first_name": "Ivan",
                "username": "shyrokyi_shershen",
                "type": "private"
            },
            "date": 1703927963,
            "text": "/create_pdf",
            "entities": [
                {
                    "offset": 0,
                    "length": 11,
                    "type": "bot_command"
                }
            ]
        }
    })

images2pdf_msgs.append({
        "update_id": 424229041,
        "message": {
            "message_id": 1934,
            "from": {
                "id": 395578806,
                "is_bot": False,
                "first_name": "Ivan",
                "username": "shyrokyi_shershen",
                "language_code": "uk"
            },
            "chat": {
                "id": 395578806,
                "first_name": "Ivan",
                "username": "shyrokyi_shershen",
                "type": "private"
            },
            "date": 1703944296,
            "text": "Створити pdf 🖼"
        }
    })


images2pdf_msgs.append({
        "update_id": 424229044,
        "message": {
            "message_id": 1939,
            "from": {
                "id": 395578806,
                "is_bot": False,
                "first_name": "Ivan",
                "username": "shyrokyi_shershen",
                "language_code": "uk"
            },
            "chat": {
                "id": 395578806,
                "first_name": "Ivan",
                "username": "shyrokyi_shershen",
                "type": "private"
            },
            "date": 1703946280,
            "text": "Автоматична назва 🖼"
        }
    })


# merge_pdf messages
merge_pdf_msgs = []

merge_pdf_msgs.append({
        "update_id": 424229047,
        "message": {
            "message_id": 1951,
            "from": {
                "id": 395578806,
                "is_bot": False,
                "first_name": "Ivan",
                "username": "shyrokyi_shershen",
                "language_code": "uk"
            },
            "chat": {
                "id": 395578806,
                "first_name": "Ivan",
                "username": "shyrokyi_shershen",
                "type": "private"
            },
            "date": 1703946661,
            "text": "/merge_pdf",
            "entities": [
                {
                    "offset": 0,
                    "length": 10,
                    "type": "bot_command"
                }
            ]
        }
    })

merge_pdf_msgs.append({
        "update_id": 424229048,
        "message": {
            "message_id": 1953,
            "from": {
                "id": 395578806,
                "is_bot": False,
                "first_name": "Ivan",
                "username": "shyrokyi_shershen",
                "language_code": "uk"
            },
            "chat": {
                "id": 395578806,
                "first_name": "Ivan",
                "username": "shyrokyi_shershen",
                "type": "private"
            },
            "date": 1703946702,
            "text": "Об'єднати pdf 📂"
        }
    })

merge_pdf_msgs.append({
        "update_id": 424229054,
        "message": {
            "message_id": 1962,
            "from": {
                "id": 395578806,
                "is_bot": False,
                "first_name": "Ivan",
                "username": "shyrokyi_shershen",
                "language_code": "uk"
            },
            "chat": {
                "id": 395578806,
                "first_name": "Ivan",
                "username": "shyrokyi_shershen",
                "type": "private"
            },
            "date": 1703946777,
            "text": "Автоматична назва 📂"
        }
    })