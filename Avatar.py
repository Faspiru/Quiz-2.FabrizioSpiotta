class Avatar():
    def __init__(self, nombre_jugador, vida, arma, puntaje):
        self.nombre_jugador = nombre_jugador
        self.vida = vida
        self.arma = arma
        self.puntaje = puntaje
    
    def mostrar(self):
        print(f"Nombre Jugador: {self.nombre_jugador}")
        print(f"Vida: {self.vida}")
        print(f"Arma: {self.arma}")
        print(f"Puntaje: {self.puntaje}")

class FuerzaEspecial(Avatar):
    def __init__(self, nombre_jugador, vida, arma, puntaje, s_arma):
        super().__init__(nombre_jugador, vida, arma, puntaje)
        self.s_arma = s_arma
        self.estilo = "Fuerza Especial"

    def mostrar(self):
        print(f"Nombre Jugador: {self.nombre_jugador}")
        print(f"Vida: {self.vida}")
        print(f"Arma: {self.arma}")
        print(f"Puntaje: {self.puntaje}")
        print(f"Segunda Arma: {self.s_arma}")
        print(f"Estilo: {self.estilo}")

class Francotirador(Avatar):
    def __init__(self, nombre_jugador, vida, arma, puntaje, zoom, velocidad):
        super().__init__(nombre_jugador, vida, arma, puntaje)
        self.zoom = zoom
        self.velocidad = velocidad
        self.estilo = "Francotirador"
    
    def mostrar(self):
        print(f"Nombre Jugador: {self.nombre_jugador}")
        print(f"Vida: {self.vida}")
        print(f"Arma: {self.arma}")
        print(f"Puntaje: {self.puntaje}")
        print(f"Zoom: {self.zoom}")
        print(f"Velocidad: {self.velocidad}")
        print(f"Estilo: {self.estilo}")
    
class MedicoDeCombate(Avatar):
    def __init__(self, nombre_jugador, vida, arma, puntaje, cura):
        super().__init__(nombre_jugador, vida, arma, puntaje)
        self.cura = cura
        self.estilo = "Medico de Combate"
    
    def mostrar(self):
        print(f"Nombre Jugador: {self.nombre_jugador}")
        print(f"Vida: {self.vida}")
        print(f"Arma: {self.arma}")
        print(f"Puntaje: {self.puntaje}")
        print(f"Cura: {self.cura}")
        print(f"Estilo: {self.estilo}")
    
class Espia(Avatar):
    def __init__(self, nombre_jugador, vida, arma, puntaje, invisible, segundos):
        super().__init__(nombre_jugador, vida, arma, puntaje)
        self.invisible = invisible
        self.segundos = segundos
        self.estilo = "Espia"
    
    def mostrar(self):
        print(f"Nombre Jugador: {self.nombre_jugador}")
        print(f"Vida: {self.vida}")
        print(f"Arma: {self.arma}")
        print(f"Puntaje: {self.puntaje}")
        print(f"Invisible: {self.invisible}")
        print(f"Segundos: {self.segundos}")
        print(f"Estilo: {self.estilo}")
