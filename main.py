from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


bot = Bot('TOKEN', parse_mode='HTML')
dp = Dispatcher(bot=bot)


# Клавиатура региона
region_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

region_keyboard_b1 = KeyboardButton('НОВОСИБИРСКОЕ')
region_keyboard_b2 = KeyboardButton('КЕМЕРОВСКОЕ')
region_keyboard_b3 = KeyboardButton('ТОМСКОЕ')
region_keyboard_b4 = KeyboardButton('КРАСНОЯРСКОЕ')
region_keyboard_b5 = KeyboardButton('АЛТАЙСКОЕ')
region_keyboard_b6 = KeyboardButton('АППАРАТ')
region_keyboard_b7 = KeyboardButton('ПЦП')
region_keyboard_b8 = KeyboardButton('ОМСКОЕ')
region_keyboard_b9 = KeyboardButton('КЫЗЫЛЬСКОЕ')

region_keyboard.row(region_keyboard_b1, region_keyboard_b2)
region_keyboard.row(region_keyboard_b3, region_keyboard_b4)
region_keyboard.row(region_keyboard_b5, region_keyboard_b6)
region_keyboard.row(region_keyboard_b7, region_keyboard_b8)
region_keyboard.add(region_keyboard_b9)

# Основная клавиатура 1й скрипт
main_script1_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    
main_script1_b1 = KeyboardButton('КАК ВСТУПИТЬ?')
main_script1_b2 = KeyboardButton('ПРОФ ВЗНОСЫ')
main_script1_b3 = KeyboardButton('КОНТАКТЫ')
main_script1_b4 = KeyboardButton('МАТ ПОМОЩЬ')
main_script1_b5 = KeyboardButton('УСЛУГИ')
main_script1_b6 = KeyboardButton('ЗАЯВЛЕНИЕ')
main_script1_back = KeyboardButton('НАЗАД')

main_script1_keyboard.row(main_script1_b1, main_script1_b4)
main_script1_keyboard.row(main_script1_b2, main_script1_b5)
main_script1_keyboard.row(main_script1_b3, main_script1_b6)
main_script1_keyboard.add(main_script1_back)

# Клавиатура раздела "МАТ ПОМОЩЬ" 1й скрипт
aid_script1_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

aid_script1_b1 = KeyboardButton('ЛЕЧЕНИЕ')
aid_script1_b2 = KeyboardButton('СОБЫТИЯ')
aid_script1_b3 = KeyboardButton('СПОРТ')
aid_script1_b4 = KeyboardButton('ДЕТИ')

script1_back = KeyboardButton('НAЗАД')  # 1-A
aid_script1_sub_back = KeyboardButton('HАЗАД')  # 1-H
script2_back = KeyboardButton("HAЗАД")  # 1-H 2-A
aid_script2_sub_back = KeyboardButton('НАЗAД')  # 2 - A
script3_back = KeyboardButton("HAЗAД")  # 1 - H 2 - A  4 - A

aid_script1_keyboard.row(aid_script1_b1, aid_script1_b3)
aid_script1_keyboard.row(aid_script1_b2, aid_script1_b4)
aid_script1_keyboard.add(script1_back)

# Клавиатура раздела "Лечение" 1й скрипт
treatment_script1_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

treatment_script1_b1 = KeyboardButton('БОЛЬНИЧНЫЙ')
treatment_script1_b2 = KeyboardButton('ТЯЖЕЛОЕ ЗАБОЛЕВАНИЕ')
treatment_script1_b3 = KeyboardButton('ДОРОГОСТОЯЩЕЕ ЛЕЧЕНИЕ')
treatment_script1_b4 = KeyboardButton('САНАТОРИЙ')

treatment_script1_keyboard.row(treatment_script1_b1, treatment_script1_b3)
treatment_script1_keyboard.row(treatment_script1_b2, treatment_script1_b4)
treatment_script1_keyboard.add(aid_script1_sub_back)
# Клавиатура раздела "События" 1й скрипт
events_script1_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

