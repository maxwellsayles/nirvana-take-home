from abc import ABC, abstractmethod
from result import Result
from typing import List

class Reducer(ABC):
	@abstractmethod
	def reduce(self, results: List[Result]) -> Result:
		...
