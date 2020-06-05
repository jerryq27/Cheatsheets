# Review

## Questions(17...)

Base Pulse library has the following:

```javascript
pulse: {
    collections:{},
    request: {},
    services: {},
    utils: {},
    jobs: {},

    // Base
    model: {},
    data: {},
    groups: [],
    persist: [],
    routes: {},
    actions: {},
    filters: {},
    watch: {},
}
```

Each collection has this structure:

```javascript
pulse: {
    collections: {
        someCollection: {
            model: {},
            data: {},
            groups: [],
            persist: [],
            routes: {},
            actions: {},
            filters: {},
            watch: {},
        }
    }
}
```

Q: Reasoning behind the design choice of making the **base Pulse object** a collection itself?  
A:

---

Collections are a way to easily save data:

Q: Is it correct to say that **collections** are structured to be a database table's data, data structure, methods to manipulate the data, etc. all in one?  
A:

Q: Collections are not the data itself?  
A:

Q: If the **models** defines and `id` or `_id` property, but doesn't define them with the `primaryKey: true` property, are they still used as the primary key?
A:

---

> Collecting data works like a pre-built Vuex mutation function or a reducer in Redux, it handles data normalization, history and race condition prevention behind the scenes: `collection.collect(someData, 'groupName');`
You should assign data a "group" as you collect it, this is required if you want to use collected data in React/Vue components reactively.

Q: Even if the developer doesn't need to use grouping, does a group name have to be specified to collect the data?  
A:

---

Namespacing rules are also ambiguous

```javascript
import pulse from './Pulse';

let {
    collection1,
    collection2,
    collection3,
} = pulse.collections;

collection1.collect(); // This doesn't work.

pulse.collections.collection1.collect(); // This doesn't work.


pulse.collection1.collect(); //Works!

let { collection1 } = pulse;
collection1.collect(); // Works!

```

Q: **collections** are ommitted?  
A:

The documentation also defines some namespacing rules for collections.

> By default, you can access everything under the collection namespace, like this:

```javascript
collection.groupName; // array
collection.randomDataName; // boolean
collection.filterName; // cached array
collection.doSomething(); // function
```

> But if you prefer to seperate everything by type, you can access areas of your collection like so:

```javascript
collection.groups.groupName; //array
collection.data.randomDataName; // boolean
collection.filters.filterName; // cached array
collection.actions.doSomething(); // function
```

Q: There seems to be namespacing rules for the base Pulse object as well, what would they be?  
A:

---

> Using data in VueJS and React is simple with mapData(). It will return an object containing Pulse data properties that you request. The string must contain a slash, first the name of the collection, then the data property.

`pulse.mapData({ localName: 'collection/property' });`

> localName is customizable. read only, only public data.

Q: Wording should be used carefully here (I assumed it was the **data** property of a collection at first), but is it correct to assume mapData() is used to access the properties within Pulse, or just within the collections?  

i.e. are all these strings valid?  
`someCollection/groups`  
`someCollection/data`  
`collections/someCollection/groups`  
`request/someRequest`  
`services/someService`  

Q: Why `/` delimited instead of `.`?  
A:

---

> The base and request collections are created by default, with their own custom data properties and related logic. Use of these is optional, but can save you time!

```javascript
pulse: {
    collections:{},
    request: {}, // <- this is a collection too?  
    services: {},
    utils: {},
    jobs: {},

    // Base
    model: {},
    data: {},
    groups: [],
    persist: [],
    routes: {},
    actions: {},
    filters: {},
    watch: {},
}
```

**Potential Confusion:** so pulse itself is a collection, and collections are grouped within the **collections** property, but then the document says **request** and **base** are collections created by default:

Q: Does **request** also include the **model**, **groups**, **persist**, **etc.** properties?  
A:

Q: Are **services**, **utils**, and **jobs** also collections?  
A:

Q: Does **base** refer to the **base Pulse Object** in the documentation's _Default Properties_ section?  
A:

---

The _Persisting Data_ section shows:

```javascript
collection: {
  data: {
    haha: true;
  }
  persist: ['haha'];
}
```

Q: Objects defined in **data** can have keys that aren't indexes? I assumed **data** was stored using indexes:

```javascript
data: {
    1: {},
    2: {},
    3: {},
}
```

A:

Q: Can **group** names be specified in **persist**?  
A:

Pulse's `storage: 'sessionStorage'` is considered a default value, but isn't included in the provided **base Pulse object** structure.  
Q: Are there other customizable default values that haven't been included?  
A:

---

>Actions receive a context object (see Context Object) as the first paramater, this includes every registered collection by name, the routes object and all default collection functions.

Q: Is it correct to assume the **Context Object** is the **base Pulse object**?  
A:

---

Group/Data confusion:

FIRST: Validate if this information is true:  

```text
AKA dataset {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
group1[1, 5, 10]
group2[2, 3, 4, 6, 7, 8, 9]
```

