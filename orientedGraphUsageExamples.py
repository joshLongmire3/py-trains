import graphClass

print("importing the graph class and creating an oriented graph object...")
oG = graphClass.orientedGraph()

print("adding vertice 'P' ")
oG.add_vertice('P')

print("adding vertice 'Q' ")
oG.add_vertice('Q')

print("adding vertice 'R' ")
oG.add_vertice('R')

print("adding edge named:'a', source:'P', and target:'Q' ")
oG.add_edge('a','P','Q')

print("adding edge named:'c', source:'P', and target:'R' ")
oG.add_edge('c','P','R')

print("adding edge named:'b', source:'Q', and target:'R' ")
oG.add_edge('b', 'Q', 'R')

print ("the edges are:")
oG.get_edges_names()

print("the vertices are:")
oG.get_vertices_names()

ngbrhs = oG.get_vertices_neighbors('P')
print("vertice:P has src's that lead to")
print(ngbrhs)

#pythons cool and can return 2 things!
edgeSrc, edgeTrgt = oG.get_src_and_target('a')
#pythons cool and can return 2 things!
edgeSrc2, edgeTrgt2 = oG.get_src_and_target('areverse')


#i was to lazy to figure out how to format with
#printf, to put the follwin on 1 line  :)
print("a's source: ")
print(edgeSrc)
print("a's target: ")
print(edgeTrgt)

#i was to lazy to figure out how to format with
#printf, to put the follwin on 1 line  :)
print("areverse's source: ")
print(edgeSrc2)
print("areverse's target: ")
print(edgeTrgt2)

#numEdges
print('NumEdges:')
print(oG.NumEdges)
#numVertices
print('NumVertices:')
print(oG.NumVertices)


#error demonstrations
print("\ndemonstrating producing an error on inserting a edge with NAME already taken:")
print("adding edge named:'c', source:'Q', and target:'P' ")
oG.add_edge('c','Q','P')

print("\ndemonstrating producing an error on inserting a edge with PATH already existing:")
print("adding edge named:'d', source:'P', and target:'Q' ")
oG.add_edge('d','P','Q')

print("\ndemonstrating producing an error on inserting a vertice with NAME already taken:")
oG.add_vertice('P')

