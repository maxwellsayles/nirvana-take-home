import asyncio
import unittest

from endpoint import Endpoint
from endpoint_reducer_proxy import EndpointReducerProxy
from result import Result
from reducers.average_reducer import AverageReducer
from reducers.lambda_reducer import LambdaReducer
from tests.mock_endpoint import *
from typing import List

class TestEndpointReducerProxy(unittest.IsolatedAsyncioTestCase):
	def setUp(self):
		self.endpoints = self.getMockEndpoints([(1000, 10000, 5000),
												(1200, 13000, 6000),
												(1000, 10000, 6000),
												])

	def getMockEndpoints(self,
						 results: List[tuple[int, int, int]],
						 ) -> List[Endpoint]:
		return list(map(
			lambda res: MockEndpoint(res[0], res[1], res[2]),
			results,
		))

	async def testAverage(self):
		proxy = EndpointReducerProxy(AverageReducer(), self.endpoints)
		res = await proxy.get()
		self.assertEqual(res.deductible, 1066)
		self.assertEqual(res.stop_loss, 11000)
		self.assertEqual(res.oop_max, 5666)

	async def testLambda(self):
		# Return first result when sorting by
		# (oop_max asc, deductible asc, stop_loss desc)
		def step(acc, res):
			if acc.oop_max < res.oop_max:
				return acc
			elif acc.deductible < res.deductible:
				return acc
			elif acc.stop_loss > res.stop_loss:
				return acc
			else:
				return res

		proxy = EndpointReducerProxy(LambdaReducer(step), self.endpoints)
		res = await proxy.get()
		self.assertEqual(res.deductible, 1000)
		self.assertEqual(res.stop_loss, 10000)
		self.assertEqual(res.oop_max, 5000)
