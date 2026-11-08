QUESTIONS_BANK = {
    # ==========================================
    # 1. PYTHON (20 Questions: Easy, Medium, Difficult)
    # ==========================================
    "Python": [
        # Easy / Basic (7 Questions)
        {"id": 101, "difficulty": "Basic", "question": "Which keyword is used to define a function in Python?", "options": ["def", "function", "fun", "define"], "answer": "def"},
        {"id": 102, "difficulty": "Basic", "question": "What is the output of bool([]) in Python?", "options": ["True", "False", "None", "Error"], "answer": "False"},
        {"id": 103, "difficulty": "Basic", "question": "Which data structure in Python is ordered and immutable?", "options": ["List", "Tuple", "Dictionary", "Set"], "answer": "Tuple"},
        {"id": 104, "difficulty": "Basic", "question": "Which of the following is used to handle exceptions in Python?", "options": ["try / except", "do / catch", "try / catch", "error / handle"], "answer": "try / except"},
        {"id": 105, "difficulty": "Basic", "question": "What is the difference between list and tuple in Python?", "options": ["List is mutable, Tuple is immutable", "List is immutable, Tuple is mutable", "Both are mutable", "Both are immutable"], "answer": "List is mutable, Tuple is immutable"},
        {"id": 106, "difficulty": "Basic", "question": "Which file extension is used for Python files?", "options": [".pt", ".py", ".pyt", ".python"], "answer": ".py"},
        {"id": 107, "difficulty": "Basic", "question": "Which operator is used for floor division in Python?", "options": ["/", "//", "%", "**"], "answer": "//"},

        # Intermediate / Medium (7 Questions)
        {"id": 108, "difficulty": "Intermediate", "question": "What does the *args parameter allow in a function definition?", "options": ["Pass variable number of positional arguments", "Pass keyword arguments", "Pass fixed arguments", "Define global variables"], "answer": "Pass variable number of positional arguments"},
        {"id": 109, "difficulty": "Intermediate", "question": "Which built-in function pairs elements from two or more iterables?", "options": ["zip()", "map()", "filter()", "enumerate()"], "answer": "zip()"},
        {"id": 110, "difficulty": "Intermediate", "question": "What is a decorator in Python?", "options": ["A function that modifies the behavior of another function", "A code formatting tool", "A class constructor", "A module loader"], "answer": "A function that modifies the behavior of another function"},
        {"id": 111, "difficulty": "Intermediate", "question": "What is the purpose of list comprehension in Python?", "options": ["To create lists concisely in a single line", "To encrypt list data", "To sort lists in-place", "To clear list memory"], "answer": "To create lists concisely in a single line"},
        {"id": 112, "difficulty": "Intermediate", "question": "What is the difference between `is` and `==` in Python?", "options": ["`is` checks memory identity; `==` checks value equality", "`is` checks value; `==` checks identity", "Both check value equality", "Both check memory address"], "answer": "`is` checks memory identity; `==` checks value equality"},
        {"id": 113, "difficulty": "Intermediate", "question": "What does the `lambda` keyword create in Python?", "options": ["An anonymous inline function", "A loop structure", "A persistent database connection", "A multi-threaded task"], "answer": "An anonymous inline function"},
        {"id": 114, "difficulty": "Intermediate", "question": "Which built-in module is used for regular expressions in Python?", "options": ["regex", "re", "string", "parse"], "answer": "re"},

        # Advanced / Difficult (6 Questions)
        {"id": 115, "difficulty": "Advanced", "question": "What is the Global Interpreter Lock (GIL) in CPython?", "options": ["A mutex that allows only one thread to execute Python bytecode at a time", "A security feature for memory", "A garbage collector module", "A compiler optimizer"], "answer": "A mutex that allows only one thread to execute Python bytecode at a time"},
        {"id": 116, "difficulty": "Advanced", "question": "What does the __slots__ variable in a Python class do?", "options": ["Restricts dynamic attribute creation to optimize memory", "Defines private variables", "Locks class methods", "Creates static variables"], "answer": "Restricts dynamic attribute creation to optimize memory"},
        {"id": 117, "difficulty": "Advanced", "question": "How does memory management work in Python?", "options": ["Reference counting combined with generational garbage collection", "Manual memory management", "JVM garbage collection", "Stack allocation only"], "answer": "Reference counting combined with generational garbage collection"},
        {"id": 118, "difficulty": "Advanced", "question": "What is a Python Generator?", "options": ["A function returning an iterator using `yield` keyword", "A class compiler", "A script for generating documentation", "A thread process loader"], "answer": "A function returning an iterator using `yield` keyword"},
        {"id": 119, "difficulty": "Advanced", "question": "What is Method Resolution Order (MRO) in Python?", "options": ["Order in which base classes are searched when executing a method (C3 linearization)", "Alphabetical class sorting", "Execution priority of methods", "Garbage collection priority"], "answer": "Order in which base classes are searched when executing a method (C3 linearization)"},
        {"id": 120, "difficulty": "Advanced", "question": "What are descriptors in Python?", "options": ["Objects that implement __get__, __set__, or __delete__ protocol", "String documentation of classes", "File path managers", "Class constructor functions"], "answer": "Objects that implement __get__, __set__, or __delete__ protocol"}
    ],

    # ==========================================
    # 2. JAVA (20 Questions: Easy, Medium, Difficult)
    # ==========================================
    "Java": [
        # Basic (7 Questions)
        {"id": 201, "difficulty": "Basic", "question": "Which feature of Java enables 'Write Once, Run Anywhere'?", "options": ["Bytecode & JVM", "Pointers", "Multiple Inheritance", "Direct Assembly Compilation"], "answer": "Bytecode & JVM"},
        {"id": 202, "difficulty": "Basic", "question": "Which key concept in Java prevents a class from being inherited?", "options": ["static", "final", "abstract", "private"], "answer": "final"},
        {"id": 203, "difficulty": "Basic", "question": "Which primitive type holds a 64-bit signed integer in Java?", "options": ["int", "short", "long", "float"], "answer": "long"},
        {"id": 204, "difficulty": "Basic", "question": "Which entry point method signature is valid in Java?", "options": ["public static void main(String[] args)", "public void main(String args)", "static main(String[] args)", "public static int main()"], "answer": "public static void main(String[] args)"},
        {"id": 205, "difficulty": "Basic", "question": "Which package is automatically imported into every Java program?", "options": ["java.util", "java.lang", "java.io", "java.net"], "answer": "java.lang"},
        {"id": 206, "difficulty": "Basic", "question": "What is default value of a boolean variable in Java?", "options": ["true", "false", "0", "null"], "answer": "false"},
        {"id": 207, "difficulty": "Basic", "question": "Which keyword is used to create an instance of a class?", "options": ["alloc", "new", "create", "instantiate"], "answer": "new"},

        # Intermediate (7 Questions)
        {"id": 208, "difficulty": "Intermediate", "question": "What is the main difference between ArrayList and LinkedList in Java?", "options": ["ArrayList uses dynamic array; LinkedList uses doubly linked list", "LinkedList is faster for index access", "ArrayList uses pointers", "LinkedList stores immutable objects"], "answer": "ArrayList uses dynamic array; LinkedList uses doubly linked list"},
        {"id": 209, "difficulty": "Intermediate", "question": "Which block always executes regardless of whether an exception occurs in Java?", "options": ["catch", "finally", "finalize", "try"], "answer": "finally"},
        {"id": 210, "difficulty": "Intermediate", "question": "What is the difference between Method Overloading and Method Overriding?", "options": ["Overloading occurs in same class with different parameters; Overriding occurs in subclass with same parameters", "Overriding occurs in same class", "Both require static methods", "No difference"], "answer": "Overloading occurs in same class with different parameters; Overriding occurs in subclass with same parameters"},
        {"id": 211, "difficulty": "Intermediate", "question": "Which interface must be implemented to create a thread in Java?", "options": ["Runnable", "Callable", "Threadable", "Process"], "answer": "Runnable"},
        {"id": 212, "difficulty": "Intermediate", "question": "What is the purpose of the `transient` keyword in Java?", "options": ["Prevents a variable from being serialized", "Makes a variable thread-safe", "Stores variable in heap memory", "Prevents reassignment"], "answer": "Prevents a variable from being serialized"},
        {"id": 213, "difficulty": "Intermediate", "question": "Which collection class does not allow duplicate elements in Java?", "options": ["List", "Set", "Vector", "ArrayList"], "answer": "Set"},
        {"id": 214, "difficulty": "Intermediate", "question": "What is autoboxing in Java?", "options": ["Automatic conversion between primitive types and corresponding wrapper classes", "Compressing JAR files", "Automatic garbage collection", "Memory allocation for arrays"], "answer": "Automatic conversion between primitive types and corresponding wrapper classes"},

        # Advanced (6 Questions)
        {"id": 215, "difficulty": "Advanced", "question": "How does Java Memory Model manage String Constant Pool?", "options": ["Stores string literals in Heap memory to prevent duplicate objects", "Stores strings in Stack", "Deletes strings after execution", "Saves strings on Disk"], "answer": "Stores string literals in Heap memory to prevent duplicate objects"},
        {"id": 216, "difficulty": "Advanced", "question": "How does HashMap handle collision internally in Java 8+?", "options": ["Uses Linked List and transforms to Red-Black Tree when threshold exceeds 8", "Overwrites old values", "Throws OutOfMemoryError", "Uses simple arrays"], "answer": "Uses Linked List and transforms to Red-Black Tree when threshold exceeds 8"},
        {"id": 217, "difficulty": "Advanced", "question": "What is the purpose of the `volatile` keyword in Java multithreading?", "options": ["Guarantees visibility of changes to variables across threads directly from main memory", "Locks the object exclusively", "Prevents class compilation", "Optimizes JVM bytecode"], "answer": "Guarantees visibility of changes to variables across threads directly from main memory"},
        {"id": 218, "difficulty": "Advanced", "question": "What is G1 Garbage Collector in Java?", "options": ["A server-style garbage collector targeting multi-processor machines with large memory", "A single-threaded collector", "A stack-only memory clearer", "A compiler flag"], "answer": "A server-style garbage collector targeting multi-processor machines with large memory"},
        {"id": 219, "difficulty": "Advanced", "question": "What is Java Reflection API?", "options": ["Allows inspecting and modifying runtime behavior of applications/classes dynamically", "Draws UI components", "Generates documentation", "Handles socket connections"], "answer": "Allows inspecting and modifying runtime behavior of applications/classes dynamically"},
        {"id": 220, "difficulty": "Advanced", "question": "What is the difference between `fail-fast` and `fail-safe` iterators?", "options": ["Fail-fast throws ConcurrentModificationException on modification; Fail-safe works on copy of collection", "Fail-safe throws exception immediately", "Both allow unsafe modifications without notice", "Fail-fast operates on thread copies"], "answer": "Fail-fast throws ConcurrentModificationException on modification; Fail-safe works on copy of collection"}
    ],

    # ==========================================
    # 3. C (20 Questions: Easy, Medium, Difficult)
    # ==========================================
    "C": [
        # Basic (7 Questions)
        {"id": 301, "difficulty": "Basic", "question": "Which operator is used to return the address of a variable in C?", "options": ["*", "&", "->", "&&"], "answer": "&"},
        {"id": 302, "difficulty": "Basic", "question": "Which function is used for dynamic memory allocation in C?", "options": ["malloc()", "alloc()", "new", "create()"], "answer": "malloc()"},
        {"id": 303, "difficulty": "Basic", "question": "What is the correct syntax for a main function in C?", "options": ["int main()", "void main()", "main()", "func main()"], "answer": "int main()"},
        {"id": 304, "difficulty": "Basic", "question": "Which header file is required for printf() and scanf() in C?", "options": ["<stdio.h>", "<stdlib.h>", "<conio.h>", "<math.h>"], "answer": "<stdio.h>"},
        {"id": 305, "difficulty": "Basic", "question": "What is format specifier for printing an integer in C?", "options": ["%f", "%c", "%d", "%s"], "answer": "%d"},
        {"id": 306, "difficulty": "Basic", "question": "Which keyword is used to declare a constant variable in C?", "options": ["const", "final", "static", "immutable"], "answer": "const"},
        {"id": 307, "difficulty": "Basic", "question": "What character terminates strings in C?", "options": ["\\n", "\\0", ";", "EOF"], "answer": "\\0"},

        # Intermediate (7 Questions)
        {"id": 308, "difficulty": "Intermediate", "question": "What is a dangling pointer in C?", "options": ["Pointer pointing to a memory location that has been freed", "Pointer assigned NULL value", "Pointer declared without type", "Pointer pointing to main function"], "answer": "Pointer pointing to a memory location that has been freed"},
        {"id": 309, "difficulty": "Intermediate", "question": "What is difference between malloc() and calloc()?", "options": ["calloc() initializes allocated memory to zero; malloc() leaves garbage values", "malloc() is slower", "calloc takes 1 argument; malloc takes 2", "No difference"], "answer": "calloc() initializes allocated memory to zero; malloc() leaves garbage values"},
        {"id": 310, "difficulty": "Intermediate", "question": "Which storage class retains variable value between function calls in C?", "options": ["auto", "register", "static", "extern"], "answer": "static"},
        {"id": 311, "difficulty": "Intermediate", "question": "What does typedef keyword do in C?", "options": ["Creates an alias name for existing data types", "Defines new functions", "Allocates heap memory", "Imports external files"], "answer": "Creates an alias name for existing data types"},
        {"id": 312, "difficulty": "Intermediate", "question": "What is a NULL pointer in C?", "options": ["A pointer pointing to address 0 (does not point to any valid memory)", "An uninitialized pointer", "A pointer to main", "A deleted variable"], "answer": "A pointer pointing to address 0 (does not point to any valid memory)"},
        {"id": 313, "difficulty": "Intermediate", "question": "What does the sizeof operator return in C?", "options": ["Size of data type/variable in bytes", "Length of array string", "Memory address", "Bit count"], "answer": "Size of data type/variable in bytes"},
        {"id": 314, "difficulty": "Intermediate", "question": "Which function deallocates dynamic memory in C?", "options": ["free()", "delete()", "clear()", "remove()"], "answer": "free()"},

        # Advanced (6 Questions)
        {"id": 315, "difficulty": "Advanced", "question": "What is the size of a pointer in a 64-bit C compiler?", "options": ["4 bytes", "8 bytes", "2 bytes", "16 bytes"], "answer": "8 bytes"},
        {"id": 316, "difficulty": "Advanced", "question": "What is a function pointer in C?", "options": ["A pointer storing address of an executable function code in memory", "A pointer returned by function", "A recursive function", "A macro function"], "answer": "A pointer storing address of an executable function code in memory"},
        {"id": 317, "difficulty": "Advanced", "question": "What is the purpose of `volatile` keyword in C?", "options": ["Tells compiler not to optimize variable because its value can change unexpectedly outside program", "Makes variable constant", "Increases CPU speed", "Stores variable in CPU registers"], "answer": "Tells compiler not to optimize variable because its value can change unexpectedly outside program"},
        {"id": 318, "difficulty": "Advanced", "question": "What is memory leakage in C?", "options": ["Failure to deallocate dynamically allocated memory using free() before losing pointer reference", "RAM overflow", "Stack buffer overflow", "Compiler crash"], "answer": "Failure to deallocate dynamically allocated memory using free() before losing pointer reference"},
        {"id": 319, "difficulty": "Advanced", "question": "What is difference between Structure and Union in C?", "options": ["Members in structure have separate memory; Union members share same memory location", "Union holds more data", "Structure is faster", "Union cannot store integers"], "answer": "Members in structure have separate memory; Union members share same memory location"},
        {"id": 320, "difficulty": "Advanced", "question": "What is flexible array member in C structures?", "options": ["An array without explicit size declared as last member of structure for dynamic sizing", "An array that auto-sorts", "A pointer array", "A stack buffer"], "answer": "An array without explicit size declared as last member of structure for dynamic sizing"}
    ],

    # ==========================================
    # 4. SQL (20 Questions: Easy, Medium, Difficult)
    # ==========================================
    "SQL": [
        # Basic (7 Questions)
        {"id": 401, "difficulty": "Basic", "question": "Which SQL statement is used to extract data from a database?", "options": ["SELECT", "GET", "EXTRACT", "OPEN"], "answer": "SELECT"},
        {"id": 402, "difficulty": "Basic", "question": "Which clause is used to filter rows in a SQL query?", "options": ["WHERE", "HAVING", "GROUP BY", "ORDER BY"], "answer": "WHERE"},
        {"id": 403, "difficulty": "Basic", "question": "Which command is used to insert new records into a table?", "options": ["INSERT INTO", "ADD RECORD", "UPDATE", "CREATE"], "answer": "INSERT INTO"},
        {"id": 404, "difficulty": "Basic", "question": "Which SQL clause is used to sort the result set?", "options": ["ORDER BY", "SORT BY", "GROUP BY", "ALIGN BY"], "answer": "ORDER BY"},
        {"id": 405, "difficulty": "Basic", "question": "Which aggregate function calculates average value in SQL?", "options": ["AVG()", "MEAN()", "CALC_AVG()", "SUM_AVG()"], "answer": "AVG()"},
        {"id": 406, "difficulty": "Basic", "question": "Which constraint ensures that all values in a column are distinct?", "options": ["UNIQUE", "PRIMARY KEY", "CHECK", "NOT NULL"], "answer": "UNIQUE"},
        {"id": 407, "difficulty": "Basic", "question": "Which SQL keyword is used to update existing records in a table?", "options": ["UPDATE", "MODIFY", "ALTER", "CHANGE"], "answer": "UPDATE"},

        # Intermediate (7 Questions)
        {"id": 408, "difficulty": "Intermediate", "question": "Which SQL clause is used to filter records after aggregation (GROUP BY)?", "options": ["WHERE", "HAVING", "ORDER BY", "FILTER"], "answer": "HAVING"},
        {"id": 409, "difficulty": "Intermediate", "question": "Which keyword is used to remove duplicate records from a query result?", "options": ["DISTINCT", "UNIQUE", "DIFFERENT", "SINGLE"], "answer": "DISTINCT"},
        {"id": 410, "difficulty": "Intermediate", "question": "What is the main difference between WHERE and HAVING clauses?", "options": ["WHERE filters rows before grouping; HAVING filters aggregated groups", "WHERE works on aggregates; HAVING works on individual rows", "No difference", "HAVING is faster than WHERE"], "answer": "WHERE filters rows before grouping; HAVING filters aggregated groups"},
        {"id": 411, "difficulty": "Intermediate", "question": "Which JOIN returns all records from the left table and matched records from the right table?", "options": ["LEFT JOIN", "RIGHT JOIN", "INNER JOIN", "FULL OUTER JOIN"], "answer": "LEFT JOIN"},
        {"id": 412, "difficulty": "Intermediate", "question": "Which command removes all records from a table without deleting table structure?", "options": ["TRUNCATE", "DROP", "REMOVE", "CLEAR"], "answer": "TRUNCATE"},
        {"id": 413, "difficulty": "Intermediate", "question": "What does a FOREIGN KEY constraint do?", "options": ["Maintains referential integrity between tables by referencing Primary Key of another table", "Uniquely identifies table rows", "Encrypts column values", "Indexes table columns"], "answer": "Maintains referential integrity between tables by referencing Primary Key of another table"},
        {"id": 414, "difficulty": "Intermediate", "question": "What does UNION operator do in SQL?", "options": ["Combines result-set of two or more SELECT statements eliminating duplicates", "Merges database instances", "Joins tables horizontally", "Sums numerical columns"], "answer": "Combines result-set of two or more SELECT statements eliminating duplicates"},

        # Advanced (6 Questions)
        {"id": 415, "difficulty": "Advanced", "question": "Which window function assigns a unique sequential integer to rows within a partition?", "options": ["ROW_NUMBER()", "RANK()", "DENSE_RANK()", "NTILE()"], "answer": "ROW_NUMBER()"},
        {"id": 416, "difficulty": "Advanced", "question": "What does the 'I' in ACID properties stand for?", "options": ["Isolation", "Integrity", "Index", "Identifier"], "answer": "Isolation"},
        {"id": 417, "difficulty": "Advanced", "question": "How does a B-Tree Index improve query execution time?", "options": ["Reduces search space from O(N) to logarithmic O(log N)", "Stores data in cache memory", "Deletes redundant rows", "Compresses row sizes"], "answer": "Reduces search space from O(N) to logarithmic O(log N)"},
        {"id": 418, "difficulty": "Advanced", "question": "What is a Common Table Expression (CTE) defined with?", "options": ["WITH clause", "TEMP clause", "CTE clause", "DECLARE clause"], "answer": "WITH clause"},
        {"id": 419, "difficulty": "Advanced", "question": "Difference between RANK() and DENSE_RANK() window functions?", "options": ["RANK leaves gaps in sequence when ties occur; DENSE_RANK does not leave gaps", "DENSE_RANK leaves gaps; RANK does not", "Both produce identical ranks always", "RANK works only on numbers"], "answer": "RANK leaves gaps in sequence when ties occur; DENSE_RANK does not leave gaps"},
        {"id": 420, "difficulty": "Advanced", "question": "What is a clustered index in SQL databases?", "options": ["Index that determines physical order of data storage inside table", "Index built on secondary key", "An unindexed view", "A temporary RAM index"], "answer": "Index that determines physical order of data storage inside table"}
    ],

    # ==========================================
    # 5. JAVASCRIPT (20 Questions: Easy, Medium, Difficult)
    # ==========================================
    "JavaScript": [
        # Basic (7 Questions)
        {"id": 501, "difficulty": "Basic", "question": "Which keyword is used to declare a block-scoped variable in JavaScript?", "options": ["var", "let", "global", "def"], "answer": "let"},
        {"id": 502, "difficulty": "Basic", "question": "What will `typeof NaN` return in JavaScript?", "options": ["number", "nan", "undefined", "object"], "answer": "number"},
        {"id": 503, "difficulty": "Basic", "question": "Which method parses a JSON string into a JavaScript object?", "options": ["JSON.parse()", "JSON.stringify()", "JSON.toObject()", "parseJSON()"], "answer": "JSON.parse()"},
        {"id": 504, "difficulty": "Basic", "question": "How do you write a single line comment in JS?", "options": ["// comment", "/* comment */", "<!-- comment -->", "# comment"], "answer": "// comment"},
        {"id": 505, "difficulty": "Basic", "question": "Which operator performs strict equality comparison in JavaScript?", "options": ["==", "===", "=", "equals"], "answer": "==="},
        {"id": 506, "difficulty": "Basic", "question": "Which method adds elements to end of an array in JavaScript?", "options": ["push()", "pop()", "shift()", "unshift()"], "answer": "push()"},
        {"id": 507, "difficulty": "Basic", "question": "Which HTML element is used to embed JavaScript code?", "options": ["<script>", "<js>", "<javascript>", "<code_js>"], "answer": "<script>"},

        # Intermediate (7 Questions)
        {"id": 508, "difficulty": "Intermediate", "question": "What is Closure in JavaScript?", "options": ["A function bundled together with references to its surrounding lexical state", "Closing database connection", "A method for deleting variables", "An async promise handler"], "answer": "A function bundled together with references to its surrounding lexical state"},
        {"id": 509, "difficulty": "Intermediate", "question": "What is output of `3 + '3'` in JavaScript?", "options": ["'33'", "6", "NaN", "TypeError"], "answer": "'33'"},
        {"id": 510, "difficulty": "Intermediate", "question": "What does Array.prototype.map() method return?", "options": ["A new array with results of calling provided function on every element", "Modifies original array", "A boolean value", "Single reduced value"], "answer": "A new array with results of calling provided function on every element"},
        {"id": 511, "difficulty": "Intermediate", "question": "What is hoisting in JavaScript?", "options": ["Variable and function declarations are moved to top of their scope before code execution", "Moving scripts to footer", "Optimizing array iteration", "Lifting DOM elements"], "answer": "Variable and function declarations are moved to top of their scope before code execution"},
        {"id": 512, "difficulty": "Intermediate", "question": "What does `async/await` do in JavaScript?", "options": ["Syntactic sugar over Promises to write cleaner asynchronous code", "Runs multithreaded loops", "Freezes UI thread", "Compiles JS into C++"], "answer": "Syntactic sugar over Promises to write cleaner asynchronous code"},
        {"id": 513, "difficulty": "Intermediate", "question": "Difference between `null` and `undefined` in JavaScript?", "options": ["undefined means variable declared but not assigned; null is an intentional assignment of no value", "Both are identical", "null is primitive; undefined is object", "undefined is assigned manually"], "answer": "undefined means variable declared but not assigned; null is an intentional assignment of no value"},
        {"id": 514, "difficulty": "Intermediate", "question": "What is purpose of `use strict` directive in JS?", "options": ["Enforces stricter parsing and error handling in JavaScript code", "Speeds up network requests", "Enables TypeScript syntax", "Disables console logs"], "answer": "Enforces stricter parsing and error handling in JavaScript code"},

        # Advanced (6 Questions)
        {"id": 515, "difficulty": "Advanced", "question": "How does the JavaScript Event Loop manage asynchronous callbacks?", "options": ["Executes Call Stack, processes Microtask queue (Promises), then Callback Queue (Timers)", "Executes all queues simultaneously", "Uses multithreaded CPU cores", "Blocks UI thread until finished"], "answer": "Executes Call Stack, processes Microtask queue (Promises), then Callback Queue (Timers)"},
        {"id": 516, "difficulty": "Advanced", "question": "What is Prototypal Inheritance in JS?", "options": ["Objects inherit properties directly from other objects via prototype chain", "Classes compiled into binary", "Static inheritance model", "Module compilation"], "answer": "Objects inherit properties directly from other objects via prototype chain"},
        {"id": 517, "difficulty": "Advanced", "question": "What is currying in Functional JavaScript?", "options": ["Technique of converting a function with multiple arguments into sequence of nested functions with single argument", "Combining arrays", "Caching function outputs", "Asynchronous loop execution"], "answer": "Technique of converting a function with multiple arguments into sequence of nested functions with single argument"},
        {"id": 518, "difficulty": "Advanced", "question": "What is difference between `call()`, `apply()`, and `bind()`?", "options": ["call passes args individually; apply passes args array; bind returns bound function instance", "All execute immediately always", "bind takes array arguments", "No difference"], "answer": "call passes args individually; apply passes args array; bind returns bound function instance"},
        {"id": 519, "difficulty": "Advanced", "question": "What is a Proxy object in JavaScript?", "options": ["Object that wraps another object and intercepts operations like reading/writing properties", "Network HTTP proxy server", "Garbage collection wrapper", "Shadow DOM node"], "answer": "Object that wraps another object and intercepts operations like reading/writing properties"},
        {"id": 520, "difficulty": "Advanced", "question": "What is Garbage Collection mechanism in V8 Engine?", "options": ["Generational Garbage Collector using Mark-Sweep and Scavenger algorithms", "Manual pointer deletion", "Reference counter only", "Stack allocation clearer"], "answer": "Generational Garbage Collector using Mark-Sweep and Scavenger algorithms"}
    ],

    # ==========================================
    # 6. HTML & CSS (20 Questions: Easy, Medium, Difficult)
    # ==========================================
    "HTML": [
        # Basic
        {"id": 601, "difficulty": "Basic", "question": "Which HTML element specifies footer for document?", "options": ["<bottom>", "<footer>", "<section>", "<foot>"], "answer": "<footer>"},
        {"id": 602, "difficulty": "Basic", "question": "Which attribute defines inline styles in HTML?", "options": ["class", "styles", "style", "css"], "answer": "style"},
        {"id": 603, "difficulty": "Basic", "question": "Which HTML tag is used to create a hyperlink?", "options": ["<a>", "<link>", "<href>", "<url>"], "answer": "<a>"},
        {"id": 604, "difficulty": "Basic", "question": "Which tag creates an unordered bulleted list?", "options": ["<ul>", "<ol>", "<li>", "<list>"], "answer": "<ul>"},
        {"id": 605, "difficulty": "Basic", "question": "Which attribute specifies image source path in <img> tag?", "options": ["src", "href", "path", "link"], "answer": "src"},
        {"id": 606, "difficulty": "Basic", "question": "Correct HTML element for largest heading?", "options": ["<h1>", "<h6>", "<heading>", "<head>"], "answer": "<h1>"},
        {"id": 607, "difficulty": "Basic", "question": "Which HTML5 tag is used to embed video?", "options": ["<video>", "<media>", "<movie>", "<embed>"], "answer": "<video>"},

        # Intermediate
        {"id": 608, "difficulty": "Intermediate", "question": "Purpose of HTML5 `<canvas>` element?", "options": ["Render dynamic 2D/3D graphics via JavaScript", "Display audio files", "Embed database tables", "Format text"], "answer": "Render dynamic 2D/3D graphics via JavaScript"},
        {"id": 609, "difficulty": "Intermediate", "question": "Target attribute `target='_blank'` does what?", "options": ["Opens linked document in new tab/window", "Opens in same frame", "Downloads file", "Closes window"], "answer": "Opens linked document in new tab/window"},
        {"id": 610, "difficulty": "Intermediate", "question": "What is Semantic HTML?", "options": ["Using tags that clearly describe their meaning/content to browser and developer", "Using div tags everywhere", "CSS styled HTML", "Compressed HTML code"], "answer": "Using tags that clearly describe their meaning/content to browser and developer"},
        {"id": 611, "difficulty": "Intermediate", "question": "What does doctype `<!DOCTYPE html>` do?", "options": ["Informs browser about HTML version (HTML5 standard rendering mode)", "Links CSS file", "Defines page title", "Imports JS library"], "answer": "Informs browser about HTML version (HTML5 standard rendering mode)"},
        {"id": 612, "difficulty": "Intermediate", "question": "Difference between `id` and `class` attributes?", "options": ["id is unique to single element; class can be shared across multiple elements", "class is unique", "id is for CSS only", "No difference"], "answer": "id is unique to single element; class can be shared across multiple elements"},
        {"id": 613, "difficulty": "Intermediate", "question": "Which attribute provides alternative text for images if they fail to load?", "options": ["alt", "title", "src", "desc"], "answer": "alt"},
        {"id": 614, "difficulty": "Intermediate", "question": "Which HTML5 input type allows selecting date?", "options": ["type='date'", "type='calendar'", "type='day'", "type='time'"], "answer": "type='date'"},

        # Advanced
        {"id": 615, "difficulty": "Advanced", "question": "What is the Shadow DOM in HTML5 Web Components?", "options": ["Scoped DOM tree attached to element isolated from main document DOM styles/scripts", "Hidden div tag", "CSS backdrop filter", "Browser cache DOM"], "answer": "Scoped DOM tree attached to element isolated from main document DOM styles/scripts"},
        {"id": 616, "difficulty": "Advanced", "question": "Difference between LocalStorage, SessionStorage, and Cookies?", "options": ["LocalStorage persists until cleared; SessionStorage expires on tab close; Cookies sent with HTTP requests", "Cookies store unlimited data", "SessionStorage persists permanently", "LocalStorage sent to server"], "answer": "LocalStorage persists until cleared; SessionStorage expires on tab close; Cookies sent with HTTP requests"},
        {"id": 617, "difficulty": "Advanced", "question": "What are ARIA attributes in HTML?", "options": ["Accessible Rich Internet Applications tags that improve accessibility for screen readers", "Animation attributes", "Responsive CSS queries", "Routing tags"], "answer": "Accessible Rich Internet Applications tags that improve accessibility for screen readers"},
        {"id": 618, "difficulty": "Advanced", "question": "What is Cross-Origin Resource Sharing (CORS) meta header handling?", "options": ["Browser security mechanism restricting resource requests from different domain origins", "Database sharing tag", "CSS stylesheet loader", "SSL cert validator"], "answer": "Browser security mechanism restricting resource requests from different domain origins"},
        {"id": 619, "difficulty": "Advanced", "question": "What is Web Worker API in HTML5?", "options": ["Executes JS scripts in background threads without blocking main UI thread", "Automated CSS builder", "Server background worker", "Database worker"], "answer": "Executes JS scripts in background threads without blocking main UI thread"},
        {"id": 620, "difficulty": "Advanced", "question": "Difference between `async` and `defer` attributes in script tags?", "options": ["async downloads asynchronously and executes immediately; defer executes after document parsing completes", "defer executes first", "async blocks HTML parsing", "Both are identical"], "answer": "async downloads asynchronously and executes immediately; defer executes after document parsing completes"}
    ],

    # ==========================================
    # 7. MACHINE LEARNING / ML (20 Questions: Easy, Medium, Difficult)
    # ==========================================
    "Machine Learning": [
        # Basic
        {"id": 701, "difficulty": "Basic", "question": "Which technique is used to prevent Overfitting in Machine Learning models?", "options": ["Regularization (L1/L2)", "Increasing Model Complexity", "Removing Training Data", "Ignoring Validation Split"], "answer": "Regularization (L1/L2)"},
        {"id": 702, "difficulty": "Basic", "question": "Supervised Learning requires which type of dataset?", "options": ["Labeled Data", "Unlabeled Data", "Only Numerical Target Vectors", "No Target Values"], "answer": "Labeled Data"},
        {"id": 703, "difficulty": "Basic", "question": "Which algorithm is commonly used for classification based on majority voting among k neighbors?", "options": ["K-Nearest Neighbors (KNN)", "K-Means", "Linear Regression", "PCA"], "answer": "K-Nearest Neighbors (KNN)"},
        {"id": 704, "difficulty": "Basic", "question": "Linear Regression is primarily used for predicting what type of target variable?", "options": ["Continuous Numerical Value", "Categorical Class Label", "Image Mask", "Text Sequences"], "answer": "Continuous Numerical Value"},
        {"id": 705, "difficulty": "Basic", "question": "Which metric is used to evaluate classification model accuracy?", "options": ["Confusion Matrix & Accuracy Score", "Mean Squared Error (MSE)", "R-squared", "MAE"], "answer": "Confusion Matrix & Accuracy Score"},
        {"id": 706, "difficulty": "Basic", "question": "What is the split ratio commonly used for Train-Test validation?", "options": ["80:20 or 70:30", "50:50", "10:90", "100:0"], "answer": "80:20 or 70:30"},
        {"id": 707, "difficulty": "Basic", "question": "K-Means algorithm belongs to which class of Machine Learning?", "options": ["Unsupervised Learning", "Supervised Learning", "Reinforcement Learning", "Semi-supervised"], "answer": "Unsupervised Learning"},

        # Intermediate
        {"id": 708, "difficulty": "Intermediate", "question": "What does 'Overfitting' mean in Machine Learning?", "options": ["Model performs well on training data but poorly on test data", "Model performs poorly on both training and test data", "Model trains too fast", "Dataset has missing features"], "answer": "Model performs well on training data but poorly on test data"},
        {"id": 709, "difficulty": "Intermediate", "question": "What is the primary objective of Principal Component Analysis (PCA)?", "options": ["Dimensionality reduction while preserving maximum variance", "Clustering unlabeled images", "Predicting categorical targets", "Neural weight tuning"], "answer": "Dimensionality reduction while preserving maximum variance"},
        {"id": 710, "difficulty": "Intermediate", "question": "What is Bias-Variance Tradeoff?", "options": ["Balancing underfitting (high bias) and overfitting (high variance) for optimal generalization", "Balancing training time and RAM usage", "Trading dataset size for accuracy", "Selecting hyper-parameters"], "answer": "Balancing underfitting (high bias) and overfitting (high variance) for optimal generalization"},
        {"id": 711, "difficulty": "Intermediate", "question": "What is Random Forest algorithm?", "options": ["Ensemble learning method operating by constructing a multitude of decision trees during training", "Single deep decision tree", "Linear classification algorithm", "Clustering model"], "answer": "Ensemble learning method operating by constructing a multitude of decision trees during training"},
        {"id": 712, "difficulty": "Intermediate", "question": "Which evaluation metric is best for highly imbalanced datasets?", "options": ["F1-Score / ROC-AUC", "Standard Accuracy", "Mean Squared Error", "R-Squared"], "answer": "F1-Score / ROC-AUC"},
        {"id": 713, "difficulty": "Intermediate", "question": "Difference between L1 (Lasso) and L2 (Ridge) Regularization?", "options": ["L1 adds absolute weights penalty causing sparsity; L2 adds squared weights penalty", "L2 causes sparsity; L1 does not", "Both add cubic penalty", "L1 is for clustering only"], "answer": "L1 adds absolute weights penalty causing sparsity; L2 adds squared weights penalty"},
        {"id": 714, "difficulty": "Intermediate", "question": "What is Cross-Validation (e.g., K-Fold CV)?", "options": ["Resampling procedure used to evaluate machine learning models on limited data samples across K splits", "Testing on external data only", "Merging 2 datasets", "Cleaning missing values"], "answer": "Resampling procedure used to evaluate machine learning models on limited data samples across K splits"},

        # Advanced
        {"id": 715, "difficulty": "Advanced", "question": "Which ensemble technique combines weak learners sequentially to correct errors?", "options": ["Boosting (e.g., XGBoost, Gradient Boosting)", "Bagging (e.g., Random Forest)", "Stacking", "Voting"], "answer": "Boosting (e.g., XGBoost, Gradient Boosting)"},
        {"id": 716, "difficulty": "Advanced", "question": "In SVM, what does the Kernel Trick do?", "options": ["Maps input data into higher-dimensional space to make non-linear data linearly separable", "Reduces dataset size", "Removes outliers", "Performs feature scaling"], "answer": "Maps input data into higher-dimensional space to make non-linear data linearly separable"},
        {"id": 717, "difficulty": "Advanced", "question": "How does Gradient Descent algorithm update model parameter weights?", "options": ["Moves parameters in opposite direction of gradient of loss function with respect to weights", "Random weight assignment", "Moves along positive gradient direction", "Scales weights by mean value"], "answer": "Moves parameters in opposite direction of gradient of loss function with respect to weights"},
        {"id": 718, "difficulty": "Advanced", "question": "What is SMOTE (Synthetic Minority Over-sampling Technique)?", "options": ["Algorithm to handle imbalanced datasets by generating synthetic samples for minority class", "Feature reduction technique", "Outlier removal script", "Loss optimizer"], "answer": "Algorithm to handle imbalanced datasets by generating synthetic samples for minority class"},
        {"id": 719, "difficulty": "Advanced", "question": "What is Naive Bayes classifier 'naive' assumption?", "options": ["Assumes all input features are mutually independent given the class label", "Assumes data is linearly separable", "Assumes normal distribution only", "Assumes no missing values"], "answer": "Assumes all input features are mutually independent given the class label"},
        {"id": 720, "difficulty": "Advanced", "question": "What is SHAP (SHapley Additive exPlanations) used for in ML?", "options": ["Explainable AI framework explaining individual predictions based on game theoretic Shapley values", "Hyperparameter tuning library", "Model compression", "Dataset augmentation"], "answer": "Explainable AI framework explaining individual predictions based on game theoretic Shapley values"}
    ]
}