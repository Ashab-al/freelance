from pyrogram import Client, filters
import asyncio
import aiogram
from aiogram import Bot
from aiogram.utils.exceptions import ChatNotFound
from aiogram.utils.exceptions import BadRequest
from aiogram import types
import gspread
from google.oauth2.service_account import Credentials
import logging
import re
import os
import json

# Проверить наличие файла 'keyword.json'
if not os.path.isfile('keyword.json'):
    # Если файла нет, создать его
    open('keyword.json', 'a').close()

# Проверить наличие файла 'clients.json'
if not os.path.isfile('clients.json'):
    # Если файла нет, создать его
    open('clients.json', 'a').close()

#Списки клиентов
SMM_CLIENTS = []
AVITO_CLIENTS = []
ASSISTANT_CLIENTS = []
BUHGALTER_CLIENTS = []
GRAFDESIGN_CLIENTS = []
COPIRATE_CLIENTS = []
SITE_CLIENTS = []
TARGET_CLIENTS = []
CHATBOTS_CLIENTS = []
TEHSPEC_CLIENTS = []
#Списки клиентов
KEYWORD_SMM = []
EXCEPTONS_SMM = []

KEYWORD_AVITO = []
EXCEPTONS_AVITO = []

KEYWORD_ASSISTANT = []
EXCEPTONS_ASSISTANT= []

KEYWORD_BUHGALTER = []
EXCEPTONS_BUHGALTER = []

KEYWORD_GRAFDESIGN = []
EXCEPTONS_GRAFDESIGN = []

KEYWORD_COPIRATE = []
EXCEPTONS_COPIRATE = []

KEYWORD_SITE = []
EXCEPTONS_SITE = []

KEYWORD_TARGET = []
EXCEPTONS_TARGET = []

KEYWORD_CHATBOTS = []
EXCEPTONS_CHATBOTS = []

KEYWORD_TEHSPEC = []
EXCEPTONS_TEHSPEC = []

EXCEPTONS_USERNAME = []

#Общие ключевые слова
GENERAL_FILTER_EXCEPTONS = []

#Статус подписки
SUBSCRIPTION_STATUS = []

#Статус подписки для каждого
SUBSCRIPTION_STATUS_FOR_EACH = {}

#Platform id всех клиентов
PLATFORM_ID = []
#Фильтры

# Определение функции, которая загружает данные из файла JSON
def load_json_from_file(file_name: str):
    # Открываем файл для чтения ('r' означает 'read')
    # Используем оператор with для автоматического закрытия файла после использования
    with open(file_name, 'r', encoding='utf-8') as f:
        # Используем функцию json.load() для преобразования данных из JSON в словарь Python
        data = json.load(f)
    # Возвращаем данные, полученные из файла
    return data


def sheet_open():
    # Открыть таблицу по названию
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
        ]

    creds = Credentials.from_service_account_file(filename='savvy-temple-380003-e855ebfc1557.json', scopes=scopes)
    client = gspread.authorize(creds)
    
    return client
    # Открыть таблицу по названию

def get_column_data(list_name: str):
    sheet = sheet_open().open('Фриланс заказы | Асхаб').worksheet(list_name)
    # Получаем все значения из столбца A
    column_data = sheet.get_all_records()
    return column_data


API_TOKEN_BOT = '6201167294:AAG_bC1dDYSvN4PxblRbFfR22zmzcZfjymg'

TELEGRAM_BOT = Bot(token=API_TOKEN_BOT)
keyboard = types.InlineKeyboardMarkup()

#юзербот
api_id = "29712677"
api_hash = "5c0fd5a6b02023ccd790af47f90055d6"
chat_id = "-1001786162328"
app = Client("my_account", api_id=api_id, api_hash=api_hash)

