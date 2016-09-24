from collections import OrderedDict, deque
import math

def print_distances(distance_vector):
    # Actions to match the expected output:
    # - removing the first element because the graph indexes start from 1.
    # - removing the starting index (the one with distance 0);
    # - converting inf values in -1
    distance_vector = distance_vector[1:]
    distance_vector.remove(0)
    distance_vector_with_ones = [str(-1) if math.isinf(distance) else str(distance) for distance in distance_vector]
    print " ".join(distance_vector_with_ones)

def read_graph_data():
    node_number, edge_number = map(int,raw_input().strip().split(' '))
    nodes_adjacency_list = OrderedDict()
    for edge_index in range(edge_number):
        from_vertex, to_vertex = map(int,raw_input().strip().split(' '))
        # Adding the edge to the 2 adjacency lists.
        nodes_adjacency_list.setdefault(from_vertex, []).append(to_vertex)
        nodes_adjacency_list.setdefault(to_vertex, []).append(from_vertex)
    starting_vertex = int(raw_input().strip())
    return node_number, nodes_adjacency_list, starting_vertex

def shortest_path(node_number, nodes_adjacency_list, starting_vertex):
    edge_weight = 6
    # node_number + 1 because the node indexes are given starting from 1.
    visited = [False] * (node_number + 1)
    distances = [float("inf")] * (node_number + 1)
    node_queue = deque([starting_vertex])
    distances[starting_vertex] = 0

    while node_queue:
        current_node = node_queue.popleft()
        adjacent_nodes = nodes_adjacency_list[current_node]
        for adjacent_node in adjacent_nodes:
            if distances[current_node] + edge_weight < distances[adjacent_node]:
                distances[adjacent_node] = distances[current_node] + edge_weight
            if not visited[adjacent_node] and adjacent_node not in node_queue:
                node_queue.append(adjacent_node)
        visited[current_node] = True

    return distances

test_cases = int(raw_input().strip())
processed_cases = 0

while processed_cases < test_cases:
    distances = shortest_path(*read_graph_data())
    print_distances(distances)
    processed_cases += 1
