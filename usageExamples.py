import graphClass

print("importing the graph class and creating a graph object...")
g = graphClass.theGraph()

print("adding vertice 'P' ")
g.add_vertice('P')

print("adding vertice 'Q' ")
g.add_vertice('Q')

print("adding vertice 'R' ")
g.add_vertice('R')

print("adding edge named:'a', source:'P', and target:'Q' ")
g.add_edge('a','P','Q')

print("adding edge named:'c', source:'P', and target:'R' ")
g.add_edge('c','P','R')

print("adding edge named:'b', source:'Q', and target:'R' ")
g.add_edge('b', 'Q', 'R')

print ("the edges are:")
g.get_edges_names()

print("the vertices are:")
g.get_vertices_names()

ngbrhs = g.get_vertices_neighbors('P')
print("vertice:P has src's that lead to")
print(ngbrhs)

#pythons cool and can return 2 things!
edgeSrc, edgeTrgt = g.get_src_and_target('a')

#i was to lazy to figure out how to format with
#printf, to put the follwin on 1 line  :)
print("a's source: ")
print(edgeSrc)
print("a's target: ")
print(edgeTrgt)



print("\ndemonstrating producing an error on inserting a edge with name already taken:")
print("adding edge named:'c', source:'Q', and target:'P' ")
g.add_edge('c','Q','P')

print("\ndemonstrating producing an error on inserting a edge with PATH already existing:")
print("adding edge named:'d', source:'P', and target:'Q' ")
g.add_edge('d','P','Q')