def update_clients():
    global SMM_CLIENTS, AVITO_CLIENTS, ASSISTANT_CLIENTS, BUHGALTER_CLIENTS, GRAFDESIGN_CLIENTS, \
            COPIRATE_CLIENTS, SITE_CLIENTS, TARGET_CLIENTS, CHATBOTS_CLIENTS, TEHSPEC_CLIENTS, SUBSCRIPTION_STATUS, \
            PLATFORM_ID, SUBSCRIPTION_STATUS_FOR_EACH
    
    print("Обновить список клиентов Асхаб Алхазуров аккаунт 2")

 

    result_get_data_json = load_json_from_file(file_name='clients.json')
    
    SMM_CLIENTS = result_get_data_json["smm_clients"]
    AVITO_CLIENTS = result_get_data_json["avito_clients"]
    ASSISTANT_CLIENTS = result_get_data_json["assistant_clients"]
    BUHGALTER_CLIENTS = result_get_data_json["buhgalter_clients"]
    GRAFDESIGN_CLIENTS = result_get_data_json["grafdesign_clients"]
    COPIRATE_CLIENTS = result_get_data_json["copirate_clients"]
    SITE_CLIENTS = result_get_data_json["site_clients"]
    TARGET_CLIENTS = result_get_data_json["target_clients"]
    CHATBOTS_CLIENTS = result_get_data_json["chatbots_clients"]
    TEHSPEC_CLIENTS = result_get_data_json["tehspec_clients"]
    SUBSCRIPTION_STATUS = result_get_data_json["subscription_status"]
    PLATFORM_ID = result_get_data_json["platform_id"]
    SUBSCRIPTION_STATUS_FOR_EACH = result_get_data_json["subscription_status_for_each"]
    print("\n\n\n!!!!!Аккаунт 2!!!!")
    app.send_message(chat_id=int(chat_id), text="Обновление списка клиентов (Новый аккаунт 1) - 100%")
    print(f"Авито - {AVITO_CLIENTS}\n\nSMM - {SMM_CLIENTS}")
    print(f"Ассистент - {ASSISTANT_CLIENTS}\n\nБухгалтер - {BUHGALTER_CLIENTS}")
    print(f"Графический дизайн - {GRAFDESIGN_CLIENTS}\n\nКопирайтер - {COPIRATE_CLIENTS}")
    print(f"Сайт - {SITE_CLIENTS}\n\nТаргет - {TARGET_CLIENTS}")
    print(f"Чат-боты - {CHATBOTS_CLIENTS}\n\nТех-спец - {TEHSPEC_CLIENTS}")
    print(SUBSCRIPTION_STATUS_FOR_EACH)
    print("\n\n\n")


