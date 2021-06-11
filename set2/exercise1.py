"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"


some_words = ['what', 'does', 'this', 'line', 'do', '?']

# I think this will print "what does this line do?"
for word in some_words:
    print(word) # it printed each word on a seperate line"

# I think this will print the same as the previous line"
for x in some_words:
    print(x) # it printed the same"

# I think this will print "['what', 'does', 'this', 'line', 'do', '?']"
print(some_words) # It printed "['what', 'does', 'this', 'line', 'do', '?']"

# I think this will print "some_words contains more than 3 words"
if len(some_words) > 3:
    print('some_words contains more than 3 words') # it printed "some_words contains more than 3 words"

# I'm not sure :/
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    #prints computer specs + date and time
    print(platform.uname())

usefulFunction()
