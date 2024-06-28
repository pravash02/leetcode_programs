from collections import deque, defaultdict


# Print BFS reversal from from a given graph - iteration
class GraphIter:
    def __init__(self):
        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to the graph
    def addEdge(self, u, v):
        print(self.graph)
        self.graph[u].append(v)

    def bfs(self, startNode, vertices):
        # Create a queue for BFS
        q = deque()
        visited = [False] * vertices

        # Mark the current node as visited and enqueue it
        visited[startNode] = True
        q.append(startNode)

        # Iterate over the queue
        while q:
            # Dequeue a vertex from queue and print it
            currentNode = q.popleft()
            print(currentNode, end=" ")

            # Get all adjacent vertices of the dequeued vertex
            # If an adjacent has not been visited, then mark it visited and enqueue it
            for neighbor in self.graph[currentNode]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)


# Print BFS traversal from a given graph - recursion
class GraphRev:
    def __init__(self):
        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to the graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Utility function for BFS (recursive)
    def bfsUtil(self, queue, visited):
        # Mark the current node as visited and print it
        if not queue:
            return

            # Dequeue a vertex from the queue
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in self.graph[node]:
            if not visited[neighbour]:
                queue.append(neighbour)
                visited[neighbour] = True

        # Recursive call for the next node in the queue
        self.bfsUtil(queue, visited)

    # The function to do BFS traversal. It uses recursive BFSUtil()
    def bfs(self, startNode, vertices):
        visited = [False] * vertices
        # Create a queue for BFS and enqueue the start node
        queue = deque([startNode])

        # Mark the source node as visited
        visited[startNode] = True

        # Call the recursive helper function to print BFS traversal
        self.bfsUtil(queue, visited)
        print()


def main():
    # Number of vertices in the graph
    vertices = 5

    g = GraphIter()

    # Add edges to the graph
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 4)

    # Perform BFS traversal starting from vertex 0
    print("Breadth First Traversal starting from vertex 0:", end=" ")
    g.bfs(0, vertices)

    g1 = GraphRev()

    # Add edges to the graph
    g1.addEdge(0, 1)
    g1.addEdge(0, 2)
    g1.addEdge(1, 3)
    g1.addEdge(1, 4)
    g1.addEdge(2, 4)

    # Perform BFS traversal starting from vertex 0
    print("Breadth First Traversal starting from vertex 0:", end=" ")
    g1.bfs(0, vertices)


if __name__ == "__main__":
    main()
