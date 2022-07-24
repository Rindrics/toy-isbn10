import re


class ISBN10:
    def __init__(self, isbn):
        self.code = isbn
        self.validate()


    def validate(self):
        self._check_length()
        self._check_digits()
        self._check_tenth_char()
        self._check_sum()


    def _check_length(self):
        if len(self.code) != 10:
            raise ValueError("Length of code: {} (should be 10)".format(len(self.code)))


    def _check_digits(self):
        invalid_chars = re.findall("\\D", self.code[:-1])
        if invalid_chars:
            raise ValueError(
                "Only digits are allowed for the 1st--9th character (found: " +
                ", ".join(invalid_chars) +
                ")"
                )


    def _check_tenth_char(self):
        non_numeric = re.match("\\D", self.code[-1])
        non_x = re.match("[^xX]", self.code[-1])
        if non_numeric and non_x:
            raise ValueError(
                "Only digits or 'X' ('x') are allowed for the 10th character(found: '" +
                non_x[0] +
                "')"
                )


    def _check_sum(self):
        code_int = [int(i) for i in self.code if i != 'x' and i != 'X']

        if len(code_int) == 9:  # this occurs when 'x' is omitted by previous procedure
            code_int.append(10)

        total = sum([(10 - i) * code_int[i] for i in range(len(code_int))])

        if total % 11 != 0:
            raise ValueError("Incorrect combination of digits")


if __name__ == "__main__":
    isbns = [
        "123456789x",
        "123456789a",
        "1234567890",
        "abc4567890",
        "too-short",
        "too-loooooooong",
        ]

    for i in isbns:
        try:
            ISBN10(i)
            print("'{}' is valid ISBN-10 number".format(i))
        except ValueError as error:
            print("{}: '{}'".format(error, i))
