from abc import ABC, abstractmethod
from result import Result

class Endpoint(ABC):
	@abstractmethod
	async def get(self) -> Result:
		...
