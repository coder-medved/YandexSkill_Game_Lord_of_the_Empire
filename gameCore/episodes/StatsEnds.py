OneHundredPercentChurch = """
    "Кондрат $ Сэр, влияние, оказываемое церковью слишком большое. Вы больше не управляете страной. // Что же... // Почему... // 0 0 0 0 $ 0 0 0 0 // None"
    true:
        "*Против вас организовали заговор. Вы были отправлены в темницу.* // Продолжить // None // 0 0 0 0 // None"
        "Дух прошлого короля $ Теперь, ты тоже здесь. // Здравствуйте! // Опять ты // 0 0 0 0 $ 0 0 0 0 // None"
        true:
            "Дух прошлого короля $ Все короли прокляты демоном, мы не исключение, наша учесть ждёт всех... // Да // Нет // 0 0 0 0 $ 0 0 0 0 // None"
            true:
                "Дух прошлого короля $ Ещё никому не удавалось обхитрить демона... // Продолжить // None //  // None"
                "До конца своих дней вы находитесь в заключении, пока вы и ваша душа не умирает от внутренней тоски. // None // None //  // None"
            false:
                "Дух прошлого короля $ Ещё никому не удавалось обхитрить демона... // Продолжить // None //  // None"
                "До конца своих дней вы находитесь в заключении, пока вы и ваша душа не умирает от внутренней тоски. // None // None //  // None"
        false:
            "Дух прошлого короля $ Все короли прокляты демоном, мы не исключение, наша учесть ждёт всех... // Да // Нет // 0 0 0 0 $ 0 0 0 0 // None"
            true:
                "Дух прошлого короля $ Ещё никому не удавалось обхитрить демона... // Продолжить // None //  // None"
                "До конца своих дней вы находитесь в заключении, пока вы и ваша душа не умирает от внутренней тоски. // None // None //  // None"
            false:
                "Дух прошлого короля $ Ещё никому не удавалось обхитрить демона... // Продолжить // None //  // None"
                "До конца своих дней вы находитесь в заключении, пока вы и ваша душа не умирает от внутренней тоски. // None // None //  // None"
    false:
        "*Против вас организовали заговор. Вы были отправлены в темницу.* // Продолжить // None // 0 0 0 0 // None"
        "Дух прошлого короля $ Теперь, ты тоже здесь. // Здравствуйте! // Опять ты // 0 0 0 0 $ 0 0 0 0 // None"
        true:
            "Дух прошлого короля $ Все короли прокляты демоном, мы не исключение, наша учесть ждёт всех... // Да // Нет // 0 0 0 0 $ 0 0 0 0 // None"
            true:
                "Дух прошлого короля $ Ещё никому не удавалось обхитрить демона... // Продолжить // None //  // None"
                "До конца своих дней вы находитесь в заключении, пока вы и ваша душа не умирает от внутренней тоски. // None // None //  // None"
            false:
                "Дух прошлого короля $ Ещё никому не удавалось обхитрить демона... // Продолжить // None //  // None"
                "До конца своих дней вы находитесь в заключении, пока вы и ваша душа не умирает от внутренней тоски. // None // None //  // None"
        false:
            "Дух прошлого короля $ Все короли прокляты демоном, мы не исключение, наша учесть ждёт всех... // Да // Нет // 0 0 0 0 $ 0 0 0 0 // None"
            true:
                "Дух прошлого короля $ Ещё никому не удавалось обхитрить демона... // Продолжить // None //  // None"
                "До конца своих дней вы находитесь в заключении, пока вы и ваша душа не умирает от внутренней тоски. // None // None //  // None"
            false:
                "Дух прошлого короля $ Ещё никому не удавалось обхитрить демона... // Продолжить // None //  // None"
                "До конца своих дней вы находитесь в заключении, пока вы и ваша душа не умирает от внутренней тоски. // None // None //  // None"   
    """
