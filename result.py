class Result(object):
	def __init__(self, deductible: int, stop_loss: int, oop_max: int):
		self.deductible = deductible
		self.stop_loss = stop_loss
		self.oop_max = oop_max

	def __repr__(self) -> str:
		return '{{deductible: {0}, stop_loss: {1}, oop_max: {2}}}'.format(
			self.deductible,
			self.stop_loss,
			self.oop_max,
		)
