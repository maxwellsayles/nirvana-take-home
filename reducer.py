from abc import ABC, abstractmethod
from result import Result
from typing import List

class Reducer(ABC):
	@staticmethod
	@abstractmethod
	def reduce(results: List[Result]) -> Result:
		...
