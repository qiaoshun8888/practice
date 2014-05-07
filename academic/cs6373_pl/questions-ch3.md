## Chapter 3
- Define syntax and semantics.
    - Syntax: the form or structure of the expressions, statements, and program units.
    - Semantics: the meaning of the expressions, statements, and program units.
    - Syntax and semantics provide a language's definition.

- Describe the operation of a general language generator.
    - A device that generates sentences of a language
    - One can determine if the syntax of a particular sentence is syntactically correct by comparing it to the structure of the generator.

- Describe the operation of a general language recognizer.
    - A recognition device reads input strings over the alphabet of the language and decides whether the input strings belong to the language.
    - Syntax analysis part of a compiler

- Define a left-recursive grammar rule.
    - A -> Aa

- Distinguish between static and dynamic semantics.
    - Nothing to do with meaning
    - Extra rules on how syntactic units connect
        - Type and compatibility conversions.
    - Context-free grammars (CFGs) cannot describe all of the syntax of programming languages
    - Categories of constructs that are trouble:
        - Context-free, but cumbersome

- What purpose do predicates serve in an attribute grammar?
    - To check for the attribute consistency

- What is the difference between a synthesized and an inherited attribute?
    - The **synthesized attributes** are the result of the attribute evaluation rules, and may also use the values of the **inherited attributes**. The **inherited attributes** are passed down from parent nodes. In some approaches, **synthesized attributes** are used to pass semantic information up the parse tree, while **inherited attributes** help pass semantic information down it.

- What is the primary use of attribute grammars?
    - Extension to context-free grammar

- Describe the two levels of uses of operational semantics.
    - Natural operational semantics
    - Structural operational semantics

- In denotational semantics, what are the syntactic and semantic domains?
    - The mapping functions of a denotational semantics programming language specification, like all functions in mathematics, have a domain and a range.

    - The **syntactic domain** is called the domain because it is syntactic structures that are mapped. The domain is the collection of values that are legitimate parameters to the function; the range is the collections of objects to which the parameters are mapped.
    
    - The **semantic domain** is called the range.

- What is stored in the state of a program for denotational semantics?
    - The state of a program for denotational semantics is **the value of all its current variables**.

- Which part of an inference rule is the antecedent?
    - The **top part** of an inference rule is called **antecedent**.

#### Problem Set

- Rewrite the BNF of Example 3.4 to give + precedence over * and force + to be right associative.
```
<assign> → <id> = <expr>
<id> → A | B | C
<expr> → <expr> * <term>
       | <term>
<term> → <factor> + <term>
       | <factor>
<factor> → ( <expr> )
         | <id>
```

- Rewrite the BNF of Example 3.4 to add the ++ and -- unary operators of Java.
```
<assign> → <id> = <expr>
<id> → A | B | C
<expr> → <expr> + <term>
       | <term>
<term> → <term> * <factor>
       | <factor>
<factor> → ( <expr> )
         | <id>
         | <id> ++
         | <id> --
```

- Write a BNF description of the Boolean expressions of Java, including the three operators &&, ||, and ! and the relational expressions.
```
<expr> -> <expr> && <term>
        | <term>
<term> -> <factor> || <term>
        | <factor>
<factor> -> (<expr>)
          | <id>
          | !<factor>
          | <id> == <id>
          | <id> >= <id>
          | <id> <= <id>
          | <id> != <id>
          | <id> > <id>
          | <id> < <id>
```

