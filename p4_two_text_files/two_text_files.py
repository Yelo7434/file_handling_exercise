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
    