## ES6 Track 
The most recent standardized version is called ECMAScript 6 (ES6), released in 2015. This new version of the language adds some powerful features that will be covered in this section of challenges, including:

* Arrow functions
* Classes
* Modules
* Promises
* Generators
* `let` and `const`


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
    
 11) A new feature of ES6 is the template literal. This is a special type of string that makes creating complex strings easier. Template literals allow you to create multi-line strings and to use string interpolation features to create strings.

    const person = {
      name: "Zodiac Hasbro",
      age: 56
    };
    
    // Template literal with multi-line and string interpolation
    const greeting = `Hello, my name is ${person.name}!
    I am ${person.age} years old.`;
    
    console.log(greeting); // prints
    // Hello, my name is Zodiac Hasbro!
    // I am 56 years old.
    
  12) Write Concise Object Literal Declarations Using Object Property Shorthand

    const getMousePosition = (x, y) => ({ x, y });
    
  This returns object `{x:x,y:y`
  
  13) Write Concise Declarative Functions with ES6

USsually ,
`    const person = {
      name: "Taylor",
      sayHello: function() {
        return `Hello! My name is ${this.name}.`;
      }
    };`
    
   In ES6,
`       const person = {
      name: "Taylor",
      sayHello() {
        return `Hello! My name is ${this.name}.`;
      }
    };`
    
  14) Use class Syntax to Define a `Constructor` Function

Usually, to create a class,
    var SpaceShuttle = function(targetPlanet){
      this.targetPlanet = targetPlanet;
    }
    var zeus = new SpaceShuttle('Jupiter');
    

The `class` syntax simply replaces the constructor function creation:

    var SpaceShuttle = function(targetPlanet){
      this.targetPlanet = targetPlanet;
    }
    var zeus = new SpaceShuttle('Jupiter');
    
 In ES6, we can make use of constructor instead of function,
 
     class SpaceShuttle {
      constructor(targetPlanet) {
        this.targetPlanet = targetPlanet;
      }
    }
    const zeus = new SpaceShuttle('Jupiter');
    
 15) Use `getters` and `setters` to Control Access to an Object.  
Getter functions are meant to simply return (get) the value of an object's private variable to the user without the user directly accessing the private variable.

Setter functions are meant to modify (set) the value of an object's private variable based on the value passed into the setter function. This change could involve calculations, or even overwriting the previous value completely.

    class Book {
      constructor(author) {
        this._author = author;
      }
      // getter
      get writer() {
        return this._author;
      }
      // setter
      set writer(updatedAuthor) {
        this._author = updatedAuthor;
      }
    }
    const novel = new Book('anonymous');
    console.log(novel.writer);  // anonymous
    novel.writer = 'newAuthor';
    console.log(novel.writer);  // newAuthor
    
 16) Create a Module` Script`
In order to make JavaScript more modular, clean, and maintainable; ES6 introduced a way to easily share code among JavaScript files. This involves exporting parts of a file for use in one or more other files, and importing the parts you need, where you need them. In order to take advantage of this functionality, you need to create a script in your HTML document with a type of `module`. Here’s an example:

    <script type="module" src="filename.js"></script>
    
  17) Use `export` to Share a Code Block

    const add = (x, y) => {
      return x + y;
    }
    
    export { add };
    
  18) Reuse JavaScript Code Using` import`

    import { add } from './math_functions.js';
   To import all fucntions,
  `import * as myMathModule from "./math_functions.js";`
    
   19) Use `export default` in case only one value being exported from a file.

`export default function add(x,y)=>{
             return x+y;
             }`
  20) Use `import` for export default values.

`import add from "./math_funtions.js"`

21) Create a Javascript `Promise`
A promise in JavaScript is exactly what it sounds like - you use it to make a promise to do something, usually asynchronously. When the task completes, you either fulfill your promise or fail to do so. `Promise` is a constructor function, so you need to use the `new` keyword to create one. It takes a function, as its argument, with two parameters - `resolve` and `reject`. These are methods used to determine the outcome of the promise. The syntax looks like this:

    const myPromise = new Promise((resolve, reject) => {
    
    });
    
 A promise has three states: `pending`, `fulfilled`, and `rejected`. The promise you created in the last challenge is forever stuck in the `pending` state because you did not add a way to complete the promise. The `resolve` and `reject` parameters given to the promise argument are used to do this. `resolve` is used when you want your promise to succeed, and `reject` is used when you want it to fail. These are methods that take an argument, as seen below.
 
 22) Handling fulfilled Promise with `then` and Rejected Promise with `catch`

Promises are most useful when you have a process that takes an unknown amount of time in your code (i.e. something asynchronous), often a server request. When you make a server request it takes some amount of time, and after it completes you usually want to do something with the response from the server. This can be achieved by using the `then` method. The `then` method is executed immediately after your promise is fulfilled with `resolve`. 

`catch` is the method used when your promise has been rejected. It is executed immediately after a promise's `reject` method is called.
Example - 

`const  makeServerRequest = new  Promise((resolve, reject) =\> {
// responseFromServer is set to false to represent an unsuccessful response from a server
let  responseFromServer = false;
if(responseFromServer) {
resolve("We got the data");
} else {
reject("Data not received");
}
});
makeServerRequest.then(result =\> {
console.log(result);
});

makeServerRequest.catch( error =\> {
console.log(error);
})`







