# Implementation-of-Computational-Methods-Evidence-2

## Description


The grammar that I have chosen is a new notation for chess moves. Chess notation is a system used to record the moves played in a game of chess. In this system, each square on the board has a unique identifier based on a combination of a letter and a number. The letters represent the columns of the board, from "a" to "h", and the numbers represent the rows from 1 to 8.

For example, the movement of a pawn from the e2 square to the e4 square is written down as "e4". Another example is when a knight moves from the g1 square to the f3 square, then it is recorded as "Nf3", where "N" represents the knight.

In addition to moves, chess notation can also include special symbols and abbreviations to indicate different aspects of the game, such as check, checkmate, castling, piece captures, pawn promotions, among others.

However, for this evidence, I cannot use that notation because that would be analyzing a word, like the last evidence. Therefore, I decide to translate the chess notation to English.

Here are some examples of how this grammar may look:

Nf3 → white knight moves to f3 square.
Bxc6 → white bishop captures night on c6 square.
Qh5 → The white queen moves to h5 square.
O-O → White castles kingside (the king moves two squares to g1 and the rook moves to f1).
exd5 → The white pawn on the e-file captures on the d5 square.
Rd8 → The black rook moves to the d8 square.
Ne5+ → The white knight gives a check on the e5 square.

Yet, due to the complexity of chess, I had to shorten this grammar to only include pieces capturing other pieces, checkmate, and simple moves. I also allow illegal moves, such as pieces of the same color capturing themselves.

For this evidence, I will create a Restricted Context-Free Grammar (RCFG). As explained by Carol Critchlow & David J. Eck on the website eng.libretexts.org, a Context-Free Grammar (CFG) is a formal grammar that consists of a set of rewriting rules where each rule has a single non-terminal symbol on the left-hand side, which can be replaced by a sequence of symbols (terminal or non-terminal) on the right-hand side.

Here is a visual example using a screenshot from Critchlow, Carol & Eck, David J.'s work:

