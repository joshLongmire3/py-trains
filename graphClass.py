class edgeClass:
  def __init__(self, name, src, dst):
    self.Name = name
    self.Src = src
    self.Dst = dst


#class cyclicEdge inherits from edgeClass class
class cyclicEdgeClass(edgeClass):
#constructor
  def __init__(self, name, src, dst, cyclicOrder):
      edgeClass.__init__(self, name, src, dst)
      self.CyclicOrder = cyclicOrder


class verticeClass:
  def __init__(self, name):
    self.Name = name


class theGraph:
#constructor
  def __init__(self):
    self.NumVertices = 0
    self.NumEdges = 0
    self.Vertices = []
    self.Edges = []

#edge names should be unique and lower case
#only one edge with one name with exist from a src to a target
  def add_edge(self, name, src, dst):
    #see if the name is taken by another edge
    for edge in self.Edges:
       if edge.Name == name:
          print("err:edge name already taken")
          return
    
    #see if the edges path already exists
    for edge in self.Edges:
       if edge.Src == src and edge.Dst == dst:
          print("err: this edges path already exists")
          return
 
    e = edgeClass(name, src, dst) 
    self.Edges.append(e)
    self.NumEdges = self.NumEdges + 1
 

#vertice names should be unique and upper case
  def add_vertice(self, name):
    #see if the name is taken by another edge
    for vertice in self.Vertices:
       if vertice.Name == name:
          print("err:vertice name already taken")
          return

    v = verticeClass(name)
    self.Vertices.append(v)
    self.NumVertices = self.NumVertices + 1


#prints the names of the edges
#in the set of edges
  def get_edges_names(self):
    for edge in self.Edges:
        print edge.Name


#prints the names of the vertices
#in the set of vertices
  def get_vertices_names(self):
    for vertice in self.Vertices:
       print vertice.Name 


#returns alist of names of vertices
#only adds if our passed in vertice is src 
#simply add (or statement edge.Dest==vertice)
#if we can get from a target to a source 
  def get_vertices_neighbors(self, vertice):
    neighborList = []
    
    for edge in self.Edges:
       #if our vertice is the src to an edge
       if edge.Src == vertice:
          #addThe dst's name to the list
          neighborList.append(edge.Dst) 
    #ret list of dst vertice names
    return neighborList


#returns the names of both the src and the dst (-1 if edgeName not found)
#a given edge can have only one src and only one target
  def get_src_and_target(self, passedEdgeName):
    edgeSrc = -1
    edgeDst = -1
    #find the edge whos name was passed in 
    for edge in self.Edges:
      if edge.Name == passedEdgeName:
         edgeSrc = edge.Src
         edgeDst = edge.Dst
    
    return edgeSrc, edgeDst





#class orientedGrpah inherits from theGraph class
class orientedGraph(theGraph):

#constructor
  def __init__(self):
      theGraph.__init__(self)



#an overridden addEdgeClass that automatically
#adds a second edge in the reverse direction for us
#edge names should be unique and lower case
#only one edge with one name will exist from a src to a target
  def add_edge(self, name, src, dst):
    #see if the name is taken by another edge
    for edge in self.Edges:
       if edge.Name == name:
          print("err:edge name already taken")
          return

    #see if the edges path already exists
    for edge in self.Edges:
       if edge.Src == src and edge.Dst == dst:
          print("err: this edges path already exists")
          return

    e = edgeClass(name, src, dst)
    self.Edges.append(e)
    self.NumEdges = self.NumEdges + 1
    #now add a second edge in the reverse direction
    name = name + 'reverse' #add the string 'reverse' to the end of the 
                           #edges name as it is the reverse of what we added
    #reverse the order of src/dst as reverse edge direc
    eRev = edgeClass(name, dst, src)
    self.Edges.append(eRev)
    self.NumEdges = self.NumEdges + 1




class ribbonGraph(orientedGraph):

#constructor
  def __init__(self):
      orientedGraph.__init__(self)
      self.CyclicVerticesDict = {}


#an overridden addEdgeClass that automatically
#adds a second edge in the reverse direction for us
#ALSO uses cyclicEdges instead of regular edges

#edge names should be unique and lower case
#only one edge with one name will exist from a src to a target
  def add_edge(self, name, src, dst, cyclicOrderNorm, cyclicOrderReverse):
    #see if the name is taken by another edge
    for edge in self.Edges:
       if edge.Name == name:
          print("err:edge name already taken")
          return

    #see if the edges path already exists
    for edge in self.Edges:
       if edge.Src == src and edge.Dst == dst:
          print("err: this edges path already exists")
          return

    e = cyclicEdgeClass(name, src, dst, cyclicOrderNorm)
    self.Edges.append(e)
    self.NumEdges = self.NumEdges + 1
    #now add a second edge in the reverse direction
    name = name + 'reverse' #add the string 'reverse' to the end of the 
                           #edges name as it is the reverse of what we added
    #reverse the order of src/dst as reverse edge direc
    eRev = cyclicEdgeClass(name, dst, src, cyclicOrderReverse)
    self.Edges.append(eRev)
    self.NumEdges = self.NumEdges + 1

    
   
    

#fills in the list of edges in cyclic order
#into the dictionary CyclicVerticesDict
#CALL THIS ONCE per VERTICE when all the edges for the vertice have been added
  def make_cyclic_dict_entry(self, vertice):
    #1.get list of all cyclicEdge objects with vertice as source
    unsortedCyclicEdgeList = []
    for cyclicedge in self.Edges:
       if cyclicedge.Src == vertice or cyclicedge.Dst == vertice:
          unsortedCyclicEdgeList.append(cyclicedge)

    #2.sort list of cyclicEdge objects by cyclic order number
    sortedCyclicEdgeList = sorted( unsortedCyclicEdgeList, key=lambda cyclicEdgeClass: cyclicEdgeClass.CyclicOrder)

    #3.insert the edge objects in cyclic order now into the dictionary in ribbonGraph 
    self.CyclicVerticesDict[vertice] = sortedCyclicEdgeList #works better if just insert as a list!!!
    #for index,cyclicedge in enumerate(sortedCyclicEdgeList):
      # if index >= 1:
         # self.CyclicVerticesDict[vertice].append(cyclicedge)
       



#next function (retuyrns nexts edges name)
#requires the edge to be in the dictionarry first!
  def get_cyclic_orders_next(self, verticeName, edgeName):
           # for index, object in enumerate(list)
          for index,cyclicedge in enumerate(self.CyclicVerticesDict[verticeName]):
             if cyclicedge.Name == edgeName:
                if index+1 >= len(self.CyclicVerticesDict[verticeName]):
                   #wrap around to start
                   print(self.CyclicVerticesDict[verticeName][0].Name)
                   return self.CyclicVerticesDict[verticeName][0].Name
                else:
                   #just add 1 to index to get next
                   print(self.CyclicVerticesDict[verticeName][index+1].Name)
                   return self.CyclicVerticesDict[verticeName][index+1].Name



#see the cyclic order list objects
  def get_cyclic_object(self, verticeName):
       print(self.CyclicVerticesDict[verticeName])



#see the cyclic order of edges one by one given a vertice
  def get_cyclic_order(self, verticeName):
      for cyclicedge in self.CyclicVerticesDict[verticeName]:
          print(cyclicedge.Name)






 
