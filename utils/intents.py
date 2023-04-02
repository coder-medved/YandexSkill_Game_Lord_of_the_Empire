"""
etot file nuzhen dlya obrabotki estestvennogo yazika. use a `isInCommandOr` function with this arrays.
"""

YesIntents = ['да', 'ок', 'конечно', 'соглас', 'окей', 'поехали', 'лес гоу', 'вперёд', 'вперед', 'норм', 'ага', 'угу',
              'несомненно', 'разумеется', 'безусловно', 'хорошо', 'действительно', 'ладно', 'точно', 'йес', 'погнали',
              'в самом деле', 'несомнено', 'подтвержд', 'допустим', 'положительный ответ', 'истина', 'тру', 'ясно',
              'возможно', 'верно', 'уверен', 'го', 'давай', 'хочу']
NoIntents = ['не ', 'нет', 'фигушки', 'ничуть', 'отнюдь', 'нефига', 'нехрена', 'ни фига',
             'ни шиша', 'хренушки', 'отрица', 'отказ', 'ни']
RepeatIntents = ['что', 'повтори', 'ещё раз', 'еще раз', 'репит', 'повтор', 'не пон', 'не догнал',
                 'не вкурил', 'ало', 'ась', 'але', 'алё', 'не расслыш', 'не услыш']
HelpIntents = ['помог', 'помощь', 'хелп', 'подмога', 'поддержка', 'не умею', 'не знаю', 'как ', 'расскаж']
WhatDoYouCanIntents = ['владеешь', 'в силах', 'умеешь', 'можешь', 'способ']
WhoAreDevelopersIntents = ['разраб', 'кто ', 'создал', 'является',
                           'ответствен', 'занимался', 'создател']
ContactDevelopersIntents = ['связ', 'контакт', 'обратиться', 'установить связь',
                            'написать', 'сообщить', 'созвониться', 'задать', 'сказа']
LetsPlayIntents = ['играть', 'начать', 'сыграть', 'гоу', 'вперед', 'вперёд', 'погнали', 'начнем', 'начнём', 'старт']
BackIntents = ['назад', 'откат', 'отмена', 'обратно', 'вспять', 'взад', 'обрат']
HowToUseIntents = ['использовать', 'применять', 'экплуатировать', 'пользоваться', 'употреблять',
                   'распоряжаться', 'юзать', 'использовать', 'польз', 'как играть','научи']
ExitIntents = ['выход', 'выйди', 'покинуть', 'выйти', 'слинять']
MenuIntents = ['меню', 'главное', 'основное', 'начало', 'начальное']
ResetIntents = ['сброс', 'удали', 'сбрас', 'очист', 'обнул', 'рестарт', 'восстанов', 'сотри', 'стер']
StatsIntents = ['стат', 'оценк', 'результат', 'отчёт', 'отчет', 'данные', 'показател', 'анализ', 'характеристик',
                'цифры', 'числа', 'смерт', 'концов', 'перс', 'геро', 'достиж']
