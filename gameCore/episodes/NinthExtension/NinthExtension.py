NinthExtension = """
    "[bundle]"
    bundle:
        "Охотник Сильвестр $ Случаи нападения медведей на деревню участились, что прикажете делать? // Я сам разберусь! // Отправьте армию! //  // None"
        true:
            "*Вы отправляетесь в чащу леса, где был замечен медведь. Вдруг, вы слышите хруст ветки. Медведь нападает* // Напасть в ответ // Обороняться //  // None"
            true:
                "[chance] 60 40"
                chance:
                    "*Вам удалось ранить медведя, после чего он убежал* // Продолжить // None //  // None"
                    true:
                        "{TenthExtension}"
                    "*Медведь отразил вашу атаку и нанёс контрудар. Вы лежите на земле и бездыханно погибаете* // None // None //  // None"
            false:
                "*Медведь нападает, как внезапно его пронзает стрела* // Продолжить // None //  // None"
                "Лучник Ираклий $ Здравствуйте, владыка! Я рад, что смог помочь вам одолеть это существо. Наши земли пропитаны слухами о вас // Спасибо! // Тебе не стоило вмешиваться //  // None"
                true:
                    "*Герой взглянул на вас довольным взглядом и ушёл, не промолвив ни слова* // Продолжить // None //  // None"
                    "{TenthExtension}"
                false:
                    "Лучник Ираклий $ В следующий раз тебе никто не поможет // Продолжить // None //  // None"
                    "{TenthExtension}"
        false:
            "{TenthExtension}"
"""