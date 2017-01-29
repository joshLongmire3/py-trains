import graphClass

print("importing the graph class and creating a ribbon graph object...")
rG = graphClass.ribbonGraph()

print("adding vertice 'P' ")
rG.add_vertice('P')

print("adding vertice 'Q' ")
rG.add_vertice('Q')

print("adding vertice 'R' ")
rG.add_vertice('R')

print("adding edge named:'a', source:'P', and target:'Q', 3, 1 ")
rG.add_edge('a','P','Q', 3, 1)#cyclic value on edge P to Q is 1 
                              #and cyclic value on edge Q to P is 3

print("adding edge named:'c', source:'P', and target:'R', 4, 7 ")
rG.add_edge('c','P','R', 4, 7)

print("adding edge named:'b', source:'Q', and target:'R', 2, 5 ")
rG.add_edge('b', 'Q', 'R', 2, 5)

print ("the edges are:")
rG.get_edges_names()

print("the vertices are:")
rG.get_vertices_names()

rG.make_cyclic_dict_entry('P')

print("the cyclic order of P is:")
rG.get_cyclic_order('P')

print("the cyclic object of P are:")
rG.get_cyclic_object('P')

print("the edge after creverse in P's list is:")
rG.get_cyclic_orders_next('P', 'creverse') 

