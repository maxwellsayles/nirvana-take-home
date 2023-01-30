import asyncio
import unittest

from endpoint_reducer_proxy import EndpointReducerProxy
from result import Result
from reducers.average import AverageReducer
from tests.mock_endpoint import *

class TestEndpointReducerProxy(unittest.IsolatedAsyncioTestCase):
	async def testAverage(self):
		m1 = MockEndpoint1()
		m2 = MockEndpoint2()
		m3 = MockEndpoint3()

		proxy = EndpointReducerProxy(AverageReducer(), [m1, m2, m3])
		res = await proxy.get()
		self.assertEqual(res.deductible, 1066)
		self.assertEqual(res.stop_loss, 11000)
		self.assertEqual(res.oop_max, 5666)