- Using the grammar in Example 3.2, show a parse tree and a leftmost derivation for each of the following statements:
```
a. A = A * (B + (C * A))
b. B = C * (A * C + B)
c. A = A * (B + (C))

    Example 3.2:
    <assign> → <id> = <expr>
    <id> → A | B | C
    <expr> → <id> + <expr>
            | <id> * <expr>
            | ( <expr> )
            | <id>

    a. Derivation: A = A * (B + (C * A))
    <assign> => <id> = <expr>
             => A = <id> * <expr>
             => A = A * (<expr>)
             => A = A * (<id> + <expr>)
             => A = A * (B + (<expr>))
             => A = A * (B + (<id> * <id>))
             => A = A * (B + (C * A))

    a. Parse Tree
        <assign>
        /  |  \
      <id> = <expr>
       |     /  |  \
       A   <id> *  <expr>
            |     /   |  \
            A    ( <expr> )
                  /   |  \
                <id>  +  <expr>
                 |      /   |  \
                 B     ( <expr> )
                        /   |  \
                      <id>  * <id>
                        |       |
                        C       A

    b. Derivation: B = C * (A * C + B)
    <assign> => <id> = <expr>
             => B = <id> * <expr>
             => B = C * (<expr>)
             => B = C * (<id> * <expr>)
             => B = C * (A * <id> + <id>)
             => B = C * (A * C + B)

    b. Parse Tree
    <assign>
        <id>
            B
        =
        <expr>
            <id>
                C
            *
            <expr>
                (
                <expr>
                    <id>
                        A
                    *
                    <expr>
                        <id>
                            C
                        +
                        <id>
                            B
                )

    c. Derivation: A = A * (B + (C))
    <assign> => <id> = <expr>
             => A = <id> * <expr>
             => A = A * (<expr>)
             => A = A * (<id> + <expr>)
             => A = A * (B + (<expr>))
             => A = A * (B + (<id>))
             => A = A * (B + (C))
    c. Parse Tree
    <assign>
        <id>
            A
        =
        <expr>
            <id>
                A
            *
            <expr>
                (
                <expr>
                    <id>
                        B
                    +
                    <expr>
                        (
                        <expr>
                            <id>
                                C
                        )
                )
```


- Using the grammar in Example 3.4, show a parse tree and a leftmost derivation for each of the following statements:
```
a. A = ( A + B ) * C
b. A = B + C + A
c. A = A * (B + C)
d. A = B * (C * (A + B))

    Example 3.4
    <assign> → <id> = <expr>
    <id> → A | B | C
    <expr> → <expr> + <term>
           | <term>
    <term> → <term> * <factor>
           | <factor>
    <factor> → ( <expr> )
             | <id>

    a. Derivation: A = ( A + B ) * C
    <assign> => <id> = <expr>
             => A = <term>
             => A = <term> * <factor>
             => A = <factor> * <id>
             => A = (<expr>) * C
             => A = (<expr> + <term>) * C
             => A = (<term> + <factor>) * C
             => A = (<factor> + <id>) * C
             => A = (<id> + B) * C
             => A = (A + B) * C

    a. Parse Tree
    <assign>
        <id>
        =
        <expr>
            <term>
                <term>
                    <factor>
                        (
                        <expr>
                            <expr>
                                <term>
                                    <factor>
                                        <id>
                                            A
                            +
                            <term>
                                <factor>
                                    <id>
                                        B
                        )
                *
                <factor>
                    <id>


    d. Derivation: A = B * (C * (A + B))
    <assign> => <id> = <expr>
             => A = <term>
             => A = <term> * <factor>
             => A = <factor> * (<expr>)
             => A = <id> * (<term>)
             => A = B * (<term> * <factor>)
             => A = B * (<factor> * (<expr>))
             => A = B * (<id> * (<expr> + <term>))
             => A = B * (C * (<expr> + <term>))
             => A = B * (C * (<term> + <factor>))
             => A = B * (C * (<factor> + <id>))
             => A = B * (C * (<id> + B))
             => A = B * (C * (A + B))

    d. Parse Tree
    <assign>
        <id>
            A
        =
        <expr>
            <term>
                <term>
                    <factor>
                        <id>
                            B
                *
                <factor>
                    (
                    <expr>
                        <term>
                            <term>
                                <factor>
                                    <id>
                                        C
                            *
                            <factor>
                                (
                                <expr>
                                    <expr>
                                        <term>
                                            <factor>
                                                <id>
                                                    A
                                    +
                                    <term>
                                        <factor>
                                            <id>
                                                B
                                )
                    )
```

- Prove that the following grammar is ambiguous:
```
<S> → <A>
<A> → <A> + <A> | <id>
<id> → a | b | c

1.
    <S>
        <A>
            <A>
                <A>
                    <id>
                        a
                +
                <A>
                    <id>
                        b
            +
            <A>
                <id>
                    c

2.
    <S>
        <A>
            <A>
                <id>
                    a
            +
            <A>
                <A>
                    <id>
                        b
                +
                <A>
                    <id>
                        c
```


