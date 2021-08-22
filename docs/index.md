# Primitives

[![azure-devops-builds](https://img.shields.io/azure-devops/build/proofit404/primitives/18?style=flat-square)](https://dev.azure.com/proofit404/primitives/_build/latest?definitionId=18&branchName=master)
[![azure-devops-coverage](https://img.shields.io/azure-devops/coverage/proofit404/primitives/18?style=flat-square)](https://dev.azure.com/proofit404/primitives/_build/latest?definitionId=18&branchName=master)
[![pypi](https://img.shields.io/pypi/v/primitives?style=flat-square)](https://pypi.org/project/primitives)
[![python](https://img.shields.io/pypi/pyversions/primitives?style=flat-square)](https://pypi.org/project/primitives)

Fake objects designed with OOP in mind.

**[Documentation](https://proofit404.github.io/primitives) |
[Source Code](https://github.com/proofit404/primitives) |
[Task Tracker](https://github.com/proofit404/primitives/issues)**

Mock objects makes your tests worst. Usage of mock objects is considered an
anti-pattern by many experienced developers. Mock objects blindly respond to any
interaction. Patch function is able to put such objects in any place in your
code. It does not matter if that code was written in a way to be configured or
not. This situation has several consequences.

First of all, your tests start making assumptions about implementation of tested
code. This creates high coupling between tests and code. You no more could
easily change your code because 25 tests are aware of the name of the function
in the middle of the call stack.

The second unpleasant details about mocks is its fragile blind trust to the
client code. Writing mocks of proper quality is extremely complicated. You need
a ton of assert statements at the end of the test to check that only expected
methods were called. In addition API of the mock library in python is an ugly
procedural code. It requires a 3 lines just to define a dumb method returning
predefined value on mock. This harms readability of tests dramatically.

I was upset with mock library for the long time. I decided to design a
collection of strict composable objects without ability to put them at random
place in code. Here is what I came with!

## Pros

- Fake objects with strict behavior will highlight problems in your code earlier
- Nice composable API makes definition of complex objects short and concrete
- Force user to use composition instead of patch

## Example

The `primitives` library gives you a collection of objects with ability to
define expected behavior as set of short expressions. For example, you could
define a function returning `None` like this:

```pycon

>>> from primitives import Instance, Callable, Argument

>>> func = Callable()

>>> func()

```

Let's try to test a function below using `primitives` fake objects and standard
`unittest.mock` library for comparison.

```pycon

>>> def greet_many(repo):
...    for user in repo.users():
...        print(user.greet('Hello'))

>>> greet_many(Instance(users=Callable([
...     Instance(greet=Callable('Hello, John', Argument('Hello'))),
...     Instance(greet=Callable('Hello, Kate', Argument('Hello'))),
... ])))
Hello, John
Hello, Kate

```

We would leave `unittest.mock` implementation to the reader as a homework.

## Questions

If you have any questions, feel free to create an issue in our
[Task Tracker](https://github.com/proofit404/primitives/issues). We have the
[question label](https://github.com/proofit404/primitives/issues?q=is%3Aopen+is%3Aissue+label%3Aquestion)
exactly for this purpose.

## Enterprise support

If you have an issue with any version of the library, you can apply for a paid
enterprise support contract. This will guarantee you that no breaking changes
will happen to you. No matter how old version you're using at the moment. All
necessary features and bug fixes will be backported in a way that serves your
needs.

Please contact [proofit404@gmail.com](mailto:proofit404@gmail.com) if you're
interested in it.

## License

`primitives` library is offered under the two clause BSD license.

<p align="center">&mdash; ⭐ &mdash;</p>
<p align="center"><i>The <code>primitives</code> library is part of the SOLID python family.</i></p>
