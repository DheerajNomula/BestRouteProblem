from itertools import permutations

class BruteForceAlgo(BaseRoutingAlgo):
    def find_route(self, end):
        """
        Find the route from the start node (Aman) to the end node using a brute force approach.
        Assuming R1, R2, C1, C2 are the nodes, the algorithm will generate all possible permutations of the nodes
        and calculate the weight of each permutation based on the condition that Restaurants are traversed before Customers. 
        The route with the shortest weight will be returned.

        The algorithm generates all permutations of the nodes, which takes O(n!) time, 
        where n is the total number of nodes (restaurants + customers).
        
        """
        # Combine the restaurants and customers into a single list
        nodes = self.restaurants + self.customers

        # Generate all permutations of the nodes
        node_permutations = list(permutations(nodes))

        # Initialize the shortest route and its weight
        shortest_route = None
        shortest_weight = float('infinity')

        # Iterate over all permutations of nodes
        for node_permutation in node_permutations:
            # Check if each restaurant is visited before its corresponding customer
            if not all(node_permutation.index('R' + str(i)) < node_permutation.index('C' + str(i)) for i in range(1, len(self.restaurants) + 1)):
                continue
            # Calculate the weight of the route
            weight = self.calculate_weight(self.start, node_permutation[0])
            for i in range(len(node_permutation) - 1):
                weight += self.calculate_weight(node_permutation[i], node_permutation[i + 1])
            weight += self.calculate_weight(node_permutation[-1], end)

            # Update the shortest route and its weight if necessary
            if weight < shortest_weight:
                shortest_route = (self.start,) + node_permutation + (end,)
                shortest_weight = weight

        return shortest_weight