class Vertex:
	def __init__ (self, vertex):
		self.name = vertex
		self.adjacents = {}

	def __str__ (self):
		return str(self.name) + ' neighbour: ' + str([x.name for x in self.adjacents])

	def add_neighbour(self, neighbour, distance=0):
		self.adjacents[neighbour] = distance

	def get_connections(self):
		return self.adjacents.keys()

	def get_name(self):
		return self.name

	def get_distance(self, neighbour):
		return self.adjacents[neighbour]


class Graph:
	def __init__ (self):
		self.vert_dict = {}
		self.num_vertices = 0

	def __iter__ (self):
		return iter(self.vert_dict.values())

	def add_vertex(self, node):
		self.num_vertices = self.num_vertices + 1
		new_vertex = Vertex(node)
		self.vert_dict[node] = new_vertex
		return new_vertex

	def get_vertex(self, index):
		if index in self.vert_dict:
			return self.vert_dict[index]
		else:
			return None

	def add_edge(self, start, dest, distance = 0):
		if start not in self.vert_dict:
			self.add_vertex(start)
		if dest not in self.vert_dict:
			self.add_vertex(dest)

		self.vert_dict[start].add_neighbour(self.vert_dict[dest], distance)
		self.vert_dict[dest].add_neighbour(self.vert_dict[start], distance)

	def get_vertices(self):
		return self.vert_dict.keys()

def dijkstra(g, start, destination):
	best_path = {}
	visited = {}
	current = float('inf')
	total = 0
	current_node = g.get_vertex(start)
	destination_node = g.get_vertex(destination)


	while True:
		print '(current node is = %s)' %(current_node)
		for next_node in current_node.get_connections():
			#mark nodes that have been visited and put into best path
			visited[current_node.get_name()] = current_node.get_name()
			best_path[current_node.get_name()] = current_node.get_name()
			#check each node distance and ignore node if it is in visited array
			if ((current_node.get_distance(next_node) < current) and (next_node.get_name() not in visited) ):
				current = current_node.get_distance(next_node)
				bestNodeSoFar = next_node
		#set new current node
		total += current_node.get_distance(bestNodeSoFar)
		current_node = bestNodeSoFar
		current = float('inf') # reset the current distance for a new node
		
		#break out of loop if shortest path is found
		if (current_node == destination_node):
			print '(final node is = %s)' %(current_node.get_name())
			print 'total distance to node is: %s' %(total)
			best_path[current_node.get_name()] = current_node.get_name()
			break
		
if __name__ == '__main__':

    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)  
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    dijkstra(g, 'a', 'f')

    #for v in g:
     #   for w in v.get_connections():
       #     vid = v.get_name()
      #      wid = w.get_name()
     #       print '( %s , %s, %3d)'  % ( vid, wid, v.get_distance(w))

    #for v in g:
     #   print 'g.vert_dict[%s]=%s' %(v.get_name(), g.vert_dict[v.get_name()])
