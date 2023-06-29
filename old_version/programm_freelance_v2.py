import asyncio
import aiogram
import gspread
import logging
import re
from pyrogram import Client, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from aiogram import Bot
from aiogram.utils.exceptions import ChatNotFound
from aiogram import types
from google.oauth2.service_account import Credentials



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
#Фильтры


@api_view(['GET'])
def get_data(request):
    data = {"key": "value"}  # здесь может быть любая логика, возвращающая данные
    return Response(data)


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
api_id = "16040522"
api_hash = "49e800b2772a1c33b6b16a785a38431d"
chat_id = "-1001786162328"
app = Client("my_account", api_id=api_id, api_hash=api_hash)

def update_clients():
    global SMM_CLIENTS, AVITO_CLIENTS, ASSISTANT_CLIENTS, BUHGALTER_CLIENTS, GRAFDESIGN_CLIENTS, \
            COPIRATE_CLIENTS, SITE_CLIENTS, TARGET_CLIENTS, CHATBOTS_CLIENTS, TEHSPEC_CLIENTS
    
    print("Обновить список клиентов Асхаб Алхазуров")

    app.send_message(chat_id=int(chat_id), text="Обновление списка клиентов - 0%") 

    result_get_data_sheet = get_column_data(list_name="Общие")

    SMM_CLIENTS = [item['SMM'] for item in result_get_data_sheet if item['SMM'] != 0 and item['SMM'] != '']

    AVITO_CLIENTS = [item['Авито'] for item in result_get_data_sheet if item['Авито'] != 0 and item['Авито'] != '']

    ASSISTANT_CLIENTS = [item['Ассистент'] for item in result_get_data_sheet if item['Ассистент'] != 0 and item['Ассистент'] != '']
 

    BUHGALTER_CLIENTS = [item['Бухгалтерия'] for item in result_get_data_sheet if item['Бухгалтерия'] != 0 and item['Бухгалтерия'] != '']

    GRAFDESIGN_CLIENTS = [item['Графический дизайн'] for item in result_get_data_sheet if item['Графический дизайн'] != 0 and item['Графический дизайн'] != '']

    COPIRATE_CLIENTS = [item['Копирайт'] for item in result_get_data_sheet if item['Копирайт'] != 0 and item['Копирайт'] != '']


    SITE_CLIENTS = [item['Сайты'] for item in result_get_data_sheet if item['Сайты'] != 0 and item['Сайты'] != '']

    TARGET_CLIENTS = [item['Таргет'] for item in result_get_data_sheet if item['Таргет'] != 0 and item['Таргет'] != '']


    CHATBOTS_CLIENTS = [item['Чат-боты'] for item in result_get_data_sheet if item['Чат-боты'] != 0 and item['Чат-боты'] != '']
    
    TEHSPEC_CLIENTS = [item['Тех-спец'] for item in result_get_data_sheet if item['Тех-спец'] != 0 and item['Тех-спец'] != '']
       

   
    # app.send_message(chat_id=int(chat_id), text=f"Авито - {AVITO_CLIENTS}\n\nSMM - {SMM_CLIENTS}")
    # app.send_message(chat_id=int(chat_id), text=f"Ассистент - {ASSISTANT_CLIENTS}\n\nБухгалтер - {BUHGALTER_CLIENTS}")
    # app.send_message(chat_id=int(chat_id), text=f"Графический дизайн - {GRAFDESIGN_CLIENTS}\n\nКопирайтер - {COPIRATE_CLIENTS}")
    # app.send_message(chat_id=int(chat_id), text=f"Сайт - {SITE_CLIENTS}\n\nТаргет - {TARGET_CLIENTS}")
    app.send_message(chat_id=int(chat_id), text=f"Чат-боты - {CHATBOTS_CLIENTS}\n\nТех-спец - {TEHSPEC_CLIENTS}")

