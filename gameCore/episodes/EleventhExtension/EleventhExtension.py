EleventhExtension = """
    "Господин Авдей $ Кто-то объедает нашу армию, ресурсов становится всё меньше, что нам делать? // Поймать и наказать предателя // Ничего // 0 0 0 0 $ 0 0 0 0 // None"
    true:
        "Командир Родион $ Вот он: *вы видите маленького мальчишку*, что прикажете с ним делать? // Палач! // Отпустить // 0 0 0 0 $ 0 0 0 0 // None"
        true:
            "*Мальчик начинает плакать, вы смеетесь и отпускаете его.* // Продолжить // None // 0 0 0 0 // None"
            "Епископ Галактион $ Наша церковь не имеет никакой силы, количество атеистов растёт, нужно вводить ужесточённые меры. // Да // Нет // +15 0 0 0 $ -25 0 +25 0 // None"
            true:
                "Крестьянин Иакинф $ Милорд, незнакомка передала вам яблоко, хотите съесть его? // Да // Нет // 0 0 0 0 $ 0 0 0 0 // None"
                true:
                    "[chance] 50 50"
                    chance:
                        "*Вы откусываете... и чувствуете всю сладость яблока, вам очень понравилось.* // Продолжить // None // 0 0 0 0 // None"
                        true:
                            "{TwelfthExtension}"
                        "*Вы откусываете, но сразу же чувствуете сильнейшую боль в сердце. Вы были отравлены.* // None // None //  // None"
                false:
                    "{TwelfthExtension}"
            false:
                "Кондрат $ Сэр, еретики хотят убить вас после того, как узнали о том, что вы верующий, они не хотят такого царя, вот-вот они ворвутся сюда. // Что же.... // Почему... //  // None"
                true:
                    "Бежать было слишком поздно, они заполонили весь дворец. Вас поймали и скормили собакам. // None // None //  // None"
                false:
                    "Бежать было слишком поздно, они заполонили весь дворец. Вас поймали и скормили собакам. // None // None //  // None"
        false:
            "Епископ Галактион $ Наша церковь не имеет никакой силы, количество атеистов растёт, нужно вводить ужесточённые меры. // Да // Нет // +15 0 0 0 $ -25 0 +25 0 // None"
            true:
                "Крестьянин Иакинф $ Милорд, незнакомка передала вам яблоко, хотите съесть его?  // Да // Нет // 0 0 0 0 $ 0 0 0 0 // None"
                true:
                    "[chance] 50 50"
                    chance:
                        "*Вы откусываете... и чувствуете всю сладость яблока, вам очень понравилось.* // Продолжить // None // 0 0 0 0 // None"
                        true:
                            "{TwelfthExtension}"
                        "*Вы откусываете, но сразу же чувствуете сильнейшую боль в сердце. Вы были отравлены.* // None // None //  // None"
                false:
                    "{TwelfthExtension}"
            false:
                "Кондрат $ Сэр, еретики хотят убить вас после того, как узнали о том, что вы верующий, они не хотят такого царя, вот-вот они ворвутся сюда. // Что же.... // Почему... //  // None"
                true:
                    "Бежать было слишком поздно, они заполонили весь дворец. Вас поймали и скормили собакам. // None // None //  // None"
                false:
                    "Бежать было слишком поздно, они заполонили весь дворец. Вас поймали и скормили собакам. // None // None //  // None"
    false:
        "*Ваша армия беднеет, так что об этом узнают все. Революция была неизбежна, как и потеря вашей головы.* // None // None //  // None"
"""
