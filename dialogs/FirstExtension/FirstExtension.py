FirstExtension = """
    "Мы можем повысить арендную плату в домах, которые мы построили для малоимущих // Да // Нет // None"
    true:
        "Как вы могли так поступить с нами? // Смирись и терпи! // Моя вина // None"
        true:
            "Владыка! Армия соседней страны группируется у Западной границы нашего государства, отправить армию? // Да // Нет // None"
            true:
                "У нас кончается вооружение, что нам делать, сэр!? // Срочно отступаем! // Бог с нами! // None"
                true:
                    "*Армия перегрупировалась и сокрушила наступление* // Продолжить // None // None"
                    "{SecondExtension}"
                false:
                    "[chance] 65 35"
                    chance:
                        "Нам удалось отбиться, враг отступает! // Продолжить // None // None"
                        true:
                            "{SecondExtension}"
                    
                    "Владыка, нам не удалось остановить врага, они приближаются к нам! // Что... // Что... // None"
                        true:
                            "*Армия врага вошла в столицу, вы были казнены!* // None // None // None"
                        false:
                            "*Армия врага вошла в столицу, вы были казнены!* // None // None // None"
            false:
                "У нас кончается вооружение, что нам делать, сэр!? // Срочно отступаем! // Бог с нами! // None"
                true:
                    "*Армия перегрупировалась и сокрушила наступление* // Продолжить // None // None"
                    "{SecondExtension}"
                false:
                    "[chance] 65 35"
                    chance:
                        "Нам удалось отбиться, враг отступает! // Продолжить // None // None"
                        true:
                            "{SecondExtension}"
                    
                    "Владыка, нам не удалось остановить врага, они приближаются к нам! // Что... // Что... // None"
                        true:
                            "*Армия врага вошла в столицу, вы были казнены!* // None // None // None"
                        false:
                            "*Армия врага вошла в столицу, вы были казнены!* // None // None // None"
        false:
            "Владыка! Армия соседней страны группируется у Западной границы нашего государства, отправить армию? // Да // Нет // None"
            true:
                "У нас кончается вооружение, что нам делать, сэр!? // Срочно отступаем! // Бог с нами! // None"
                true:
                    "*Армия перегрупировалась и сокрушила наступление* // Продолжить // None // None"
                    "{SecondExtension}"
                false:
                    "[chance] 65 35"
                    chance:
                        "Нам удалось отбиться, враг отступает! // Продолжить // None // None"
                        true:
                            "{SecondExtension}"
                    
                    "Владыка, нам не удалось остановить врага, они приближаются к нам! // Что... // Что... // None"
                        true:
                            "*Армия врага вошла в столицу, вы были казнены!* // None // None // None"
                        false:
                            "*Армия врага вошла в столицу, вы были казнены!* // None // None // None"
            false:
                "Армия врага развернулась, ложная тревога, нам больше ничего не угрожает! // Да // Нет // None"
                true:
                    "{SecondExtension}"
                false:
                    "{SecondExtension}"

    
    
    
    
    
    
    
    false:
        "Владыка! Армия соседней страны группируется у Западной границы нашего государства, отправить армию? // Да // Нет // None"
        true:
            "У нас кончается вооружение, что нам делать, сэр!? // Срочно отступаем! // Бог с нами! // None"
            true:
                "*Армия перегрупировалась и сокрушила наступление* // Продолжить // None // None"
                "{SecondExtension}"
            false:
                "[chance] 65 35"
                chance:
                    "Нам удалось отбиться, враг отступает! // Продолжить // None // None"
                    true:
                        "{SecondExtension}"
                    
                    "Владыка, нам не удалось остановить врага, они приближаются к нам! // Что... // Что... // None"
                        true:
                            "*Армия врага вошла в столицу, вы были казнены!* // None // None // None"
                        false:
                            "*Армия врага вошла в столицу, вы были казнены!* // None // None // None"
        false:
            "Армия врага развернулась, ложная тревога, нам больше ничего не угрожает! // Да // Нет // None"
            true:
                "{SecondExtension}"
            false:
                "{SecondExtension}"





"""