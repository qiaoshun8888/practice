# Mid-term Review

1. Short answers about the history or programming language design
    - COBOL
        - Major feature: FLOW-MATIC features, Long names(up to 330 characters), with hyphens.
        - Period created: First design meeting - 1959. Published in 1960.
        - Target usage: Business
    - ADA
        - Major feature: 
        - Period created: 
        - Target usage: 
    - BASIC: The beginning of timesharing
        - Major feature: easy to learn and use, friendly, fast turnaround for homework, free and private access, first widely used language with time sharing. 
        - Period created: Designed 1963
        - Target usage: non-science students
    - FORTRAN: Th
        - Major feature: Led to the idea of compiled programming languages. For scientific computations. 
        - Period created: 1957 - Fortran I, 1958 Fortran II, 1960-1962 Fortran IV, 1978 - Fortran 77, Fortran 90, 95, 03, 08
        - Target usage: Scientific computations
    - PL/1
        - Major feature: Scientific computing and business computing
        - Period created: 1963
        - Target usage: Shops need two kinds of computers.
    - PASCAL
        - Major feature: Small, simple, nothing really new
        - Period created: 1971
        - Target usage: Teaching structured programming
    - C
        - Major feature: Powerful set of operators, but poor type checking. 
        - Period created: 1972
        - Target usage: systems programming


2. Computations (BNF, operational, axiomatic and denotational semantic) that are drawn from the development of meta-languages to describe the design of a programming language definition. 
    - draw a parse tree; show left most derivation or right-most derivation; show a grammer is ambiguous; change an operator precedence; convert between BNF and EBNF;
        - parse tree: a hierarchical representation of a derivation
        - a grammer is ambiguous if and only if it generates a sentential form that has two or more distinct parse trees.
        - EBNF: (), [], {}

    - Remove a left-recursion problem;

# Review Questions:
## Chapter 1
- What programming language has dominated scientific computing over the past 50 years? 
    - Fortran

- What programming language has dominated business applications over the past 50 years?
    - COBOL

- What programming language has dominated artificial intelligence over the past 50 years? 
    - LISP

- In what language is most of UNIX written? 
    - C

- What is one example of a lack of orthogonality in the design of C?
    - *in C, you cannot return a static array*

- What language used orthogonality as a primary design criterion? 
    - ALGOL 68

- What primitive control statement is used to build more complicated control statements in languages that lack them?
    - GOTO

- What construct of a programming language provides process abstraction?
    - Subprogram

- What is aliasing? 
    - Different names for the same memory cell

- What is exception handling? 
    - Allow program to intercept run-time errors

- What have been the strongest influences on programming language design over the past 50 years? 
    - ALGOL

- What is the name of the category of programming languages whose structure is dictated by the von Neumann computer architecture? 
    - Imperative 

- What are the three general methods of implementing a programming language?
    - Compilation
    - Pure interpretation
    - Hybrid implementation systems

- Which produces faster program execution, a compiler or a pure interpreter? 
    - Compiler

- What does a linker do? 
    - Load module/executable image
