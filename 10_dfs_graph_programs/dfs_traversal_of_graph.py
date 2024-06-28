from collections import defaultdict, deque


# Print DFS reversal from from a given graph - iteration
class GraphIter:
    def __init__(self):
        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # The function to do DFS traversal iteratively
    def DFS(self, start):
        # Create a set to store visited vertices
        visited = set()
        # Create a stack for DFS
        stack = deque()
        stack.append(start)

        while stack:
            # Pop a vertex from stack
            vertex = stack.pop()

            # If not visited, mark it as visited and print it
            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)

                # Get all adjacent vertices of the popped vertex
                # If a adjacent has not been visited, then push it to the stack
                adjList = self.graph[vertex]
                for i in reversed(range(len(adjList))):
                    u = adjList[i]
                    if u not in visited:
                        stack.append(u)

                # for neighbour in self.graph[vertex]:
                #     if neighbour not in visited:
                #         stack.append(neighbour)


# Print DFS traversal from a given graph - recursion
class GraphRev:
    def __init__(self):
        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, startNode, visited):

        # Mark the current node as visited and print it
        visited.add(startNode)
        print(startNode, end=' ')

        # Recur for all the vertices adjacent to this vertex
        for neighbour in self.graph[startNode]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    # The function to do DFS traversal. It uses recursive DFSUtil()
    def DFS(self, startNode):

        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function to print DFS traversal
        self.DFSUtil(startNode, visited)


# Driver Code
if __name__ == '__main__':
    g = GraphIter()  # Total 5 vertices in graph
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g1 = GraphRev()  # Total 5 vertices in graph
    g1.addEdge(0, 1)
    g1.addEdge(0, 2)
    g1.addEdge(1, 2)
    g1.addEdge(2, 0)
    g1.addEdge(2, 3)
    g1.addEdge(3, 3)

    print("Following is Depth First Traversal")
    g.DFS(2)
    g1.DFS(2)
