# Design Patterns

[Checkpoint](https://youtu.be/tv-_1er1mWI?t=345)

Design patterns were created to solve a variety of different
problems that appear frequently in Object Oriented Programming.

There are three main categories for design patterns:

1. Creational Patterns - deals with how objects are created.
1. Structural Patterns - deals with how objects relate to eachother.
1. Behavioral Patterns - deals with how objects communicate with eachother.

It is important to remember that these patterns can be helpful, but can aslo
be used improperly and add unnecessary complexity and boilerplate code. A good
rule of thumb is to see if the language's features already use a pattern before
implementing one. 

For example, a constant global object in JavaScript is a Singleton object by default
because of how JavaScript treats it as global data and passes it around by reference.
However, the same cannot be said for languages like Java and C++.

## Creational Patterns

Creational patterns deal with how objects are created. They provides a way to control
the creation of objects by hiding the creation logic.

### Singleton Pattern

A singleton is a very simple creational pattern. It creates one, and only one, instance of an object:

```ts
class Settings {
    static instance: Settings;
    public readonly mode = 'dark';

    // Prevent the use of the 'new' keyword to instantiate this object.
    private constructor() {}

    static getInstance(): Settings {
        if(!Settings.instance) {
            Settings.instance = new Settings();
        }
        
        return Settings.instance;
    }
}

const settings = Settings.getInstance();
```


[Single Instance Example](https://www.tutorialspoint.com/design_pattern/singleton_pattern.htm)

### Prototype Pattern

The prototype pattern clones objects that would otherwise be too costly to re-create:

```ts
// JavaScript, every object inherits from the Object class.
// That's why functionality is modified using the object's 'prototype'.
const ninja = {
    dissapear() {
        return "Poof!";
    }
}

// Args: prototype, additional properties.
const herald = Object.create(ninja, { name: { value: "herald" } });

// No dissapear() function..
console.log(herald); // { name: "herald" }

// Still works since JavaScript looks through the prototype tree.
herald.dissapear(); // "Poof!" 

Object.getPrototypeOf(herald); // Gets the ninja object.
```

**Problem**: With class inheritance, the hierarchy of objects can get complicated real quick.

**Solution**: This pattern provides an alternative for objects to inherit from an already defined object instead of a class.


[Cloning Shapes Example](https://www.tutorialspoint.com/design_pattern/prototype_pattern.htm)

### Builder Pattern

**Problem**: Creating objects with a lot of properties in the constructor can be make for a complex parameter list:

```java
public class Burger {

    private String bun;
    private boolean ketchup;
    private boolean mustard;
    private boolean kraut;

    public Burger(String bun, boolean ketchup, boolean mustard, boolean kraut) {
        this.bun = bun;
        this.ketchup = ketchup;
        this.mustard = mustard;
        this.kraut = kraut;
    }

}

public class Main {

    public static void main(String[] args) {
        // It's difficult to determine the properties of this object based on the parameters.
        Burger burger = new Burger("wheat", false, true, false);
    }

}
```

**Solution**: This pattern builds the object step-by-step using methods instead:

```java
public class Burger {

    private String bun;
    private boolean ketchup;
    private boolean mustard;
    private boolean kraut;

    public Burger(String bun) {
        this.bun = bun;
    }

    public Burger addKetchup() {
        this.ketchup = true;
        return this;
    }

    public Burger addMustard() {
        this.mustard = true;
        return this;
    }

    public Burger addKraut() {
        this.kraut = true;
        return this;
    }
}

public class Main {
    public static void main(String[] args) {
        // Breaking it down into methods makes it easier to see what object properties are being changed.
        Burger burger = new Burger("white")
            .addKetchup()
            .addKraut();
    }
}
```

[Meal Example](https://www.tutorialspoint.com/design_pattern/builder_pattern.htm)

### Factory Pattern

Factory for objects with the same super class.

**Problem**: Sometimes the creation of an object will be based on a condition:

```java
public class IOSButton extends Button {
    // code
}
public class AndroidButton extends Button {
    // Code
}

public class Main {
    public static void main(String[] args) {
        Button button;
        Button button2;

        // Numerous conditionals like these would be difficult to maintain.
        if(getOS() == "ios") {
            button = new IOSButton();
        }
        else {
            button = new AndroidButton();
        }

        // Other code

        if(getOS() == "ios") {
            button2 = new IOSButton();
        }
        else {
            button2 = new AndroidButton();
        }
    }
}
```

**Solution**: This pattern determines which object to instantiate:

```java
public class IOSButton extends Button {
    // code
}
public class AndroidButton extends Button {
    // Code
}
public class ButtonFactory {
    public static Button createButton(String os) {
        if(os == "ios") {
            return new IOSButton();
        }
        else {
            return new AndroidButton();
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Button button = ButtonFactory(getOS());

        // Other code

        Button button2 = ButtonFactory(getOS());
    }
}
```

[Shape Example](https://www.tutorialspoint.com/design_pattern/factory_pattern.htm)

### Abstract Factory Pattern

Factory for factories pattern.  
[Rounded Shapes Example](https://www.tutorialspoint.com/design_pattern/abstract_factory_pattern.htm)

## Structural Patterns

Structural Patterns deal with how objects relate to eachother. They provide ways to structure
objects to obtain new functionalities.  

### Facade Pattern

Pattern that hides complexity by providing simplified methods.

**Problem**: Implentations can get complex real quick and would be difficult to use by other objects:

```java
// These functions are most likely very complex, and the House object is also getting complex.
public class House {
    public void setElectricalSystemVoltage(int voltage) {
        // Complicated low level code
    }
    public void turnOnElectricalSystem() {
        // Complicated low level code
    }

    public void setPlumbingSystemPressure(int pressure) {
        // Complicated low level code
    }
    public void turnOnPlumbingSystem() {
        // Complicated low level code
    }
}
```

**Solution**: This pattern hides the low-level logic that another object doesn't really need to know about:

```java
public class ElectricalSystem {
    public void setVoltage(int voltage) {
        // Complicated low level code
    }
    public void turnOn() {
        // Complicated low level code
    }
    public void turnOff() {
        // Complicated low level code
    }
}
public class PlumbingSystem {
    public void setPressure(int pressure) {
        // Complicated low level code
    }
    public void turnOn() {
        // Complicated low level code
    }
    public void turnOff() {
        // Complicated low level code
    }
}

// Complext logic is hidden.
public class House {
    private PlumbingSystem plumbing;
    private ElectricalSystem electical;

    public House() {
        plumbing = new PlumbingSystem();
        electrical = new ElectricalSystem();
    }

    public void turnOnSystems() {
        plumbing.setPressure(500);
        plumbing.turnOn();

        electrical.setVoltage(120);
        electrical.turnOn();
    }

    public void shutdown() {
        plumbing.turnOff();
        electrical.turnOff();
    }
}

// Makes for a much easier to use object.
public class Main {
    public static void main(String[] args) {
        House myHouse = new House();
        house.turnOnSystems();
        house.shutdown();
    }
}
```

[Shape Maker Example](https://www.tutorialspoint.com/design_pattern/facade_pattern.htm)

### Proxy Pattern

Creating Proxy objects to reduce the memory footprint of the real objects.  
[Proxy Image Example](https://www.tutorialspoint.com/design_pattern/proxy_pattern.htm)

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


### Flyweight Pattern

Used to reduce number of objects created and reduce memory usage.  
[Random Shape Properties Example](https://www.tutorialspoint.com/design_pattern/flyweight_pattern.htm)


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
