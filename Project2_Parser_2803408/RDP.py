"""
run from RDP = main


--- Luke Stempuzis
--- 2803408
--- 10/13/22
--- Project 2 Recursive Decent Parser to evaluate an Arithmetic Equation

========= <>   Documentation <>    =============

-Union:
    -- https://peps.python.org/pep-0604/
    -- in python 3.10 PEP 604 – Allow writing union types as 'X | Y'

- yield: seemed like what he wanted based on the video, i got it to work properly
    -- generators -> https://www.programiz.com/python-programming/generator
    -- generators are functions that return an iterable set of items, one at a time, in a special way meaning they can be iterated upon

    
    
    Python Generator functions allow you to declare a function that behaves likes an iterators
    -- It is used to abstract a container of data to make it behave like an iterable object.

https://realpython.com/introduction-to-python-generators/ -> stuff on yield generators

------------------------------------------------------------------------------------

==== <> Notes from Video <>====
Precedence and Associativity
x + 5 * y ->(Should be interpreted as)-> x + (5*y)

Grammar for Expressions: Defines a Language

expr -> term + expr  		 // rule                                        E -> T+E
expr -> term – expr
expr -> term

term -> factor * term		 // term is a non-terminal here                 T -> F*T
term -> factor / term		 // the ‘/’ and ‘*’ are terminals               T -> F*T
term -> factor                                                              T->F

factor -> identifier		 // identifier is a set of tokens/things        F->ID
factor -> integer                                                           F->INT
factor -> (expr) 		    // parentheses are also terminal symbols        F ->E

Tokens: View the input as a series of tokens (would we use str functions here?)

expr -> term + expr | term – expr | term                                    E->T+E|T-E|T
term -> factor * term | factor/term | factor                                T->F*T|F/T|F
factor -> identifier | integer | (expr) – factor                            F-> ID|INT|E-F

identifier -> char{char}  	 // char {char | digit | _ }
integer -> digit{digit} 	 // {digit}+

Float // don’t worry about floats for this project

Lexical Analysis: “Lexer” or “Tokenizer” preforms the tokenization of the input.
Code: function scanToken()	 // this scans the input and sets the next
Variable: nextToken		     // token to point to the newly scanned token
•	OOP – represent the tree with objects (classes)
•	Make classes called Multiply, add, subject, multiplication, division also for identifier and integer.
-	Each class will have a print method
-	A eval method (evaluate the subtrees)
-	Function for each non-terminal grammar symbol (@12:30)



"""


from lexer import *
import tokenizer

global nextToken
nextToken = None

global generator
generator = None


def scanToken():
    global nextToken, generator
    # set value of nextToken using the tokenizer generator
    try:
        nextToken = generator.__next__()
    except:
        nextToken = None


def parseE():
    global nextToken
    # E -> T
    a = parseT()
    while True:
        if isinstance(nextToken, str) and nextToken == "+":
            scanToken()
            # E -> T + E
            b = parseE()
            if not b:
                return None
            a = Add(a, b)
        elif isinstance(nextToken, str) and nextToken == "-":
            scanToken()
            # E -> T - E
            b = parseE()
            if not b:
                return None
            a = Subtract(a, b)
        elif isinstance(nextToken, str) and nextToken == "=" and isinstance(a, ID):
            scanToken()
            # ID = E
            b = parseE()
            if not b:
                return None
            a.equals = b
        else:
            # E -> T
            return a


def parseF():
    global nextToken
    if isinstance(nextToken, ID) or isinstance(nextToken, Integer):
        temp = nextToken
        scanToken()
        # F -> ID / Integer
        return temp
    elif isinstance(nextToken, str) and nextToken == "(":
        scanToken()
        # F -> (E)
        a = parseE()
        if not a:
            return None
        if isinstance(nextToken, str) and nextToken == ")":
            scanToken()
            return a
        else:
            return None
    elif isinstance(nextToken, str) and nextToken == "-":
        scanToken()
        # F -> -F
        return Negate(parseF())
    else:
        return None


def parseT():
    global nextToken
    # T -> F
    a = parseF()
    while True:
        if isinstance(nextToken, str) and nextToken == "*":
            scanToken()
            # T -> F * T
            b = parseT()
            if not b:
                return None
            a = Mult(a, b)
        elif isinstance(nextToken, str) and nextToken == "/":
            scanToken()
            # T -> F / T
            b = parseT()
            if not b:
                return None
            a = Div(a, b)
        else:
            # T -> F
            return a


if __name__ == "__main__":
    # get expression from user
    expression = input("Please enter your expresssion: ")
    # initialize token generator
    generator = tokenizer.scanToken(expression)

    # parse expression
    # using try block -> catch exceptions
    try:
        scanToken()
        resultTree = parseE()

        if not nextToken is None:
            raise Exception("Invalid Expression")

        print("Result:", resultTree.eval(1))

    except Exception as e:
        print(e)
