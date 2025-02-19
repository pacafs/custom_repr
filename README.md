# Custom Repr

A simple decorator to add pretty representation to Python classes.

## Installation

```sh
pip install custom-repr
```

## Usage

```python
from custom_repr import add_repr

@add_repr  # Add this decorator to every class you want to use the custom_repr format
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 30)

print(person)  # Person(name: "John", age: 30)