events_script1_b1 = KeyboardButton('ВЫХОД НА ПЕНСИЮ')
events_script1_b2 = KeyboardButton('ТРАУР')
events_script1_b3 = KeyboardButton('ФОРС-МАЖОР')
events_script1_b4 = KeyboardButton('ЮБИЛЕЙ')
events_script1_b5 = KeyboardButton('СОКРАЩЕНИЕ')
events_script1_b6 = KeyboardButton('СТАЖ РАБОТЫ')
events_script1_b7 = KeyboardButton('ТЯЖЕЛОЕ ПОЛОЖЕНИЕ')

events_script1_keyboard.row(events_script1_b1, events_script1_b5)
events_script1_keyboard.row(events_script1_b2, events_script1_b6)
events_script1_keyboard.row(events_script1_b3, events_script1_b7)
events_script1_keyboard.row(events_script1_b4, aid_script1_sub_back)
# Клавиатура раздела "Дети" 1й скрипт
children_script1_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

children_script1_b1 = KeyboardButton("РОЖДЕНИЕ/УСЫНОВЛЕНИЕ ДЕТЕЙ")
children_script1_b2 = KeyboardButton("ЛЕЧЕНИЕ РЕБЕНКА")
children_script1_b3 = KeyboardButton("ДЕНЬ ЗНАНИЙ")
children_script1_b4 = KeyboardButton("ДЕНЬ ЗАЩИТЫ ДЕТЕЙ")

children_script1_keyboard.row(children_script1_b1, children_script1_b3)
children_script1_keyboard.row(children_script1_b2, children_script1_b4)
children_script1_keyboard.add(aid_script1_sub_back)
# Клавиатура раздела "Услуги" 1й скрипт
services_script1_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

services_script1_b1 = KeyboardButton("ЮРИДИЧЕСКИЕ КОНСУЛЬТАЦИИ")
services_script1_b2 = KeyboardButton("МЫ КОМАНДА")
services_script1_b3 = KeyboardButton("СКИДКИ")

services_script1_keyboard.row(services_script1_b1, services_script1_b3)
services_script1_keyboard.row(services_script1_b2, script1_back)
# Основная клавиатура 2й скрипт
main_script2_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

main_script2_b1 = KeyboardButton("КAК ВСТУПИТЬ?")  # 1 - A
main_script2_b3 = KeyboardButton("KОНТАКТЫ")  # 1 - K
main_script2_b4 = KeyboardButton("МAТ ПОМОЩЬ")  # 1 - A
main_script2_b5 = KeyboardButton("УCЛУГИ")  #1 - C
main_script2_b6 = KeyboardButton("ЗAЯВЛЕНИЕ")  # 1 - A

main_script2_keyboard.row(main_script2_b1, main_script2_b4)
main_script2_keyboard.row(main_script1_b2, main_script2_b5)
main_script2_keyboard.row(main_script2_b3, main_script2_b6)
main_script2_keyboard.add(main_script1_back)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await bot.send_photo(message.chat.id, 'img_url')
    await bot.send_message(message.chat.id, "Вас приветствует Профсоюз Сибирского банка!")
    await bot.send_photo(message.chat.id, 'img_url')
    await message.answer("В каком отделении вы работаете?", reply_markup=region_keyboard)


# 1й скрипт начало
@dp.message_handler(text=['НОВОСИБИРСКОЕ', 'КЕМЕРОВСКОЕ', 'ТОМСКОЕ', 'КРАСНОЯРСКОЕ', 'АЛТАЙСКОЕ', 'АППАРАТ', 'ПЦП'])
async def region_script1_message(message: types.Message):
    await bot.send_photo(message.chat.id, 'img_url')
    await message.answer("Что тебя интересует?", reply_markup=main_script1_keyboard)


@dp.message_handler(text='КАК ВСТУПИТЬ?')
async def how_to_join_script1_message(message: types.Message):
    await bot.send_photo(message.chat.id, "img_url")
    await message.answer("Чтобы вступить в наш Профсоюз нужно заполнить и подписать "
                         "электронное «Заявление на удержание профсоюзных взносов из заработной платы» "
                         "во внутренней сети в АС Пульс.\n"
                         "Важно в поисковой строке выбрать <u><b>Профсоюз Сибирского банка</b></u>.\n"
                         "На следующий день в телефонном справочнике в разделе «Достижения» "
                         "появится значок «Член профсоюза» и его название.")


