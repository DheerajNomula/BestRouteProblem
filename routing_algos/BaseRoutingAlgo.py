import heapq

class BaseRoutingAlgo:
    def __init__(self, graph):
        """
        Initialize the base routing algorithm with a graph.
        The graph is a dictionary where the keys are nodes and the values are dictionaries of neighbours and their distances.

        Assumption: 
        Notation R1, R2, ... will be used for restaurants and C1, C2, ... will be used for customers.
        Aman is the starting node
        """
        self.graph = graph
        self.start = "Aman"

         # Separate the nodes into restaurants and customers
        self.restaurants = [node for node in self.graph if node.startswith('R')]
        self.customers = [node for node in self.graph if node.startswith('C')]


    def dijkstra(self, start, end, time_calculator):
        """
        Implementation Dijkstra's algorithm to find the shortest path from start to end.
        """
        # Initialize the distances to infinity
        distances = {node: float('infinity') for node in self.graph}
        distances[start] = 0

        # Initialize the priority queue with the start node
        queue = [(0, start)]

        while queue:
            # Pop the node with the smallest distance
            current_distance, current_node = heapq.heappop(queue)

            # If the current node is the end node, return its distance
            if current_node == end:
                return distances[end]

            # If the current node has not been visited yet
            if current_distance == distances[current_node]:
                # Update the distances to the neighboring nodes
                for neighbor in self.graph[current_node].items():
                    # todo can be optimised by calculating only once at the time of initialisation of graph
                    weight = time_calculator.calculate(start, end)

                    distance = current_distance + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(queue, (distance, neighbor))

        # If there's no path from start to end, raise an exception
        raise ValueError("No path from {} to {}.".format(start, end))
    
    
    
    def calculate_weight(self, start, end, time_calculator):
        """
        Calculate the weight (time) between the start node and the end node using the provided TimeCalculator.
        If there's no direct edge between the start and end nodes, use Dijkstra's algorithm to find the shortest path.
        """
        if start not in self.graph or end not in self.graph:
            raise ValueError("Both start and end nodes must be in the graph.")
        
        if end in self.graph[start]:
            # If there's a direct edge, return its weight
            return time_calculator.calculate(start, end)
        else:
            # If there's no direct edge, use Dijkstra's algorithm to find the shortest path
            return self.dijkstra(start, end, time_calculator)

    def find_route(self, start, end):
        """
        Find the route from the start node to the end node.
        This method should be overridden by subclasses with specific routing algorithms.
        """
        raise NotImplementedError("Subclasses should implement this method.")