# Create a custom stream that duplicates stdout
class CustomStream:
    def __init__(self, file, stdout):
        self.file = file
        self.stdout = stdout
    def write(self, text):
        # Write to both the file and the original stdout
        self.file.write(text)
        self.stdout.write(text)