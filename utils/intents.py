"""
etot file nuzhen dlya obrabotki estestvennogo yazika. use a `isInCommandOr` function with this arrays.
"""

YesIntents = ['да', 'ок', 'конечно', 'соглас', 'окей', 'поехали', 'лес гоу', 'вперёд', 'вперед', 'норм', 'ага', 'угу',
              'несомненно', 'разумеется', 'безусловно', 'хорошо', 'действительно', 'ладно', 'точно', 'йес', 'погнали',
              'в самом деле', 'несомнено', 'подтвержд', 'допустим', 'положительный ответ', 'истина', 'тру', 'ясно',
              'возможно', 'верно', 'уверен', 'го', 'давай']
NoIntents = ['не ', 'нет', 'фигушки', 'ничуть', 'отнюдь', 'нефига', 'нехрена', 'ни фига',
             'ни шиша', 'хренушки', 'отрица', 'отказ', 'ни']
RepeatIntents = ['что','чё','че','повтори', 'ещё раз', 'еще раз', 'репит', 'повтор', 'не понял', 'не догнал', 'не вкурил', 'ало', 'ась']
HelpIntents = ['помог', 'помощь', 'хелп', 'подмога', 'поддержка', 'как ']
WhatDoYouCanIntents = ['владеешь', 'в силах', 'умеешь', 'можешь', 'способ']
WhoAreDevelopersIntents = ['разраб', 'кто ', 'создал', 'является',
                           'ответствен', 'занимался', 'создател']
ContactDevelopersIntents = ['связ', 'контакт', 'обратиться',
                            'установить связь',
                            'написать', 'сообщить', 'созвониться', 'задать', 'разраб']
LetsPlayIntents = ['играть', 'начать', 'сыграть', 'гоу', 'вперед', 'погнали']
BackIntents = ['назад', 'откат', 'отмена', 'обратно', 'вспять', 'взад', 'обрат']
HowToUseIntents = ['использовать', 'применять', 'экплуатировать', 'пользоваться', 'употреблять',
                   'распоряжаться', 'юзать', 'использовать', 'польз']
ExitIntens = ['выйти', 'выход', 'выйди', 'покинуть', 'выйти', 'бежать', 'слинять']
MenuIntents = ['меню', 'главное', 'основное', 'начало', 'старт', 'начальное']
ResetIntents = ['сброс', 'удали', 'сбрас', 'очист', 'обнул', 'рестарт', 'восстанов']
StatsIntents = ['стат', 'оценк', 'результат', 'отчёт', 'отчет', 'данные', 'показател', 'анализ', 'характеристик',
                'цифры', 'числа']
