from reducer import Reducer
from result import Result
from typing import Iterable

class AverageReducer(Reducer):
	@staticmethod
	def reduce(results: Iterable[Result]) -> Result:
		def avg(xs: Iterable[int]) -> int:
			xs = list(xs)
			return sum(xs) // len(xs)

		deductible = avg(map(lambda r: r.deductible, results))
		stop_loss = avg(map(lambda r: r.stop_loss, results))
		oop_max = avg(map(lambda r: r.oop_max, results))
		return Result(deductible, stop_loss, oop_max)
