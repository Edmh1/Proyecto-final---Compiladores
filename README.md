# Online Interpreter

## What is an interpreter?

An interpreter is a type of computer program that directly executes instructions written in a programming or scripting language. It does not require compilation into a machine learning program. Different types of interpreters are constructed for several languages that are traditionally associated with compilation. An interpreter consists of a set of commands that it can execute. 

### How does it work?

Interpreter transforms high level language code into machine-understandable code or an intermediate language that can be executed well. An interpreter reads every line of code, translates it into machine code and then immediately executes it. The interpreter executes every source statement line by line during execution. An interpreter provides detailed error messages and supports interactive debugging. 

### Online interpreter

An Online compiler (interpreter) is a web-based application that helps you to run code online without installing the programming language compiler on your device. It's commonly used for begginers to run and ejecute their code in a quickly way. 

## What do we need to make an interpreter?

An interpreter is a complex program, so there are multiple stages to it:

- A lexer, which is the part of an interpreter that turns a sequence of characters (plain text) into a sequence of tokens.
- A parser, in turn, takes a sequence of tokens and produces an abstract syntax tree (AST) of a language. The rules by which a parser operates are usually specified by a formal grammar.
- An interpreter is a program that interprets the AST of the source of a program on the fly (without compiling it first).

----

All that said, for our project, we decided to use _PLY_ to make our lexer and parser. Let's see and introduction to PLY and an overview: 

- ### Introduction

	PLY is a pure-Python implementation of the popular compiler construction tools lex and yacc. The main goal of PLY is to stay fairly faithful to the way in which traditional lex/yacc tools work. This includes supporting LALR(1) parsing as well as providing extensive input validation, error reporting, and diagnostics. 
	
- ### Overview

	PLY consists of two separate modules; lex.py and yacc.py, both of which are found in a Python package called ply. The lex.py module is used to break input text into a collection of tokens specified by a collection of regular expression rules. yacc.py is used to recognize language syntax that has been specified in the form of a context free grammar.

	The two tools are meant to work together. Specifically, lex.py provides an external interface in the form of a token() function that returns the next valid token on the input stream. yacc.py calls this repeatedly to retrieve tokens and invoke grammar rules. The output of yacc.py is often an Abstract Syntax Tree (AST).
	
	Like its Unix counterpart, yacc.py provides most of the features you expect including extensive error checking, grammar validation, support for empty productions, error tokens, and ambiguity resolution via precedence rules. In fact, almost everything that is possible in traditional yacc should be supported in PLY.
	
	



---

# SigmaChar

SigmaChar is the name out group decided to give to our own programming language. Let's review the basic principles of SigmaChar


- ## Control Flow Keywords:
	```
	- If → ALPHA
	- Else → BETA
	
- ## Variable Types:
	```
	- bool → STATUS
	- int → SIGMA 
	- float → REAL
	- char → CHAD
	- str → GIGACHAD
	
- ## Operators:
	```
	- Addition (+)
	- Subtraction (-)
	- Multiplication (*)
	- Division (/)
	- Greater than (>)
	- Greater than or equal to (>=)
	- Less than (<)
	- Less than or equal to (<=)
	- Equal to (==)
	- Not equal to (!=)
	- Assignment (<-)
	
- ## Logical Operators:
	```
	- not → FAKE 
	- and → MOGGED 
	- or → GOD 
	```	

- ## Symbols:
	```
	- Left Parenthesis   →  '('
	- Right Parenthesis  →  ')'
	- Body Structure     →  ':'
	- String Delimiter   →  '@'
	- Comment Delimiter  →  '#' 
	- End of Line        →  '$'
	```	

- ## Reserved words:
	```
	- print() → SIGMA_SPEAK()
	- True → VERUM
	- False → FALSUM
	- None → NIHIL
	
	```

Here's a little example: 

```
## Example 1:

SIGMA a$
a <- 3$
ALPHA(a>=1+2):
    SIGMA_SPEAK(@Estoy en el if@)$
BETA:
    SIGMA_SPEAK(@Estoy en el else@)$
$
SIGMA_SPEAK(@FIN@)$
--------------------------------------
## Example 2:

SIGMA_SPEAK(1+2/7)$
--------------------------------------
## Example 3:

GIGACHAD b <- @y@$
SIGMA_SPEAK (b) $
--------------------------------------
## Example 4:

GIGACHAD b <- @yo con mis amigo@$
GIGACHAD a <- @hola@$
SIGMA_SPEAK (a+b) $

```

## Members:

- Castro Sebastián
- Escobar Andrés
- Manotas Eddie
- Navarro Vladimir
