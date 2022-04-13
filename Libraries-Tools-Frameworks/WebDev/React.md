# React

React is a frontend reactive framework developed by Facebook.

## Basics

React creates reactive user interfaces through _React Components_.
React components can either be defined as a class or a function. Classes
are typically used with more complex components that have their own state
or define multiple functions. Functions are used with simple components
that just return an element.

```jsx
class Box extends React.Component {
    render() {
        return (
            <div id="box">React Component</div>
        );
    }
}
```

```jsx
function Box() {
    return (
        <div id="box">React Component</div>
    )
}
```

### Props

Props is an object that contains values passed down the element tree from parent to child:

```jsx
class Child extends React.Component {
    render() {
        return (
            <div>{this.props.someValue}</div>
        )
    }
}


class Parent extends React.Component {
    render() {
        return (
            <Child someValue={10}/>
        );
    }
}
```

> React elements are first class JavaScript objects. So they can passed around in functions,
stored in variables, arrays, and other objects as well.

### State

Each React Component can contain a _state_ object. This state object is what components
use to _remember_ things in a frontend applications. This state object should be considered
private to the React component it is defined in.

```jsx
class Box extends React.Component {
    constructor(props) {
        // super(props); is required when defining a constructor in a child of the React.Component class.
        super(props);
        this.state = {
            name: null,
        };
    }

    render() {
        return (
            <button onClick={() => this.setState({name: 'The Box'})}>
                {this.state.value}
            </button>
        )
    }
}
```

> Note that the state isn't updated directly, but updated using `this.setState()`. The reason for
this is that it allows React components to re-render properly. It's more difficult to detect changes
in state if it's updated directly instead of through the `setState()` method.

### Global State

Although each component can have it's own private state, when it comes to sharing values
across multiple components, it's best to define a global state in the root parent component
and pass those values into a child's props. The child then _lifts_ the new values to the 
parent so that parent can update the global state.

To perform an update to the parent's state, the child uses a function passed down from
the parent that updates the state. Since a components cannot alter another component's
state (due to a state's private nature), the parent defines a function that alters
its own state and passes that function to the child's props so that that child can
call the function.


```jsx
class Child extends React.Component {
    render() {
        return (
            <div onClick={() => this.props.onClick()}>{this.props.name}</div>
        )
    }
}


class Parent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            childName: null,
        };
    }

    setName(newName) {
        this.setState({name: 'New Name'})
    }

    render() {
        return (
            <Child name={this.state.childName} onClick={() => this.setName()}/>
        );
    }
}
```


> Asking for values from a child's private state object is possible, however this leads
to more complicated code and is more succeptible to bugs.

## Lifecycle
## Components & Styling
## Routing
## Requests
## Workflow

### Dynamic Lists

When generating lists, React will complain if a key property isn't defined. The reason
for this is that it's difficult for React to determine the order of elements or whether
they should be recreated, destroyed, or maintained. Having a unique key property helps
React make these rendering decisions.

```jsx
class List extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            listItems: ['a', 'b', 'c']
        }
    }

    render() {
        const items = this.state.listItems.map((item, i) => {
            return (
                <li key={i}>{item.data}</li>
            )
        })

        return (
            <ol>
                {items}
            </ol>
        )
    }

}
```

> The key must only be unique amongst the element's siblings. Array indices are **NOT**
recommended to be used as keys since they present the same problem defining a key is trying
to avoid.

## Advance Use

### React Hooks

## Other