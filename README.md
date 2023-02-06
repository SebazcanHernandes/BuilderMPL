# BuilderMPL

BuilderMPL (shorthand of Builder's Multi-Purpose (Programming) Language) is a programming language that contains numerous aspects of a programming language that makes it unique: object-oriented programming, web programming, game development, etc. This repository is the open-source code of the language itself for other programmers who wants to build a programming language to learn from ours.

Here are some basics of the language you must know:

## Operators, Statements, Loops

Like other programming languages, there's simple processes like operators, statements, and loops. The big difference is how the syntax works:

```bmpl
int i = 20; ~ Assigning an integer
when (i < 50) { ~ When loop
  say("Not 50\n"); ~ Output
  i++; ~ Increment i by 1
}

int a = 5; int b = 6;
if (a == b) { ~ If-but if-but statement
  say("Equal");
} but if (a < b) {
  say("a is smaller");
} but {
  say("a is bigger");
}
```

## Arrays and More Variables

Arrays work like PHP arrays, but a bit simpler. And along with that, more variables are created.

```bmpl
array a = [("consonants")><["b", "c", "d"], ("vowels")><["a", "e", "i"]]; ~ Array
var v = "Hello";
say(v); ~ Prints v
v = 12;
say(v); ~ Prints 12
dt = get_presentTime(); ~ DateTime variable
```

## Functions and Object-Oriented Programming

You can create functions, rename them through variable syntax, import them from module to module, and even apply object-oriented programming on all the code you're doing.

```
function something(var x) { ~ Function syntax
  ~ Whatever you want
  return y
}

class person = { ~ Classes
  string name, int age, var job
};
var Dave = person("Dave", 20, None);
```

## Web Programming and Game Development (Coming soon)

BuilderMPL can also be used for not just scripting webpages, but also designing! It can also help with creating games. As of now, there's not much idea on how these will be implemented.

Try out BuilderMPL today.
