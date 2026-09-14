import heapq

def dijkstra_heap(graph, start_node):
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    
    previous_nodes = {node: None for node in graph}
    

    priority_queue = [(0, start_node)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes


def get_path(previous_nodes, target_node):
    """目的地までの経路を復元するヘルパー関数"""
    path = []
    current = target_node
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    return path[::-1] 

if __name__ == "__main__":
    graph = {
        0: {1: 5, 2: 3, 4: 11},
        1: {0: 5, 2: 1, 5: 2},
        2: {0: 3, 1: 1, 3: 1, 4: 5},
        3: {2: 1, 4: 9, 5: 3},
        4: {0: 11, 2: 5, 3: 9},
        5: {1: 2, 3: 3}
    }

    start = 0
    target = 5
    distances, previous_nodes = dijkstra_heap(graph, start)
    path = get_path(previous_nodes, target)

    print(f"ノード {start} から {target} までの最短距離: {distances[target]}")
    print(f"最短経路: {' -> '.join(map(str, path))}")