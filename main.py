print("Dzień dobry")

for i in range(5):
    word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")
    
    meme_dict = {
                "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
                "LOL": "Częsta reakcja na coś zabawnego",
                "ROFL": "odpowiedź na żart",
                "SHEESH" : "lekka dezaprobata",
                "CREEPY" : "straszny, złowieszczy",
                "AGGRO" : "stać się agresywnym/zły",
                }
                
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Nie ma słowa takiego w słowniku")
