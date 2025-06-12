# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

de

# EXAMPLE


def age_checker(date_of_birth):
    """
    Checks if user is under or over 16 and return string to say access is denied or granted 

    Parameters: (list all parameters and their types)
        date_of_birth, string in format 'YYYY-MM-DD'

    Returns: (state the return value and its type)
        returns string:
        if under 16 returns - access denied, current age and the required age
        if over 16 returns - access granted

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
date of birth = 16 and over 
returns access granted
"""
age_checker("2009-04-03") => "access granted"

"""
date of birth = under 16 
returns access denied
"""
age_checker("2011-04-03") => "current age 14, required age 16, access denied"

"""
date format incorrect 

returns - error
"""
age_checker("03-04-11") = "throws error"

"""
date not a string 

returns - error
"""
age_checker(03-04-11) = "throws error"



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
