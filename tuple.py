a = int(input(''' quyidagilardan birini tanlang:
    1, 2   
    '''))
lugat = {
    "O'quvchi1":{
        "ism": "Dilshod",
        "yosh": 18,
    },
    "O'quvchi2":{
        "ism": "Dilshoda",
        "yosh": 18,
    }
}

if a == 1:
    print(lugat["O'quvchi1"])
elif a == 2:
    print(lugat["O'quvchi2"])