// import React from 'react';
// import {
//   Image,
//   View,
//   Text,
//   StyleSheet
// } from 'react-native';

// const App = () => {
//   return (
//     // <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
//     <View style={styles.container}>
//       <Text style={styles.text}>Hello world!</Text>
//       <Image source={{ uri: 'https://randomuser.me/api/portraits/men/1.jpg'}} style={styles.img}/>
//     </View>
//   )
// }

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     justifyContent: 'center',
//     alignItems: 'center',
//   },
//   text: {
//     color: 'blue',
//     fontSize: 30,
//   },
//   img: {
//     width: 150,
//     height: 150,
//     borderRadius: 150/2, //round image icon
//   }
// });

import React, { useState } from 'react';
// import { uuid } from 'uuidv4';
import {
  Alert,
  FlatList,
  StyleSheet,
  View,
} from 'react-native';
import Header from './components/Header';
import ListItem from './components/ListItem';
import AddItem from './components/AddItem';

const App = () => {
  // Name for data, and function to manipulate data.
  const [items, setItems] = useState([
    { id: 1, text: 'Milk' },
    { id: 2, text: 'Eggs' },
    { id: 3, text: 'Bread' },
    { id: 4, text: 'Juice' },
  ]);

  const deleteItem = (id) => {
    setItems(prevItems => {
      return prevItems.filter(item => item.id != id);
    });
  };

  const addItem = (text) => {
    if(!text) {
      Alert.alert('Error', 'Please enter an item', [{ text: 'OK' }]);
    }
    else{
      setItems(prevItems => {
        return [ {id: null, text}, ...prevItems, ]
      });
    }
  };

  return (
    <View style={styles.container}>
      <Header title='Shopping List'/>
      <AddItem addItem={addItem}/>
      <FlatList 
        data={items}
        renderItem={ ({item}) => <ListItem item={item} deleteItem={deleteItem}/> }/>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
  }
});

export default App;