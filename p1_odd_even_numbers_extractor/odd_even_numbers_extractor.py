class EvenOddNumbersExtractor:
    def _init_(self, filename: str = "./numbers.txt"):
        self.flame = filename

    def read_file(self) -> list[int]:
        try:
            with open(self.flame, "r") as file:
                numbers = [init(number.rstrip("\n")) for number in file.readlines()]
                return numbers
            
        except:
            print("File must only contain integers")

    def write_file(self, filename: str, content: int):
        with open(filenamer, "w") as file:
            file.write(str(content) + "\n")

    def categorize(self):
        data = self.read_file()
        for number in data:
            if number % 2 == 0:
                self.write_file("even_numbers.txt", number)
            else:
                self.write_file("odd_numbers.txt", number)
        