import unittest
import graph

class TestGraphMethods(unittest.TestCase):
	def test_compute_distance(self):
		my_edge_list = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']
		my_graph = graph.Graph(my_edge_list)
		self.assertEqual(my_graph.compute_distance("A-B-C"), 9)
		self.assertEqual(my_graph.compute_distance("A-E-B-C"), 14)
		self.assertEqual(my_graph.compute_distance("A-E-B-C-D"), 22)
		self.assertEqual(my_graph.compute_distance("A-E-B-C-D-E"), 28)
		self.assertEqual(my_graph.compute_distance("A-E-B-C-D-E-B"), 31)
		self.assertEqual(my_graph.compute_distance("A-E-B-C-D-E-B-C"), 35)
		with self.assertRaises(Exception):
			my_graph.compute_distance("dffg12")
		with self.assertRaises(Exception):
			my_graph.compute_distance("A-")
		with self.assertRaises(Exception):
			my_graph.compute_distance("A-B-")
		with self.assertRaises(Exception):
			my_graph.compute_distance("-B-")
		self.assertEqual(my_graph.compute_distance("A"), 0)
		self.assertEqual(my_graph.compute_distance("A-E-Z-C"), 'NO SUCH ROUTE')
		with self.assertRaises(Exception):
			my_graph.compute_distance("AEZC")
		with self.assertRaises(Exception):
			my_graph.compute_distance([])
		with self.assertRaises(Exception):
			my_graph.compute_distance(["A", "B"])
		with self.assertRaises(Exception):
			my_graph.compute_distance(["AEZC"])
		with self.assertRaises(Exception):
			my_graph.compute_distance(["A-B-C"])
		with self.assertRaises(Exception):
			my_graph.compute_distance(10)

	def test_find_all_routes(self):
		my_edge_list = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']
		my_graph = graph.Graph(my_edge_list)
		AE7 = graph.Edge("A", "E", 7)
		EB3 = graph.Edge("E", "B", 3)
		AB5 = graph.Edge("A", "B", 5)
		DE6 = graph.Edge("D", "E", 6)
		BC4 = graph.Edge("B", "C", 4)
		CD8 = graph.Edge("C", "D", 8)
		DC8 = graph.Edge("D", "C", 8)
		CE2 = graph.Edge("C", "E", 2)
		AD5 = graph.Edge("A", "D", 5)
		self.assertItemsEqual(my_graph.find_all_routes("A", "A"), [])
		self.assertItemsEqual(my_graph.find_all_routes("A", "B"), [ [AE7, EB3], [AB5], [AD5, DE6, EB3], [AD5, DC8, CE2, EB3], [AD5, DC8, CD8, DE6, EB3] ])
		self.assertItemsEqual(my_graph.find_all_routes("A", "6"), [])
		self.assertItemsEqual(my_graph.find_all_routes("0", "C"), [])
		self.assertItemsEqual(my_graph.find_all_routes("foo", "bar"), [])
		self.assertItemsEqual(my_graph.find_all_routes(7, "z"), [])
		with self.assertRaises(Exception):
			self.assertItemsEqual(my_graph.find_all_routes([], "C"), [])

	def test_find_all_routes_with_cycles(self):
		my_edge_list = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']
		my_graph = graph.Graph(my_edge_list)
		AE7 = graph.Edge("A", "E", 7)
		EB3 = graph.Edge("E", "B", 3)
		AB5 = graph.Edge("A", "B", 5)
		DE6 = graph.Edge("D", "E", 6)
		BC4 = graph.Edge("B", "C", 4)
		CD8 = graph.Edge("C", "D", 8)
		DC8 = graph.Edge("D", "C", 8)
		CE2 = graph.Edge("C", "E", 2)
		AD5 = graph.Edge("A", "D", 5)
		self.assertItemsEqual(my_graph.find_all_routes_with_cycles("A", "A", stops=5), [])
		self.assertItemsEqual(my_graph.find_all_routes_with_cycles("A", "B", stops=5), [[AD5, DC8, CD8, DE6, EB3], [AB5, BC4, CD8, DE6, EB3], [AE7, EB3, BC4, CE2, EB3]])
		self.assertItemsEqual(my_graph.find_all_routes_with_cycles("A", "6", stops=5), [])
		self.assertItemsEqual(my_graph.find_all_routes_with_cycles("0", "C", stops=5), [])
		self.assertItemsEqual(my_graph.find_all_routes_with_cycles("foo", "bar", stops=5), [])
		self.assertItemsEqual(my_graph.find_all_routes_with_cycles(7, "z", stops=5), [])
		with self.assertRaises(Exception):
			result = my_graph.find_all_routes_with_cycles([], "C", stops=5)
			self.assertItemsEqual(result, [])

	def test_get_route_distance(self):
		my_edge_list = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']
		my_graph = graph.Graph(my_edge_list)
		AE7 = graph.Edge("A", "E", 7)
		EB3 = graph.Edge("E", "B", 3)
		AB5 = graph.Edge("A", "B", 5)
		DE6 = graph.Edge("D", "E", 6)
		BC4 = graph.Edge("B", "C", 4)
		CD8 = graph.Edge("C", "D", 8)
		DC8 = graph.Edge("D", "C", 8)
		CE2 = graph.Edge("C", "E", 2)
		AD5 = graph.Edge("A", "D", 5)
		self.assertEqual(my_graph.get_route_distance([AD5, DE6, EB3]), 14)
		self.assertEqual(my_graph.get_route_distance([AD5, DC8, CD8, DE6, EB3]), 30)
		self.assertEqual(my_graph.get_route_distance([]), 0)
		self.assertEqual(my_graph.get_route_distance([AD5]), 5)

	def test_find_routes_with_distance(self):
		my_edge_list = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']
		my_graph = graph.Graph(my_edge_list)
		AE7 = graph.Edge("A", "E", 7)
		EB3 = graph.Edge("E", "B", 3)
		AB5 = graph.Edge("A", "B", 5)
		DE6 = graph.Edge("D", "E", 6)
		BC4 = graph.Edge("B", "C", 4)
		CD8 = graph.Edge("C", "D", 8)
		DC8 = graph.Edge("D", "C", 8)
		CE2 = graph.Edge("C", "E", 2)
		AD5 = graph.Edge("A", "D", 5)
		self.assertItemsEqual(my_graph.find_routes_with_distance("A", "A", distance=5), [])
		self.assertItemsEqual(my_graph.find_routes_with_distance("A", "B", distance=11), [ [AE7, EB3], [AB5]])
		self.assertItemsEqual(my_graph.find_routes_with_distance("A", "6", distance=5), [])
		self.assertItemsEqual(my_graph.find_routes_with_distance("0", "C", distance=5), [])
		self.assertItemsEqual(my_graph.find_routes_with_distance("foo", "bar", distance=5), [])
		self.assertItemsEqual(my_graph.find_routes_with_distance(7, "z", distance=5), [])
		with self.assertRaises(Exception):
			result = my_graph.find_routes_with_distance([], "C", distance=5)
			self.assertItemsEqual(result, [])

	def test_find_number_routes_with_distance(self):
		my_edge_list = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']
		my_graph = graph.Graph(my_edge_list)
		self.assertEqual(my_graph.find_number_routes_with_distance("A", "A", distance=5), 0)
		self.assertEqual(my_graph.find_number_routes_with_distance("A", "B", distance=11), 2)
		self.assertEqual(my_graph.find_number_routes_with_distance("A", "6", distance=5), 0)
		self.assertEqual(my_graph.find_number_routes_with_distance("0", "C", distance=5), 0)
		self.assertEqual(my_graph.find_number_routes_with_distance("foo", "bar", distance=5), 0)
		self.assertEqual(my_graph.find_number_routes_with_distance(7, "z", distance=5), 0)
		with self.assertRaises(Exception):
			result = my_graph.find_number_routes_with_distance([], "C", distance=5)
			self.assertEqual(result, 0)

	def test_get_number_routes_with_max_stops(self):
		my_edge_list = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']
		my_graph = graph.Graph(my_edge_list)
		AE7 = graph.Edge("A", "E", 7)
		EB3 = graph.Edge("E", "B", 3)
		AB5 = graph.Edge("A", "B", 5)
		DE6 = graph.Edge("D", "E", 6)
		BC4 = graph.Edge("B", "C", 4)
		CD8 = graph.Edge("C", "D", 8)
		DC8 = graph.Edge("D", "C", 8)
		CE2 = graph.Edge("C", "E", 2)
		AD5 = graph.Edge("A", "D", 5)
		self.assertEqual(my_graph.get_number_routes_with_max_stops("A", "A", max_stops=5), 0)
		self.assertEqual(my_graph.get_number_routes_with_max_stops("A", "B", max_stops=5), 8)
		self.assertEqual(my_graph.get_number_routes_with_max_stops("A", "6", max_stops=5), 0)
		self.assertEqual(my_graph.get_number_routes_with_max_stops("0", "C", max_stops=5), 0)
		self.assertEqual(my_graph.get_number_routes_with_max_stops("foo", "bar", max_stops=5), 0)
		self.assertEqual(my_graph.get_number_routes_with_max_stops(7, "z", max_stops=5), 0)
		with self.assertRaises(Exception):
			result = my_graph.get_number_routes_with_max_stops([], "C", max_stops=5)
			self.assertEqual(result, 0)

	def test_get_number_routes_with_exactly_stops(self):
		my_edge_list = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']
		my_graph = graph.Graph(my_edge_list)
		AE7 = graph.Edge("A", "E", 7)
		EB3 = graph.Edge("E", "B", 3)
		AB5 = graph.Edge("A", "B", 5)
		DE6 = graph.Edge("D", "E", 6)
		BC4 = graph.Edge("B", "C", 4)
		CD8 = graph.Edge("C", "D", 8)
		DC8 = graph.Edge("D", "C", 8)
		CE2 = graph.Edge("C", "E", 2)
		AD5 = graph.Edge("A", "D", 5)
		self.assertEqual(my_graph.get_number_routes_with_exactly_stops("A", "A", stops=5), 0)
		self.assertEqual(my_graph.get_number_routes_with_exactly_stops("A", "B", stops=5), 3)
		self.assertEqual(my_graph.get_number_routes_with_exactly_stops("A", "6", stops=5), 0)
		self.assertEqual(my_graph.get_number_routes_with_exactly_stops("0", "C", stops=5), 0)
		self.assertEqual(my_graph.get_number_routes_with_exactly_stops("foo", "bar", stops=5), 0)
		self.assertEqual(my_graph.get_number_routes_with_exactly_stops(7, "z", stops=5), 0)
		with self.assertRaises(Exception):
			result = my_graph.get_number_routes_with_exactly_stops([], "C", stops=5)
			self.assertEqual(result, 0)

	def test_find_length_shortest_route(self):
		my_edge_list = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']
		my_graph = graph.Graph(my_edge_list)
		AE7 = graph.Edge("A", "E", 7)
		EB3 = graph.Edge("E", "B", 3)
		AB5 = graph.Edge("A", "B", 5)
		DE6 = graph.Edge("D", "E", 6)
		BC4 = graph.Edge("B", "C", 4)
		CD8 = graph.Edge("C", "D", 8)
		DC8 = graph.Edge("D", "C", 8)
		CE2 = graph.Edge("C", "E", 2)
		AD5 = graph.Edge("A", "D", 5)
		self.assertEqual(my_graph.find_length_shortest_route("A", "A"), "NO SUCH ROUTE")
		self.assertEqual(my_graph.find_length_shortest_route("A", "B"), 5)
		self.assertEqual(my_graph.find_length_shortest_route("A", "C"), 9)
		self.assertEqual(my_graph.find_length_shortest_route("A", "D"), 5)
		self.assertEqual(my_graph.find_length_shortest_route("A", "E"), 7)
		self.assertEqual(my_graph.find_length_shortest_route("C", "D"), 8)
		self.assertEqual(my_graph.find_length_shortest_route("D", "C"), 8)
		self.assertEqual(my_graph.find_length_shortest_route("E", "B"), 3)
		self.assertEqual(my_graph.find_length_shortest_route("A", "6"), "NO SUCH ROUTE")
		self.assertEqual(my_graph.find_length_shortest_route("0", "C"), "NO SUCH ROUTE")
		self.assertEqual(my_graph.find_length_shortest_route("foo", "bar"), "NO SUCH ROUTE")
		self.assertEqual(my_graph.find_length_shortest_route(7, "z"), "NO SUCH ROUTE")
		with self.assertRaises(Exception):
			self.assertEqual(my_graph.find_length_shortest_route([], "C"), "NO SUCH ROUTE")

if __name__ == '__main__':
    unittest.main()