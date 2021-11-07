# vragen die er niet toe doen
# # v11 = input("wat is uw voornaam")
# # v12 = input("wat is uw achternaam?")
# v13 = input("wat is uw leeftijd?")
# v14 = input("bent u een dierenvriend?")
# vragen die er wel toe doen
# v1 = input("heeft u praktijdervaring met dieren-dressuur, jongleren of acrobatiek?")
# v2 = input("hoeveel jaar ervaring heeft u met dieren-dressuur?")
# v3 = input("hoeveel jaar ervaring heeft u met jongleren?")
# v4 = input("hoeveel jaar ervaring heeft u met acrobatiek?")
# v5 = input("heeft u een MBO diploma ondernemen?")
# v6 = input("heeft u een geldig Vrachtwagen rijbewijs?")
# v7 = input("bent u in bezit van een hoge hoed?")
# v8 = input("bent u een man of vrouw?")
# v9 = input("hoeveel centimeter is uw snor?")
# v10 = input("hoeveel centimeter is uw krulhaar?")
# v11 = input("hoeveel centimeter lang bent u?")
# v12 = input("hoeveel weegt u in hele kilo's?")
# v13 = input("heeft u het Certificaat “Overleven met gevaarlijk personeel”?")


v14 = input("wat is uw voornaam")
v15 = input("wat is uw achternaam?")
v16 = input("wat is uw leeftijd?")
v17 = input("bent u een dierenvriend?")

v1 = input("heeft u praktijdervaring met dieren-dressuur, jongleren of acrobatiek?")
if v1 == "ja":
    v2 = input("hoeveel jaar ervaring heeft u met dieren-dressuur?")
    if v2 >= "4": 
        v5 = input("heeft u een MBO diploma ondernemen?")
        if v5 == "ja":
            v6 = input("heeft u een geldig Vrachtwagen rijbewijs?")
            if v6 == "ja":
                v7 = input("bent u in bezit van een hoge hoed?")
                if v7 == "ja":
                    v8 = input("bent u een man of vrouw?")
                    if v8 == "man":
                        v9 = input("hoeveel centimeter breed is uw snor?")
                        if v9 >= "10":
                            v11 = input("hoeveel centimeter lang bent u?")
                            if v11 >= "150":
                                v12 = input("hoeveel weegt u in hele kilo's?")
                                if v12 >="90":
                                    v13 = input("heeft u het Certificaat “Overleven met gevaarlijk personeel”?")
                                    if v13 == "ja":
                                        print("U bent geschikt voor de baan")
                                    else:
                                        print("Sorry, u bent niet geschikt voor deze baan")



                                else:
                                    print("Sorry, u bent niet geschikt voor deze baan")

                            else:
                                print("Sorry, u bent niet geschikt voor deze baan")

                        else:
                            print("Sorry, u bent niet geschikt voor deze baan")
                    else:
                        v10 = input("hoeveel centimeter is uw krulhaar?")
                        if v10 >= "20":
                            v11 = input("hoeveel centimeter lang bent u?")
                            if v11 >= "150":
                                v12 = input("hoeveel weegt u in hele kilo's?")
                                if v12 >= "90":
                                    v13 = input("heeft u het Certificaat “Overleven met gevaarlijk personeel”?")
                                    if v13 == "ja":
                                        print("U bent geschikt voor de baan")
                                    else:
                                        print("Sorry, u bent niet geschikt voor deze baan")



                                else: 
                                    print("Sorry, u bent niet geschikt voor deze baan")
                            else: 
                                print("Sorry, u bent niet geschikt voor deze baan")



                        else: 
                            print("Sorry, u bent niet geschikt voor deze baan")
                else:
                    print("Sorry, u bent niet geschikt voor deze baan")
            else: 
                print("Sorry, u bent niet geschikt voor deze baan")
        else: 
            print("Sorry, u bent niet geschikt voor deze baan")














    else:
        v3 = input("hoeveel jaar ervaring heeft u met jongleren?")
        if v3 >= "5": 
            v5 = input("heeft u een MBO diploma ondernemen?")
        else:
            v4 = input("hoeveel jaar ervaring heeft u met acrobatiek?")
            if v4 >= "3":
                v5 = input("heeft u een MBO diploma ondernemen?")
            else: 
                print("Sorry, u bent niet geschikt voor deze baan")

else: 
    print("Sorry, u bent niet geschikt voor deze baan")





print(v14)
print(v15)
print(v16)
print(v17)

print(v1)
print(v2)
print(v3)
print(v4)
print(v5)
print(v6)
print(v7)
print(v8)
print(v9)
print(v10)
print(v11)
print(v12)
print(v13)

