# Day 19: Event Listeners & Higher Order Functions 🎯

## 📚 Key Concepts

### 🔄 Higher Order Functions
Higher order functions are functions that can accept other functions as parameters or return functions as results.

**Important Notes:**
- ✅ Supported in Python and many modern programming languages
- ❌ Not supported in all programming languages
- 🎯 When passing a function as a parameter, **don't include parentheses** `()`

#### Example:
```python
def my_function():
    print("Hello World!")

# ✅ Correct - without parentheses
some_method(my_function)

# ❌ Wrong - with parentheses (this calls the function immediately)
some_method(my_function())

# ✅ Recommended - using keyword arguments
button.bind(command=my_function, text="Click Me")

# ❌ Less readable - using positional arguments
button.bind(my_function, "Click Me")


what are the things I need
1. moveup, down , left and right
setheading can do all those this is done
2. Circle
alright on the first part I think the game is not working using the set heading part cause it has to work on the postioion here the next thing to do is like to use the circle in order to do that and that is great we have radius we can use that for counter clock wise and and the other thing we can use the steps to make it more less speed drawing and those things

