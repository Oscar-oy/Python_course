# Implementation of Depht First Search

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
        if vertex not in visited:
            visited.add(vertex)
            print('graph: '+ str(graph[vertex]))
            print('visited: '+str(visited))
            print(graph[vertex]-visited)
            stack.extend(graph[vertex]-visited)
            print('stack: '+str(stack))

    return visited

print(dfs(graph,'A'))