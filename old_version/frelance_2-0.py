import re
import asyncio
import logging
from google.oauth2.service_account import Credentials
import gspread
from aiogram import Bot
from pyrogram import Client, filters


# Define global variables for clients
CLIENT_LISTS = {
    "SMM": [],
    "Авито": [],
    "Ассистент": [],
    "Бухгалтерия": [],
    "Графический дизайн": [],
    "Копирайт": [],
    "Сайты": [],
    "Таргет": [],
    "Чат-боты": [],
    "Тех-спец": []
}

# Define global variables for keywords and exceptions
KEYWORDS_EXCEPTIONS = {
    "SMM": ([], []),
    "Авито": ([], []),
    "Ассистент": ([], []),
    "Бухгалтерия": ([], []),
    "Графический дизайн": ([], []),
    "Копирайт": ([], []),
    "Сайты": ([], []),
    "Таргет": ([], []),
    "Чат-боты": ([], []),
    "Тех-спец": ([], [])
}


def sheet_open():
    """
    Open a Google Spreadsheet using service account
    """
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    creds = Credentials.from_service_account_file(filename='savvy-temple-380003-e855ebfc1557.json', scopes=scopes)
    client = gspread.authorize(creds)

    return client


def get_column_data(list_name: str, col: int):
    """
    Get all the values from a specific column in a Google Spreadsheet
    """
    sheet = sheet_open().open('Фриланс заказы | Асхаб').worksheet(list_name)
    column_data = sheet.col_values(col)
    return column_data


API_TOKEN_BOT = '6201167294:AAG_bC1dDYSvN4PxblRbFfR22zmzcZfjymg'
bot = Bot(token=API_TOKEN_BOT)

# User bot settings
api_id = "16040522"
api_hash = "49e800b2772a1c33b6b16a785a38431d"
chat_id = "-1001786162328"
app = Client("my_account", api_id=api_id, api_hash=api_hash)


@app.on_message(filters.text & filters.regex(r"Асхаб Алхазуров 2003"))
def update_clients(client, message):
    """
    Update the list of clients for each category from the Google Spreadsheet
    """
    for category_name in CLIENT_LISTS.keys():
        CLIENT_LISTS[category_name] = get_column_data(list_name=category_name, col=2)
    
    message_text = "\n".join([f"{name}_CLIENTS - {clients}" for name, clients in CLIENT_LISTS.items()])
    app.send_message(chat_id=int(chat_id), text=message_text)


@app.on_message(filters.text & filters.regex(r"Обновить ключевые слова Асхаб Алхазуров"))
def update_keywords(client, message):
    """
    Update the list of keywords and exceptions for each category from the Google Spreadsheet
    """
    for category_name in KEYWORDS_EXCEPTIONS.keys():
        # Getting keywords and exceptions from the Google Spreadsheet
        keywords = get_column_data(list_name=category_name, col=3)
        exceptions = get_column_data(list_name=category_name, col=4)
        
        # Parsing keywords and exceptions
        keywords = [word for word in keywords if word.strip()]
        exceptions = [word for word in exceptions if word.strip()]
        
        KEYWORDS_EXCEPTIONS[category_name] = (keywords, exceptions)
    
    message_text = "\n".join([f"{name}_KEYWORDS - {keywords}\n{name}_EXCEPTIONS - {exceptions}" 
                              for name, (keywords, exceptions) in KEYWORDS_EXCEPTIONS.items()])
    app.send_message(chat_id=int(chat_id), text=message_text)


@app.on_message(filters.chat(chat_id))
async def reply(client, message):
    """
    Respond to each message with a specified reply for each category
    """
    for category_name in CLIENT_LISTS.keys():
        clients = CLIENT_LISTS[category_name]
        keywords, exceptions = KEYWORDS_EXCEPTIONS[category_name]
        
        if any(re.search(keyword, message.text.lower()) for keyword in keywords) and not any(
            re.search(exception, message.text.lower()) for exception in exceptions):
            for client_name in clients:
                await bot.send_message(chat_id=client_name, text=message.text.markdown)


app.run()