def update_keyword_exceptons():
    global KEYWORD_SMM, EXCEPTONS_SMM, KEYWORD_AVITO, EXCEPTONS_AVITO, KEYWORD_ASSISTANT, \
            EXCEPTONS_ASSISTANT, KEYWORD_BUHGALTER, EXCEPTONS_BUHGALTER, KEYWORD_GRAFDESIGN, \
            EXCEPTONS_GRAFDESIGN, KEYWORD_COPIRATE, EXCEPTONS_COPIRATE, KEYWORD_SITE, EXCEPTONS_SITE, \
            KEYWORD_TARGET, EXCEPTONS_TARGET, KEYWORD_CHATBOTS, EXCEPTONS_CHATBOTS, KEYWORD_TEHSPEC, EXCEPTONS_TEHSPEC, \
            EXCEPTONS_USERNAME, GENERAL_FILTER_EXCEPTONS, SUBSCRIPTION_STATUS, PLATFORM_ID, SUBSCRIPTION_STATUS_FOR_EACH
    
    print("Обновить ключевые слова Асхаб Алхазуров")

    result_get_data_json = load_json_from_file(file_name='keyword.json')
        
    KEYWORD_SMM = result_get_data_json["Ключевые слова SMM"]
    EXCEPTONS_SMM = result_get_data_json["Слова исключения SMM"]

    KEYWORD_AVITO = result_get_data_json["Ключевые слова Авито"]
    EXCEPTONS_AVITO = result_get_data_json["Слова исключения Авито"]

    KEYWORD_ASSISTANT = result_get_data_json["Ключевые слова Ассистент"]
    EXCEPTONS_ASSISTANT = result_get_data_json["Слова исключения Ассистент"]

    KEYWORD_BUHGALTER = result_get_data_json["Ключевые слова Бухгалтерия"]
    EXCEPTONS_BUHGALTER = result_get_data_json["Слова исключения Бухгалтерия"]

    KEYWORD_GRAFDESIGN = result_get_data_json["Ключевые слова Графический дизайн" ]
    EXCEPTONS_GRAFDESIGN = result_get_data_json["Слова исключения Графический дизайн"]

    KEYWORD_COPIRATE = result_get_data_json["Ключевые слова Копирайт"]
    EXCEPTONS_COPIRATE = result_get_data_json["Слова исключения Копирайт"]

    KEYWORD_SITE = result_get_data_json["Ключевые слова Сайты"]
    EXCEPTONS_SITE = result_get_data_json["Слова исключения Сайты"]

    KEYWORD_TARGET = result_get_data_json["Ключевые слова Таргет" ]
    EXCEPTONS_TARGET = result_get_data_json["Слова исключения Таргет"]

    KEYWORD_CHATBOTS = result_get_data_json["Ключевые слова Чат-боты"]
    EXCEPTONS_CHATBOTS = result_get_data_json["Слова исключения Чат-боты"]

    KEYWORD_TEHSPEC = result_get_data_json["Ключевые слова Тех-спец"]
    EXCEPTONS_TEHSPEC = result_get_data_json["Слова исключения Тех-спец"]
    
    EXCEPTONS_USERNAME = result_get_data_json["Исключения отправители" ]

    GENERAL_FILTER_EXCEPTONS = result_get_data_json["Общий фильр"]  

    app.send_message(chat_id=int(chat_id), text="Обновление ключевых слов - 100%")
    
    print("\n\n\n Аккаунт 2!!!!")
    print(f"KEYWORD_AVITO - {KEYWORD_AVITO}\n\nEXCEPTONS_AVITO - {EXCEPTONS_AVITO}")
    print(f"KEYWORD_SMM - {KEYWORD_SMM}\n\nEXCEPTONS_SMM - {EXCEPTONS_SMM}")
    print(f"KEYWORD_ASSISTANT - {KEYWORD_ASSISTANT}\n\nEXCEPTONS_ASSISTANT - {EXCEPTONS_ASSISTANT}")
    print(f"KEYWORD_BUHGALTER - {KEYWORD_BUHGALTER}\n\nEXCEPTONS_BUHGALTER - {EXCEPTONS_BUHGALTER}")
    print(f"KEYWORD_GRAFDESIGN - {KEYWORD_GRAFDESIGN}\n\nEXCEPTONS_GRAFDESIGN - {EXCEPTONS_GRAFDESIGN}")
    print(f"KEYWORD_COPIRATE - {KEYWORD_COPIRATE}\n\nEXCEPTONS_COPIRATE - {EXCEPTONS_COPIRATE}")
    print(f"KEYWORD_SITE - {KEYWORD_SITE}\n\nEXCEPTONS_SITE - {EXCEPTONS_SITE}")
    print(f"KEYWORD_TARGET - {KEYWORD_TARGET}\n\nEXCEPTONS_TARGET - {EXCEPTONS_TARGET}")
    print(f"KEYWORD_CHATBOTS - {KEYWORD_CHATBOTS}\n\nEXCEPTONS_CHATBOTS - {EXCEPTONS_CHATBOTS}")
    print(f"KEYWORD_TEHSPEC - {KEYWORD_TEHSPEC}\n\nEXCEPTONS_TEHSPEC - {EXCEPTONS_TEHSPEC}")
    print(f"EXCEPTONS_USERNAME - {EXCEPTONS_USERNAME}")
    print(GENERAL_FILTER_EXCEPTONS)
    print("\n\n\n")


def general_filter(mes):
    global GENERAL_FILTER_EXCEPTONS

    for word_exceptons in GENERAL_FILTER_EXCEPTONS:

        if re.search(rf"{word_exceptons}", mes.lower()):
            return False

    return True


@app.on_message(filters.text & filters.regex(r"\bОбновить список клиентов аккаунт 2\b"))
def message_text(client, message):
    update_clients()
    

@app.on_message(filters.text & filters.regex(r"\bОбновить ключевые слова аккаунт 2\b"))
def message_text(client, message):
    update_keyword_exceptons()


