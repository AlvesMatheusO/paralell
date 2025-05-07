import time
from grafo import grafo_simples
from grafo_chain import grafo_chain
from bfs import bfs
from paralelizacao import search_path
from concurrent.futures import ThreadPoolExecutor

grafo = grafo_simples
# grafo = grafo_chain

def sequencial(reps, grafo, start, end):
    t0 = time.perf_counter()

    for _ in range(reps):
        bfs(grafo, start, end)
    return time.perf_counter() - t0

def paralelo(reps, grafo, start, end):
    t0 = time.perf_counter()
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(search_path, grafo, start, end)
            for _ in range(reps)
        ]

        for f in futures: 
            _ = f.result()
        return time.perf_counter() - t0
    
if __name__ == "__main__":
    start, end = 'A', 'F'
    # start, end = '1', '1000'

    print("Corretude: ", bfs(grafo, start, end))

    reps = 200
    ts = sequencial(reps, grafo, start, end)
    tp = paralelo(reps, grafo, start, end)

    speedup = ts/tp if tp > 0 else float('inf')

    print(f"Sequencial ({reps}x): {ts:.4f}s")
    print(f"Paralelo   ({reps}x): {tp:.4f}s")
    print(f"Speedup aprox.: {speedup:.2f}×")