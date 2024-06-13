from collections import defaultdict


# Create a class for the graph
class Graph:
    def __init__(self):
        # Initialize an empty dictionary to store the graph
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        # Add an edge to the graph
        self.graph[u].append(v)

    def BFS(self, s):
        # Perform a breadth-first search starting from the given source vertex
        visited = [False] * (max(self.graph) + 1)  # Initialize all vertices as not visited
        queue = []  # Initialize an empty queue

        queue.append(s)  # Add the source vertex to the queue
        visited[s] = True  # Mark the source vertex as visited

        while queue:
            # Dequeue a vertex from the queue and print it
            s = queue.pop(0)
            print(s, end=' ')

            # Get all adjacent vertices of the dequeued vertex
            # If an adjacent vertex has not been visited, mark it as visited and enqueue it
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


# Create a new graph object
g = Graph()

# Add edges to the graph
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

# Call the BFS function, starting from vertex 2
print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
g.BFS(2)
