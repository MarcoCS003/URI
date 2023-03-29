while True:
    try:
        e = input()
        contador = 0
        for i in e:
            if contador < 0:
                print("incorrect")
                break
            if i == "(":
                contador += 1
            elif i == ")":
                contador -= 1
        else:

            if contador == 0:
                print("correct")
            else:
                print("incorrect")
    except EOFError:
            break