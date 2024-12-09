import json
count = 0
with open('dump.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
while True:          
    print(" 1 Вывести все записи\n 2 Вывести запись по полю\n 3 Добавить запись\n 4 Удалить запись по полю\n 5 Выйти из программы")
    choise = input("Что выберете? ")

    if choise == "1":
        print("----------Все записи----------")
        for i in data:
            print(f"""Номер цветка: {i["id"]} 
        Название: {i["name"]}
        Латинское название: {i["latin_name"]}
        Краснокнижный цветок? {i["is_red_book_flower"]}
        Цена: {i["price"]} BYN\n""")
        count +=1

    elif choise == "2":
        print("----------Запись по полю----------")
        item = int(input("Введите поле которое вывести "))
        for i, flower in enumerate(data):
            if flower['id'] == item:
                print(f"""Номер цветка: {flower["id"]} 
        Название: {flower["name"]}
        Латинское название: {flower["latin_name"]}
        Краснокнижный цветок? {flower["is_red_book_flower"]}
        Цена: {flower["price"]} BYN\n""")
            else:        
                print(f"Запись с ID {item} не найдена.")
        count +=1
        

    elif choise == "3":
        print("----------Добавить запись----------") 
        newDct = {}
        newDct["id"] = len(data) + 1
        newDct["name"] = input("Введите названия цветка ")
        newDct["latin_name"] = input("Введите латинское имя цветка ")
        newDct["is_red_book_flower"] = input("Введите краснокнижный ли цветок True/False ")
        newDct["price"] = input("Введите цену цветка ")
        data.append(newDct)
        print("----------Запись добавлена----------") 
        count +=1
    elif choise == "4":
        print("----------Удалить запись----------") 
        itemDel = input("Введите поле которое хотите удалить ")
        indexDelete = -1
        for i, item in enumerate(data):
            if item["id"] == indexDelete:
                indexDelete = i
                break
        data.pop(indexDelete)
        print("----------Запись удалена----------") 
        count +=1


    elif choise == "5":
        print("Количество выполненных операций с записями ", count) 
        print("----------Пока----------")
        break 
         
