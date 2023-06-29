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

# Функция для добавления данных в формате JSON в файл
def add_json_in_file(file_name: str, data, folder_name: str = 'ubuntu2'):
    try:
        # Проверка существования директории
        if not os.path.isdir(folder_name):
            # Создание директории, если она не существует
            os.mkdir(folder_name)

        # Открытие файла для записи данных. Используется кодировка utf-8
        with open(os.path.join(folder_name, file_name), 'w', encoding='utf-8') as f:
            # Запись данных в файл в формате JSON с отступами (indent=4)
            # Параметр ensure_ascii=False гарантирует, что символы, которые не являются ASCII,
            # будут записаны как есть, а не преобразованы в последовательности escape.
            json.dump(data, f, ensure_ascii=False, indent=4)

        # Возврат True, если файл был успешно записан
        return True
    except Exception as e:
        # Вывод информации об ошибке, если она произошла
        print(f"An error occurred: {e}")

        # Возврат False, если произошла ошибка
        return False
    


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
api_id = "14784408"
api_hash = "82bc0317e29988a8afb596880a99793e"
chat_id = "-1001786162328"
app = Client("my_account", api_id=api_id, api_hash=api_hash)

def update_clients():
    global SMM_CLIENTS, AVITO_CLIENTS, ASSISTANT_CLIENTS, BUHGALTER_CLIENTS, GRAFDESIGN_CLIENTS, \
            COPIRATE_CLIENTS, SITE_CLIENTS, TARGET_CLIENTS, CHATBOTS_CLIENTS, TEHSPEC_CLIENTS, SUBSCRIPTION_STATUS, \
            PLATFORM_ID, SUBSCRIPTION_STATUS_FOR_EACH
    
    print("Обновить список клиентов Асхаб Алхазуров")

    app.send_message(chat_id=int(chat_id), text="Обновление списка клиентов - 0%") 

    result_get_data_sheet = get_column_data(list_name="Общие")
    

    SMM_CLIENTS = [item['SMM'] for item in filter(lambda item: item["SMM"] != 0 and item["SMM"] != '', result_get_data_sheet)]
    AVITO_CLIENTS = [item['Авито'] for item in filter(lambda item: item["Авито"] != 0 and item["Авито"] != '', result_get_data_sheet)]
    ASSISTANT_CLIENTS = [item['Ассистент'] for item in filter(lambda item: item["Ассистент"] != 0 and item["Ассистент"] != '', result_get_data_sheet)]
    BUHGALTER_CLIENTS = [item['Бухгалтерия'] for item in filter(lambda item: item["Бухгалтерия"] != 0 and item["Бухгалтерия"] != '', result_get_data_sheet)]
    GRAFDESIGN_CLIENTS = [item['Графический дизайн'] for item in filter(lambda item: item["Графический дизайн"] != 0 and item["Графический дизайн"] != '', result_get_data_sheet)]
    COPIRATE_CLIENTS = [item['Копирайт'] for item in filter(lambda item: item["Копирайт"] != 0 and item["Копирайт"] != '', result_get_data_sheet)]
    SITE_CLIENTS = [item['Сайты'] for item in filter(lambda item: item["Сайты"] != 0 and item["Сайты"] != '', result_get_data_sheet)]
    TARGET_CLIENTS = [item['Таргет'] for item in filter(lambda item: item["Таргет"] != 0 and item["Таргет"] != '', result_get_data_sheet)]
    CHATBOTS_CLIENTS = [item['Чат-боты'] for item in filter(lambda item: item["Чат-боты"] != 0 and item["Чат-боты"] != '', result_get_data_sheet)]    
    TEHSPEC_CLIENTS = [item['Тех-спец'] for item in filter(lambda item: item["Тех-спец"] != 0 and item["Тех-спец"] != '', result_get_data_sheet)]
    SUBSCRIPTION_STATUS = [item['Подписка (Ложь если нет)'] for item in filter(lambda item: item["Подписка (Ложь если нет)"] != 0 and item["Подписка (Ложь если нет)"] != '', result_get_data_sheet)]   
    PLATFORM_ID = [item['platform_id'] for item in filter(lambda item: item["platform_id"] != 0 and item["platform_id"] != '', result_get_data_sheet)]   
    SUBSCRIPTION_STATUS_FOR_EACH = dict(zip(PLATFORM_ID, SUBSCRIPTION_STATUS))

    clients_dict = {
        "smm_clients": SMM_CLIENTS,
        "avito_clients": AVITO_CLIENTS,
        "assistant_clients": ASSISTANT_CLIENTS,
        "buhgalter_clients": BUHGALTER_CLIENTS,
        "grafdesign_clients": GRAFDESIGN_CLIENTS,
        "copirate_clients": COPIRATE_CLIENTS,
        "site_clients": SITE_CLIENTS,
        "target_clients": SITE_CLIENTS,
        "chatbots_clients": CHATBOTS_CLIENTS,
        "tehspec_clients": TEHSPEC_CLIENTS,
        "subscription_status": SUBSCRIPTION_STATUS,
        "platform_id": PLATFORM_ID,
        "subscription_status_for_each": SUBSCRIPTION_STATUS_FOR_EACH
        }
    print(clients_dict)
    #Добавления словаря clients_dict в файл clients.json в папке ubuntu2
    result_add_json_file = add_json_in_file(file_name='clients.json', data=clients_dict, folder_name='ubuntu2')

    print(f"Авито - {AVITO_CLIENTS}\n\nSMM - {SMM_CLIENTS}")
    print(f"Ассистент - {ASSISTANT_CLIENTS}\n\nБухгалтер - {BUHGALTER_CLIENTS}")
    print(f"Графический дизайн - {GRAFDESIGN_CLIENTS}\n\nКопирайтер - {COPIRATE_CLIENTS}")
    print(f"Сайт - {SITE_CLIENTS}\n\nТаргет - {TARGET_CLIENTS}")
    print(f"Чат-боты - {CHATBOTS_CLIENTS}\n\nТех-спец - {TEHSPEC_CLIENTS}")
    print(SUBSCRIPTION_STATUS_FOR_EACH)