OneHundredPercentArmy = """
    "Кондрат $ Срочно! Владыка, армия ополчилась против вас, желая свергнуть вас. // Что же... // Почему... //  // None"
    "*Военные больше не видят в вас лидера и управляющего. Вы были заперты в грязной темнице своего замка, доживать последние дни.* // None // None //  // None"
    "*Военные больше не видят в вас лидера и управляющего. Вы были заперты в грязной темнице своего замка, доживать последние дни.* // None // None //  // None"

"""

OneHundredPercentNation = """
    "Кондрат $ Владыка, все безумно счастливы, каждый хочет вас поцеловать, они сломали наши ворота и уже направляются к нам. // Что же... // Остановите... // 0 0 0 0 $ 0 0 0 0 // None"
    true:
        "*Не успели вы договорить, как тысяча довольных жителей налетели на вас. Утонув в толпе, вам не удалось выплыть.* // None // None //  // None"
    false:
        "*Не успели вы договорить, как тысяча довольных жителей налетели на вас. Утонув в толпе, вам не удалось выплыть.* // None // None //  // None"

"""

OneHundredPercentFinance = """
    "Кондрат $ Наша держава разбогатела настолько сильно, что политическую власть перехватили высшие чины. Вы больше не управляете государством. // Что же... // Почему... //  // None"
    true:
        "*Вашу судьбу обрекли на служение в монастыре, но увы, по пути туда вы были лишены жизни.* // None // None //  // None"
    false:
        "*Вашу судьбу обрекли на служение в монастыре, но увы, по пути туда вы были лишены жизни.* // None // None //  // None"

"""

ZeroPercentChurch = """
    "Кондрат $ Сэр, еретики хотят убить вас после того, как узнали о том, что вы верующий, они не хотят такого царя, вот-вот они ворвутся сюда. // Что же... // Почему... //  // None"
    true:
        "*Бежать было слишком поздно, они заполонили весь дворец. Вас поймали и скормили собакам.* // None // None //  // None"
    false:
        "*Бежать было слишком поздно, они заполонили весь дворец. Вас поймали и скормили собакам.* // None // None //  // None"
"""

ZeroPercentArmy = """
    "Кондрат $ Разведчики соседних государств разузнали, то что наша армия находится в плачевном состоянии, вот-вот они начнут военные действия // Что же... // Как... //  // None"
    true:
        "*Соседние государства объединись, чтоб свергнуть вас. Вам стоит больше думать о своей безопасности* // None // None //  // None"
    false:
        "*Соседние государства объединись, чтоб свергнуть вас. Вам стоит больше думать о своей безопасности* // None // None //  // None"
"""  # grustno =(

ZeroPercentNation = """ 
    "Кондрат $ Владыка! Народу не нравится ваша власть, он хочет уничтожить вас и вашу власть. // Что же... // Как... //  // None"
    true:
        "*Вы были пойманы и отправлены на публичную виселицу. Стоит лучше думать о своём народе* // None // None //  // None" 
    false:
        "*Вы были пойманы и отправлены на публичную виселицу. Стоит лучше думать о своём народе* // None // None //  // None"
"""  # sad

ZeroPercentFinance = """
    "Кондрат $ Повелитель, экономика страны была полностью разрушена, наша защита больше не может сдерживать протесты жителей. // Что же... // Как... //  // None"
    true:
        "*Вы были пойманы и отправлены на публичную виселицу. Стоит лучше думать о финансах своего государства* // None // None //  // None"
    false:
        "*Вы были пойманы и отправлены на публичную виселицу. Стоит лучше думать о финансах своего государства* // None // None //  // None"
"""

# концовки при переполнении/недостатка какой-то статы
# формат такой-же
# full - когда стата заполняется на 100+
# empty - когда стата опускается до 0-

test = """

"""

StatsEnds = {
    "church": {
        "full": OneHundredPercentChurch,
        "empty": ZeroPercentChurch,
    },
    "army": {
        "full": OneHundredPercentArmy,
        "empty": ZeroPercentArmy,
    },
    "nation": {
        "full": OneHundredPercentNation,
        "empty": ZeroPercentNation,
    },
    "coffers": {
        "full": OneHundredPercentFinance,
        "empty": ZeroPercentFinance,
    },
}
