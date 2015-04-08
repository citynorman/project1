import MySQLdb
#To be used as a base class for representing data from a data table in the mySQL database.

class DataTable:
	def __init__(self, db, name):
		self.db = db
		self.name = name
		self.dbc = self.db.cursor()
		self.debug = 1

	def __getitem__(self, item): #Creates single item.
		self.dbc.execute("select * from %s limit %s, 1" \
			% (self.name, item))
		return self.dbc.fetchone()

	def __iter__(self):
		"""creates a data set
			and returns an iterator (self)"""
		q = "select * from %s" % (self.name)
		self._query(q)
		# an Iterator is an object with a next() method
		return self

	def next(self):
		"""returns the next item in the data set,
			or tells Python to stop"""
		r = self.dbc.fetchone()
		if not r:
			raise StopIteration #Handle and rethrow here?
		return r

	def _query(self, q):
		if self.debug: print "Query: %s" % (q)
		self.dbc.execute(q)
