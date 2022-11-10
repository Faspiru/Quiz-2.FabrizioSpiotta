from Avatar import FuerzaEspecial, Francotirador, MedicoDeCombate, Espia

edd = {
    "f_special":
    [
        {"name": "potatoGOD", "life": 200, "weapon": "M16", "points": 800, "secondW": "Luger P08"},
        {"name": "xXHenryXx", "life": 150, "weapon": "Remington 1100", "points": 1450, "secondW": "Desert-Eagle"},
        {"name": "TrollMaster", "life": 400, "weapon": "M249", "points": 590, "secondW": "Nagant M1895"}
    ],
    "snipper":
    [
        {"name": "WhiteDeath", "life": 100, "weapon": "M28 Pystykorva", "points": 1990, "zoom": "x8", "spplus": 1.25}
    ],
    "medic":
    [
        {"name": "Delta", "life": 100, "weapon": "SPAS-12", "points": 545, "cure": 379},
        {"name": "Bot5001", "life": 100, "weapon": "Colt AR-15", "points": 8940, "cure": 500}
    ],
        
    "spy":
    [
        {"name": "XAnonimousX", "life": 100, "weapon": "PSS-2", "points": 795, "ins": True, "time": 5},
        {"name": "Spooky", "life": 100, "weapon": "GSh-18", "points": 4505, "ins": False, "time": 9}
    ]
}

def get_players():
    jugadores = []
    for type, list_players in edd.items():
        if type == "f_special":
            for player in list_players:
                fuerza_especial_player = FuerzaEspecial(player.get("name"), player.get("life"), player.get("weapon"), player.get("points"), player.get("secondW"))
                jugadores.append(fuerza_especial_player)
        elif type == "snipper":
            for player in list_players:
                francotirador_player = Francotirador(player.get("name"), player.get("life"), player.get("weapon"), player.get("points"), player.get("zoom"), player.get("spplus"))
                jugadores.append(francotirador_player)
        elif type == "medic":
            for player in list_players:
                medico_player = MedicoDeCombate(player.get("name"), player.get("life"), player.get("weapon"), player.get("points"), player.get("cure"))
                jugadores.append(medico_player)
        elif type == "spy":
            for player in list_players:
                espia_player = Espia(player.get("name"), player.get("life"), player.get("weapon"), player.get("points"), player.get("ins"), player.get("time"))
                jugadores.append(espia_player)
    return jugadores

def mostrar_jugadores(jugadores):
    print("-----JUGADORES QUE ESTAN EN LA PARTIDA-----")
    print()
    for jugador in jugadores:
        if jugador.estilo == "Fuerza Especial":
            print("---FUERZAS ESPECIALES---")
            jugador.mostrar()
            print()
        elif jugador.estilo == "Francotirador":
            print("---FRANCOTIRADORES---")
            jugador.mostrar()
            print()
        elif jugador.estilo == "Medico de Combate":
            print("---MEDICOS DE COMBATE---")
            jugador.mostrar()
            print()
        elif jugador.estilo == "Espia":
            print("---ESPIAS---")
            jugador.mostrar()
            print()

def banear_jugadores(jugadores, lista_negra):
    hacker_option = input("Cual es el nombre de usuario del hacker detectado? (escribalo correctamente): ")
    deleted = False
    for jugador in jugadores:
        if hacker_option == jugador.nombre_jugador:
            deleted = True
            jugadores.remove(jugador)
            lista_negra.append(jugador)
            print("Jugador baneado exitosamente")
            print()
    if deleted == False:
        print("No se ha encontrado el jugador seleccionado en la partida")
        print()

def get_second_weapon(jugadores):
    segundas_armas = []
    for jugador in jugadores:
        if jugador.estilo == "Fuerza Especial":
            segundas_armas.append({jugador.nombre_jugador: jugador.s_arma})
    return segundas_armas

    
def get_mas_p_player(jugadores):
    max_p = 0
    for jugador in jugadores:
        puntos_actuales = jugador.puntaje
        while max_p < puntos_actuales:
            max_p = puntos_actuales
    return max_p
        
def main():
    lista_negra = []
    jugadores = get_players()
    while True:
        print("-----BASE DE DATOS JUGADORES-----")
        print()
        option = input("Que desea realizar? \n 1. Ver personajes \n 2. Banear al hacker \n 3. Mostrar jugadores baneados \n 4. Mostrar armas secundarias \n 5. Mostrar puntaje maximo \n 6. Salir \n --> ")
        while not option.isnumeric() or not int(option) in range(1,7):
            option = input("Ingreso Invalido. Que desea realizar? \n 1. Ver personajes \n 2. Banear al hacker \n 3. Mostrar jugadores baneados \n 4. Mostrar armas secundarias \n 5. Mostrar puntaje maximo \n 6. Salir \n --> ")
        if option == "1":
            mostrar_jugadores(jugadores)
        elif option == "2":
            mostrar_jugadores(jugadores)
            banear_jugadores(jugadores, lista_negra)
        elif option == "3":
            print("----JUGADORES BANEADOS----")
            print()
            for baneados in lista_negra:
                baneados.mostrar()
                print()
        elif option == "4":
            segundas_armas = get_second_weapon(jugadores)
            print("----JUGADORES CON SEGUNDA ARMA----")
            print()
            for jugadores in segundas_armas:
                for key, value in jugadores.items():
                    print(f"jugador: {key} --> segunda arma: {value}")
            print()
        elif option == "5":
            max_p = get_mas_p_player(jugadores)
            print(f"EL maximo numero de puntos en la partida es: {max_p}")
        else:
            break
main()