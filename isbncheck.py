class ISBN10:
    def __init__(self, isbn):
        self.code = isbn
        self.validate()

    def validate(self):
        if len(self.code) != 10:
            raise ValueError

        code_int = [int(i) for i in self.code if i != 'x' and i != 'X']

        if len(code_int) == 9:  # this occurs when 'x' is omitted by previous procedure
            code_int.append(10)

        total = sum([(10 - i) * code_int[i] for i in range(len(code_int))])

        if total % 11 != 0:
            raise ValueError


if __name__ == "__main__":
    isbn = "123456789x"
    print("'{}' is valid ISBN-10 number".format(isbn))