@dp.message_handler(text='ПРОФ ВЗНОСЫ')
async def prof_payments_script1_message(message: types.Message):
    await bot.send_photo(message.chat.id, "img_url")
    await message.answer("Бюджет Профсоюза складывается из профсоюзных взносов работающих участников. "
                         "Взнос равен 0,7% от оклада и удерживается один раз в месяц при выплате зарплаты. "
                         "Взнос не удерживается из премии, больничных, декретных, пособий и других выплат. "
                         "Пример, при окладе 20 000 рублей взнос 140 рублей.")


@dp.message_handler(text='КОНТАКТЫ')
async def contacts_script1_message(message: types.Message):
    await bot.send_photo(message.chat.id, "img_url")
    await message.answer("Новости и полезная информация публикуются в Сообществе ПРОФСОЮЗ Сибирского банка в "
                         "<u><b><a href='foreign_url'>"
                         "Друге</a></b></u>. Подписывайтесь и будьте в курсе активностей.\n\n"
                         "Для оперативных коммуникаций с Профсоюзом воспользуйтесь сервисом "
                         "<u><b>"
                         "<a href="
                         "'foreign_url'"
                         ">«Профсоюз»</a></b></u> в Друге:\n\n«Задать вопрос»;\n«Со мной поступили несправедливо»;\n"
                         "«Предложить идею»;\n«Оценить работу профсоюза»;\n«Консультация юриста».\n\n"
                         "Вы можете обратиться лично к председателям Первичных организаций на территориях\n\n"
                         "Председатель Профсоюза аппарата СИБ/ Новосибирского ГОСБ/ ПЦП г. "
                         "Новосибирск – Фарафонов Сергей Владимирович\n"
                         "Председатель Профсоюза Красноярск / Абакан – Лихторович Наталья Николаевна\n"
                         "Председатель Профсоюза Алтай - Кустов Владимир Владимирович\n"
                         "Председатель Профсоюза Кемерово - Шведов Виктор Геннадьевич\n"
                         "Председатель Профсоюза Томск - Алейникова Любовь Викторовна")


@dp.message_handler(text='МАТ ПОМОЩЬ')
async def material_aid_script1_message(message: types.Message):
    await bot.send_photo(message.chat.id, 'img_url')
    await message.answer("Мат помощь", reply_markup=aid_script1_keyboard)


@dp.message_handler(text='НAЗАД')  # в основное меню
async def script1_main_back_message(message: types.Message):
    await region_script1_message(message)


@dp.message_handler(text='HАЗАД')  # подраздел -> МАТ ПОМОЩЬ
async def material_aid_script1_sub_back_message(message: types.Message):
    await material_aid_script1_message(message)


@dp.message_handler(text='ЛЕЧЕНИЕ')
async def treatment_script1_message(message: types.Message):
    await message.answer("Выберите интересующий Вас раздел:\n\n•	Больничный\n•	Тяжелое заболевание\n"
                         "•	Дорогостоящее лечение\n•	Санаторий", reply_markup=treatment_script1_keyboard)


@dp.message_handler(text='БОЛЬНИЧНЫЙ')
async def treatment_script1_btn1_message(message: types.Message):
    await message.answer("Материальная помощь до 5 000 рублей в год представляется работающим членам Профсоюза "
                         "при стаже от одного года. Для получения выплаты необходимо оформить "
                         "Заявление + приложить копии больничных листов от 30 дней. "
                         "Документы необходимо направить в адрес председателя своей первичной организации Профсоюза.")


