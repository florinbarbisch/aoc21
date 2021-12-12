def find_paths_to_end(graph, visited_small_cave_twice, visited_nodes, start_node):
    paths = []
    visited_small_cave_twice = visited_small_cave_twice or (start_node.islower() and start_node in visited_nodes)
    visited_nodes = visited_nodes.copy()
    visited_nodes.append(start_node)
    if start_node == "end":
        return [visited_nodes]
    for node in graph[start_node]:
        if node.isupper() or (node not in visited_nodes) or (not visited_small_cave_twice and node not in ("start", "end")):
            paths.extend(find_paths_to_end(graph, visited_small_cave_twice, visited_nodes, node)) 
    return paths

with open("input.txt", "r") as file:
    graph = {}
    for line in file:
        edge = line.rstrip().split("-")
        if edge[0] in graph: graph[edge[0]].add(edge[1])
        else:                graph[edge[0]] =  {edge[1]}
        if edge[1] in graph: graph[edge[1]].add(edge[0]) # undirected graph
        else:                graph[edge[1]] =  {edge[0]}
    print(len(find_paths_to_end(graph, False, [], "start")))