import os

# Проверить наличие файла 'keyword.json'
if not os.path.isfile('keyword.json'):
    # Если файла нет, создать его
    open('keyword.json', 'a').close()

# Проверить наличие файла 'clients.json'
if not os.path.isfile('clients.json'):
    # Если файла нет, создать его
    open('clients.json', 'a').close()