@dp.message_handler(text='ТЯЖЕЛОЕ ЗАБОЛЕВАНИЕ')
async def treatment_script1_btn2_message(message: types.Message):
    await message.answer("Материальная помощь до 15 000 рублей в год (зависит от размера ежемесячных членских взносов) "
                         "представляется работающим членам Профсоюза при стаже от одного года. Для получения выплаты "
                         "необходимо оформить Заявление + приложить копии выписок, эпикризы. Не распространяется "
                         "на косметологию, стоматологию, лазерное лечение зрения и другие операции, связанные "
                         "с улучшением внешности, а также ЭКО и т.п. Документы необходимо направить "
                         "в адрес председателя своей первичной организации Профсоюза.")


@dp.message_handler(text='ДОРОГОСТОЯЩЕЕ ЛЕЧЕНИЕ')
async def treatment_script1_btn3_message(message: types.Message):
    await message.answer("Материальная помощь до 15 000 рублей в год (зависит от размера ежемесячных членских взносов) "
                         "представляется работающим членам Профсоюза при стаже от двух лет. Для получения "
                         "выплаты необходимо оформить Заявление + приложить копии квитанций об оплате, "
                         "заключение о необходимости проведения лечения. Не распространяется на косметологию, "
                         "стоматологию, лазерное лечение зрения и другие операции, связанные с улучшением "
                         "внешности, а также ЭКО и т.п. Документы необходимо направить в адрес "
                         "председателя своей первичной организации Профсоюза.")


@dp.message_handler(text='САНАТОРИЙ')
async def treatment_script1_btn4_message(message: types.Message):
    await message.answer("Материальная помощь до 15 000 рублей один раз в три года "
                         "(зависит от размера ежемесячных членских взносов) представляется работающим "
                         "членам Профсоюза при стаже от трех лет. Для получения выплаты необходимо оформить "
                         "Заявление + приложить копии: договора, квитанций об оплате, обратного талона "
                         "(справка о пребывании в санатории). Документы необходимо направить в адрес "
                         "председателя своей первичной организации Профсоюза.")


@dp.message_handler(text='СОБЫТИЯ')
async def events_script1_message(message: types.Message):
    await message.answer("Выберите интересующий Вас раздел:\n\n•	Выход на пенсию\n•	Траур\n"
                         "•	Форс-мажор\n•	Юбилей\n•	Сокращение\n•	Стаж работы\n"
                         "•	Тяжелое положение\n", reply_markup=events_script1_keyboard)


@dp.message_handler(text='ВЫХОД НА ПЕНСИЮ')
async def events_script1_btn1_message(message: types.Message):
    await message.answer("Материальная помощь до 3 000 рублей представляется работающим членам Профсоюза "
                         "при стаже от трех лет. Для получения выплаты необходимо оформить Заявление. "
                         "Документы необходимо направить в адрес председателя своей первичной организации Профсоюза.")


@dp.message_handler(text='ТРАУР')
async def events_script1_btn2_message(message: types.Message):
    await message.answer("Материальная помощь до 10 000 рублей (зависит от размера ежемесячных членских взносов) "
                         "представляется работающим членам Профсоюза при стаже от одного года. Для получения "
                         "выплаты необходимо оформить Заявление + приложить копии: свидетельство о смерти; "
                         "свидетельство о родственной связи (о рождении; заключение брака). Документы "
                         "необходимо направить в адрес председателя своей первичной организации Профсоюза.")


@dp.message_handler(text='ФОРС-МАЖОР')
async def events_script1_btn3_message(message: types.Message):
    await message.answer("Материальная помощь при возмещении материальных потерь вследствие стихийных бедствий, "
                         "причинения физического, имущественного вреда, несчастного случая, катастроф, "
                         "и т.п. до 40 000 рублей в год представляется работающим членам Профсоюза при стаже "
                         "от одного года. Для получения выплаты необходимо оформить Заявление + приложить "
                         "копии документов, подтверждающих произошедший несчастный случай. "
                         "Документы необходимо направить в адрес председателя своей первичной организации Профсоюза.")


@dp.message_handler(text='ЮБИЛЕЙ')
async def events_script1_btn4_message(message: types.Message):
    await message.answer("Материальная помощь до 5 000 рублей представляется работающим членам Профсоюза "
                         "при достижении юбилейной даты дня рождения - 55-летия и стаже от трех лет. Для получения "
                         "выплаты необходимо оформить Заявление + приложить копию паспорта. Документы необходимо "
                         "направить в адрес председателя своей первичной организации Профсоюза.")


