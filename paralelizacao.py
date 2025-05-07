# encapsula a chamada do bfs para ser usada em paralelo
from bfs import bfs

def search_path(grafo, start, end):
    return bfs(grafo, start, end);
