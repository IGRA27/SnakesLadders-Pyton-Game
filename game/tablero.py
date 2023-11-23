class Tablero:
    def __init__(self):
        #cabeza a cola de serpiente
        self.serpientes = {16:6,46:25,49:11,62:19,64:60,74:53,89:68,92:88,95:75,99:80}
        #de abajo a arriba de escaleras:
        self.escaleras = {2:38,7:14,8:31,15:26,28:84,21:42,36:44,51:67,71:91,78:98,87:94}

    def verificar_casilla(self, posicion):
        #reviso primero si es escalera
        if posicion in self.escaleras:
            return self.escaleras[posicion]
        #reviso si es serp
        elif posicion in self.serpientes:
            return self.serpientes[posicion]
        #misma posicion si no es escalera o serpiente
        return posicion





        