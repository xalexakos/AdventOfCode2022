class ParseData:
    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        f = open(self.filepath)
        return [line.rstrip() for line in f.readlines()]
