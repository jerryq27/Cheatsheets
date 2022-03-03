# Flutter

## Basics

## State

### Provider

The `provider` package defines a number of _Providers_ to handle
different types of state updates.

* Provider - This is the base provider class. It doesn't rebuild components on state change and requires a reload.
* ChangeNotifierProvider - Rebuilds components when changes to the state are detected.

To use this package, it has to be included in the `pubspec.yaml`
file:

```yaml
dependencies:
    provider: ^$VERSION
```

To use any of these Provider classes, a state (AKA model) class for the data must be defined:

```dart
class Character {
    String name = "Luffy";

    void changeName(String newName) {
        name = newName;
    }
}
```

#### ChangeNotifierProvider

The base Provider class will update the state, but the values won't be refelected in the
components. For a more reactive behavior, the _ChangeNotifierProvider_ class is used.

First, update the state/model class to extend _ChangeNotifier_ and add an `notifyListeners()`
to every method that makes any changes to the state:

```dart
class Character with ChangeNotifier {
    String name = "Luffy";

    void changeName(String newName) {
        name = newName;
        // Notifies components that the state has changed.
        notifyListeners();
    }
}
```

Child components wrapped in a _Consumer_ widget will be rebuilt when a `notifyListeners()` is
encountered:

```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'character.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider<Character>(
      create: (context) => Character(),
      child: MaterialApp(
          title: 'Flutter Demo',
          theme: ThemeData(
            primarySwatch: Colors.blue,
          ),
          home: const HomePage()),
    );
  }
}

```

## Lifecycle

## Components & Styling

## Routing

## Requests

## Workflow

## Other