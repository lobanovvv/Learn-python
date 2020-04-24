from pathlib import Path

# Create instance object with relative path
path = Path("email")
print(path.exists()) # False

path.mkdir()
print(path.exists()) # True

path.rmdir()
print(path.exists()) # False