def update_keyword_exceptons():
    global KEYWORD_SMM, EXCEPTONS_SMM, KEYWORD_AVITO, EXCEPTONS_AVITO, KEYWORD_ASSISTANT, \
            EXCEPTONS_ASSISTANT, KEYWORD_BUHGALTER, EXCEPTONS_BUHGALTER, KEYWORD_GRAFDESIGN, \
            EXCEPTONS_GRAFDESIGN, KEYWORD_COPIRATE, EXCEPTONS_COPIRATE, KEYWORD_SITE, EXCEPTONS_SITE, \
            KEYWORD_TARGET, EXCEPTONS_TARGET, KEYWORD_CHATBOTS, EXCEPTONS_CHATBOTS, KEYWORD_TEHSPEC, EXCEPTONS_TEHSPEC
    
    print("Обновить ключевые слова Асхаб Алхазуров")


    app.send_message(chat_id=int(chat_id), text="Обновление ключевых слов - 0%")

    result_get_data_sheet = get_column_data(list_name="Фильтр")

    KEYWORD_SMM = [item['Ключевые слова SMM'] for item in result_get_data_sheet if item['Ключевые слова SMM'] != ""]
    EXCEPTONS_SMM = [item['Слова исключения SMM'] for item in result_get_data_sheet if item['Слова исключения SMM'] != ""]
    app.send_message(chat_id=int(chat_id), text="Обновление ключевых слов - 10%")

    KEYWORD_AVITO = [item['Ключевые слова Авито'] for item in result_get_data_sheet if item['Ключевые слова Авито'] != ""]
    EXCEPTONS_AVITO = [item['Слова исключения Авито'] for item in result_get_data_sheet if item['Слова исключения Авито'] != ""]

    KEYWORD_ASSISTANT = [item['Ключевые слова Ассистент'] for item in result_get_data_sheet if item['Ключевые слова Ассистент'] != ""]
    EXCEPTONS_ASSISTANT= [item['Слова исключения Ассистент'] for item in result_get_data_sheet if item['Слова исключения Ассистент'] != ""]


    KEYWORD_BUHGALTER = [item['Ключевые слова Бухгалтерия'] for item in result_get_data_sheet if item['Ключевые слова Бухгалтерия'] != ""]
    EXCEPTONS_BUHGALTER = [item['Слова исключения Бухгалтерия'] for item in result_get_data_sheet if item['Слова исключения Бухгалтерия'] != ""]

    KEYWORD_GRAFDESIGN = [item['Ключевые слова Графический дизайн'] for item in result_get_data_sheet if item['Ключевые слова Графический дизайн'] != ""]
    EXCEPTONS_GRAFDESIGN = [item['Слова исключения Графический дизайн'] for item in result_get_data_sheet if item['Слова исключения Графический дизайн'] != ""]


    KEYWORD_COPIRATE = [item['Ключевые слова Копирайт'] for item in result_get_data_sheet if item['Ключевые слова Копирайт'] != ""]
    EXCEPTONS_COPIRATE = [item['Слова исключения Копирайт'] for item in result_get_data_sheet if item['Слова исключения Копирайт'] != ""]

    KEYWORD_SITE = [item['Ключевые слова Сайты'] for item in result_get_data_sheet if item['Ключевые слова Сайты'] != ""]
    EXCEPTONS_SITE = [item['Слова исключения Сайты'] for item in result_get_data_sheet if item['Слова исключения Сайты'] != ""]


    KEYWORD_TARGET = [item['Ключевые слова Таргет'] for item in result_get_data_sheet if item['Ключевые слова Таргет'] != ""]
    EXCEPTONS_TARGET = [item['Слова исключения Таргет'] for item in result_get_data_sheet if item['Слова исключения Таргет'] != ""]

    KEYWORD_CHATBOTS = [item['Ключевые слова Чат-боты'] for item in result_get_data_sheet if item['Ключевые слова Чат-боты'] != ""]
    EXCEPTONS_CHATBOTS = [item['Слова исключения Чат-боты'] for item in result_get_data_sheet if item['Слова исключения Чат-боты'] != ""]
    

    KEYWORD_TEHSPEC = [item['Ключевые слова Тех-спец'] for item in result_get_data_sheet if item['Ключевые слова Тех-спец'] != ""]
    EXCEPTONS_TEHSPEC = [item['Слова исключения Тех-спец'] for item in result_get_data_sheet if item['Слова исключения Тех-спец'] != ""]

    EXCEPTONS_USERNAME = [item['Исключения отправители'] for item in result_get_data_sheet if item['Исключения отправители'] != ""]
    


    # app.send_message(chat_id=int(chat_id), text=f"KEYWORD_SMM - {KEYWORD_SMM}\n\nEXCEPTONS_SMM - {EXCEPTONS_SMM}")
    # app.send_message(chat_id=int(chat_id), text=f"KEYWORD_AVITO - {KEYWORD_AVITO}\n\nEXCEPTONS_AVITO - {EXCEPTONS_AVITO}")
    # app.send_message(chat_id=int(chat_id), text=f"KEYWORD_ASSISTANT - {KEYWORD_ASSISTANT}\n\nEXCEPTONS_ASSISTANT - {EXCEPTONS_ASSISTANT}")
    # app.send_message(chat_id=int(chat_id), text=f"KEYWORD_BUHGALTER - {KEYWORD_BUHGALTER}\n\nEXCEPTONS_BUHGALTER - {EXCEPTONS_BUHGALTER}")
    # app.send_message(chat_id=int(chat_id), text=f"KEYWORD_GRAFDESIGN - {KEYWORD_GRAFDESIGN}\n\nEXCEPTONS_GRAFDESIGN - {EXCEPTONS_GRAFDESIGN}")
    # app.send_message(chat_id=int(chat_id), text=f"KEYWORD_COPIRATE - {KEYWORD_COPIRATE}\n\nEXCEPTONS_COPIRATE - {EXCEPTONS_COPIRATE}")
    # app.send_message(chat_id=int(chat_id), text=f"KEYWORD_SITE - {KEYWORD_SITE}\n\nEXCEPTONS_SITE - {EXCEPTONS_SITE}")
    # app.send_message(chat_id=int(chat_id), text=f"KEYWORD_TARGET - {KEYWORD_TARGET}\n\nEXCEPTONS_TARGET - {EXCEPTONS_TARGET}")
    # app.send_message(chat_id=int(chat_id), text=f"KEYWORD_CHATBOTS - {KEYWORD_CHATBOTS}\n\nEXCEPTONS_CHATBOTS - {EXCEPTONS_CHATBOTS}")
    # app.send_message(chat_id=int(chat_id), text=f"KEYWORD_TEHSPEC - {KEYWORD_TEHSPEC}\n\nEXCEPTONS_TEHSPEC - {EXCEPTONS_TEHSPEC}")
    app.send_message(chat_id=int(chat_id), text=f"EXCEPTONS_USERNAME - {EXCEPTONS_USERNAME}")





