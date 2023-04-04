def converter():
    req1 = input("Введите евро или рубли ")
    req2 = int(input("Введите количество долларов "))
    ed = req2*0.916
    rd = req2*77.95
    if req1 == "евро":
        print(ed)
    else:
        print(rd)




