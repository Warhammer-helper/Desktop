
class Profession:
	def __init__(self, name: str, stastistics: str):
		self.name : str = name
		self.stastistics : str = stastistics
		print(self.name + " has been created!")

	def getName(self):
		return self.name

	def getPrimary(self, primaryId: int):
		try:
			if (primaryId < 0 or primaryId > 7): raise IndexError
			result = int(self.stastistics[primaryId*2]) * 10 + int(self.stastistics[primaryId*2+1])
		except IndexError:
			result = 0
			print(Profession.__name__ + ": Invalid primary ability id")
		return result

	def getSecondary(self, secondaryId: int):
		try:
			if(secondaryId < 0 or secondaryId > 7): raise IndexError
			result = int(self.stastistics[secondaryId+16])
		except IndexError:
			result = 0
			print(Profession.__name__ + ": Invalid primary ability id")
		return result
