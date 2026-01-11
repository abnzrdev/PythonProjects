# Programming Paradigms: Personal Notes

## Understanding Programming Paradigms

### Procedural Programming
- Programs follow a step-by-step approach
- Code organized into procedures/functions
- Data and operations are separate
- Like following a recipe: first do this, then do that

### Functional Programming
- Based on mathematical functions
- **Avoiding state change** means functions don't modify existing data structures or variables
  - Instead of changing a list, create a new list with the changes
  - This reduces bugs and makes code more predictable
- **Immutable data** means once created, data doesn't change
  - Examples: strings, tuples in Python are immutable
  - Lists are mutable (can be changed)
- **Functions as first-class citizens** means functions can be:
  - Stored in variables
  - Passed to other functions as arguments
  - Returned from other functions

```python
# Functions as first-class citizens example
def create_multiplier(factor):
    # Returns a new function
    return lambda x: x * factor

double = create_multiplier(2)  # Store function in variable
triple = create_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

### Object-Oriented Programming (OOP)
- Programs built around objects that contain data and code
- Classes serve as templates/blueprints for creating objects
- Objects have properties (attributes) and behaviors (methods)
- When creating programs using oop the thing that someone has to care about what it has and what it does.

```python
# Creating different objects from the same class template
class CoffeeMachine:
    def __init__(self, brand, price_per_cup, capacity):
        self.brand = brand
        self.price_per_cup = price_per_cup
        self.capacity = capacity
        self.water_level = capacity
        
    def make_coffee(self):
        if self.water_level >= 50:
            self.water_level -= 50
            return f"Coffee made! Cost: ${self.price_per_cup}"
        return "Not enough water!"

# Different coffee machines from same template
office_machine = CoffeeMachine("BrewMaster", 2.50, 2000)
home_machine = CoffeeMachine("HomeBrew", 0, 1000)

print(office_machine.make_coffee())  # Coffee made! Cost: $2.50
print(home_machine.make_coffee())    # Coffee made! Cost: $0
```

## When to Use Each Paradigm

### Procedural Programming
- **Best for:** Simple scripts, small utilities, straightforward tasks
- **Pros:** Easy to learn, quick to implement, straightforward logic
- **Cons:** Harder to maintain larger programs, limited code reuse

### Functional Programming
- **Best for:** Data processing, mathematical operations, concurrent programming
- **Pros:** Fewer bugs, easier testing, better for parallel processing
- **Cons:** Steeper learning curve, can be less intuitive for modeling real-world objects

### Object-Oriented Programming
- **Best for:** Large applications, systems modeling real-world entities, GUIs
- **Pros:** Better organization, data protection, code reuse through inheritance
- **Cons:** Overkill for simple problems, requires more planning, potential performance overhead

## Additional Important Programming Concepts

### Event-Driven Programming
- Program flow determined by events (user actions, system events)
- Common in GUIs, web development, mobile apps
- Example: Coffee machine interface responding to button presses

### Declarative Programming
- Focus on what to do rather than how to do it
- Examples include SQL, HTML, CSS
- Instead of loops to filter data, you just declare what data you want

### Design Patterns
- Reusable solutions to common programming problems
- Examples: Singleton (ensuring one instance), Factory (creating objects)
- Help structure code in maintainable ways

### SOLID Principles (for OOP)
- **S**ingle Responsibility: Each class has one job
- **O**pen/Closed: Open for extension, closed for modification
- **L**iskov Substitution: Derived classes can substitute base classes
- **I**nterface Segregation: Many specific interfaces better than one general one
- **D**ependency Inversion: Depend on abstractions, not implementations

## Practical Approach

Most modern applications combine multiple paradigms:
- Use OOP to model the overall system structure
- Use functional approaches for data processing
- Use procedural code for simple sequential operations
- Use event-driven programming for user interfaces

Choose the right tool for each specific problem rather than trying to force everything into one paradigm.

For your coffee machine project, consider a mix of OOP (to model the machine itself) with some functional concepts (for data processing) to create clean, maintainable code.

#### Deep Dive into SOLID Principles

##### Open/Closed Principle
The class itself should not be modified - instead, extend functionality by creating new classes that inherit from it.

```python
# Original class - DON'T MODIFY THIS
class Shape:
    def area(self):
        pass

# RIGHT way - extending without modifying the original
class Circle(Shape):  # ✅ New class extends Shape without changing it
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):  # ✅ Another extension without changing original
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Think of it like building blocks - don't break open existing blocks, just stack new ones on top
class CoffeeMachine:
    def make_coffee(self):
        return "Basic coffee"

class EspressoMachine(CoffeeMachine):
    def make_espresso(self):  # New feature added without changing original
        return "Espresso shot"
```

##### Liskov Substitution Principle
When creating a subclass, it must do the same thing as the parent class, just in a different way. All subclasses must be able to substitute their parent class.

```python
class Bird:
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        print("Flying through the air")

class WalkingBird(Bird):
    def move(self):
        print("Walking on the ground")

# Both can substitute Bird - they both move, just differently
def make_bird_move(bird: Bird):
    bird.move()  # Works with any Bird subclass

make_bird_move(FlyingBird())  # Flying through the air
make_bird_move(WalkingBird())  # Walking on the ground
```

##### Interface Segregation Principle
Don't add methods that a class doesn't need. Include only the functionality and attributes that the class can actually use.

```python
# BAD - forcing classes to implement methods they don't need
class AllInOneDevice:
    def print_document(self):
        pass
    def scan_document(self):
        pass
    def fax_document(self):
        pass

# GOOD - separate interfaces for different capabilities
class Printer:
    def print_document(self):
        pass

class Scanner:
    def scan_document(self):
        pass

class SimplePrinter(Printer):  # Only implements what it needs
    def print_document(self):
        print("Printing document")

class AllInOnePrinter(Printer, Scanner):  # Implements multiple interfaces only if it can
    def print_document(self):
        print("Printing document")
    
    def scan_document(self):
        print("Scanning document")
```
##### Dependency Inversion Principle
High-level classes should depend on concepts/abstractions, not on specific concrete implementations. Think of it like electrical outlets - your house depends on the outlet standard, not on specific devices.

**What it means:** Instead of your main code being tied to specific implementations, it should work with general concepts that any implementation can follow.

**The Three-Part Structure:**

1. **Concept Class (Abstract/Interface)** - defines what should happen
```python
class PaymentMethod:
    def pay(self, amount):
        pass  # Just the concept, doesn't do actual work
```