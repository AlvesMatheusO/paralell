import math

def splitGraph(graph, numParts):
    nodes = list(graph.keys())
    # Divide em pedaços de tamanho aproximado, garantindo que nenhum fique vazio
    chunk = math.ceil(len(nodes) / numParts)
    subgraphs = []

    for i in range(numParts):
        start_idx = i * chunk
        end_idx   = start_idx + chunk
        part = nodes[start_idx:end_idx]

        # induce o subgrafo: só arestas entre nós de `part`
        sg = {
            n: [v for v in graph[n] if v in part]
            for n in part
        }
        subgraphs.append(sg)

    return subgraphs
