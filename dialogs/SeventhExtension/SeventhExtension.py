SeventhExtension = """
    "В соседней деревушке жители начали ходить на четвереньках и гавкать, что нам делать? // Ничего // Отправить армию //  // None"
    true:
        "*Церковь восприняла их еретиками и сама разобралась с ними..* // Продолжить // None //  // None"
        "Владыка, церковь хочет провести глобальные реформы. Вы согласны? // Да // Нет //  // None"
        true:
            "Дайте нам власть, чтоб остановить ересей // Да // Нет //  // None"
            true:
                "Сэр, влияние, оказываемое церковью слишком большое. Вы больше не управляете страной. // Что... // Что... //  // None"
                true:
                    "*Против вас организовали заговор. Вы были отправлены в темницу* // Продолжить // None //  // None"
                    "Теперь, ты тоже здесь // Здравствуйте! // Опять ты //  // None"
                    true:
                        "Все короли прокляты демоном, мы не исключение, наша учесть ждёт всех.. // Да // Нет //  // None"
                        true:
                            "Ещё никому не удавалось обхитрить демона.. // None // None //  // None"
                        false:
                            "Ещё никому не удавалось обхитрить демона.. // None // None //  // None"                                
                    false:
                        "Все короли прокляты демоном, мы не исключение, наша учесть ждёт всех.. // Да // Нет //  // None"
                false:
                    "*Против вас организовали заговор. Вы были отправлены в темницу* // Продолжить // None //  // None"
                    "Теперь, ты тоже здесь // Здравствуйте! // Опять ты //  // None"
            false:
                "Владыка, могу ли я построить больницу? Это поможет уменьшить заболеваемость различных болезней // Да // Нет //  // None"
                true:
                    "{EighthExtension}"
                false:
                    "{EighthExtension}"
        false:
            "Владыка, могу ли я построить больницу? Это поможет уменьшить заболеваемость различных болезней // Да // Нет //  // None"
            true:
                "{EighthExtension}"
            false:
                "{EighthExtension}"
    
    
    
    
    false:
        "Владыка, церковь хочет провести глобальные реформы // Да // Нет //  // None"
        true:
            "Дайте нам власть, чтоб остановить ересей // Да // Нет //  // None"
            true:
                "Сэр, влияние, оказываемое церковью слишком большое. Вы больше не управляете страной. // Что... // Что... //  // None"
                true:
                    "*Против вас организовали заговор. Вы были отправлены в темницу* // Продолжить // None //  // None"
                    "Теперь, ты тоже здесь // Здравствуйте! // Опять ты //  // None"
                    true:
                        "Все короли прокляты демоном, мы не исключение, наша учесть ждёт всех.. // Да // Нет //  // None"
                        true:
                            "Ещё никому не удавалось обхитрить демона.. // None // None //  // None"
                        false:
                            "Ещё никому не удавалось обхитрить демона.. // None // None //  // None"
                    false:
                        "Все короли прокляты демоном, мы не исключение, наша учесть ждёт всех.. // Да // Нет //  // None"
                        true:
                            "Ещё никому не удавалось обхитрить демона.. // None // None //  // None"
                        false:
                            "Ещё никому не удавалось обхитрить демона.. // None // None //  // None"
                false:
                    "*Против вас организовали заговор. Вы были отправлены в темницу* // Продолжить // None //  // None"
                    "Теперь, ты тоже здесь // Здравствуйте! // Опять ты //  // None"
                    true:
                        "Все короли прокляты демоном, мы не исключение, наша учесть ждёт всех.. // Да // Нет //  // None"
                        true:
                            "Ещё никому не удавалось обхитрить демона.. // None // None //  // None"
                        false:
                            "Ещё никому не удавалось обхитрить демона.. // None // None //  // None"
                    false:
                        "Все короли прокляты демоном, мы не исключение, наша учесть ждёт всех.. // Да // Нет //  // None"
                        true:
                            "Ещё никому не удавалось обхитрить демона.. // None // None //  // None"
                        false:
                            "Ещё никому не удавалось обхитрить демона.. // None // None //  // None"
            false:
                "Владыка, могу ли я построить больницу? Это поможет уменьшить заболеваемость различных болезней // Да // Нет //  // None"
                true:
                    "{EighthExtension}"
                false
                    "{EighthExtension}"
        false:
            "Владыка, могу ли я построить больницу? Это поможет уменьшить заболеваемость различных болезней // Да // Нет //  // None"
            true:
                "{EighthExtension}"
            false:
                "{EighthExtension}"



















"""




