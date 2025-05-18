"""
Insert your code bellow 

our task is to implement an algorithm that can find the way out of a maze.

The maze representation is like this:

    [
      [1,1,1,1,1],
      [1,0,0,1,1],
      [1,1,0,1,1],
      [1,1,0,0,0],
      [1,1,1,1,1],
    ]

So we have a map like this

    integer 0 represents walls

    integer 1 represents valid cells

    cell (0,0) is the starting point (it is the top left corner)

    the bottom right cell is the destination (so this is what we are looking for)

So the solution should be something like this (S represents the states in the solution set):

    [
      [S,-,-,-,-],
      [S,-,-,-,-],
      [S,-,-,-,-],
      [S,-,-,-,-],
      [S,S,S,S,S],
    ]

Good luck!


"""
from collections import deque
from typing import List, Tuple, Optional

Matriz = List[List[int]]
Camino = List[Tuple[int, int]]


def buscar_camino_bfs(laberinto: Matriz) -> Optional[Camino]:
    """Devuelve el camino más corto (incluyendo origen y destino) usando BFS.
    Regresa None si no existe salida.
    """
    # validación
    if not laberinto or not laberinto[0]:
        return None

    filas, columnas = len(laberinto), len(laberinto[0])
    destino = (filas - 1, columnas - 1)

    # comprobamos que origen y destino sean celdas transitables (== 1)
    if laberinto[0][0] == 0 or laberinto[destino[0]][destino[1]] == 0:
        return None

    # cola para BFS y diccionario para reconstrucción del camino
    cola: deque[Tuple[int, int]] = deque([(0, 0)])
    padre: dict[Tuple[int, int], Optional[Tuple[int, int]]] = {(0, 0): None}

    # desplazamientos: abajo, arriba, derecha, izquierda
    movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while cola:
        fila, col = cola.popleft()

        # si llegamos al destino terminamos la búsqueda
        if (fila, col) == destino:
            break

        # revisamos vecinos
        for df, dc in movimientos:
            nf, nc = fila + df, col + dc
            dentro_limites = 0 <= nf < filas and 0 <= nc < columnas
            if dentro_limites and laberinto[nf][nc] == 1 and (nf, nc) not in padre:
                padre[(nf, nc)] = (fila, col)  # Registramos de dónde venimos
                cola.append((nf, nc))

    # si nunca alcanzamos el destino salimos con None
    if destino not in padre:
        return None

    # reconstruimos el camino desde el destino al origen
    camino: Camino = []
    actual: Optional[Tuple[int, int]] = destino
    while actual is not None:
        camino.append(actual)
        actual = padre[actual]

    return camino[::-1]  # invertimos para obtener origen → destino


def pintar_solucion(laberinto: Matriz, camino: Camino) -> List[List[str]]:
    """Crea una matriz de strings con 'S' en el camino y '-' en el resto."""
    filas, columnas = len(laberinto), len(laberinto[0])
    salida = [["-" for _ in range(columnas)] for _ in range(filas)]
    for f, c in camino:
        salida[f][c] = "S"
    return salida


def resolver_e_imprimir(laberinto: Matriz) -> None:
    """Resuelve el laberinto y muestra la solución en pantalla."""
    camino = buscar_camino_bfs(laberinto)
    if camino is None:
        print("No se encontró salida\n")
        return

    solucion = pintar_solucion(laberinto, camino)
    for fila in solucion:
        print(fila)
    print()


if __name__ == '__main__':
    ### Your code must succesfully solve the following mazes:
    
    m = [[1, 0, 0, 1],
         [1, 0, 0, 1],
         [1, 0, 0, 1],
         [1, 1, 1, 1]
         ]

    easy_maze = [
        [1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 1]
    ]

    medium_maze = [
        [1, 1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0, 1]
    ]   
    hard_maze = [
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]

    for lab in (m, easy_maze, medium_maze, hard_maze):
        resolver_e_imprimir(lab)





