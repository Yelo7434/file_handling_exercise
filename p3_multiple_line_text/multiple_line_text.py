class MultipleLineText:
    def __init__(self, filename: str = "mylife.txt"):
        self.filename = filename

    def multiple_line_text(self):
        try:
            with open(self.filename, 'a') as file:
                while True:
                    text = input("Enter line: ")
                    more = input("Are there more lines (y/n)? ")
                    file.write(text + "\n")
                    
                    if more != 'y':
                        break