@app.on_message(filters.text & filters.regex(r"Обновить список клиентов Асхаб Алхазуров"))
def message_text(client, message):
    update_clients()
    



@app.on_message(filters.text & filters.regex(r"Обновить ключевые слова Асхаб Алхазуров"))
def message_text(client, message):
    update_keyword_exceptons()


@app.on_message(filters.text & ~filters.user("RubyStart_bot"))
async def message_text(client, message):
    global KEYWORD_SMM, EXCEPTONS_SMM, KEYWORD_AVITO, EXCEPTONS_AVITO, KEYWORD_ASSISTANT, \
            EXCEPTONS_ASSISTANT, KEYWORD_BUHGALTER, EXCEPTONS_BUHGALTER, KEYWORD_GRAFDESIGN, \
            EXCEPTONS_GRAFDESIGN, KEYWORD_COPIRATE, EXCEPTONS_COPIRATE, KEYWORD_SITE, EXCEPTONS_SITE, \
            KEYWORD_TARGET, EXCEPTONS_TARGET, KEYWORD_CHATBOTS, EXCEPTONS_CHATBOTS, KEYWORD_TEHSPEC, EXCEPTONS_TEHSPEC, \
            SMM_CLIENTS, AVITO_CLIENTS, ASSISTANT_CLIENTS, BUHGALTER_CLIENTS, GRAFDESIGN_CLIENTS, \
            COPIRATE_CLIENTS, SITE_CLIENTS, TARGET_CLIENTS, CHATBOTS_CLIENTS, TEHSPEC_CLIENTS
    try:
        message_text = message.text
        username = message.from_user.username
        if f"@{username}" not in EXCEPTONS_USERNAME:
            print(EXCEPTONS_USERNAME)
            print(username)
            print(f"@{username}" not in EXCEPTONS_USERNAME)
            print(f"@{username}" in EXCEPTONS_USERNAME)
            #Чат-боты
            await filtering_messages_by_category(category_name='Чат-боты', message=message_text,
                                                keywords=KEYWORD_CHATBOTS, exceptons=EXCEPTONS_CHATBOTS,
                                                client_list=CHATBOTS_CLIENTS,
                                                user_id_customer=username, bot=TELEGRAM_BOT)
            
            #SMM
            await filtering_messages_by_category(category_name='SMM', message=message_text,
                                                keywords=KEYWORD_SMM, exceptons=EXCEPTONS_SMM,
                                                client_list=SMM_CLIENTS,
                                                user_id_customer=username, bot=TELEGRAM_BOT)
            
            #Авито
            await filtering_messages_by_category(category_name='Авито', message=message_text,
                                                keywords=KEYWORD_AVITO, exceptons=EXCEPTONS_AVITO, 
                                                client_list=AVITO_CLIENTS,
                                                user_id_customer=username, bot=TELEGRAM_BOT)
        
            #Ассистент
            await filtering_messages_by_category(category_name='Ассистент', message=message_text,
                                                keywords=KEYWORD_ASSISTANT, exceptons=EXCEPTONS_ASSISTANT,
                                                client_list=ASSISTANT_CLIENTS,
                                                user_id_customer=username, bot=TELEGRAM_BOT)
            
            #Бухгалтер
            await filtering_messages_by_category(category_name='Бухгалтер', message=message_text,
                                                keywords=KEYWORD_BUHGALTER, exceptons=EXCEPTONS_BUHGALTER,
                                                client_list=BUHGALTER_CLIENTS,
                                                user_id_customer=username, bot=TELEGRAM_BOT)
            
            #Графический дизайн
            await filtering_messages_by_category(category_name='Графический дизайн', message=message_text,
                                                keywords=KEYWORD_GRAFDESIGN, exceptons=EXCEPTONS_GRAFDESIGN,
                                                client_list=GRAFDESIGN_CLIENTS,
                                                user_id_customer=username, bot=TELEGRAM_BOT)
            
            #Копирайтер
            await filtering_messages_by_category(category_name='Копирайтер', message=message_text,
                                                keywords=KEYWORD_COPIRATE, exceptons=EXCEPTONS_COPIRATE,
                                                client_list=COPIRATE_CLIENTS,
                                                user_id_customer=username, bot=TELEGRAM_BOT)

            #Сайты
            await filtering_messages_by_category(category_name='Сайты', message=message_text,
                                                keywords=KEYWORD_SITE, exceptons=EXCEPTONS_SITE,
                                                client_list=SITE_CLIENTS,
                                                user_id_customer=username, bot=TELEGRAM_BOT)

            #Таргет
            await filtering_messages_by_category(category_name='Таргет', message=message_text,
                                                keywords=KEYWORD_TARGET, exceptons=EXCEPTONS_TARGET,
                                                client_list=TARGET_CLIENTS,
                                                user_id_customer=username, bot=TELEGRAM_BOT)
            
            #Тех-спец
            await filtering_messages_by_category(category_name='Тех-спец', message=message_text,
                                                keywords=KEYWORD_TEHSPEC, exceptons=EXCEPTONS_TEHSPEC,
                                                client_list=TEHSPEC_CLIENTS,
                                                user_id_customer=username, bot=TELEGRAM_BOT)

        else:
            print(username)
    except AttributeError as a:
        print(a)



    


