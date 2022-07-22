class ISBN10:
    def __init__(self, isbn):
        self.isbn = isbn

    def validate_isbn10(self):
        if len(self.isbn) != 10:
            return "invalid"

        self.isbn = [int(i) for i in self.isbn if i != 'x' and i != 'X']

        if len(self.isbn) == 9:  # this occurs when 'x' is omitted by previous procedure
            self.isbn.append(10)

        total = sum([(10 - i) * self.isbn[i] for i in range(len(self.isbn))])

        if total % 11 == 0:
            return "valid"
        else:
            return "invalid"


if __name__ == "__main__":
    isbn = "123456789x"
    print("'{}' is {} ISBN-10 number".format(isbn, ISBN10().validate_isbn10(isbn)))
