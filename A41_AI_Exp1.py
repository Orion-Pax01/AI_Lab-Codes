# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 20:12:53 2023

@author: User
"""

#implement DFS BFS search algorithms using undirected graph.

from collections import deque

# Define a graph using an adjacency list.
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'A'],
    'E': ['D', 'F'],
    'F': ['C', 'E']
}

def bfs(graph, start):
    visited = set()  # Keep track of visited nodes
    queue = deque([start])  # Use a queue for BFS
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

def dfs(graph, start):
    visited = set()  # Keep track of visited nodes
    stack = [start]  # Use a stack for DFS

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            # Push unvisited neighbors onto the stack in reverse order.
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

print("\n")

print("BFS Traversal: ") #BFS
bfs(graph, 'A')

print("\n")

print("Dfs Traversal: ") #DFS
dfs(graph, 'A')

print("\n")