- Describe, in English, the language defined by the following grammar:
```
<S> → <A> <B> <C>
<A> → a <A> | a
<B> → b <B> | b
<C> → c <C> | c
```
One or more a, then one or more b, then one or more c.

- Consider the following grammar:
```
<S> → <A> a <B> b
<A> → <A> b | b
<B> → a <B> | a
Which of the following sentences are in the language generated by this grammar?
- a. baab
- b. bbbab X
- c. bbaaaaa X
- d. bbaab
```

- Consider the following grammar:
```
<S> → a <S> c <B> | <A> | b
<A> → c <A> | c
<B> → d | <A>
Which of the following sentences are in the language generated by this grammar?
a. abcd
b. acccbd X
c. acccbcc X
d. acd X
e. accc 
```

- Write a grammar for the language consisting of strings that have n copies of the letter a followed by the same number of copies of the letter b, where n > 0. For example, the strings ab, aaaabbbb, and aaaaaaaabbbbbbbb are in the language but a, abb, ba, and aaabb are not.
```
<S> => a<S>b | ab
```

- Convert the following EBNF to BNF:
```
S → A{bA}
A → a[b]A
    S => A | SbA
    A => abA | aA
```


- Using the virtual machine instructions given in Section 3.5.1.1, give an operational semantic definition of the following:
```
a. Java do-while
b. Ada for
c. C++ if-then-else
d. C for
e. C switch
```

    **a. Java do-while**
    do {
        statements;
    while (expr);
    
    Operational semantic definition:
    loop:   statements
            if (expr == true) goto loop
    out:    ...

 
    **d. C for**
    for (expr1; expr2; expr3) {
        statements;
    }
    
    Operational semantic definition:
            expr1;
    loop:   if (expr2 == 0) goto out
            statements
            expr3
            goto loop
    out:    ...
    
- Compute the weakest precondition for each of the following assignment statements and postconditions:
```
a. a = 2 * (b - 1) - 1 {a > 0}
b. b = (c + 10) / 3 {b > 6}
c. a = a + 2 * b - 1 {a > 1}
d. x = 2 * y + x - 1 {x > 11}

    a > 0, b - 1 > 1/2, b > 3/2
    b > 6, c + 10> 18, c > 8
    a > 1, a + 2 * b - 1 > 1, b > (2 - a) / 2
    x > 11, 2 * y + x - 1 > 11, y > 6 - x/2
    
    ** Note that the appearance of the left side of the assignment statement in its right side does not affect the process of computing the weakest precondition. ** (**PDF page 151**)
```

- Compute the weakest precondition for each of the following sequences of assignment statements and their postconditions:
```
a. a = 2 * b + 1;
   b = a - 3
   {b < 0}
   
   a - 3 < 0, a < 3
   2 * b + 1 < 3, b < 1
   
   ** The weakest precondition is the least restrictive precondition that will guarantee the validity of the associated postcondition.** (**PDF page 149**)
   
   So the weakest precondition is {b < 1}
```
```
b. a = 3 * (2 * b + a);
   b = 2 * a - 1
   {b > 5}
   
   2 * a - 1 > 5, a > 3
   3 * (2 * b + a) > 3, b > (1 - a) / 2 (**This is the final result**)
```

- Compute the weakest precondition for each of the following selection constructs and their postconditions:
```
a. if (a == b)
      b = 2 * a + 1
   else
      b = 2 * a;
   {b > 1}
   
   2 * a + 1 > 1, a > 0
   2 * a > 1, a > 1 / 2
   
   So the weakest precondition is {a > 0}
```
```   
b. if (x < y)
      x = x + 1
   else
      x = 3 * x
   {x < 0}
   
   x + 1 < 0, x < -1
   3 * x < 0, x < 0
   
   So the weakest precondition is {x < 0}
```
```   
c. if (x > y)
      y = 2 * x + 1
   else
      y = 3 * x - 1;
   {y > 3}
   
   2 * x + 1 > 3, x > 1
   3 * x - 1 > 3, x > 4 / 3
   
   So the weakest precondition is {x > 1}
```


