# encapsula a chamada do bfs para ser usada em paralelo
from concurrent.futures import ThreadPoolExecutor
from bfs import bfs
from foster import splitGraph

def search_path(grafo, start, end, numParts=4):
    
    subgraphs = splitGraph(grafo, numParts)
    resultados = []
    
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(bfs, sg, start, end)
            for sg in subgraphs
        ]
        for fut in futures:
            resultados.extend(fut.result())
    
    return resultados
