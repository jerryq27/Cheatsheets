# Pulse

## Basics

PulseJS is a state library with some added functionality for Vue, React, and vanilla JS.

Values are stored in the same way a database would save data.

### Collections

PreBuilt Collection methods included in every collection
(Recommended to be called within **actions** methods):
`someCollection.indexes.someGroup;` - Returns array of primary keys (indexes).
`someCollection.put(ID, groupName)` - Puts data by ID (or array of IDs) to a group.
`someCollection.move(ID, groupName)` - Moves data by ID (or array of IDs) from one group to another group.
`` - .
`` - .
`` - .
`` - .
`` - .

#### Models

Used to structure how the data is stored, SQL table columns!

```javascript
model: {
    id: {
        primaryKey: true,
        type: Number, // not yet implemented.
        required: true, // not yet implemented.
    }
}
```

Data not meeting the model's requirements are inserted into the Error's object as a "Data Rejection".

#### Groups

Groups are a way to categorize data.

Groups create arrays based on the primary keys of the data called **Indexes**.
    If an object's primary key changes, data is rebuilt from the index, which is faster.
Groups can be created in 2 ways:

1. Using a Collection's **group** property (Allows for `someCollection.someGroup;` access.
2. Created dynamically, but must be accessed with `someCollection.getGroup('someGroup);`

#### Data

#### Persist

Used to save **data** properties locally.
Data keys are stored here.

Features to be implemented:

* Saving an entire collection
* Custom storage option per collection.