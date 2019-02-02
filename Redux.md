# Redux
[Redux] is a centralized and predictable state container for web apps.
Works well with frameworks like [React].

## Basics
Redux has 3 concepts:
* Store - Where the centralized state for the React app is housed.
* Actions - Developer-defined actions that describe a state modification.
* Reducers - Uses actions to modify the store.

### Store
Where the centralized state of the entire app is located.

##### initialState.js
```javascript
// 'export' required to use outside the file.
export initial_state = {
    addValue: '',
    updateValue: 'Updtae Me',
    deleteValue: 'Delete Me'
};
```

##### store.js
```javascript
import { createStore } from 'redux';
import { initialState } from './initialState';
import { reducer } from './reducer'; // Needed to create the store.

const store = createStore(reducer);
// Optional to detect changes made to the store.
store.subscribe(() => {
    console.log('State changed: ', store.getState());
});

export default store;
```

### Actions
Actions are user defined, they are objects with usually 2 properties:

```javascript
var someAction = {
    type: 'SOME_ACTION',
    value: 'some_value'
}

/*  Redux function passed in when using Redux. 
    It sends the action object to the Reducer. */
dispatch(someAction); 
```

Since Actions are user defined, there are many approaches to implementing them.
#### Method 1:
The actions can be defined in two files: `actionTypes.js` and 
`actions.js`.

##### actionTypes.js
```javascript
// Constants defining our action types.
export const constants = {
    ADD_ACTION:     'ADD_ACTION',
    UPDATE_ACTION:  'UPDATE_ACTION',
    DELETE_ACTION:  'DELETE_ACTION',
}
```

##### actions.js
```javascript
// Functions returning objects that can be passed to the reducers.
import { constants } from './actionTypes';

export addAction = valueToAdd => {
    type: constants.ADD_ACTION,
    value: valueToAdd
}

export updateAction = updateValue => {
    type: constants.UPDATE_ACTION,
    value: updateValue
}

export deleteAction = deleteValue => {
    type: constants.DELETE_ACTION,
    value: deleteValue
}
```

##### example.js
```javascript
import { addAction } from './actions';

let exampleVal = 10;
dispatch(addAction(exampleVal));
```
###### Pros:
* Just two files.
* Easier to understand.

###### Cons:
* With many actions, `actions.js` can get long and difficult to manage.
* Can be difficult to work with multiple reducers.

#### Method 2:
Having a `constants.js` file with multiple action files.

##### constants.js
```javascript
export const constants = {
    ADD_ACTION:     'ADD_ACTION',
    UPDATE_ACTION:  'UPDATE_ACTION',
    DELETE_ACTION:  'DELETE_ACTION',
}
```

##### add.js
```javascript
import { constants } from './constants';

export addAction = valueToAdd => {
    type: constants.ADD_ACTION,
    value: valueToAdd
}
```

##### update.js
```javascript
import { constants } from './constants';

export updateAction = updateValue => {
    type: constants.UPDATE_ACTION,
    value: updateValue
}
```

##### delete.js
```javascript
import { constants } from './constants';

export deleteAction = deleteValue => {
    type: constants.DELETE_ACTION,
    value: deleteValue
}
```

###### Pros:
* Separates actions and logic which makes it easier to work with multiple reducers.
* Shorter files.
* Working with React-form is also easier.
* Server calls and other logic can also be handled by Redux in an understandale way.

###### Cons:
* With more actions, there are more files to manage.
* Potentially more difficult to understand.

### Reducers
Reducers are a JavaScript function that modifies the store based on object received 
from `dispatch()`. They are usually writted as a single `switch` statement since 
actions are defined by constants.

```javascript
import { initialState } from './initialState';
import { constants } from './constants';

export const reducer = (state = initialState, action) => {
    const newState = {...state}; // Make a hard copy of the current state.

    switch(action.type) {
        case constants.ADD:
            newState.addValue = action.value;
            return newState;
        case constants.UPDATE:
            newState.updateValue = 'Update Me';
            return newState;
        case constants.DELETE:
            newState.deleteValue = '';
            return newState;
        default:
            return newState;
    }
}
```

## React-Redux
To use Redux with React, you need to install the package.
```
npm install redux react-redux
```

Redux provides a `Provider` component, which should be the root component
in the React app. It passes the store to the whole application.
##### app.js
```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import store from './store/';

if(document.getElementById('root')) {
    ReactDOM.render(
        // Provider allows us to inject the store into the app.
        <Provider store={store}><Main/></Provider>,
        document.getElementById('root')
    );
}
```

To access the store in a React component, Redux will connect the store to 
the component's `props` through the use of the `connect` function.

The `connect` function takes two functions as arguments:
* `mapStateToProps` - Allows the component to access the store's values.
* `mapDispatchToProps` - Allows the component to access the reducer to 
modify the store.

##### Main.js
```jsx
import React, { Component } from 'react';
import { connect } from 'react-redux';
import  { add }  from './store/actions/';

class App extends Component {

    render() {
        ...
            // This will call the function that will pass an action
            // to the reducer with the value 'Add Me'.
            <div onClick={() => this.props.addValue('Add Me')}>
                Click Me!
            </div>
        ...

    }

}

mapStateToProps = state => {
    return {
        // <prop value>: <store value>
        update: state.updateValue,
    }
}

mapDispatchToProps = dispatch => {
    return {
        // <prop function>: <action to send to the reducer>
        addValue: (value) => dispatch(add(value)),
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(App);
```

### Multiple Reducers
This approach has multiple files for multiple reducers.
The initial state is also devided into substates (an object for each reducer file).

##### initialState.js

```javascript
initialState = {
    auth: {
        username: '',
        password: '',
        // Other auth related values.
    },
    messages: {
        error_msg: 'An error has occured.',
        custom_msg: '',
        // Other message related values.
    }
}
```

##### auth.js
```javascript
import initialState from './initialState';

export default authReducer = (state = initialState.auth, action) => {
    switch(action.type) {
       // Statements..
    }
}
```

##### messages.js
```javascript
import initialState from './initialState';

export default messagesReducer = (state = initialState.auth, action) => {
    switch(action.type) {
       // Statements..
    }
}
```

In `reducer.js` we combine the reducers into a single reducer and use that to create
the store.
##### reducer.js
```javascript
import { combineReducers } from 'redux'
import authReducer from './auth';
import messagesReducer from './messages'

const reducer = combineReducers({
    auth: authReducer,
    load: loadReducer,
});

export default reducer;
```

This reducer is used in the creation of the store:
```javascript
import { createStore } from 'redux';
import reducer from './reducer';

const store = createStore(reducer);

export default store;
```

[Redux]: https://redux.js.org/
[React]: https://reactjs.org/
