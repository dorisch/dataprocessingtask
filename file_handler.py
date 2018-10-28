import os

class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        
    def file_ext(self):
        name, ext = os.path.splitext(self.filename)
        return ext.lower()



