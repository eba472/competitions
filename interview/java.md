https://www.softwaretestinghelp.com/core-java-interview-questions/

Q1 What is Java?

High level programming language | Sun microsystems | 1995 | 
apps, websites , games | Collection of objects

Q2 What are the features of Java?

OOP | platform-independent |  High performance | Multi-threaded

Q3 How does Java enable high performance?
Just In Time compiler (JIT) : bytecode -> machine language 

Q4  Name the Java IDE’s?
Eclipse, IntelliJ IDEA(for JVM-based languages)

Q5 What do you mean by Constructor?
invoked when create new object | method with the same name as class | default if not created
can be overloaded | If the user created a constructor with a parameter then he should create another constructor explicitly without a parameter.

Q6 What is meant by the Local variable and the Instance variable?
Local variable : inside method
Instance variable : inside class

Q7 What is a Class?
All Java codes are defined in a Class. It has variables(states) and methods.

Q8 What is an Object?
Instance of a class | State & Behavior | "new()" keyword

Q9 What are the OOPs concepts?

- Q10 Inheritance : class extend another class | reuse | Super class -> Sub class | Private members => no inherit | no multiple inheritance in Java 
- Q11 Encapsulation : protection | maintainability | all the instance variables private => getter, setter | 
- Q12 Polymorphism : Many forms | overriding | not overloading
    - Q13 overriding (Same method name, argument, return type )
    - Q14 overloading (Same method name | diff argument types & return type )
- Q15 Interface: Template with only method declarations (not implementations)
  - all methods: public abstract void
  - all variables: public static final
  - implements not extend
  - Should implement every method
- Abstraction
  - Q16 What is meant by Abstract class?
    - Some methods are abstract(Just declaration) | => concrete Subclass

Q17 Difference between Array and Array List.
Given size | Dynamic size
Put value by index | Can put value in the end

Q18 Difference between String, String Builder, and String Buffer.

String: Stored in constant string pool | cannot be erased
String Buffer: stored in stack | synchronized <> thread safe => slower | new value => replaces old values
String Builder: same as above but not synchronized <> Faster

Q19 Explain about Public and Private access specifiers.
Public: Can be accessed from anywhere
Private: Can be accessed only in class

Q20 Difference between Default and Protected access specifiers.
Default: visible only inside the package
Protected: if a class extends then it is visible even if it is outside the package.

Q21 


