# Serpientes y Escaleras Python Juego

Autor: Isaac Reyes

## Descripción
Este proyecto es una implementación digital del clásico juego de mesa "Snakes & Ladders". Seleccione el lenguaje Python y está diseñado para ser ejecutado en la consola. El juego soporta dos jugadores que compiten para alcanzar primero la casilla 100 en el tablero, navegando a través de serpientes y escaleras.

## Estructura del Proyecto
```
SnakesLadders-Python-Game
│
├── game                  #Carpeta para los módulos principales del juego
│   ├── __init__.py         #Archivo init para hacer que 'juego' sea un paquete de Python
│   ├── dado.py         #Funciones relacionadas con el dado 
│   ├── jugador.py          #Clase Jugador y lógica relacionada
│   └── tablero.py             #Clase Tablero y lógica relacionada
│
├── tests                  #Carpeta para pruebas unitarias
│   ├── __init__.py
│   ├── test_dado.py     #Pruebas para la logica del Dado
│   ├── test_jugador.py     #Pruebas para la clase Jugador
│   └── test_tablero.py        #Pruebas para la clase Tablero
|
├── main.py                 #Script principal para ejecutar juego
│
└── README.md               #Documentación del proyecto
```

## Características
- **Tablero Dinámico:** El tablero tiene serpientes y escaleras en posiciones predefinidas que cambian el curso del juego.
- **Juego Multijugador:** Soporte para dos jugadores, jugando turnos alternos. (se pueden aumentar el numero de jugadores)
- **Interacción Basada en Consola:** Interfaz sencilla basada en consola para lanzar el dado y mover las fichas. (Se puede crear una en Java, la cual tengo experiencia, e incluso en , esa recien estoy aprendiendo)


## Cómo empezar e instalar
Para jugar, necesitarás Python instalado en tu máquina.
Clona esto en el local:
git clone https://github.com/IGRA27/SnakesLadders-Pyton-Game.git

## Cómo Jugar?
1. Navega a la carpeta del proyecto. (donde se clono)
3. Ejecuta `main.py` usando Python. (en la terminal) Es decir: python main.py
4. Sigue las instrucciones en la consola para jugar el juego.

## Requisitos
- Python 3.0 y superiores

## Pruebas
Para ejecutar las pruebas, navega a la carpeta `tests` y ejecuta los scripts de prueba individuales:
python -m unittest discover -s tests (Antes de del main.py)



