from dialogs.FifthExtension.FifthExtension import *

FourthExtension = f'''
    "В этом году прекрасный урожай! // Накормите всех людей! // Всё в казну! // None"
    true:
        "Мяу-мяу // Продолжить // None // None"
            true:
                "*Вы слышите, как чья-то кошка подзывает вас к себе, в то же время вы приближаетесь к ней* // Продолжить // None // None"
                true:
                    "Хочешь сыграть в игру? // Да // Нет // None"
                    true:
                        "Несколько столетий назад, ты попросил о власти, которую ты никогда не видел, в обмен на свою человеческую сущность - свою душу // Продолжить // None // None"
                        true:
                            "Теперь я здесь, чтоб дать тебе ту самую власть, "владыка", если ты сможешь угодить мне, то ты получишь её // Да // Нет // None"
                            true:
                                "Мяу-мяу // Продолжить // None // None"
                                true:
                                    {FifthExtension}
                            false:
                                "Твоя династия всегда мечтала об этом и вот пришло время, когда я услышал вашу волю // Продолжить // None // None"
                                true:
                                    "*Вы чувствуете слабость и падаете* // Продолжить // None // None"
                                    true:
                                        {FifthExtension}
                    false:
                        "У тебя нет выбора, я правлю этим миром.. // Я - владыка // Кто ты? // None"
                        true:
                            "Я - тот, кто будет управлять твоей судьбой // Продолжить // None // None"
                            true:
                                "Несколько столетий назад, ты попросил о власти, которую ты никогда не видел, в обмен на свою человеческую сущность - свою душу // Продолжить // None // None"
                                true:
                                    "Теперь я здесь, чтоб дать тебе ту самую власть, "владыка", если ты сможешь угодить мне, то ты получишь её // Да // Нет // None"
                                    true:
                                        "Мяу-мяу // Продолжить // None // None"
                                        true:
                                            {FifthExtension}
                                    false:
                                        "Твоя династия всегда мечтала об этом и вот пришло время, когда я услышал вашу волю // Продолжить // None // None"
                                        true:
                                            "*Вы чувствуете слабость и падаете* // Продолжить // None // None"
                                            true:
                                                {FifthExtension}
                        false:
                            " Я - тот, кто будет управлять твоей судьбой"
                            true:
                                "Несколько столетий назад, ты попросил о власти, которую ты никогда не видел, в обмен на свою человеческую сущность - свою душу // Продолжить // None // None"
                                true:
                                    "Теперь я здесь, чтоб дать тебе ту самую власть, "владыка", если ты сможешь угодить мне, то ты получишь её // Да // Нет // None"
                                    true:
                                        "Мяу-мяу // Продолжить // None // None"
                                        true:
                                            {FifthExtension}
                                    false:
                                        "Твоя династия всегда мечтала об этом и вот пришло время, когда я услышал вашу волю // Продолжить // None // None"
                                        true:
                                            "*Вы чувствуете слабость и падаете* // Продолжить // None // None"
                                            true:
                                                {FifthExtension}
    
    
    
    
    
    false:
        "Мяу-мяу // Продолжить // None // None"
            true:
                "*Вы слышите, как чья-то кошка подзывает вас к себе, в то же время вы приближаетесь к ней* // Продолжить // None // None"
                true:
                    "Хочешь сыграть в игру? // Да // Нет // None"
                    true:
                        "Несколько столетий назад, ты попросил о власти, которую ты никогда не видел, в обмен на свою человеческую сущность - свою душу // Продолжить // None // None"
                        true:
                            "Теперь я здесь, чтоб дать тебе ту самую власть, "владыка", если ты сможешь угодить мне, то ты получишь её // Да // Нет // None"
                            true:
                                "Мяу-мяу // Продолжить // None // None"
                                true:
                                    {FifthExtension}
                            false:
                                "Твоя династия всегда мечтала об этом и вот пришло время, когда я услышал вашу волю // Продолжить // None // None"
                                true:
                                    "*Вы чувствуете слабость и падаете* // Продолжить // None // None"
                                    true:
                                        {FifthExtension}
                    false:
                        "У тебя нет выбора, я правлю этим миром.. // Я - владыка // Кто ты? // None"
                        true:
                            "Я - тот, кто будет управлять твоей судьбой // Продолжить // None // None"
                            true:
                                "Несколько столетий назад, ты попросил о власти, которую ты никогда не видел, в обмен на свою человеческую сущность - свою душу // Продолжить // None // None"
                                true:
                                    "Теперь я здесь, чтоб дать тебе ту самую власть, "владыка", если ты сможешь угодить мне, то ты получишь её // Да // Нет // None"
                                    true:
                                        "Мяу-мяу // Продолжить // None // None"
                                        true:
                                            {FifthExtension}
                                    false:
                                        "Твоя династия всегда мечтала об этом и вот пришло время, когда я услышал вашу волю // Продолжить // None // None"
                                        true:
                                            "*Вы чувствуете слабость и падаете* // Продолжить // None // None"
                                            true:
                                                {FifthExtension}
                        false:
                            " Я - тот, кто будет управлять твоей судьбой // Продолжить // None // None"
                            true:
                                "Несколько столетий назад, ты попросил о власти, которую ты никогда не видел, в обмен на свою человеческую сущность - свою душу // Продолжить // None // None"
                                true:
                                    "Теперь я здесь, чтоб дать тебе ту самую власть, "владыка", если ты сможешь угодить мне, то ты получишь её // Да // Нет // None"
                                    true:
                                        "Мяу-мяу // Продолжить // None // None"
                                        true:
                                            {FifthExtension}
                                    false:
                                        "Твоя династия всегда мечтала об этом и вот пришло время, когда я услышал вашу волю // Продолжить // None // None"
                                        true:
                                            "*Вы чувствуете слабость и падаете* // Продолжить // None // None"
                                            true:
                                                {FifthExtension}










'''