text = """Ильин Кирилл - Тимлид (руководит процессом разработки)

Плюснин Александр - Главный Разработчик (отвечает за всю оболочку навыка)

Кунакбаев Радмир - Разработчик и Сценарист (дополняет функционал и придумывает весь сценарий игры)

Лесовой Кирилл - Разработчик и Тестировщик (обеспечивает навык полным функционалом игры и фиксирует ошибки)

Кутников Родион - Дизайнер (рисует АРТ картинки и придумывает дизайн для навыка)"""


def getConfig(event):
    config = {
        "text": text,
        "tts": """Ильин Кирилл, Плюснин Александр, Кунакбаев Радмир, Лесовой Кирилл, Кутников Родион""",
        "buttons": [
            "Повторить ещё раз",
            "Что ты умеешь?",
            "Назад",
            "Выход"
            ,
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1521359/3349afd66fa90845fd03",
            "title": "СОЗДАТЕЛИ НАВЫКА",
            "description": text
        },
    }

    session_state = {"branch": "whoAreCreators"}

    return {
        'message': config["text"],
        "tts": config["tts"],
        "buttons": config["buttons"],
        "card": config["card"],
        "session_state": session_state,
    }