@dp.message_handler(text='СОКРАЩЕНИЕ')
async def events_script1_btn5_message(message: types.Message):
    await message.answer("Материальная помощь при увольнении по сокращению численности или штата "
                         "работников до 10 000 рублей (зависит от размера "
                         "ежемесячных членских взносов) представляется работающим членам "
                         "Профсоюза при стаже от пяти лет. Для получения выплаты "
                         "необходимо оформить Заявление. Документы необходимо "
                         "направить в адрес председателя своей первичной организации Профсоюза.")


@dp.message_handler(text='СТАЖ РАБОТЫ')
async def events_script1_btn6_message(message: types.Message):
    await message.answer("Материальная помощь до 5 000 рублей представляется работающим членам Профсоюза при стаже "
                         "от трех лет. Для получения выплаты необходимо оформить Заявление + "
                         "приложить справку от работодателя о непрерывном стаже работы. "
                         "Общий стаж работы в Сбербанке должен быть равен 15, 20, 25, 30, 35, 40 лет "
                         "в текущем году. Документы необходимо направить в адрес председателя "
                         "своей первичной организации Профсоюза.")


@dp.message_handler(text='ТЯЖЕЛОЕ ПОЛОЖЕНИЕ')
async def events_script1_btn7_message(message: types.Message):
    await message.answer("Материальная помощь при тяжелом материальном положении/иных обстоятельствах "
                         "до 10 000 рублей в год (зависит от размера ежемесячных членских взносов) "
                         "представляется работающим членам Профсоюза при стаже от трех лет. Для получения "
                         "выплаты необходимо оформить Заявление + приложить копии документов, "
                         "подтверждающих тяжелое материальное положение. Документы необходимо направить "
                         "в адрес председателя своей первичной организации Профсоюза.")


@dp.message_handler(text='СПОРТ')
async def sport_script1_message(message: types.Message):
    await message.answer("Материальная помощь на спортивно-оздоровительные абонементы до 3 000 рублей "
                         "в год (зависит от размера ежемесячных членских взносов) представляется работающим "
                         "членам Профсоюза при стаже от двух лет. Для получения выплаты необходимо"
                         "оформить Заявление + приложить копии: чеков об оплате, абонементов, "
                         "билетов, и т.д. Документы необходимо направить в адрес председателя "
                         "своей первичной организации Профсоюза.")


@dp.message_handler(text='ДЕТИ')
async def children_script1_message(message: types.Message):
    await message.answer("Выберите интересующий Вас раздел:\n\n•	Рождение/усыновление детей\n"
                         "•	Лечение ребенка\n•	День знаний\n•	День защиты детей\n",
                         reply_markup=children_script1_keyboard)


@dp.message_handler(text='РОЖДЕНИЕ/УСЫНОВЛЕНИЕ ДЕТЕЙ')
async def children_script1_btn1_message(message: types.Message):
    await message.answer("Материальная помощь до 3 000 рублей представляется работающим членам Профсоюза "
                         "и находящимся в декрете при стаже от одного года. Для получения выплаты необходимо "
                         "оформить Заявление + приложить Копию свидетельства о рождении/ усыновлении/ "
                         "опекунстве ребенка. Документы необходимо направить в адрес "
                         "председателя своей первичной организации Профсоюза.")


@dp.message_handler(text='ЛЕЧЕНИЕ РЕБЕНКА')
async def children_script1_btn2_message(message: types.Message):
    await message.answer("Материальная помощь на лечение ребенка/ помощь детям с ограниченными "
                         "возможностями до 10 000 рублей в год (зависит от размера ежемесячных членских взносов) "
                         "представляется работающим членам Профсоюза при стаже от двух лет. "
                         "Для получения выплаты необходимо оформить Заявление + приложить копию квитанции "
                         "об оплате, заключение о необходимости проведения лечения. Документы необходимо "
                         "направить в адрес председателя своей первичной организации Профсоюза.")


