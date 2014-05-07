# Mid-term Review

1. Short answers about the history or programming language design
    - COBOL
        - Major feature: The first language for business applications, FLOW-MATIC features, Long names(up to 330 characters), with hyphens.
        - Period created: First design meeting - 1959. Published in 1960.
        - Target usage: Business
    - ADA
        - Major feature: data abastraction, exception handling, generic program units, concurrent execution
        - Period created: 83, 95
        - Target usage: embeded system application, critical system application
    - BASIC: The beginning of timesharing
        - Major feature: easy to learn and use, friendly, fast turnaround for homework, free and private access, first widely used language with time sharing. 
        - Period created: Designed 1963
        - Target usage: non-science students
    - FORTRAN: Dominated science programming 50 years 
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


```
1950      1955      1960      1965      1970      1975      1980      1985      1990      1995      2000      2005
------------------------------------------------------------------------------------------------------------------------
                    1960 COBOL & ALGOL 60   1972 C & PROLOG                      
          1954 FORTRAN 0    1963 BASIC & PL/1
              1957 FORTRAN I              1971 PASCAL
                1958 FORTRAIN II & ALGOL 58 & LISP               1983 ADA      1990 FORTRAN 90            2003 FORTRAN 03
                    1960-62 FORTRAN IV                1977 FORTRAN 77
```

2. Computations (BNF, operational, axiomatic and denotational semantic) that are drawn from the development of meta-languages to describe the design of a programming language definition. 
    - draw a parse tree; show left most derivation or right-most derivation; show a grammer is ambiguous; change an operator precedence; convert between BNF and EBNF;
        - parse tree: a hierarchical representation of a derivation
        - a grammer is ambiguous if and only if it generates a sentential form that has two or more distinct parse trees.
        - EBNF: (), [], {}

    - Remove a left-recursion problem;
