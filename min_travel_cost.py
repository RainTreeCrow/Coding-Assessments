# The country of Hackerland is represented as a graph of cities numbered from 1 to g_nodes.
# The cities are connected through g_edges bidirectional roads
# where the ith road connects city g_from[i] and city g_to[i]
# and the amount of fuel required to travel a road is g_weight[i] units.

# The cars in Hackerland have an infinite fuel capacity.
# The cost of one unit of fuel in the ith city is arr[i].
# Any amount of fuel can be obtained in any city.

# Given two cities A and B (1 ≤ A, B ≤ road_nodes),
# find the minimum cost to travel from city A to city B.
# If it is not possible, return -1.

import heapq

def getMinCost(g_nodes, g_from, g_to, g_weight, arr, A, B):
    # Step 1: Build the graph as an adjacency list.
    graph = {i: [] for i in range(1, g_nodes + 1)}
    for i in range(len(g_from)):
        graph[g_from[i]].append((g_to[i], g_weight[i]))
        graph[g_to[i]].append((g_from[i], g_weight[i]))

    # Step 2: Initialize the priority queue (min-heap) to track the state (cost, city, fuel left).
    # Initially, we start at city A with 0 cost and full flexibility on fuel.
    min_heap = [(0, A)]  # (current cost, city)
    
    # Step 3: Dictionary to store the minimum cost to reach each city
    min_cost = {i: float('inf') for i in range(1, g_nodes + 1)}
    min_cost[A] = 0  # Start city with zero cost
    
    # Step 4: Process the heap until it's empty.
    while min_heap:
        current_cost, city = heapq.heappop(min_heap)
        
        # If we reach city B, return the minimum cost
        if city == B:
            return current_cost
        
        # Step 5: Travel to neighboring cities
        for neighbor, travel_cost in graph[city]:
            # Calculate the cost to reach the neighboring city
            new_cost = current_cost + travel_cost * arr[city - 1]  # Current city's fuel cost
            
            # If the new cost to reach the neighbor is cheaper, update it
            if new_cost < min_cost[neighbor]:
                min_cost[neighbor] = new_cost
                heapq.heappush(min_heap, (new_cost, neighbor))
    
    # If we can't reach city B, return -1
    return -1

# Example usage
g_nodes = 4
g_from = [1, 2, 2]
g_to = [2, 3, 4]
g_weight = [3, 1, 7]
arr = [3, 6, 2, 2]
A = 1
B = 4

print(getMinCost(g_nodes, g_from, g_to, g_weight, arr, A, B))