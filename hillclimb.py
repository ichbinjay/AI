import random

def tsp_hill_climbing(distance_matrix, iterations=1000):
    # Initialize the current solution as a random permutation of the cities
    current_solution = list(range(len(distance_matrix)))
    random.shuffle(current_solution)
    
    # Define a function to calculate the total distance of a given solution
    def calculate_total_distance(solution):
        total_distance = 0
        for i in range(len(solution)-1):
            total_distance += distance_matrix[solution[i]][solution[i+1]]
        total_distance += distance_matrix[solution[-1]][solution[0]]  # Add the distance back to the starting city
        return total_distance
    
    # Iterate the hill climbing algorithm for a certain number of iterations
    for i in range(iterations):
        # Generate all neighboring solutions by swapping two cities
        neighbors = []
        for j in range(len(current_solution)-1):
            for k in range(j+1, len(current_solution)):
                neighbor = current_solution.copy()
                neighbor[j], neighbor[k] = neighbor[k], neighbor[j]
                neighbors.append(neighbor)
        
        # Evaluate the neighboring solutions and choose the best one
        best_neighbor = min(neighbors, key=calculate_total_distance)
        
        # If the best neighbor is better than the current solution, update the current solution
        if calculate_total_distance(best_neighbor) < calculate_total_distance(current_solution):
            current_solution = best_neighbor
    
    # Return the final solution
    return current_solution
