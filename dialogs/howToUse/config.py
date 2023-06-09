from random import choice

ttss = ["""
        Навык "Владыка Империи" - карточная квест-игра, которая позволит вам стать владыкой и управлять своим государством.
        Вам предстоит принимать сложные решения, которые повлияют на будущее вашего государства.
        В игре присутствует 4 фракции: церковь, народ, армия, казна. Во время истории они будут слева на карточках.
        Необходимо не допустить полного понижения или заполнения показателей фракций, иначе вы проиграете.
        Чтобы начать игру, скажите "Играть" или нажмите на соответствующую кнопку.
        Выбор можно сделать с помощью кнопок на нижней панели или голосовым вводом.
        Желаем удачи!
        Варианты ответов которые вам доступы в данной категории: Повторить ещё раз, Что ты умеешь?, Назад, Выход.
        """,
        """
        Данный навык представляет собой карточную квест-игру, где вы принимаете на себя роль владыки и управляете своим государством. 
        Вам предстоит делать сложные решения, которые приведут к определенному результату. 
        В игре присутствует 4 фракции: церковь, народ, армия, казна. Они изображены слева на карточке в процессе игры.
        Необходимо не допустить полного понижения или заполнения показателей фракций, иначе вы проиграете.
        Для того, чтоб начать игру скажите или нажмите на кнопку, Играть. 
        Выбор можно сделать с помощью кнопок на нижней панели или голосового ввода. 
        Приятного времяпрепровождения!
        Варианты ответов которые вам доступы в данной категории: Повторить ещё раз, Что ты умеешь?, Назад, Выход.
        """,
        """
        Вам предстоит попробовать свои силы в карточной квест-игре, где вы становитесь владыкой, управляющим своим государством.
        Вам придется принимать множество трудных решений, которые будут иметь последствия на дальнейшее развитие событий.
        В игре доступны 4 фракции: церковь, народ, армия и казна. Вы их увидите во время игры слева на карточках.
        Необходимо следить за показателями каждой из фракций, избегая их полного упадка или слишком быстрого насыщения. В противном случае вы проиграете.
        Чтобы начать игру, скажите или нажмите на кнопку "Играть".
        Выбор можно производить при помощи кнопок на нижней панели или голосового ввода.
        Вперёд, Владыка!
        Варианты ответов которые вам доступы в данной категории: Повторить ещё раз, Что ты умеешь?, Назад, Выход.
        """,
        """
        Вам предстоит вступить в карточную квест-игру, где вы будете играть за владыку, управляющего своим государством.
        Ваша задача состоит в том, чтобы принимать сложные решения, которые окажут влияние на дальнейшую игру.
        В игре доступны 4 фракции: церковь, народ, армия и казна. Вы их увидите во время игры слева на карточках.
        Вам необходимо удерживать показатели каждой из фракций на приемлемом уровне, не допуская их полного падения или переполнения. В противном случае вы проиграете.
        Чтобы начать игру, произнесите или нажмите на кнопку "Играть".
        Выбор можно производить при помощи кнопок на нижней панели или голосового ввода.
        Приятного пользования!
        Варианты ответов которые вам доступы в данной категории: Повторить ещё раз, Что ты умеешь?, Назад, Выход.
        """,
        """
        Вам предстоит сыграть в карточную квест-игру, где вы воплощаете себя в роль владыки, управляющего своим государством.
        В процессе игры вам придется принимать сложные решения, которые окажут влияние на последующий результат.
        В игре присутствуют 4 фракции: церковь, народ, армия и казна. Во время истории они будут слева на карточках.
        Необходимо удерживать показатели каждой из фракций на уровне, не допуская их полного падения или насыщения, иначе вы проиграете.
        Для начала игры произнесите или нажмите на кнопку "Играть".
        Выбор можно сделать с помощью кнопок на нижней панели или голосового ввода.
        Приятного времяпрепровождения!
        Варианты ответов которые вам доступы в данной категории: Повторить ещё раз, Что ты умеешь?, Назад, Выход.
        """]


def getConfig(event):
    tts = choice(ttss)
    config = {
        "tts": f"""{tts}""",

        "buttons": [
            "Повторить ещё раз",
            "Что ты умеешь?",
            "Назад",
            "Выход",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1521359/3349afd66fa90845fd03",
            "title": "КАК ИГРАТЬ?",
            "description": tts,
        },
    }

    session_state = {"branch": "howToUse"}

    return {
        'message': config["tts"],
        "tts": config["tts"],
        "buttons": config["buttons"],
        "card": config["card"],
        "session_state": session_state,
    }
