from Helper import isCustomer


class TSP(BaseRoutingAlgo):
    def find_route(self, end):
        """
        Find the route from the start node (Aman) to the end node using the Traveling Salesman Problem (TSP) approach.
        """
        # Combine the restaurants and customers into a single list
        nodes = self.restaurants + self.customers

        # Initialize the memoization table
        memo = [[None] * len(nodes) for _ in range(1 << len(nodes))]

        # Calculate the weight from the start node to the first node in each permutation
        start_weight = [self.calculate_weight(self.start, node) for node in nodes]

        # Use dynamic programming to solve the TSP
        return min(start_weight[i] + self.tsp(1 << i, i, nodes, memo) for i in range(len(nodes)))

    def tsp(self, mask, pos, nodes, memo):
        """
        Solve the TSP using dynamic programming.
        """
        # If all nodes have been visited, return the weight of the edge to the end node
        if mask == (1 << len(nodes)) - 1:
            return self.calculate_weight(nodes[pos], self.end)

        # If the result has been memoized, return it
        if memo[mask][pos] is not None:
            return memo[mask][pos]

        # Initialize the result to infinity
        res = float('infinity')

        # Try to visit each node that has not been visited yet
        for nxt in range(len(nodes)):
            # Check if the next node is a customer and its corresponding restaurant has not been visited yet
            if isCustomer(nodes[nxt]) and (mask & (1 << nodes.index('R' + nodes[nxt][1:]))) == 0:
                continue
            if mask & (1 << nxt) == 0:
                res = min(res, self.calculate_weight(nodes[pos], nodes[nxt]) + self.tsp(mask | (1 << nxt), nxt, nodes, memo))

        # Memoize and return the result
        memo[mask][pos] = res
        return res