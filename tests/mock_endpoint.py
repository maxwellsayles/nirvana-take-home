from endpoint import Endpoint
from result import Result

class MockEndpoint(Endpoint):
	def __init__(self, deductible: int, stop_loss: int, oop_max: int):
		self.result = Result(deductible, stop_loss, oop_max)

	async def get(self) -> Result:
		return self.result
