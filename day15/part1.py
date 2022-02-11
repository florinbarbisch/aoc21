# start at starting position
# find adjecant nodes sort possible paths by their risk levels
# check for paths with the lowest risk levels

def find_node(graph, x, y, risk):
    
    pass

# just use A*
with open("test.txt", "r") as file:
    graph = [[int(x) for x in line.rstrip()] for line in file]
    len_x, len_y = len(graph), len(graph[0])
    start = (0, 0, 0, len_x*len_y)
    end = (len_x-1, len_y-1, , len_x*len_y)
    closed_nodes = set()
    open_nodes = {start} # start at (0|0) with risk of 0 and the (chebyshev distance + risk_level)
    while len(open_nodes) > 0:
        current_node = None
        for node in open_nodes:
            if node[3] < current_node[3]:
                current_node = node
        if node[0] == len_x-1 and node[1] == len_y-1:
            # do
            print("done")
            break
        open_nodes.remove(current_node)
        closed_nodes.add(current_node)

        for neighbor in 
            
    