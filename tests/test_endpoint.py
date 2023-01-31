import asyncio
import unittest

from result import Result
from reducers.average_reducer import AverageReducer
from tests.mock_endpoint import *

class TestEndpoint(unittest.IsolatedAsyncioTestCase):
	async def testAverageOfEndpoints(self):
		m1 = MockEndpoint(1000, 10000, 5000)
		m2 = MockEndpoint(1200, 13000, 6000)
		m3 = MockEndpoint(1000, 10000, 6000)

		res1 = await m1.get()
		res2 = await m2.get()
		res3 = await m3.get()

		res = AverageReducer().reduce([res1, res2, res3])
		self.assertEqual(res.deductible, 1066)
		self.assertEqual(res.stop_loss, 11000)
		self.assertEqual(res.oop_max, 5666)
