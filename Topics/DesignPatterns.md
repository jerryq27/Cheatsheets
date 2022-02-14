# Design Patterns

There are four main categories.  

1. Creational Patterns
1. Structural Patterns
1. Behavioral Patterns
1. J2EE Patterns

## Creational Patterns

Creational patterns provides a way to control the creation of objects by hiding the creation logic.

### Factory Pattern

Factory for objects with the same super class.  
[Shape Example](https://www.tutorialspoint.com/design_pattern/factory_pattern.htm)

### Abstract Factory Pattern

Factory for factories pattern.  
[Rounded Shapes Example](https://www.tutorialspoint.com/design_pattern/abstract_factory_pattern.htm)

### Singleton Pattern

Creates one, and only one, instance of an object.  
[Single Instance Example](https://www.tutorialspoint.com/design_pattern/singleton_pattern.htm)

### Builder Pattern

Building complex objects from smaller objects.  
[Meal Example](https://www.tutorialspoint.com/design_pattern/builder_pattern.htm)

### Prototype Pattern

Cloning objects that would otherwise be too costly to re-create.  
[Cloning Shapes Example](https://www.tutorialspoint.com/design_pattern/prototype_pattern.htm)

## Structural Patterns

Structural Patterns provide ways to compose objects to obtain new functionalities.  

### Adapter Pattern

Used to combine the capability of two incompatible interfaces.  
[Media Player Example](https://www.tutorialspoint.com/design_pattern/adapter_pattern.htm)

### Bridge Pattern

Used to decouple an abstract class from its implementation so they can be used independently.  
[Drawing Shapes Example](https://www.tutorialspoint.com/design_pattern/bridge_pattern.htm)

### Filter Pattern

Allows for the filtering of a set of objects based on a certain criteria.  
[Person Example](https://www.tutorialspoint.com/design_pattern/filter_pattern.htm)

### Composite Pattern

Treating a group of objects as a single object in a tree-like structure.  
[Employees Example](https://www.tutorialspoint.com/design_pattern/composite_pattern.htm)

### Decorator Pattern

Allows adding functionality to an existing object without altering its structure.  
[Shape Borders Example](https://www.tutorialspoint.com/design_pattern/decorator_pattern.htm)

### Facade Pattern

Pattern that hides complexity by providing simplified methods.  
[Shape Maker Example](https://www.tutorialspoint.com/design_pattern/facade_pattern.htm)

### Flyweight Pattern

Used to reduce number of objects created and reduce memory usage.  
[Random Shape Properties Example](https://www.tutorialspoint.com/design_pattern/flyweight_pattern.htm)

### Proxy Pattern

Creating Proxy objects to reduce the memory footprint of the real objects.  
[Proxy Image Example](https://www.tutorialspoint.com/design_pattern/proxy_pattern.htm)

## Behavioral Patterns

Behavioral Patterns are specifically concerned with communication between objects.

### Chain of Responsibility Pattern

This pattern uses a chain of objects of receivers who have a reference to each other. If one receiver can't handle a request, it is passed to the next receiver.  
[Logger Example](https://www.tutorialspoint.com/design_pattern/chain_of_responsibility_pattern.htm)

### Command Pattern

This pattern uses a request object as a command which is passed into an invoker object, the invoker then looks for and passes the command object to the appropriate object that can handle this command.  
[Stock Example](https://www.tutorialspoint.com/design_pattern/command_pattern.htm)

### Interpreter Pattern

Provides a way to evaluate language grammar or expressions.  
[Interpreter Example](https://www.tutorialspoint.com/design_pattern/interpreter_pattern.htm)

### Iterator Pattern

This pattern is used to get elements from a collection in a sequential manner without knowing its underlying representation.  
[Name List Example](https://www.tutorialspoint.com/design_pattern/iterator_pattern.htm)

### Mediator Pattern

Reduces communication complexity between multiple objects.  
[Chatroom Example](https://www.tutorialspoint.com/design_pattern/mediator_pattern.htm)

### Memento Pattern

Used to restore an object to a previous state.  
[State Example](https://www.tutorialspoint.com/design_pattern/memento_pattern.htm)

### Observer Pattern

Used when an object has a one to many relationship with other objects, such that if one object is modified, the dependent objects are notified automatically.  
[Octal/Hex/Binary Example](https://www.tutorialspoint.com/design_pattern/observer_pattern.htm)

### State Pattern

Class behavior changes based on its state.  
[Context/State Example](https://www.tutorialspoint.com/design_pattern/state_pattern.htm)

### Null Object Pattern

Replaces null checking with a do-nothing null object that provides default behavior in case data is not available.  
[Customer Example](https://www.tutorialspoint.com/design_pattern/null_object_pattern.htm)

### Strategy Pattern

Class behavior or algorithm can be changed at run time.  
[Add/Subtract/Multiply Example](https://www.tutorialspoint.com/design_pattern/strategy_pattern.htm)

### Template Pattern

Defined methods are provided by an abstract class which a subclass can override, but the original definition needs to be invoked someway. It's defined definition is preferred in most cases.  
[Game Example](https://www.tutorialspoint.com/design_pattern/template_pattern.htm)

### Visitor Pattern

A visitor class changes the executing algorithm based on the object being visited.  
[Computer Parts Example](https://www.tutorialspoint.com/design_pattern/visitor_pattern.htm)

## J2EE Patterns

These design patterns are specifically concerned with the presentation tier. These patterns are identified by Sun Java Center.
