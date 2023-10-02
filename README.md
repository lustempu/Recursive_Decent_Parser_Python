# Recursive_Decent_Parser_Python
Project Description: Recursive Decent Parser in Python 
In Python Language we are to implement a simple Recursive Descent Parse to handle an arithmetic expression.
After entering a valid line of code (such as x = 3 + 4 * 2) output the list of components you have processed, such as:

C1: x = C2

C2: 3 + C3

C3: 4 * 2

Precedence and Associativity
x + 5 * y ->(Should be interpreted as)-> x + (5*y)
Grammar for Expressions: Defines a Language

expr -> term + expr  		 // rule                                        E -> T+E
expr -> term – expr
expr -> term

term -> factor * term		 // term is a non-terminal here                 T -> F*T
term -> factor / term		 // the ‘/’ and ‘*’ are terminals               T -> F*T
term -> factor                                                          T -> F

factor -> identifier		 // identifier is a set of tokens/things        F -> ID
factor -> integer                                                       F -> INT
factor -> (expr) 		    // parentheses are also terminal symbols        F -> E

Tokens: View the input as a series of tokens 

expr -> term + expr | term – expr | term                                E -> T+E|T-E|T
term -> factor * term | factor/term | factor                            T -> F*T|F/T|F
factor -> identifier | integer | (expr) – factor                        F -> ID|INT|E-F

identifier -> char{char}  	 // char {char | digit | _ }
integer -> digit{digit} 	 // {digit}+

Note: Floats are not required for this project



