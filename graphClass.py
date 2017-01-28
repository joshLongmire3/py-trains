class edgeClass:
  def __init__(self, name, src, dst):
    self.Name = name
    self.Src = src
    self.Dst = dst


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
