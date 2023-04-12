import numpy as np


def tsp_steep_ascent_hill_climbing(cost_matrix, src_node):
    num_nodes = len(cost_matrix)
    curr_node = src_node
    visited_nodes = [src_node]
    path_cost = 0

    while len(visited_nodes) < num_nodes:
        best_neighbor = None
        best_cost = np.inf

        for neighbor in range(num_nodes):
            if neighbor not in visited_nodes:
                neighbor_cost = cost_matrix[curr_node][neighbor]
                if neighbor_cost < best_cost:
                    best_neighbor = neighbor
                    best_cost = neighbor_cost

        if best_neighbor is None:
            return None  # no solution found

        visited_nodes.append(best_neighbor)
        path_cost += best_cost
        curr_node = best_neighbor

    # add cost of returning to the source node
    path_cost += cost_matrix[curr_node][src_node]
    visited_nodes.append(src_node)

    return visited_nodes, path_cost


def main():
    cost_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]

    src_node = 0
    visited_nodes, path_cost = tsp_steep_ascent_hill_climbing(cost_matrix, src_node)
    print(visited_nodes)
    print(path_cost)

if __name__ == '__main__':
    main()
