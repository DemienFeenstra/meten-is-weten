pad = input("kies een pad! links of rechts")
if pad == "links":
    print("opdracht: red de prinses en pas op voor de draak!")
    goud = input("je gaat het kasteel in en ziet een kist vol goud ter waarde van 5 miljoen! neem je het mee of laat je het liggen en ga je de prinses zoeken? vul meenemen of laten liggen in!")

    if goud == "meenemen":
        print("de draak werd wakker en roostert je! ververs de pagina om opnieuw te beginnen!")

    elif goud == "laten liggen":
        print("je gaat verder het kasteel in om de prinses te zoeken!")

        val = input("er is een diep gat met lava voor je op je pad! pak je de houten trap en loop je er overheen of klim je via de muur voorzichtig? vul trap of muur in!")
        if val == "trap":
            print("de houten trap vliegt in de fik door de lava dus je valt in de lava! ververs de pagina om op nieuw te beginnen!")

        elif val == "muur":
            print("je klimt voorzichtig via de muur en komt om het gat heen. je hebt de prinses gevonden! ontsnap nu uit het kasteel!")

        zwaard = input(" onderweg naar de uitgang komt de draak achter je aan en je komt een zwaard tegen van 2 meter lang op je pad! pak je het op of laat je het liggen? kies oppakken of laten liggen!")
        if zwaard == "oppakken":
            print("je hebt het zwaard opgepakt en de draak verslagen! ontsnap nu uit het kasteel met de prinses!")

            print("de deur van het kasteel zit op slot met een 2 cijfer code! lees de volgende vragen goed en beantwoord daarna de vragen goed om de code te ontcijferen!")

            print("vraag 1: hoe lang was het zwaard?")

            print("vraag 2: hoeveel miljoen was het goud waard?")

            ontsnappen = input(" vul nu de 2 cijfers van de antwoorden aan elkaar in!")

            if ontsnappen == "25":
                print(" je bent ontsnapt met de prinses! gefeliciteerd je hebt gewonnen en je leeft nog lang en gelukkig met de prinses!")
            else:
                print("je hebt de code niet gekraakt en de draak heeft het gevecht toch net nog overleeft! hij roostert je met zijn laatste vuur adem! ververs de pagina om opnieuw te beginnen!")
        
        elif zwaard == "laten liggen":
            print("je hebt het zwaard niet opgepakt en de draak zet jou en de prinses in vuur en vlam! ververs de pagina om opnieuw te beginnen!")
elif pad == "rechts":
    eten = input("je bent verdwaald in een groot bos. je hebt helemaal niks bij je en je sterft van de honger! je komt een konijn tegen die je kunt eten of je plukt wat bessen! wat doe je? vul konijn of bessen in!")

    if eten == "konijn":
        print("je hebt het konijn vermoord maar om het te roosteren je moet een kampvuur maken!")

        kampvuur = input("je moet hout vinden voor een kampvuur! ga op zoek naar hout of eet het konijn rauw! vul hout of konijn eten in!")
        
        if kampvuur == "hout":
            print("je gaat op zoek naar hout en komt een beer tegen!")

            beer = input("je komt een beer tegen wat doe je? heel hard weg rennen of weg sluipen? kies rennen of sluipen!")
            
            if beer == "rennen":
                print("je rent heel hard weg maar de beer komt je achterna een vermoord je! ververs de pagina om opnieuw te beginnen!")
            elif beer == "sluipen":
                print("je bent weggeslopen en de beer heeft je niet gezien dus je bent even veilig!")

                wapen = input("je kunt een houten speer maken van takken die je tegen komt! maar je kunt ze ook gebruiken voor je kampvuur! wat doe je? kies: speer maken of kies voor: voor kampvuur!")

                if wapen == "speer maken":
                    print("de beer valt je aan maar gelukkig heb je een speer gemaakt dus je verslaat de beer!")

                    beerEten = input("je hebt de beer verslagen maar je sterft van de honger! je ziet ook de uitweg van het bos! ga je het bos uit of de beer roosteren en eten! kies beer opeten of bos uitgaan!")

                    if beerEten == "beer opeten":
                        print("je hebt de beer geroostert en opgegeten dus je kunt nu veilig en met een volle maag het bos verlaten! gefeliciteerd je hebt gewonnen!")
                    
                    if beerEten == "bos uitgaan":
                        print("je bent het bos uit gegaan maar je verhongerd! ververs de pagina om opnieuw te beginnen!")
        elif kampvuur == "konijn eten":
                print("je hebt het konijn gegeten maar het konijn had een ziekte dus je sterft! ververs de pagina om op nieuw te beginnen!")
    elif eten == "bessen":
            print("de bessen waren giftig en je gaat dus dood! ververs de pagina om op nieuw te beginnen!")