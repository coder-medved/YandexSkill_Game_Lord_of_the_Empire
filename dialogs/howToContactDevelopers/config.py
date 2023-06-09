from random import choice

ttss = [
    "Вы всегда можете написать на нашу почту.",
    "Вы всегда можете написать нам на почту.",
    "Если у вас есть вопросы, не стесняйтесь обращаться к нам по электронной почте.",
    "Наша электронная почта всегда открыта для ваших просьб и предложений.",
    "Если у вас возникли какие-либо вопросы, пожелания или замечания, не стесняйтесь связаться с нами по электронной почте.",
    "Мы всегда готовы ответить на ваши вопросы и принять ваши предложения, написав нам на электронную почту.",
    "Если вам требуется наша помощь или вы хотите получить дополнительную информацию, не стесняйтесь обратиться к нам по электронной почте.",
    "Наша техническая поддержка всегда готова помочь вам с любыми вопросами или предложениями, направленными на улучшение нашей работы. Не стесняйтесь писать нам на электронную почту.",
    "Хотите оставить свой отзыв о нашем навыке или предложить свои идеи? Напишите нам на электронную почту, и мы обязательно рассмотрим ваше сообщение.",
    "Наша команда всегда готова помочь вам решить любые вопросы. Не стесняйтесь обратиться к нам по электронной почте в любое время.",
    "Не нашли нужную информацию в нашем навыке? Напишите нам на почту, и мы с радостью поможем вам разобраться.",
    "Если у вас возникли какие-либо проблемы или вопросы, мы всегда доступны по электронной почте."
]

Answer = [
    "Варианты ответов которые вам доступны в данной категори - это. Повторить ещё раз, Что ты умеешь?, Назад, Выход."
]

def getConfig(event):
    tts = choice(ttss)
    config = {
        "tts": f"""{tts}. super. scripts. debugers. @ yandex. точка. ru. {Answer}""",
        "buttons": [
            "Повторить ещё раз",
            "Что ты умеешь?",
            "Назад",
            "Выход",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1521359/3349afd66fa90845fd03",
            "title": "КАК СВЯЗАТЬСЯ С НАМИ?",
            "description": """
            Почта команды: ✉️Связь с нами: SuperScriptsDebugers@yandex.ru.. Варианты ответов: Повторить ещё раз, Что ты умеешь?, Назад, Выход.
            """,
        },
    }

    session_state = {"branch": "howToContactDevelopers"}

    return {
        "message": config["tts"],
        "tts": config["tts"],
        "buttons": config["buttons"],
        "card": config["card"],
        "session_state": session_state,
    }