These questions are based on the assumption of how this structure looks in my head.

I assume that **groups** turn the **data** property into something like:

```javascript
data: {
    group1: [
        {}, //id 0
        {}, //id 1
        {}, //id 2
    ],
    group2: [
        {}, //id 0
        {}, //id 1
        {}, //id 2
    ]
}
```

`someCollection.put(ID, groupName)` - Puts data by ID (or array of IDs) to a group.  
Q: What happens if the ID's are taken and we try the `put()` method?  
A:

The documentation has an example formatted like:
`someCollection.put(1, 'group2');`

Q: But shouldn't the group be specified?  
`someCollection.group1.put(1, 'group2');`
A:

In my example, I'm moving something from **group1** with the **id 1** to **group2** which already has the **id 1** taken.
This also brings the question:
Q: When using built-in collection methods like `.put()`, `.move()`, `.update()`, how are the keys kept unique?  
    Is it appended to the end of group2?  
    Will group1's id's update since the item with **id 1** has been put to another group?  
    The `put()` and `move()`, `put()` moves data into a group, `move()` moves data from one group to another, so why does put only accept an ID and not an object? where does it get the data from with only an ID?  
    How do `delete()` and `update()` know which group's values are being modified

---

> Filters allow you to alter data before passing it to your component without changing the original data. Essentially getters in VueX. 

Q: Would it be correct to assume that filters are basically data validaters?  
A:

---

> Data not meeting the model's requirements are inserted into the Error's object as a "Data Rejection".  

Q: Possibly a JavaScript noob question, is the error object stored in the base Pulse object or where can it be accessed?  
A:

---

## ReadMe Rewrite Proposal

This is from my perspective reading through the documentation.

* I assumed at first that collections would hold my state(s) (coming from a Redux background).

```javascript
// Redux structure
initialState = {
    auth: {
        username: '',
        password: '',
        token: '',
    },
    info: {
        firstName: '',
        lastName: '',
        age: 0,
    },
    prefs: {
        displayName: '',
        theme: 'light',
        autologin: false,
    }
}
```

```javascript
// Collections assumption.
collections: {
    auth: {
        username: '',
        password: '',
        token: '',
    },
    info: {
        firstName: '',
        lastName: '',
        age: 0,
    },
    prefs: {
        displayName: '',
        theme: 'light',
        autologin: false,
    }
}
```

* So it took a bit to wrap my head around what collections were exactly.
After reading about how Pulse is structuring data in a database-like style, things made more sense.
* Another assumption I made with groups is that each group would store data, but have their own indexes as well, since `someCollection.groupName.indexes` return [0 - n].
So I thought if every group restarts the index, how could you move data between groups? (This was before I read about primary keys and the whole database structure)
* The documentation is also assuming that the developer is familiar with Vue, or other state managers.

> The only assumption Pulse should make is that the developer is looking for a centralized state for whatever framework they are using.

* The word choice should be used carefully to avoid confusion, for example Pulse defines **data** as a property of collection, but the documentation uses the word **data**
to refer to Pulse and Collection's properties, and section headers like **Accessing Data** give off the wrong impression.
  * Ex. `collection.collect(res.data.channel, groupName);`, new term,
          **channel**, what is a channel in this context? a group?  
* Documentation provides some explanations to save data to Pulse, but not to grab the saved data from Pulse.
  * Did find `findById`, but maybe how to grab all data in a collection? By groups? relational data? Some examples would help a potential dev planning on using Pulse.
* Most of the examples are using the Notify functionality to demonstrate how Pulse works. These examples should be generic for any use case,
especially if Pulse is trying to target various frameworks: React, Vuew, Vanilla JS, etc.

> The documentation should explain the core concepts of what Pulse IS, a state manager, instead of a state manager for Notify (Which is how the current documentation feels like).

Ideas for Pulse's Core concepts:

### Pulse

Pulse structures data like a database would, using primary keys.

### Collections

Collections contain everything needed to work with a 'table' of data.

* **models** - the table's columns.
* **data** - the table's rows.
* **actions** - methods to work with table data.

### Groups

Groups are used to categorize the data in the collection's data (table).
Example data set

```javascript
food: {
    data: {
        0: 'apple',
        1: 'carrot',
        2: 'orange',
    },
    groups: [
        'fruits',
        'vegetables',
    ],
}
```

`pulse.food.fruits.indexes; // [0, 2]`

`pulse.food.vegetables.indexes; // [1]`

### Data Validation

Data validation is done with filters. (Needs Confirmation)

### Namespacing Rules

## Some Ideas

* Pulse/collection monitor - display the current state of a collection, or pulse itself (for devs), might cause issues with large data sets.

**RANDOM UNIMPORTANT IDEA**: How about changing `pulse-framework` to just `pulse` or `pulsejs`? lol.