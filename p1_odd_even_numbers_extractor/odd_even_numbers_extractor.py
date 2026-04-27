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

            