

SecondExtension = """
    "Улицы нашей прекрасной столицы воняют сточными водами, нужно построить канализацию // Да // Нет // 0 0 +20 -10 $ 0 0 -10 +5 // None"    
    true:
        "[bundle]"
        bundle:
            "Мой друг-врач спас меня от смертельной болезни, он хочет поговорить с вами, но тот немного маг // Впустить его.. // Я занят // 0 0 +5 0 $ 0 0 -5 0 // None"
            true:
                "Здравствуйте, я маг-целитель Хрисанф, я хочу вам предложить защиту от смерти, либо улучшить вам жизнь своими навыками // Да // Нет // 0 0 +5 0 $ 0 0 0 0 // None"
                true:
                    "Вы сможете обратиться ко мне за любой помощью! *даёт вам странную нить и уходит* // Продолжить // None //  // None"
                "[bundle]"
                bundle:
                    "Правитель соседнего государства заявляет, что вы должны спасти его дочь // Да // Нет //  // None"
                    true:
                        "*Вы отправляетесь на место, где последний раз видели дочь царя. Вдруг, вы слышите крики из чащи леса и спешите к ним.* // Продолжить // None //  // None"
                        "Прошу, спаси меня! // Да // Нет //  // None"
                        true:
                            "Ты хочешь забрать её? // Напасть! // Да //  // None"
                            true:
                                "*Вы ожесточённо сражаетесь с драконом, но он одерживает вверх* // Что... // Что... //  // None"
                                true:
                                    "Вы летите прямо в пасть к дракону и вспоминаете лучшие моменты своей жизни* // None // None //  // None"
                                false:
                                    "Вы летите прямо в пасть к дракону и вспоминаете лучшие моменты своей жизни* // None // None //  // None"
                            false:
                                "Хорошо, она твоя, мы не в сказках, чтоб сражаться // Продолжить // None //  // None"
                                "*Вместе с принцессой вы выходите из пещеры* // Продолжить // None //  // None"
                                "Хотите ли вы стать моим принцем? // Да // Нет //  // None"
                                true:
                                    "{ThirdExtension}"
                                false:
                                    "{ThirdExtension}"
                        false:
                            "Вы разворачиваетесь и убегаете.. // Продолжить // None //  // None"
                            "{ThirdExtension}"
                        false:
                            "{ThirdExtension}"       
                    false:
                        "{ThirdExtension}"
            false:
                "[bundle]"
                bundle:
                    "Правитель соседнего государства заявляет, что вы должны спасти его дочь // Да // Нет //  // None"
                    true:
                        "*Вы отправляетесь на место, где последний раз видели дочь царя. Вдруг, вы слышите крики из чащи леса и спешите к ним.* // Продолжить // None //  // None"
                        "Прошу, спаси меня! // Да // Нет //  // None"
                        true:
                            "Ты хочешь забрать её? // Напасть! // Да //  // None"
                            true:
                                "*Вы ожесточённо сражаетесь с драконом, но он одерживает вверх* // Что... // Что... //  // None"
                                true:
                                    "Вы летите прямо в пасть к дракону и вспоминаете лучшие моменты своей жизни* // None // None //  // None"
                                false:
                                    "Вы летите прямо в пасть к дракону и вспоминаете лучшие моменты своей жизни* // None // None //  // None"
                            false:
                                "Хорошо, она твоя, мы не в сказках, чтоб сражаться // Продолжить // None //  // None"
                                "*Вместе с принцессой вы выходите из пещеры* // Продолжить // None //  // None"
                                "Хотите ли вы стать моим принцем? // Да // Нет //  // None"
                                true:
                                    "{ThirdExtension}"
                                false:
                                    "{ThirdExtension}"
                        false:
                            "Вы разворачиваетесь и убегаете.. // Продолжить // None //  // None"
                            "{ThirdExtension}"
                    false:
                        "{ThirdExtension}"       
        false:
            "[bundle]"
            bundle:
                "Правитель соседнего государства заявляет, что вы должны спасти его дочь // Да // Нет //  // None"
                true:
                    "*Вы отправляетесь на место, где последний раз видели дочь царя. Вдруг, вы слышите крики из чащи леса и спешите к ним.* // Продолжить // None //  // None"
                    "Прошу, спаси меня! // Да // Нет //  // None"
                    true:
                        "Ты хочешь забрать её? // Напасть! // Да //  // None"
                        true:
                            "*Вы ожесточённо сражаетесь с драконом, но он одерживает вверх* // Что... // Что... //  // None"
                            true:
                                "Вы летите прямо в пасть к дракону и вспоминаете лучшие моменты своей жизни* // None // None //  // None"
                            false:
                                "Вы летите прямо в пасть к дракону и вспоминаете лучшие моменты своей жизни* // None // None //  // None"
                        false:
                            "Хорошо, она твоя, мы не в сказках, чтоб сражаться // Продолжить // None //  // None"
                            "*Вместе с принцессой вы выходите из пещеры* // Продолжить // None //  // None"
                            "Хотите ли вы стать моим принцем? // Да // Нет //  // None"
                            true:
                                "{ThirdExtension}"
                            false:
                                "{ThirdExtension}"
                    false:
                        "Вы разворачиваетесь и убегаете.. // Продолжить // None //  // None"
                        "{ThirdExtension}"
                false:
                    "{ThirdExtension}"
    
    
    
    
    
    
    
    
    false:
        "[bundle]"
        bundle:
            "Мой друг-врач спас меня от смертельной болезни, он хочет поговорить с вами, но тот немного маг // Впустить его.. // Я занят // 0 0 +5 0 $ 0 0 -5 0 // None"
            true:
                "Здравствуйте, я маг-целитель Хрисанф, я хочу вам предложить защиту от смерти, либо улучшить вам жизнь своими навыками // Да // Нет // 0 0 +5 0 $ 0 0 0 0 // None"   
                true:
                    "Вы сможете обратиться ко мне за любой помощью! *даёт вам странную нить и уходит* // Продолжить // None //  // None"
                    "Правитель соседнего государства заявляет, что вы должны спасти его дочь // Да // Нет // None"
                "[bundle]"
                bundle:
                    true:
                        "*Вы отправляетесь на место, где последний раз видели дочь царя. Вдруг, вы слышите крики из чащи леса и спешите к ним.* // Продолжить // None //  // None"
                        "Прошу, спаси меня! // Да // Нет // None"
                        true:
                            "Ты хочешь забрать её? // Напасть! // Да // None"
                            true:
                                "*Вы ожесточённо сражаетесь с драконом, но он одерживает вверх* // Что... // Что... // None"
                                true:
                                    "Вы летите прямо в пасть к дракону и вспоминаете лучшие моменты своей жизни* // None // None // None"
                                false:
                                    "Вы летите прямо в пасть к дракону и вспоминаете лучшие моменты своей жизни* // None // None // None"
                            false:
                                "Хорошо, она твоя, мы не в сказках, чтоб сражаться // Продолжить // None //  // None"
                                "*Вместе с принцессой вы выходите из пещеры* // Продолжить // None //  // None"
                                "Хотите ли вы стать моим принцем? // Да // Нет // None"
                                true:
                                    "{ThirdExtension}"
                                false:
                                    "{ThirdExtension}"
                    false:
                        "Вы разворачиваетесь и убегаете.. // Продолжить // None //  // None"
                        "{ThirdExtension}"        
            false:
                "[bundle]"
                bundle:
                    "Правитель соседнего государства заявляет, что вы должны спасти его дочь // Да // Нет // None"   
                    true:
                        "*Вы отправляетесь на место, где последний раз видели дочь царя. Вдруг, вы слышите крики из чащи леса и спешите к ним.* // Продолжить // None //  // None"
                        "Прошу, спаси меня! // Да // Нет // None"
                        true:
                            "Ты хочешь забрать её? // Напасть! // Да // None"
                            true:
                                "*Вы ожесточённо сражаетесь с драконом, но он одерживает вверх* // Что... // Что... // None"
                                true:
                                    "Вы летите прямо в пасть к дракону и вспоминаете лучшие моменты своей жизни* // None // None // None"
                                false:
                                    "Вы летите прямо в пасть к дракону и вспоминаете лучшие моменты своей жизни* // None // None // None"
                            false:
                                "Хорошо, она твоя, мы не в сказках, чтоб сражаться // Продолжить // None //  // None"
                                "*Вместе с принцессой вы выходите из пещеры* // Продолжить // None //  // None"
                                "Хотите ли вы стать моим принцем? // Да // Нет // None"
                                true:
                                    "{ThirdExtension}"
                                false:
                                    "{ThirdExtension}"
                    false:
                        "Вы разворачиваетесь и убегаете.. // Продолжить // None //  // None"
                        "{ThirdExtension}"     
        false:
            "[bundle]"
            bundle:
                "Правитель соседнего государства заявляет, что вы должны спасти его дочь // Да // Нет // None"
                true:
                    "*Вы отправляетесь на место, где последний раз видели дочь царя. Вдруг, вы слышите крики из чащи леса и спешите к ним.* // Продолжить // None //  // None"
                    "Прошу, спаси меня! // Да // Нет // None"
                    true:
                        "Ты хочешь забрать её? // Напасть! // Да // None"
                        true:
                            "*Вы ожесточённо сражаетесь с драконом, но он одерживает вверх* // Что... // Что... // None"
                            true:
                                "Вы летите прямо в пасть к дракону и вспоминаете лучшие моменты своей жизни* // None // None // None"
                            false:
                                "Вы летите прямо в пасть к дракону и вспоминаете лучшие моменты своей жизни* // None // None // None"
                        false:
                            "Хорошо, она твоя, мы не в сказках, чтоб сражаться // Продолжить // None //  // None"
                            "*Вместе с принцессой вы выходите из пещеры* // Продолжить // None //  // None"
                            "Хотите ли вы стать моим принцем? // Да // Нет // None"
                            true:
                                "{ThirdExtension}"
                            false:
                                "{ThirdExtension}"
                    false:
                        "Вы разворачиваетесь и убегаете.. // Продолжить // None //  // None"
                        "{ThirdExtension}"
                false:
                    "{ThirdExtension}"








"""