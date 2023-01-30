import asyncio

from endpoint import Endpoint
from reducer import Reducer
from result import Result
from typing import Collection

class EndpointReducerProxy(Endpoint):

	def __init__(self, reducer: Reducer, endpoints: Collection[Endpoint]):
		self.reducer = reducer
		self.endpoints = endpoints

	async def get(self) -> Result:
		awaitables = [endpoint.get() for endpoint in self.endpoints]
		results = await asyncio.gather(*awaitables)
		return self.reducer.reduce(results)
