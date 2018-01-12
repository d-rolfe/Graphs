""" Edge class used to represent edges in a graph """

class Edge():
	def __init__(self, start=None, end=None, weight=None):
		""" initializes an edge object """
		self.start = start
		self.end = end
		self.weight = int(weight)

	def __eq__(self, other):
		if isinstance(self, other.__class__):
			return self.__dict__ == other.__dict__
		return False

	def __ne__(self, other):
		return not self.__eq__(other)

	def __repr__(self):
		return self.start + self.end + str(self.weight)

	def __str__(self):
		return self.start + self.end + str(self.weight)