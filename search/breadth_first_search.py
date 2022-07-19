# BFS for Graph
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # add edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def BFS(self, s):
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1 )
        # Create a queue for BFS
        queue = []
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i] = True
        print("\n")


# Test Case
if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print ("Following is Breadth First Traversal (starting from vertex 2)")
    g.BFS(2)