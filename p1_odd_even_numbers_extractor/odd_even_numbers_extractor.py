class OddEvenNumbersExtractor:
    def __init__(self, filename: str = "./numbers.txt"):
        self.filename = filename

    def read_file(self) -> list[int]:
        try:
            with open(self.filename, "r") as file:
                return [int(number.strip()) for number in file.readlines()]
        except ValueError:
            print("File must only contain integers")
            return []
        except FileNotFoundError:
            print("File not found")
            return []

    def write_file(self, filename: str, content: int):
        with open(filename, "w") as file:
            file.write(str(content) + "\n")

    def categorize(self):
        data = self.read_file()
        for number in data:
            if number % 2 == 0:
                self.write_file("even_numbers.txt", number)
            else:
                self.write_file("odd_numbers.txt", number)

if __name__ == "__main__":
    extractor = OddEvenNumbersExtractor()
    extractor.categorize()