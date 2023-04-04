import sys
def converter():
    req1 = input("Введите евро или рубли ")
    if req1 != "рубли" or "евро":
        print("Пожалуйста, следуйте инструкции")
        sys.exit()
    req2 = int(input("Введите количество долларов "))
    ed = req2*0.916
    rd = req2*77.95
    if req1 == "евро":
        print(ed)
    elif req1 == "рубли":
        print(rd)


converter()

