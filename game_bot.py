from random import *
import json
games=[]
games.append("Call of duty")
games.append("Wolfenshtein")
games.append("Mafia")
games.append("Battlefield")
games.append("Stalker")
games.append("Metro")
games.append("God of war")
games.append("The last of us")
games.append("Rezident Evil")
games.append("Tomd Raider")

def save():
    with open("games.json", "w",encoding="utf-8") as fh:
        fh.write(json.dumps(games,ensure_ascii=False))
    print("Ваша игротека была успешно сохранена в файле games.json")

while True:
    command=input("Введите команду:  ")
    if command=="/start":
        print("Игротека начала работу")
    elif command=="/stop":
        print("Бот остановил свою работу, чтобы запустить заново введите команду /start")
        break
    elif command=="/all":
        print("Список игр:")
        print(games)
    elif command=="/add":
        f=input("Введите название игры ")
        games.append(f)
        print("Игра успешно добавлена в коллекцию!")
    elif command=="/help":
        print("/start -запуск бота, /stop - остановка работы бота, /add - добавить игру в коллекцию, /help - ознакомиться со списком доступных команд, /delete - удаление игры из коллекции, /save - сохранение, /random - великое око выберет вам игру")
    elif command=="/delete":

        f=input("Введите название игры, которую удалит бот ")
        if f in games:
            games.remove(f)
            print("Игра была успешна удалена с вашего списка, чтобы снова ее добавить, воспользуйтесь командой /add")
        else:
            print("Такой игры нет в игротеке, изучите список игр, через команду /all")
        try:
                games.remove(f)
                print("Игра была успешно удалена!")
        except:
            print("Такой игры нет в игротеке, изучите список игр, через команду /all")
    elif command=="/random":
        print("Великое око указало на - "+ choice(games))
    elif command=="/save":
        save()
    else:
        print("Неопознанная команда, ознакомтесь со списком команд через /help")

            

 
