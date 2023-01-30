import asyncio
import unittest

from result import Result
from reducers.average import AverageReducer
from tests.mock_endpoint import *

class TestEndpoint(unittest.IsolatedAsyncioTestCase):
	async def testAverageOfEndpoints(self):
		m1 = MockEndpoint1()
		m2 = MockEndpoint2()
		m3 = MockEndpoint3()

		res1 = await m1.get()
		res2 = await m2.get()
		res3 = await m3.get()

		res = AverageReducer().reduce([res1, res2, res3])
		self.assertEqual(res.deductible, 1066)
		self.assertEqual(res.stop_loss, 11000)
		self.assertEqual(res.oop_max, 5666)
