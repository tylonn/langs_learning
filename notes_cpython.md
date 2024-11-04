## CPython - An Adventure  

The idea of this notes is to document my exploration of CPython interpreter. Let's see where it leads me.

### Day 1 - Understanding how the program starts  

First we should start at the beginning. For that, we will understand in a first moment how the interpreter starts i.e. its entry point in the file `Python/python.c`.  
In this file we have the Python Header which contains declarations for all the functions and data structures used throughout the interpreter. In C, a header is a file with a `.h` extension and typically contains declarations of functions (Prototypes), macros, constants, and data types that are shared between multiple source files.  
We also have in this file a preprocessor directive (starting with `#`) which is a instruction that is executed by the the preprocessor before the compilation of the code. The preprocessor in C is a tool that is responsible for performing textual substitutions and manipulate the code, handling the inclusion of files, and macro substitution. It basically produces an expanded source file without any preprocessor directives, which is then passed to the compiler.  



