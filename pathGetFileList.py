from pathlib import Path

path1 = Path(".")
arrWithFileList = path1.glob('*.py')
for item in arrWithFileList:
	print(item)
