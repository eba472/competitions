
### Why?
- Modern
- Concise: Automatically generated equals(), hashCode(), toString(), and copy() in data class
- Safe: Kotlin can infer that the result is non-null & Nullability is part of Kotlin’s type system
- Expressive:  Destructure etc.
- Interoperable:  Use any existing JVM library or framework & Call Kotlin code from Java without an issue
- Multiplatform: Provide platform-specific implementations in the platform modules


### Input/output
- print() 
- println() - The cursor moves to the beginning of the next line.


### String
```
val hello = "Hello World"
val stringLength = hello.length
```

### Function
```
fun sum(a: Int, b: Int): Int {
 return a + b
}
```

### Variables

- val : declares immutable variables
- var : declares mutable variables

### Exceptions
- EOFException is a checked exception in Java that occurs when an end of file or end of stream is reached unexpectedly during input.