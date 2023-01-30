from endpoint import Endpoint
from result import Result

class MockEndpoint1(Endpoint):
	async def get(self) -> Result:
		return Result(1000, 10000, 5000)

class MockEndpoint2(Endpoint):
	async def get(self) -> Result:
		return Result(1200, 13000, 6000)

class MockEndpoint3(Endpoint):
	async def get(self) -> Result:
		return Result(1000, 10000, 6000)
