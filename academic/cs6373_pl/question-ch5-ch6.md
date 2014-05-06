#Homework 2 (Xin Zhou 0522261)

##Chapter 5

**4. Dynamic type binding is closely related to implicit heap-dynamic variables. Explain this relationship.**

- They both are bound only when they are assigned values.

**7. Assume the following Javascript program was interpreted using static-scoping rules. What value of x is displayed in function sub1? Under dynamic-scoping rules, what value of x is displayed in function sub1?**
```
var x;
function sub1() {
    document.write("x = " + x + "<br />");
}
function sub2() {
    var x;
    x = 10;
    sub1();
}
x = 5;
sub2();
```

- When the program is interpreted using static scoping, the x should be displayed as 5. When the program is interpreted using dynamic scoping, the x should be displayed as 10.

##Chapter 6

**15. What are the arguments for and against Java’s implicit heap storage recovery, when compared with the explicit heap storage recovery required in C++? Consider real-time systems.**

- For: If programs cannot explicitly deallocate heap-dynamic variables, there will not be dangling pointers. Java's implicit heap storage recovery is the solution to the dangling-pointer problem.

- Against: The heap management can be a very complex run-time process. It needs more space and time for collectting garbage.



**21. In what way is static type checking better than dynamic type checking?**

- It will save time in runtime for checking the types.
- It is better to detect errors at compile time than at run time, because the earlier correction is usually less costly.
