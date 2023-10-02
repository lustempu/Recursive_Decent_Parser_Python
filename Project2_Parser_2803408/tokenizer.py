from lexer import *
# from lexer import Integer, ID


def _scanToken(token: str):
    # idenentify type of token
    if token.isnumeric():
        return Integer(token)
    elif token.isalpha():
        return ID(token)
    else:
        return token


def scanToken(token: str):
    # collect characters of each token
    currentToken: str = ""
    if isinstance(token, str):
        # parse each character in token
        for c in token:
            # concatenate it to the current token
            currentToken += c

            # if token is an operator
            if c in "+-*/=()":

                # yield the previous token
                if len(currentToken) != 1:
                    yield _scanToken(currentToken[:-1])

                # then yield this operator
                yield currentToken[-1]
                # reset token
                currentToken = ""

            elif c == " ":
                # if space is after token
                if len(currentToken) != 1:
                    yield _scanToken(currentToken[:-1])
                # reset token/ ignore space
                currentToken = ""

        if len(currentToken) != 0:
            # yield the last operator
            yield _scanToken(currentToken)
    else:
        raise TypeError("input must be an instance of str")


if __name__ == "__main__":
    for token in scanToken(input()):
        print(type(token))
        print(token)
