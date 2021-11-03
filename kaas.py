vraag1 = input("is de kaas geel?")
if vraag1 == "ja": 
    vraag2 = input("zitten er gaten in?")
    if vraag2 == "ja":
        vraag5 = input("is de kaas belachelijk duur?")
        if vraag5 == "ja":
            print("Emmenthaler")
        else:
            print("Leerdammer")
    else:
        vraag6 = input("is de kaas hard als steen?")
        if vraag6 == "ja":
            print("pamigiano Reggiano")
        else: 
            vraag8 = input("is de kaas zilter?")
            if vraag8 == "ja":
                print("milner")
            else: 
                print("Goudse kaas")
else:
    vraag3 = input("heeft de blauwe kaas schimmels?")
    if vraag3 == "ja":
        vraag4 = input("heeft de kaas een korst?")
        if vraag4 == "ja":
            print("Bleu de Rochbaron")
        else:
            print("Foume d'Ambert")
    else: 
        vraag7 = input("heeft de kaas een korst?")
        if vraag7 == "ja":
            print("Camembert")
        else: 
            print("Mozzarella")

        



