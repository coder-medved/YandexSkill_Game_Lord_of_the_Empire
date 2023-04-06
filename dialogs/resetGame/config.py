from random import choice

ttss = ['Вы уверены в том, что хотите сбросить сохранение?',
        'Вы уверены, что хотите сбросить последнее приключение?',
        'Вы точно хотите сбросить игровой прогресс?',
        'Вы убедились, что хотите удалить сохранение?']

config = {
    "tts":
        """
        Вы уверены в том, что хотите сбросить сохранение?
        """,
    "buttons": [
        "Да",
        "Нет",
    ],
    "card": {
        "type": "BigImage",
        "image_id": "1540737/eef2ca09cbd5d5cf9d01",
        "title": "СБРОСИТЬ СОХРАНЕНИЕ?",
        "description":
            """
            Вы уверены в том, что хотите сбросить сохранение?
            """,
    },
}

session_state = {"branch": "resetGame"}


def getConfig(event):
    tts = choice(ttss)
    card = config["card"].copy()
    card["description"] = tts
    return {
        'message': tts,
        "tts": tts,
        "buttons": config["buttons"],
        "card": card,
        "session_state": session_state,
    }
