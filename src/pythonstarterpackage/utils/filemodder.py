class FileModder:

	@staticmethod
	def read_file(filepath: str) -> list:
		lines = []
		with open(filepath,'r') as f:
			for line in f:
				if line[0] != '#':
					lines.append(line.rstrip('\n'))
		return lines
