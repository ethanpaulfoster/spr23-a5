#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!
# Checks that the program outputs "3" for an input of "6 / 2"
assert run("6 / 2").output == "3"
# Checks that the program outputs "24" for an input of "6 * 4"
assert run("6 * 4").output == "24"

###

print("All tests passed!")