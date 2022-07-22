def validate_isbn(isbn):
    if len(isbn) != 10:
        return "invalid"

    isbn = [int(i) for i in isbn if i != 'x' and i != 'X']

    if len(isbn) == 9:  # this occurs when 'x' is omitted by previous procedure
        isbn.append(10)

    total = sum([(10 - i) * isbn[i] for i in range(len(isbn))])

    if total % 11 == 0:
        return "valid"
    else:
        return "invalid"


if __name__ == "__main__":
    isbn = "123456789x"
    print("'{}' is {} ISBN-10 number".format(isbn, validate_isbn(isbn)))
