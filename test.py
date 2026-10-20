from pathlib import Path

folder = Path.home() / "Downloads"

print(folder)
print(folder.exists())
print(folder.is_dir())

for item in folder.iterdir():
    print(item.name)