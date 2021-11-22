# Implementation of Breadth First Search


'''
An alternative algorithm called Breath-First search provides us with the ability to return the same results as DFS but with the added guarantee to return the shortest-path first. This algorithm is a little more tricky to implement in a recursive manner instead using the queue data-structure, as such I will only being documenting the iterative approach. The actions performed per each explored vertex are the same as the depth-first implementation, however, replacing the stack with a queue will instead explore the breadth of a vertex depth before moving on. This behavior guarantees that the first path located is one of the shortest-paths present, based on number of edges being the cost factor.
'''

# We'll assume our Graph is in the form:

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs(graph,start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()

        if  vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)

    return visited

print(dfs(graph,'A'))


