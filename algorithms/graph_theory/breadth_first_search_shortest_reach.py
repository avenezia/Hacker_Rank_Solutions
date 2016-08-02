from collections import defaultdict

def read_graph_data():
    node_number, edge_number = map(int,raw_input().strip().split(' '))
    nodes_adjacency_list = defaultdict(list)
    for edge_index in range(edge_number):
        from_vertex, to_vertex = map(int,raw_input().strip().split(' '))
        nodes_adjacency_list[from_vertex] = to_vertex
        nodes_adjacency_list[to_vertex] = from_vertex
    starting_vertex = int(raw_input().strip())
    return nodes_adjacency_list, starting_vertex

test_cases = int(raw_input().strip())
processed_cases = 0

#TODO: to be completed and refactored
while processed_cases < test_cases:
    edge_weight = 6
    nodes_adjacency_list, starting_vertex = read_graph_data()
    node_number = len(nodes_adjacency_list.keys())
    # node_number + 1 because the node indexes are given starting from 1.
    visited = [False] * (node_number + 1)
    distances = [float("inf")] * (node_number + 1)
    node_queue = [starting_vertex]
    distances[starting_vertex] = 0
    while node_queue:
        current_node = node_queue.pop(0)
        adjacent_nodes = nodes_adjacency_list[current_node]
        for adjacent_node in adjacent_nodes:
            if distances[current_node] + edge_weight < distances[adjacent_node]:
                distances[adjacent_node] = distances[current_node] + edge_weight
            if not visited[adjacent_node]:
                node_queue.append(adjacent_node)
        visited[current_node] = True
    processed_cases += 1