@dp.message_handler(text='ДЕНЬ ЗНАНИЙ')
async def children_script1_btn3_message(message: types.Message):
    await message.answer("Материальная помощь ко Дню знаний для первоклассников/выпускников до 3 000 рублей "
                         "представляется работающим членам Профсоюза при стаже от одного года. Для получения "
                         "выплаты необходимо оформить Заявление + приложить оригиналы копии свидетельства о "
                         "рождении, копии аттестата о получении среднего (средне специального) образования. "
                         "Документы необходимо направить в адрес председателя своей первичной организации Профсоюза.")


@dp.message_handler(text='ДЕНЬ ЗАЩИТЫ ДЕТЕЙ')
async def children_script1_btn4_message(message: types.Message):
    await message.answer("Материальная помощь ко Дню защиты детей 3000 рублей на первого ребенка и 1000 рублей "
                         "на каждого последующего представляется работающим членам Профсоюза. Для получения "
                         "выплаты необходимо оформить Заявление. Документы необходимо направить в адрес "
                         "председателя своей первичной организации Профсоюза.")


@dp.message_handler(text='УСЛУГИ')
async def services_script1_message(message: types.Message):
    await bot.send_photo(message.chat.id, "img_url")
    await message.answer("•	Юридические консультации\n•	Мы команда\n•	Скидки\n", reply_markup=services_script1_keyboard)


@dp.message_handler(text="ЮРИДИЧЕСКИЕ КОНСУЛЬТАЦИИ")
async def services_script1_btn1_message(message: types.Message):
    await message.answer("Каждый член Профсоюза может получить качественную юридическую "
                         "консультацию по личным вопросам или взаимоотношениям с ПАО Сбербанк "
                         "(трудовых, кредитных, иных). Для получения бесплатной консультации "
                         "необходимо создать обращение в Друге: сервис <u><b><a href="
                         "'foreign_url'>"
                         "«Профсоюз»</a></b></u>, шаблон «Консультация юриста».")


@dp.message_handler(text='МЫ КОМАНДА')
async def services_script1_btn2_message(message: types.Message):
    await message.answer("Для подразделений Профсоюз частично финансирует экскурсии, командообразующие "
                         "мероприятия и прочие активности для коллектива. Необходимо заблаговременно согласовать в "
                         "Профсоюзом финансирование по ходатайству Руководителя СПП, списку участников и другим "
                         "подтверждающим документам по запросу профкома Профсоюза.")


@dp.message_handler(text='СКИДКИ')
async def services_script1_btn3_message(message: types.Message):
    await message.answer("Профсоюз заключает соглашения с партнерами для предоставления скидок членам Профсоюза. "
                         "С перечнем партнеров и размерами скидок можно ознакомиться в разделе «Файлы» – "
                         "Сообщество Профсоюз Сибирского банка во внутренней сети.")


@dp.message_handler(text='ЗАЯВЛЕНИЕ')
async def statement_message(message: types.Message):
    await bot.send_photo(message.chat.id, 'img_url')
    await message.answer("Для получения материальной помощи необходимо заполнить Заявление. "
                         "Шаблоны заявлений размещены в разделеВ «Файлы» – Сообщество Профсоюз Сибирского "
                         "банка во внутренней сети СберДруга. К Заявлению всегда прилагаются копии подтверждающих "
                         "документов. Пакет на материальную помощь следует направить внутренней банковской почтой "
                         "председателю Профсоюза своего отделения.")


@dp.message_handler(text='НАЗАД')
async def main_back_message(message: types.Message):
    await bot.send_photo(message.chat.id, 'img_url')
    await message.answer("Вы вернулись в главное меню. В каком отделении вы работаете?", reply_markup=region_keyboard)
# 1й скрипт конец

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .


@dp.message_handler()
async def unknown_request(message: types.Message):
    await message.answer("Я Вас не понимаю! Воспользуйтесь клавиатурой под полем ввода для интересущего Вас запроса.")


if __name__ == "__main__":
    executor.start_polling(dp)
