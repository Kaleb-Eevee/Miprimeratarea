meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta comun a algo gracioso",
            "PAPEADA": "Una respuesta ingeniosa ante algun comentario de forma constructiva y no hecha para humillar",
            "GG": "Abreviacion de Good Game o Buena Partida",
            "CREEPY": "Se refiere a algo aterrador o siniestro",
            "IDK": "Abreviacion de I Don´t Know o Yo no se" ,
            "EPICO": "En terminos modernos, es una palabra utilizada cuando no sabes que decir, a veces es molesto",
            "WDYM": "Abreviacion de What Do You Mean? o Que quieres decir?"
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(meme_dict)
else:
    print("Esa palabra no se ha encontrado, ¡regrese más tarde!")
