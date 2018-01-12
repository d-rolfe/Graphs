# Graphs
a python library implementing a graph and edge class and various methods

README
================================================================
Author: Darren Rolfe

Installation
================================================================
Have Python 2.7.x installed.


Execution
================================================================
To run as a script:

python graphy.py

This will run the main method of the graph.py file, which displays
the output for the 10 questions.

To run the unit tests:

python unittests.py

If all tests pass, the script will output 'OK' at the end.


Developer Notes
================================================================
You may also want to use graph.py as a module, in which case you
can simply import it as normal.

import graph

You would then instantiate a graph object, and pass in a list of
strings that represent edges in a graph, following the given 
format:

my_graph = Graph(['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7'])

You can then call various methods of the Graph class for computing
paths, etc. There is a list of available methods below.

Design Notes
================================================================
The Graph class works by maintaining a map where in the keys of
the map are nodes and the values are lists of edges originating
from that node.

The edges in the map are represented using an Edge class, which has
a starting node, ending node, and the weight (distance) between
those nodes.

The methods for finding routes use a depth first search algorithm.


Graph Class Methods
================================================================
  compute_distance(self, route)
      compute the distance along a certain route

  depth_first_search(self, start, end, curr_route=[])
      finds a route between two nodes

  find_all_routes(self, start, end, curr_route=[])
      finds all routes between two nodes, no cycles allowed

  find_all_routes_with_cycles(self, start, end, curr_route=[], stops=None)
      finds all routes between two nodes with exactly stops number of stops, allowing cycles

  find_length_shortest_route(self, start, end)
      finds the distance of the shortest route from start to end

  find_number_routes_with_distance(self, start, end, distance)
      finds the number of routes from start to end with distance less than distance

  find_routes_with_distance(self, start, end, curr_route=[], distance=None)
      finds a route between two nodes with less than distance between them, allowing cycles

  get_number_routes_with_exactly_stops(self, start, end, stops=None)
      the number of different routes between two nodes with exactly stops number of stops

  get_number_routes_with_max_stops(self, start, end, max_stops=None)
      the number of different routes between two nodes with a maximum of max_stops stops

  get_route_distance(self, route)
      returns the distance of a route
