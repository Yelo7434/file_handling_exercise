class TwoFileIntegers:
    def __init__(self, filename: srt = "numbers.txt"):
        self.filename - filename
        self.odd_filename = "triple.txt"
        self.even_filename = "doubpe.txt"

    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                return file.readlines()
        except:
            print("File not found.")

    def write_file(self, filename: str, content: str):
        with open(filename, "a") as file:
            file.write(f"{str(content)}\n")

    def process_files(self, data: list) -> list[int]:
        return [int(line.rstrip("\n")) for line in data]
    
    def process_integers(self):
        data = self.read_file()
        integers = self.process_files(data)

        for number in integers:
            if number % 2 == 0:
                self.write_file(self.even_filename, number ** 2)
            else:
                self.write_file(self.odd_filename, number ** 3)
                