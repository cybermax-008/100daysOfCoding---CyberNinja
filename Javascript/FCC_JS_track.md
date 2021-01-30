# Javascript Track FCC

### Concepts covered so far

**Basics:**
- Variable creation using `var`
- Data types - `number`, `string`, `undefined`, `float`, `boolean`
- Arithematic operations : sum, subtract, multiply, modulo, division
- Increment and decrement variable
- Escape sequences - Usage of `\`
- Access characters in String
- Arrays
- Access and Modify elements in Arrays using index
- 2D Arrays - Access and Modify
- Array methods - `push()`, `pop()`, `unshift()`, `shift()`
- Using Functions in JS
- Global and local scope of variables
- Conditions - `if else and else if`
- Switch cases 
- Objects in JS
- Object operations : Access, Modify and remove
- JSON
- Nested Objects
- Nested Arrays 
- Loops : `for` , `while` and `do while`
- USing `recursion`
- Generate Random numbers 
- Type casting using `parseInt(string,radix)`
- Recursion for countup (need to review)
- Recursion for countdown ( need to review)

**ES6:**
The most recent standardized version is called ECMAScript 6 (ES6), released in 2015. This new version of the language adds some powerful features that will be covered in this section of challenges, including:

* Arrow functions
* Classes
* Modules
* Promises
* Generators
* `let` and `const`


## ES6 Track 

**Explore difference betweeen `var` , `let` and `const`**
Using `use strict;` make sure that you do make unsafe actions. Using `var` allow you to re-assign your variable. Using `let` will not allow you to repeat same variable names.
- If we declare a variable with `var`, it is declared golablly or locally. But, `let`, it has the scope limited to the block or statement or expression.
- `cont` variable is used, if you do not want to change it anytime in the code.
- if a array is declared using `const`, the variable can't be used to reassign to some new array. but, the array elements are still mutable.

1) To make sure the object is immutable, we need to freeze the object using `Object.freeze(obj)`.
2) We can use `=>` arrow function to define anonymous functions. 
The below function,
`const myFunc = function() {
      const myVar = "value";
      return myVar;
       }`
       Can be rewritten using `=>`
   `const myFunc = () => {
      const myVar = "value";
      return myVarWrite 
    }`
    
   3) Write Arrow function with arguments.
   Just like a regular function, you can pass arguments into an arrow function.

    // doubles input value and returns it
    const doubler = (item) => item * 2;
    doubler(4); // returns 8
    

If an arrow function has a single parameter, the parentheses enclosing the parameter may be omitted.

    // the same function, without the parameter parentheses
    const doubler = item => item * 2;
    

It is possible to pass more than one argument into an arrow function.

    // multiplies the first input value by the second and returns it
    const multiplier = (item, multi) => item * multi;
    multiplier(4, 2); // returns 8`
    
 4) Use rest parameter to give variable number of arguments.

Check out this code:

    function howMany(...args) {
      return "You have passed " + args.length + " arguments.";
    }
    console.log(howMany(0, 1, 2)); // You have passed 3 arguments.
    console.log(howMany("string", null, [1, 2, 3], { })); // You have passed 4 arguments`
    
  The rest parameter eliminates the need to check the `args` array and allows us to apply `map()`, `filter()` and `reduce()` on the parameters array.
  
    const  sum = (...args) => args.reduce((a, b) =\> a \+ b, 0);

5) Use spread operator `...args` to evaluate arrays in place.

Usually, we use `.apply()` like,
   ` var arr = [6, 89, 3, 45];
    var maximus = Math.max.apply(null, arr); // returns 89`
    
We had to use `Math.max.apply(null, arr)` because `Math.max(arr)` returns `NaN`. `Math.max()` expects comma-separated arguments, but not an array. The spread operator makes this syntax much better to read and maintain.
Using spread operator, it `...args` unpacks the array elements.
`const arr = [6, 89, 3, 45];
const maximus = Math.max(...arr); // returns 89`

6) Deconstructing assignement can be used to assign values taken from an object neatly.

Usually, we extarct values from object like,
    `const user = { name: 'John Doe', age: 34 };`
    
    `const name = user.name; // name = 'John Doe'
    const age = user.age; // age = 34`
    
Using deconstructive assingment,
`const { name, age } = user;`

This will automatically assign respective values from the `user`.
7) We can also use different variables to assign using deconstructive assignment.

    `const { name: userName, age: userAge } = user;`
    
 8) We can also deconstruct values from an array, or swap values between variables.

    `const [a, b,,, c] = [1, 2, 3, 4, 5, 6];
    console.log(a, b, c); // 1, 2, 5`
    
   ` let  a = 8, b = 6;
    [a,b]= [b,a];`
    
   9) We can extarct sub-array from an array using decosntruction.

`const myArray = [1,2,3,4,5];
   const [a,b,...arr] = myArray;
    console.log(a,b); \\ it il print 1 and 2
    console.log(arr); \\ it will print 3,4,5`
    
   10) Use Deconstructive assignment to pass an object as function parameter.
Usually,
   ` const profileUpdate = (profileData) => {
      const { name, age, nationality, location } = profileData;
      // do something with these variables
    }`
    
  We can also,
      `const profileUpdate = ({ name, age, nationality, location }) => {
      /* do something with these fields */
    }`
    
    



