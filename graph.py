import pdb
import re
from edge import Edge

""" The Graph class works by maintaining a map where in the keys of
the map are nodes and the values are lists of edges originating
from that node. """

class Graph():
	def __init__(self, edges=[]):
		self.graph_map = {}
		self.edges = []
		""" populate edge list """
		for edge in edges:
			self.edges.append(Edge(edge[0], edge[1], int(edge[2])))
		""" populate graph map """
		for edge in self.edges:
			if edge.start not in self.graph_map:
				self.graph_map[edge.start] = []
				self.graph_map[edge.start].append(edge)
			elif edge.start in self.graph_map:
				self.graph_map[edge.start].append(edge)


	def get_edges(self):
		return self.edges

	def get_graph_map(self):
		return self.graph_map

	def compute_distance(self, route):
		""" compute the distance along a certain route """
		if not re.match(r'^[A-Z](-[A-Z])*$', route):
			raise Exception("Invalid input route syntax")
		route_nodes = route.split('-')
		if not route_nodes:
			return 'NO SUCH ROUTE'

		curr_node = route_nodes[0]
		distance = 0;
		for target_node in route_nodes[1:]:
			""" check if edge exists from curr_node to target_node """
			if self.graph_map[curr_node]:
				for edge in self.graph_map[curr_node]:
					if edge.end == target_node:
						distance += int(edge.weight)
						curr_node = target_node
						break
				# out of loop
				""" handle if edge to target_node not found """
				if curr_node != target_node:
					return 'NO SUCH ROUTE'
			else:
				return 'NO SUCH ROUTE'
		return distance

	def depth_first_search(self, start, end, curr_route=[]):
		""" finds a route between two nodes """
		if start not in self.graph_map or end not in self.graph_map:
			return curr_route

		curr_node = start
		edge_list = self.graph_map[curr_node]

		if not edge_list:
			return curr_route

		for edge in edge_list:
			if edge.end == end:
				curr_route.append(edge)
				return curr_route
			elif edge not in curr_route:
				curr_route.append(edge)
				curr_route = self.depth_first_search(edge.end, end, curr_route)
				return curr_route

	def find_all_routes(self, start, end, curr_route=[]):
		""" finds all routes between two nodes, no cycles allowed """
		try:
			if start not in self.graph_map or end not in self.graph_map:
				return []
		except Exception:
			print "Invalid input"
			raise

		if start == end and curr_route != []:
			return [curr_route]

		edge_list = self.graph_map[start]
		if not edge_list:
			return [curr_route]

		routes = []
		for edge in edge_list:
			if edge not in curr_route:
				curr_route.append(edge)
				found_routes = self.find_all_routes(edge.end, end, list(curr_route))
				for route in found_routes:
					routes.append(route)
				curr_route.pop()
		return routes

	def find_all_routes_with_cycles(self, start, end, curr_route=[], stops=None):
		""" finds all routes between two nodes with exactly stops number of stops, allowing cycles """
		if not stops:
			return []

		try:
			if start not in self.graph_map or end not in self.graph_map:
				return []
		except Exception:
			print "Invalid input"
			raise

		if len(curr_route) > stops:
			return []

		if start == end and curr_route != []:
			if len(curr_route) == stops:
				return [curr_route]

		edge_list = self.graph_map[start]
		if not edge_list:
			return [curr_route]

		routes = []
		for edge in edge_list:
			curr_route.append(edge)
			found_routes = self.find_all_routes_with_cycles(edge.end, end, list(curr_route), stops)
			for route in found_routes:
				if route not in routes:
					routes.append(route)
			curr_route.pop()
		return routes

	def get_number_routes_with_max_stops(self, start, end, max_stops=None):
		""" the number of different routes between two nodes with a maximum of max_stops stops """
		routes = []

		for i in range(1, max_stops+1):
			found_routes = self.find_all_routes_with_cycles(start, end, [], i)
			if found_routes:
				for route in found_routes:
					if route:
						routes.append(route)
		return len(routes)

	def get_number_routes_with_exactly_stops(self, start, end, stops=None):
		""" the number of different routes between two nodes with exactly stops number of stops """
		routes = []
		routes = self.find_all_routes_with_cycles(start, end, [], stops)
		return len(routes)

	def find_length_shortest_route(self, start, end):
		""" finds the distance of the shortest route from start to end"""
		routes = self.find_all_routes(start, end)
		smallest = None
		for route in routes:
			route_distance = 0
			for edge in route:
				edge_distance = int(edge.weight)
				route_distance += edge_distance
			if smallest:
				if smallest[1] > route_distance:
					smallest = (route, route_distance)
			else:
				smallest = (route, route_distance)
		if smallest:
			return smallest[1]
		else:
			return "NO SUCH ROUTE"

	def get_route_distance(self, route):
		""" returns the distance of a route """
		if not route:
			return 0
		route_distance = 0
		for edge in route:
			route_distance += int(edge.weight)
		return route_distance

	def find_routes_with_distance(self, start, end, curr_route=[], distance=None):
		""" finds a route between two nodes with less than distance between them, allowing cycles """
		routes = []
		if start not in self.graph_map or end not in self.graph_map:
			return []

		if self.get_route_distance(curr_route) > distance:
			return []

		if start == end and curr_route != []:
			if self.get_route_distance(curr_route) == distance:
				pass
			elif self.get_route_distance(curr_route) < distance:
				routes.append(curr_route)

		edge_list = self.graph_map[start]
		if not edge_list:
			return [curr_route]

		for edge in edge_list:
			curr_route.append(edge)
			found_routes = self.find_routes_with_distance(edge.end, end, list(curr_route), distance)
			for route in found_routes:
				if route not in routes:
					routes.append(route)
			curr_route.pop()
		return routes

	def find_number_routes_with_distance(self, start, end, distance):
		""" finds the number of routes from start to end with distance less than distance """
		routes = []
		routes = self.find_routes_with_distance(start, end, [], distance)
		return len(routes)
		

def main():
	my_edge_list = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']
	my_graph = Graph(my_edge_list)
	# print "Edges: {edges}".format(edges=my_graph.get_edges())
	# print "Graph: {graph}".format(graph=my_graph.get_graph_map())
	print "1. The distance of the route A-B-C..... {answer}".format(answer=my_graph.compute_distance("A-B-C"))
	print "2. The distance of the route A-D..... {answer}".format(answer=my_graph.compute_distance("A-D"))
	print "3. The distance of the route A-D-C..... {answer}".format(answer=my_graph.compute_distance("A-D-C"))
	print "4. The distance of the route A-E-B-C-D..... {answer}".format(answer=my_graph.compute_distance("A-E-B-C-D"))
	print "5. The distance of the route A-E-D..... {answer}".format(answer=my_graph.compute_distance("A-E-D"))
	print "6. The number of trips starting at C and ending at C with a maximum of 3 stops..... {answer}".format(answer=my_graph.get_number_routes_with_max_stops('C', 'C', 3))
	print "7. The number of trips starting at A and ending at C with exactly 4 stops..... {answer}".format(answer=my_graph.get_number_routes_with_exactly_stops('A', 'C', 4))
	print "8. The length of the shortest route (in terms of distance to travel) from A to C.....{answer}".format(answer=my_graph.find_length_shortest_route('A', 'C'))
	print "9. The length of the shortest route (in terms of distance to travel) from B to B.....{answer}".format(answer=my_graph.find_length_shortest_route('B', 'B'))
	print "10. The number of different routes from C to C with a distance of less than 30.....{answer}".format(answer=my_graph.find_number_routes_with_distance('C', 'C', 30))

if __name__ == "__main__":
	main()


