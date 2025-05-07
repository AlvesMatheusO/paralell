from collections import deque

def bfs(grafo, start, end):
    fila = deque([[start]])
    caminhos = []

    while fila:
        caminho = fila.popleft()
        no = caminho[-1]

        if no == end:
            caminhos.append(caminho)
            continue

        for vizinho in grafo.get(no, []): 
            if vizinho not in caminho:
                fila.append(caminho + [vizinho])
    return caminhos
