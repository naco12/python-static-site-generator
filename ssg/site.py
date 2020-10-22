import pathlib
from pathlib import Path
# defining a class Site
class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)