@app.on_message(filters.text & ~filters.user("RubyStart_bot"))
async def message_text(client, message):
    global KEYWORD_SMM, EXCEPTONS_SMM, KEYWORD_AVITO, EXCEPTONS_AVITO, KEYWORD_ASSISTANT, \
            EXCEPTONS_ASSISTANT, KEYWORD_BUHGALTER, EXCEPTONS_BUHGALTER, KEYWORD_GRAFDESIGN, \
            EXCEPTONS_GRAFDESIGN, KEYWORD_COPIRATE, EXCEPTONS_COPIRATE, KEYWORD_SITE, EXCEPTONS_SITE, \
            KEYWORD_TARGET, EXCEPTONS_TARGET, KEYWORD_CHATBOTS, EXCEPTONS_CHATBOTS, KEYWORD_TEHSPEC, EXCEPTONS_TEHSPEC, \
            SMM_CLIENTS, AVITO_CLIENTS, ASSISTANT_CLIENTS, BUHGALTER_CLIENTS, GRAFDESIGN_CLIENTS, \
            COPIRATE_CLIENTS, SITE_CLIENTS, TARGET_CLIENTS, CHATBOTS_CLIENTS, TEHSPEC_CLIENTS, \
            EXCEPTONS_USERNAME, GENERAL_FILTER_EXCEPTONS, SUBSCRIPTION_STATUS, PLATFORM_ID, SUBSCRIPTION_STATUS_FOR_EACH
    try:
        message_text = message.text
        username = message.from_user.username
        if f"@{username}" != "@None":
            if f"@{username}" in EXCEPTONS_USERNAME:
                return False
            else:
                if general_filter(mes=message_text):
                    #Чат-боты
                    
                    await filtering_messages_by_category(category_name='Чат-боты', message=message_text,
                                                        keywords=KEYWORD_CHATBOTS, exceptons=EXCEPTONS_CHATBOTS,
                                                        client_list=CHATBOTS_CLIENTS, bot=TELEGRAM_BOT, username_customer=username, subscription=SUBSCRIPTION_STATUS_FOR_EACH)
                    
                    #SMM
                    await filtering_messages_by_category(category_name='SMM', message=message_text,
                                                        keywords=KEYWORD_SMM, exceptons=EXCEPTONS_SMM,
                                                        client_list=SMM_CLIENTS, bot=TELEGRAM_BOT, username_customer=username, subscription=SUBSCRIPTION_STATUS_FOR_EACH)
                    
                    #Авито
                    await filtering_messages_by_category(category_name='Авито', message=message_text,
                                                        keywords=KEYWORD_AVITO, exceptons=EXCEPTONS_AVITO, 
                                                        client_list=AVITO_CLIENTS, bot=TELEGRAM_BOT, username_customer=username, subscription=SUBSCRIPTION_STATUS_FOR_EACH)
                
                    #Ассистент
                    await filtering_messages_by_category(category_name='Ассистент', message=message_text,
                                                        keywords=KEYWORD_ASSISTANT, exceptons=EXCEPTONS_ASSISTANT,
                                                        client_list=ASSISTANT_CLIENTS, bot=TELEGRAM_BOT, username_customer=username, subscription=SUBSCRIPTION_STATUS_FOR_EACH)
                    
                    #Бухгалтер
                    await filtering_messages_by_category(category_name='Бухгалтер', message=message_text,
                                                        keywords=KEYWORD_BUHGALTER, exceptons=EXCEPTONS_BUHGALTER,
                                                        client_list=BUHGALTER_CLIENTS, bot=TELEGRAM_BOT, username_customer=username, subscription=SUBSCRIPTION_STATUS_FOR_EACH)
                    
                    #Графический дизайн
                    await filtering_messages_by_category(category_name='Графический дизайн', message=message_text,
                                                        keywords=KEYWORD_GRAFDESIGN, exceptons=EXCEPTONS_GRAFDESIGN,
                                                        client_list=GRAFDESIGN_CLIENTS, bot=TELEGRAM_BOT, username_customer=username, subscription=SUBSCRIPTION_STATUS_FOR_EACH)
                    
                    #Копирайтер
                    await filtering_messages_by_category(category_name='Копирайтер', message=message_text,
                                                        keywords=KEYWORD_COPIRATE, exceptons=EXCEPTONS_COPIRATE,
                                                        client_list=COPIRATE_CLIENTS, bot=TELEGRAM_BOT, username_customer=username, subscription=SUBSCRIPTION_STATUS_FOR_EACH)

                    #Сайты
                    await filtering_messages_by_category(category_name='Сайты', message=message_text,
                                                        keywords=KEYWORD_SITE, exceptons=EXCEPTONS_SITE,
                                                        client_list=SITE_CLIENTS, bot=TELEGRAM_BOT, username_customer=username, subscription=SUBSCRIPTION_STATUS_FOR_EACH)

                    #Таргет
                    await filtering_messages_by_category(category_name='Таргет', message=message_text,
                                                        keywords=KEYWORD_TARGET, exceptons=EXCEPTONS_TARGET,
                                                        client_list=TARGET_CLIENTS, bot=TELEGRAM_BOT, username_customer=username, subscription=SUBSCRIPTION_STATUS_FOR_EACH)
                    
                    #Тех-спец
                    await filtering_messages_by_category(category_name='Тех-спец', message=message_text,
                                                        keywords=KEYWORD_TEHSPEC, exceptons=EXCEPTONS_TEHSPEC,
                                                        client_list=TEHSPEC_CLIENTS, bot=TELEGRAM_BOT, username_customer=username, subscription=SUBSCRIPTION_STATUS_FOR_EACH)

    except (ChatNotFound, aiogram.utils.exceptions.BotBlocked, BadRequest, AttributeError) as a:
        print(a, "324 строка")



