import unittest

from result import Result
from reducers.average import AverageReducer

class TestAverageReducer(unittest.TestCase):
	def runTest(self):
		res1 = Result(1000, 10000, 5000)
		res2 = Result(1200, 13000, 6000)
		res3 = Result(1000, 10000, 6000)
		res = AverageReducer.reduce([res1, res2, res3])
		self.assertEqual(res.deductible, 1066)
		self.assertEqual(res.stop_loss, 11000)
		self.assertEqual(res.oop_max, 5666)
