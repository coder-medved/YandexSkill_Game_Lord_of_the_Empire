Opening = """
    "Ты - истинный владыка? // Да // Нет //  // None"
    true:
        "Значит, из-за тебя мне пришлось покинуть этот мир // Да // Нет //  // None"
        "Раз так, то разбирайся со всеми проблемами сам, удачи. Все они преследуют только свои интересы, скоро ты это поймешь. // Ты о ком? // Что? //  // None"
        "Попытайся справиться с четырьмя фракциями своего государства, так чтоб ты и твоя голова осталась на месте // Продолжить // None //  // None"
        "*Призрак тоскливо смотрит на вас и исчезает. Вы входите в тронный зал.* // Продолжить // None //  //  None"
        "{FirstExtension}"
        
    false:
        "Если ты не король, то нам не о чем говорить, прощай // Сладких снов! // Я - владыка //  //  None"
        true:
            "*Призрак пропадает, вы входите в зал и смотрите на свой трон* // Продолжить // None //  //  None"
            "{FirstExtension}"
        false:
            "Значит, из-за тебя мне пришлось покинуть этот мир // Да // Нет //  //  None"
            "Раз так, то разбирайся со всеми проблемами сам, удачи. Все они преследуют только свои интересы, скоро ты это поймешь. // Ты о ком? // Что? //  //  None"
            "Попытайся справиться с четырьмя фракциями своего государства, так чтоб ты и твоя голова осталась на месте // Продолжить // None //  //  None"
            "*Призрак тоскливо смотрит на вас и исчезает. Вы входите в тронный зал.* // Продолжить // None //  //  None"
            "{FirstExtension}"
        

"""