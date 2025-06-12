# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

To find a task among all my notes. To do this I will need to check if the line contains the string #TODO

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def to_do_finder(my_notes):
    """

    Parameters: (list all parameters and their types)
       list of strings

    Returns: (state the return value and its type)
        True or False

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
If the string contains #TODO will return True

"""
to_do_finder("#TODO buy milk") => True

"""
If the string does not contain #TODO then will return False

"""
to_do_finder("drink tea")

"""
If the string contains TODO (no #) will return False

"""
to_do_finder("TODO buy crisps") => False

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!