![](https://github.com/Dieg0Lir4/Implementation-of-Computational-Methods-Evidence-2/blob/main/17.jpg)

Critchlow, Carol & Eck, David J. "Context-Free Grammars." LibreTexts, https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_and_Computation_Fundamentals/Foundations_of_Computation_(Critchlow_and_Eck)/04%3A_Grammars/4.01%3A_Context-free_Grammars Accessed April 28, 2024.

But for this evidence I will sumbit a Restricted Context-Free Grammar (RCFG), which is basically a form of Context-Free Grammar (CFG) that has additional restrictions.

Modal:

The first step is to generate a grammar that recognizes the language. 
According to Lawrence University a context free grammar has to four main components (V, Σ, R, S)

Variables (V) are symbols that can be replaced.
Terminals (Σ) are symbols that cannot be replaced. They are the final elements that appear in the strings generated by the grammar.
Rules (R) define how variables can be replaced.
The start variable (S) is the starting point for generating strings. It is the variable from which the replacement process begins.

So let's start by doing a grammar quick grammar not caring about ambiguity

![](https://github.com/Dieg0Lir4/Implementation-of-Computational-Methods-Evidence-2/blob/main/16.jpg)

note: The non terminal B has all the option for the boxes in a chessboard, and piece is also a non terminal variable just that I cut it out the screen shot

Now, let's check for ambiguity. For example, let's write, 'White piece captures black piece in b1.'

Here is one way of representing it:

![](https://github.com/Dieg0Lir4/Implementation-of-Computational-Methods-Evidence-2/blob/main/15.jpg)

however there is another tree to the sentence “white piece captures black piece in b1”

![](https://github.com/Dieg0Lir4/Implementation-of-Computational-Methods-Evidence-2/blob/main/14.jpg)

The problem is that 'G' has too many ways of calling itself repeatedly in many different ways. So, let's make the rules more specific and use abbreviated notation to consolidate the rules into a single one.

Here are the new rules to avoid ambiguity:

![](https://github.com/Dieg0Lir4/Implementation-of-Computational-Methods-Evidence-2/blob/main/13.jpg)

By adding more non-terminals, I can prevent calling the same non-terminal repeatedly and taking different paths to construct the same sentences. However, now we have to face a new problem: left recursion. Left recursion, as explained by Geeks for Geeks, can create an infinite loop, leading to a decrease in performance.

Here is the left recursion in my grammar:

![](https://github.com/Dieg0Lir4/Implementation-of-Computational-Methods-Evidence-2/blob/main/12.jpg)

As you can see, 'G' can grow infinitely to the left without stopping. Let's fix that by using the method demonstrated by Western University on their website: https://www.csd.uwo.ca/~mmorenom/CS447/Lectures/Syntax.html/node8.html

![](https://github.com/Dieg0Lir4/Implementation-of-Computational-Methods-Evidence-2/blob/main/11.jpg)

By using that method now the grammar looks like this:

![](https://github.com/Dieg0Lir4/Implementation-of-Computational-Methods-Evidence-2/blob/main/10.jpg)

And the tree likes this, eliminating the left recursion:

![](https://github.com/Dieg0Lir4/Implementation-of-Computational-Methods-Evidence-2/blob/main/9.jpg)

Now lets use this website https://www.cs.princeton.edu/courses/archive/spring20/cos320/LL1/

to check that my grammar is correct

Writing my grammar:

* G ::= P G'
* G' ::= M G'
* G' ::= ''
* M ::= captures P in B
* M ::= moves to B
* M ::= checkmates C king in B
* P ::= C F
* C ::= black
* C ::= white
* F ::= king
* F ::= queen
* F ::= bishop
* F ::= knight
* F ::= rook
* F ::= pawn
* B ::= L N
* L ::= a
* L ::= b
* L ::= c
* L ::= d
* L ::= e
* L ::= f
* L ::= g
* L ::= h
* N ::= 1
* N ::= 2
* N ::= 3
* N ::= 4
* N ::= 5
* N ::= 6
* N ::= 7
* N ::= 8

First and Follow Table:

![](https://github.com/Dieg0Lir4/Implementation-of-Computational-Methods-Evidence-2/blob/main/8.jpg)

Transition Table:

![](https://github.com/Dieg0Lir4/Implementation-of-Computational-Methods-Evidence-2/blob/main/7.jpg)
![](https://github.com/Dieg0Lir4/Implementation-of-Computational-Methods-Evidence-2/blob/main/6.jpg)
![](https://github.com/Dieg0Lir4/Implementation-of-Computational-Methods-Evidence-2/blob/main/5.jpg)

Now lets make some examples to see if works


Lets try with:


white pawn captures black pawn in b 1
Expecting a success
Result:

![](https://github.com/Dieg0Lir4/Implementation-of-Computational-Methods-Evidence-2/blob/main/4.jpg)

black queen moves to f 4
Expecting a success
Result:

![](https://github.com/Dieg0Lir4/Implementation-of-Computational-Methods-Evidence-2/blob/main/3.jpg)

black queen captures rook
Expecting a failure
Result

![](https://github.com/Dieg0Lir4/Implementation-of-Computational-Methods-Evidence-2/blob/main/2.jpg)

white pawn moves to d 9
Expecting a failure
Result:

![](https://github.com/Dieg0Lir4/Implementation-of-Computational-Methods-Evidence-2/blob/main/1.jpg)

## Implementation

Please make sure you have NLTK installed to run this code. You can install it with 
```
pip install nltk
```

Additionally, download the punkt package.

The code is in the file: evidencia2.py

To run the code in the project terminal, use the following command:

```
python evidencia2.py
```

It will prompt you to enter a sentence and will return the tree with a message if it is valid. If it's not valid, it will display a message saying it's invalid.

Note: In some trees, due to the word size, the tree may display the word order incorrectly, but if it's valid.

#### HOWEVER, I recommend using this link to run python online in case it is not working locally: https://colab.research.google.com/drive/1e9Y42n0k0-RqTfDpTF4azuzjQcgoVZ6M?usp=sharing

## TESTS

You can run the tests by typing:
```
run all tests
```
When prompted to enter a sentence.

If you want to manually test:

Here are the inputs with the expected results:

VALID:

INPUT: black pawn moves to c 5 .

INPUT: white king captures black bishop in b 3 .

INPUT: black queen captures white knight in a 2 .

INVALID:

INPUT: black pawn moves to 9 c .

INPUT: white king captures bishop in 3 b .

INPUT: queen captures white knight in 2 a .

### IMPORTANT NOTE: don't forget the period (.) at the end of the sentences if writing the testes manually. Using words not defined in the grammar will end the program. The first time it will take time to start because is downloding punkt

## Analysis

This is a Context-Free Grammar (CFG), and Context-Free Grammars are at Level 2 of the Chomsky Hierarchy.
Since are classifed in four types

Type 0: Unrestricted grammars
Type 1: Context-sensitive grammars
Type 2: Context-free grammars
Type 3: Regular grammars

why is type 2 because:

the left-hand side of each production rule consists of a single non-terminal symbol

right-hand side of each production rule can be a sequence of terminals and/or non-terminals.

Why is not type 0 or 1:

0 and 1 allow production rules where the left-hand side can have a string of terminals and/or non-terminals

Why is not type 3:

3 allows for production rules where the right-hand side has no more than one non-terminal, which must be at the end


Now lets check its time complexity



## Bibliography

Chess notation & algebraic notation. (n.d.). Chess.com. https://www.chess.com/terms/chess-notation

Libretexts. (2020, July 7). 4.1: Context-free grammars. Engineering LibreTexts. https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_and_Computation_Fundamentals/Foundations_of_Computation_(Critchlow_and_Eck)/04%3A_Grammars/4.01%3A_Context-free_Grammars

Context free grammars. (n.d.). http://www2.lawrence.edu/fast/GREGGJ/CMSC515/chapt02/CFG.html

GeeksforGeeks. (2023, April 18). Removing direct and indirect left recursion in a grammar. GeeksforGeeks. https://www.geeksforgeeks.org/removing-direct-and-indirect-left-recursion-in-a-grammar/

Elimination of left recursion. (n.d.). https://www.csd.uwo.ca/~mmorenom/CS447/Lectures/Syntax.html/node8.html

Wikipedia contributors. (2024, April 22). Chomsky hierarchy. Wikipedia. https://en.wikipedia.org/wiki/Chomsky_hierarchy