#Функция которая смотрит подходит ли вакансия для какой-то категории. 
#Если подходит то отправляет эту вакансию пользователям

async def filtering_messages_by_category(category_name, message: str, keywords: list, exceptons: list, client_list: list, \
                                        bot, username_customer, subscription: dict):
    try:
        
        for word_ex in exceptons:
            
            if re.search(rf"{word_ex}", message.lower()):
                return False

        for word_key in keywords: 
            if re.search(rf"\b{word_key}\b", message.lower()):
                await send_message_bot(message, category_name, client_list, bot, username=username_customer,subscription_status_all_users=subscription)
                return True
                
                
    except AttributeError as e:
        print(f"Функция filtering_messages_by_category. Ошибка: {e}")

async def send_message_bot(message, category_name, user_list, bot, username, subscription_status_all_users: dict):
    global SUBSCRIPTION_STATUS_FOR_EACH
    # Создание сообщения
    
    keyboard_subscribe_true = create_keyboard(user=username, link="https://t.me/")
    keyboard_subscribe_false = create_keyboard(user="RubyStar_bot", link="https://t.me/")

    message_false = message
    message_false = re.sub(r'@\w+', '', message_false)
    message_false = re.sub(r'http\S+|www\S+', '', message_false)

    finish_message_subscribe_true = f"Категория: {category_name}\n\nОтправитель: @{username}\n\nСообщение от клиента:\n\n{message}\n\n------------------\nПолучите самые актуальные предложения для фрилансеров всего за 1000 рублей в месяц на RubyStar Bot. Этот бот специально разработан для поиска заказов, подходящих вашим специализациям и интересам - https://t.me/RubyStar_bot\n------------------"
    finish_message_subscribe_false = f"Категория: {category_name}\n\nОтправитель: Чтобы узнать, нужно оплатить подписку @RubyStar_bot\n\nСообщение от клиента:\n\n{message_false}\n\n------------------\nПолучите самые актуальные предложения для фрилансеров всего за 1000 рублей в месяц на RubyStar Bot. Этот бот специально разработан для поиска заказов, подходящих вашим специализациям и интересам - https://t.me/RubyStar_bot\n------------------"

    print(username)
    for user_id in user_list:
        print("ЭТО ЮЗЕР ИД", user_id)
        if SUBSCRIPTION_STATUS_FOR_EACH[str(user_id)] == "TRUE":
            try:
                await bot.send_message(chat_id=user_id, text=finish_message_subscribe_true, reply_markup=keyboard_subscribe_true)
            except (ChatNotFound, aiogram.utils.exceptions.BotBlocked, AttributeError) as er:
                print(er, "412 строка", user_id)
                continue
        else:
            print(user_id, "ПОДПИСКИ НЕТ")
            try:
                await bot.send_message(chat_id=user_id, text=finish_message_subscribe_false, reply_markup=keyboard_subscribe_false)
            except (ChatNotFound, aiogram.utils.exceptions.BotBlocked, AttributeError) as er:
                print(er, "418 строка", user_id)
                continue

    return True


def create_keyboard(user, link):
    # Создание клавиатуры
        keyboard = types.InlineKeyboardMarkup()
        #print("Сообщение отправляется", message)

        # Создание кнопки со ссылкой на пользователя
        button_text = "🍒Перейти к пользователю"
        user_url = f"{link}{user}"
        button = types.InlineKeyboardButton(text=button_text, url=user_url)

        # Добавление кнопки в клавиатуру
        keyboard.add(button)
        return keyboard

app.run()
