from random import choice

ttss = ["""
Умею я многое. Вы можете обратиться за помощью для решения вопросов во время игры. 
Так же можете играть в игру, которая имеет захватывающий сюжет и геймплей! 
Чтобы продолжить, пожалуйста, скажите "продолжить играть". 
Если вы не расслышали текст, можете попросить повторить его еще раз.
Для дополнительной помощи, нажмите кнопку или скажите "Помощь".
Ну и конечно, если вам надоело играть - просто нажмите кнопку или скажите "Выйти".
""",
        """
Могу я многое. Если у вас возникнут вопросы во время игры, обращайтесь ко мне за помощью.
Также вы можете наслаждаться игрой с увлекательным сюжетом и геймплеем! 
Чтобы продолжить, пожалуйста, скажите "продолжить играть". 
Если вы не расслышали текст, можете попросить повторить его еще раз.
Для дополнительной помощи, нажмите кнопку или скажите "Помощь".
Ну и конечно, если вам надоело играть - просто нажмите кнопку или скажите "Выйти".
"""]


def getConfig(event):
    tts = choice(ttss)
    config = {
        "tts": tts,
        "buttons": [
            "Повторить ещё раз",
            "Помощь",
            "Назад",
            "Выход",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1521359/3349afd66fa90845fd03",
            "title": "ЧТО Я УМЕЮ?",
            "description": tts,
        },
    }

    session_state = {"branch": "whatYouCan"}

    return {
        'message': config["tts"],
        "tts": config["tts"],
        "buttons": config["buttons"],
        "card": config["card"],
        "session_state": session_state,
    }