#Функция которая смотрит подходит ли вакансия для какой-то категории. 
#Если подходит то отправляет эту вакансию пользователям

async def filtering_messages_by_category(category_name, message: str, keywords: list, exceptons: list, client_list: list, user_id_customer, bot):
    try:
        
        for word_ex in exceptons:
            
            if re.search(rf"{word_ex}", message.lower()):
                return False

        for word_key in keywords: 
            if re.search(rf"{word_key}", message.lower()):
 
                #print("Сообщение отправляется")
                await send_message_bot(message, category_name, client_list, user_id_customer, bot)
                return True
                
                
    except AttributeError as e:
        print(f"Функция filtering_messages_by_category. Ошибка: {e}")

async def send_message_bot(message, category_name, user_list, username, bot):
    # Создание клавиатуры
    keyboard = types.InlineKeyboardMarkup()

    # Создание кнопки со ссылкой на пользователя
    button_text = "🍒Перейти к пользователю"
    user_url = f"https://t.me/{username}"
    button = types.InlineKeyboardButton(text=button_text, url=user_url)

    # Добавление кнопки в клавиатуру
    keyboard.add(button)

    # Создание сообщения
    finish_message = f"Категория: {category_name}\n\nОтправитель: @{username}\n\nСообщение от клиента:\n\n{message}\n\n------------------\nПолучите самые актуальные предложения для фрилансеров всего за 500 рублей в месяц на RubyStar Bot. Этот бот специально разработан для поиска заказов, подходящих вашим специализациям и интересам - https://t.me/RubyStar_bot\n------------------"

    # Отправка сообщения каждому пользователю в списке
    for user_id in user_list:
        try:
            await bot.send_message(chat_id=user_id, text=finish_message, reply_markup=keyboard)
        except (ChatNotFound, aiogram.utils.exceptions.BotBlocked) as er:
            print(er)

app.run()
