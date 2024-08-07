import re

def find_joke(text):
    # This regex will match exactly "a joke" and ignore case
    if re.fullmatch(r"a joke", text, re.IGNORECASE):
        return "You asked for a joke, here it is: a joke."
    else:
        return "No joke found!"

# Test the function
print(find_joke("a joke"))  # This should return the joke
print(find_joke("A JOKE"))  # This should also return the joke
print(find_joke("that's a joke"))  # This should not return the joke
