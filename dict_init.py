import json

start_message = ('Привет, *{}*! Сыграем в города? Для начала выбери режим '
                 'игры с помощью кнопок внизу. \n\n'
                 '_Пиши /start, чтобы начать новую игру. \n'
                 'Пиши /progress, чтобы посмотреть ход игры. \n'
                 'Пиши /rules, чтобы ознакомиться с правилами. \n'
                 'Пиши /info, чтобы узнать подробнее о работе бота._')

help_message = ('_Пиши /start, чтобы начать новую игру. \n'
                'Пиши /progress, чтобы посмотреть ход игры. \n'
                'Пиши /rules, чтобы ознакомиться с правилами. \n'
                'Пиши /info, чтобы узнать подробнее о работе бота._')

reply_input_field = 'Введите город...'

info_message = ('Бот имеет два режима игры: \n'
                '- *Города* 🇷🇺 *(РФ)* \n'
                '- *Города* 🌎 *(Мир)* \n\n'
                'В режиме *Города* 🇷🇺 в базе бота находятся все города, '
                'входящие в состав Российской Федерации _(около 1100)_. \n'
                '_Примечание: В РФ населённый пункт может приобрести статус '
                'города, если в нём проживает не менее 12 тысяч жителей._ \n\n'
                'В режиме *Города* 🌎 в базе бота числится _более 10 000_ '
                'городов. \n\nЛогика работы: \n'
                'Данный Бот проверяет каждую букву города с конца и '
                'отправляет вспомогательное сообщение, в случае, если '
                'следующий город должен начинаться не с последней буквы '
                'предыдущего. Вспомогательное сообщение содержит букву, '
                'на которую должен начинаться следующий город, а также '
                'буквы(у), которые не могут быть использованы. \n\n'
                'Буквы могут не пройти проверку: \n'
                '- если на них не начинается ни один город '
                '_(например: Ь, Ъ);_ \n'
                '- если городов на данную букву не осталось '
                '_(они были уже названы ранее)_ \n\nКаждый город, '
                'отправленный ботом также является ссылкой, нажав на '
                'которую можно более подробно ознакомится с населенным '
                'пунктом в интернете. \n\nАвтор бота: @drownpierrot')

rules = ('*Города* — игра для нескольких (двух или более) человек, в которой '
         'каждый участник в свою очередь называет реально существующий город '
         'любой страны, название которого начинается на ту букву, которой '
         'оканчивается название предыдущего города. \n\n_Например:_ \n'
         '_Игрок №1:_ Росто*в* \n'
         '_Игрок №2:_ *В*ыбор*г* \n'
         '_Игрок №1:_ *Г*еленджи*к* \n'
         '_Игрок №2:_ *К*азань \n\n'
         'Повторения не допускаются. Игра оканчивается, когда участник '
         'не может назвать нового города.')

errors = {
    'digit':
        'Мы же в города играем. В вашем ответе не должно быть цифр.',
    'punctuation':
        ('Мы же в города играем. В вашем ответе не должно быть символов '
         '_(кроме дефиса)_'),
    'not_town': [
        'Такого города нет в моей базе...',
        'Не знаю такого города...',
        'Может вы неправильно написали?'
    ],
    'used_town': 'Кажется этот город уже был...',
    'need_letter': {
        '0': 'Кажется Вам на *{}*',
        '1': ('Кажется {} на *{}*, \nтак как на букв{} *{}* не начинается '
              'ни один город.'),
        '2': ('Кажется {} на *{}*, \nтак как на букв{} *{}* не осталось '
              'городов.'),
        '3': 'Кажется {} на *{}*, \nтак как на букву{} *{}* '
             'не начинается ни один город, а на *{}* не осталось городов.',
        '4': ('Кажется игра окончена, так как на *{}* не начинается '
              'ни один город, а на *{}* не осталось городов.'),
        '5': ('Кажется игра окончена, так как на *{}* не начинается '
              'ни один город, а на *{}* не осталось городов.')
        }
}

with open('data/punctuation.json', 'r') as f3:
    PUNCTUATION = json.load(f3)
    # Спец. символы, которых не должно быть в названии городов

with open('data/ru/ru_towns_dict.json', 'r') as f1:
    RU_TOWNS_DICT = json.load(f1)
    # СЛОВАРЬ ВСЕХ ГОРОДОВ РФ
    # Формат: {'первая буква названия города': [список городов,
    # начинающихся на букву в ключе]}
    # Пример: {'А': ['Азов', 'Аксай'], 'Б': ['Белово', 'Белозерск']}

with open('data/ru/ru_towns_list.json', 'r') as f2:
    RU_TOWNS_LIST = json.load(f2)
    # СПИСОК ВСЕХ ГОРОДОВ РФ
    # Формат: [город, город, город]
    # Пример: ['азов', 'ак-довурак', 'аксай']

with open('data/ru/ru_links.json', 'r') as f4:
    LINKS = json.load(f4)
    # СЛОВАРЬ ССЫЛОК НА СТРАНИЦЫ ГОРОВ РФ В ВИКИПЕДДИИ

with open('data/world/towns_dict.json', 'r') as f5:
    TOWNS_DICT = json.load(f5)
    # СЛОВАРЬ ВСЕХ ГОРОВ МИРА

with open('data/world/towns_list.json') as f6:
    TOWNS_LIST = json.load(f6)
    # СПИСОК ВСЕХ ГОРОВ МИРА