def update_keyword_exceptons():
    global KEYWORD_SMM, EXCEPTONS_SMM, KEYWORD_AVITO, EXCEPTONS_AVITO, KEYWORD_ASSISTANT, \
            EXCEPTONS_ASSISTANT, KEYWORD_BUHGALTER, EXCEPTONS_BUHGALTER, KEYWORD_GRAFDESIGN, \
            EXCEPTONS_GRAFDESIGN, KEYWORD_COPIRATE, EXCEPTONS_COPIRATE, KEYWORD_SITE, EXCEPTONS_SITE, \
            KEYWORD_TARGET, EXCEPTONS_TARGET, KEYWORD_CHATBOTS, EXCEPTONS_CHATBOTS, KEYWORD_TEHSPEC, EXCEPTONS_TEHSPEC, \
            EXCEPTONS_USERNAME, GENERAL_FILTER_EXCEPTONS, SUBSCRIPTION_STATUS, PLATFORM_ID, SUBSCRIPTION_STATUS_FOR_EACH
    
    print("Обновить ключевые слова Асхаб Алхазуров")


    #app.send_message(chat_id=int(chat_id), text="Обновление ключевых слов - 0%")

    result_get_data_sheet = get_column_data(list_name="Фильтр")

    KEYWORD_SMM = [item['Ключевые слова SMM'] for item in filter(lambda item: item["Ключевые слова SMM"] != 0 and item["Ключевые слова SMM"] != '', result_get_data_sheet)]
    EXCEPTONS_SMM = [item['Слова исключения SMM'] for item in filter(lambda item: item["Слова исключения SMM"] != 0 and item["Слова исключения SMM"] != '', result_get_data_sheet)]

    KEYWORD_AVITO = [item['Ключевые слова Авито'] for item in filter(lambda item: item["Ключевые слова Авито"] != 0 and item["Ключевые слова Авито"] != '', result_get_data_sheet)]
    EXCEPTONS_AVITO = [item['Слова исключения Авито'] for item in filter(lambda item: item["Слова исключения Авито"] != 0 and item["Слова исключения Авито"] != '', result_get_data_sheet)]

    KEYWORD_ASSISTANT = [item['Ключевые слова Ассистент'] for item in filter(lambda item: item["Ключевые слова Ассистент"] != 0 and item["Ключевые слова Ассистент"] != '', result_get_data_sheet)]
    EXCEPTONS_ASSISTANT = [item['Слова исключения Ассистент'] for item in filter(lambda item: item["Слова исключения Ассистент"] != 0 and item["Слова исключения Ассистент"] != '', result_get_data_sheet)]

    KEYWORD_BUHGALTER = [item['Ключевые слова Бухгалтерия'] for item in filter(lambda item: item["Ключевые слова Бухгалтерия"] != 0 and item["Ключевые слова Бухгалтерия"] != '', result_get_data_sheet)]
    EXCEPTONS_BUHGALTER = [item['Слова исключения Бухгалтерия'] for item in filter(lambda item: item["Слова исключения Бухгалтерия"] != 0 and item["Слова исключения Бухгалтерия"] != '', result_get_data_sheet)]

    KEYWORD_GRAFDESIGN = [item['Ключевые слова Графический дизайн'] for item in filter(lambda item: item["Ключевые слова Графический дизайн"] != 0 and item["Ключевые слова Графический дизайн"] != '', result_get_data_sheet)]
    EXCEPTONS_GRAFDESIGN = [item['Слова исключения Графический дизайн'] for item in filter(lambda item: item["Слова исключения Графический дизайн"] != 0 and item["Слова исключения Графический дизайн"] != '', result_get_data_sheet)]

    KEYWORD_COPIRATE = [item['Ключевые слова Копирайт'] for item in filter(lambda item: item["Ключевые слова Копирайт"] != 0 and item["Ключевые слова Копирайт"] != '', result_get_data_sheet)]
    EXCEPTONS_COPIRATE = [item['Слова исключения Копирайт'] for item in filter(lambda item: item["Слова исключения Копирайт"] != 0 and item["Слова исключения Копирайт"] != '', result_get_data_sheet)]

    KEYWORD_SITE = [item['Ключевые слова Сайты'] for item in filter(lambda item: item["Ключевые слова Сайты"] != 0 and item["Ключевые слова Сайты"] != '', result_get_data_sheet)]
    EXCEPTONS_SITE = [item['Слова исключения Сайты'] for item in filter(lambda item: item["Слова исключения Сайты"] != 0 and item["Слова исключения Сайты"] != '', result_get_data_sheet)]

    KEYWORD_TARGET = [item['Ключевые слова Таргет'] for item in filter(lambda item: item["Ключевые слова Таргет"] != 0 and item["Ключевые слова Таргет"] != '', result_get_data_sheet)]
    EXCEPTONS_TARGET = [item['Слова исключения Таргет'] for item in filter(lambda item: item["Слова исключения Таргет"] != 0 and item["Слова исключения Таргет"] != '', result_get_data_sheet)]

    KEYWORD_CHATBOTS = [item['Ключевые слова Чат-боты'] for item in filter(lambda item: item["Ключевые слова Чат-боты"] != 0 and item["Ключевые слова Чат-боты"] != '', result_get_data_sheet)]
    EXCEPTONS_CHATBOTS = [item['Слова исключения Чат-боты'] for item in filter(lambda item: item["Слова исключения Чат-боты"] != 0 and item["Слова исключения Чат-боты"] != '', result_get_data_sheet)]

    KEYWORD_TEHSPEC = [item['Ключевые слова Тех-спец'] for item in filter(lambda item: item["Ключевые слова Тех-спец"] != 0 and item["Ключевые слова Тех-спец"] != '', result_get_data_sheet)]
    EXCEPTONS_TEHSPEC = [item['Слова исключения Тех-спец'] for item in filter(lambda item: item["Слова исключения Тех-спец"] != 0 and item["Слова исключения Тех-спец"] != '', result_get_data_sheet)]
    
    EXCEPTONS_USERNAME = [item['Исключения отправители'] for item in filter(lambda item: item["Исключения отправители"] != 0 and item["Исключения отправители"] != '', result_get_data_sheet)]

    GENERAL_FILTER_EXCEPTONS = [item['Общий фильр'] for item in filter(lambda item: item["Общий фильр"] != 0 and item["Общий фильр"] != '', result_get_data_sheet)]

    app.send_message(chat_id=int(chat_id), text="Обновление ключевых слов - 100%")
    
    keywords_and_exceptons_dict = {
        "Ключевые слова SMM": KEYWORD_SMM, "Слова исключения SMM": EXCEPTONS_SMM,
        "Ключевые слова Авито": KEYWORD_AVITO, "Слова исключения Авито": EXCEPTONS_AVITO,
        "Ключевые слова Ассистент": KEYWORD_ASSISTANT, "Слова исключения Ассистент": EXCEPTONS_AVITO,
        "Ключевые слова Бухгалтерия": KEYWORD_BUHGALTER, "Слова исключения Бухгалтерия": EXCEPTONS_BUHGALTER,
        "Ключевые слова Графический дизайн": KEYWORD_GRAFDESIGN, "Слова исключения Графический дизайн": EXCEPTONS_GRAFDESIGN,
        "Ключевые слова Копирайт": KEYWORD_COPIRATE, "Слова исключения Копирайт": EXCEPTONS_COPIRATE,
        "Ключевые слова Сайты": KEYWORD_SITE, "Слова исключения Сайты": EXCEPTONS_SITE,
        "Ключевые слова Таргет": KEYWORD_TARGET, "Слова исключения Таргет": EXCEPTONS_TARGET,
        "Ключевые слова Чат-боты": KEYWORD_CHATBOTS, "Слова исключения Чат-боты": EXCEPTONS_CHATBOTS,
        "Ключевые слова Тех-спец": KEYWORD_TEHSPEC, "Слова исключения Тех-спец": EXCEPTONS_TEHSPEC,
        "Исключения отправители": EXCEPTONS_USERNAME, 
        "Общий фильр": GENERAL_FILTER_EXCEPTONS,
        }
    #Добавления словаря clients_dict в файл keyword.json в папке ubuntu2
    result_add_json_file = add_json_in_file(file_name='keyword.json', data=keywords_and_exceptons_dict, folder_name='ubuntu2')

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


def general_filter(mes):
    global GENERAL_FILTER_EXCEPTONS

    for word_exceptons in GENERAL_FILTER_EXCEPTONS:

        if re.search(rf"{word_exceptons}", mes.lower()):
            return False

    return True


@app.on_message(filters.text & filters.regex(r"\bОбновить список клиентов\b"))
def message_text(client, message):
    update_clients()
    

@app.on_message(filters.text & filters.regex(r"\bОбновить ключевые слова\b"))
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
