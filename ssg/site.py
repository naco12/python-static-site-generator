import pathlib
from pathlib import Path
# defining a class Site
class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)
        
    # make a directory
    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

    # make the destination directory
    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                path.create_dir()
