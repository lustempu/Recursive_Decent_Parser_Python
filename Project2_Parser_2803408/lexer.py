"""

Class definitions for the program

"""


class TreeNode:
    # parent node
    """
    Lets break this TreeNode() class down:
    1. __init__():
        - initializes the class with a string or integer representation of the element
        - the def init function works like a constructor in python
        - the self keyword is used to represent the instance of the class
        - the arguments are optional, and are used to initialize the class with a string or integer representation of the element

    2. __str__():
        - just print the string representation itself

    """

    def __init__(self, itself: str | int = "") -> None:
        # string or integer representation of the element
        self.itself = itself

    def __str__(self) -> str:
        # just print the string representation itself
        return str(self.itself) + " "


class InfixOperator(TreeNode):
    # has operators  + - / *
    def __init__(self, itself: str | int, left: TreeNode, right: TreeNode) -> None:
        super().__init__(itself)
        self.left = left
        self.right = right

    def __str__(self) -> str:
        # print string of left -> this operator -> string of right
        return (
            "( " + self.left.__str__() + super().__str__() + self.right.__str__() + ") "
        )

    def eval(self, level: int = 1) -> int | float:
        # print level of depth in the recursive process, and the current evaluation
        print(f"Level_{level}:", self.left, super().__str__(), self.right)

        # use children method to evaluate the two sides, after recursively evaluate each side
        return self._eval(self.left.eval(level + 1), self.right.eval(level + 1))


class PrefixOperator(TreeNode):
    # negate
    def __init__(self, itself: str, arg: TreeNode) -> None:
        super().__init__(itself)
        self.arg = arg

    def __str__(self) -> str:
        # print operator -> operand
        return "( " + super().__str__() + self.arg.__str__() + ") "

    def eval(self, level: int = 1) -> int:
        # print level of depth in the recursive process, and the current evaluation
        print(f"Level_{level}:", super().__str__(), self.arg)

        # use children method to evaluate the two sides, after recursively evaluate each side
        return self._eval(self.arg.eval(level + 1))


class Add(InfixOperator):
    def __init__(self, left: TreeNode, right: TreeNode) -> None:
        super().__init__("+", left, right)

    def _eval(self, left: int | float, right: int | float) -> int | float:
        return left + right


class Subtract(InfixOperator):
    def __init__(self, left: TreeNode, right: TreeNode) -> None:
        super().__init__("-", left, right)

    def _eval(self, left: int | float, right: int | float) -> int | float:
        return left - right


class Mult(InfixOperator):
    def __init__(self, left: TreeNode, right: TreeNode) -> None:
        super().__init__("*", left, right)

    def _eval(self, left: int | float, right: int | float) -> int | float:
        return left * right


class Div(InfixOperator):
    def __init__(self, left: TreeNode, right: TreeNode) -> None:
        super().__init__("/", left, right)

    def _eval(self, left: int | float, right: int | float) -> int | float:
        return left / right


class Negate(PrefixOperator):
    def __init__(self, arg: TreeNode) -> None:
        super().__init__("-", arg)

    def _eval(self, arg: int | float) -> int | float:
        return -1 * arg


class Integer(TreeNode):
    def __init__(self, token) -> None:
        # validate token
        if isinstance(token, int) or (isinstance(token, str) and token.isnumeric()):
            # stor value of the integer
            self.val = int(token)
            super().__init__(str(self.val))
        else:
            super().__init__("")
            self.val = None
            raise TypeError("invalid token")

    def eval(self, level: int = 1) -> int:
        if self.val:
            print(f"Level_{level}:", self.val)
            return self.val
        else:
            raise TypeError("invalid token")


class ID(TreeNode):
    def __init__(self, token) -> None:
        # validate token
        if isinstance(token, str) and token.isalpha():
            self.val = token
            super().__init__(token)
        else:
            self.val = None
            super().__init__("")

        # the right-hand side of ID =
        self.equals: TreeNode = None

    def eval(self, level: int):
        # if there is an assigned TreeNode
        if self.equals:
            # print level of depth, and the right hand side current evaluation
            print(f"Level_{level}:", super().__str__(), "= ", self.equals)
            # evaluate the right hand side
            return self.equals.eval(level + 1)
        else:
            # return None
            return self.equals

    def __str__(self) -> str:
        if self.equals:
            return super().__str__() + "= " + self.equals.__str__()
        else:
            return super().__str__()
