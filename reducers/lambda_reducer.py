import functools

from reducer import Reducer
from result import Result
from typing import Callable, Iterable

class LambdaReducer(Reducer):
	def __init__(self, step: Callable[[Result, Result], Result]):
		self.step = step

	def reduce(self, results: Iterable[Result]) -> Result:
		return functools.reduce(self.step, results)
