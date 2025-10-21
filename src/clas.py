class CaError(Exception):
	def __init__(self, message: str) -> None:
		super().__init__(message)
		self.message = message


class CalcError:
	
	def __init__(self) -> None:
		pass

	def raise_error(self, message: str) -> None:
		raise CaError(message)

	def format(self, message: str) -> str:
		return f"Ошибка: {message}"
