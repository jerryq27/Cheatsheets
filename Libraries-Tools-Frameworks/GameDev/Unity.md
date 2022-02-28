# Unity

Unity is an easy to use game engine using C# for game logic.

TODO:

* [Video](https://www.youtube.com/watch?v=VbZ9_C4-Qbo)
* [Melee](https://www.youtube.com/watch?v=sPiVz1k-fEs)

## Basics

* Unity works with XYZ values, Z is always "forward" and the direction the default camera is pointing to.

### UI

The default windows are:

* Hierarchy - shows the game objects on the scene
* Scene - visual representation of the game objects in the scene
* Game - view from the player's perspective
* Asset store - Unity's Asset Store
* Inspector - displays the components of the selected game object along with their properties
* Project - file view of the project
* Console - displays log messages from C# scripts and errors/warnings

Key bindings:

* q,w,e,r,t - Switches between the tools in the tool bar (move, rotate, scale)
* ctrl+p - toggles the play button
* f - focus on the highlighted object in the hierarchy
* ctrl+d - duplicate selected game object

Moving around the Scene:

* Alt+Left Click - move around the scene
* Shift+Middle Click - pan around the scene
* Scroll wheel - zooms in and out

## Game Objects

Game Objects are the most basic element in Unity, like a `<div>` tag in Web Development. Everything in Unity is
Game Object (camera, light source, shapes, etc). Rendering is done from top to bottom in the order listed in the Hierachy window.

In the hierachy window, game objects can be dragged attached to each other by dragging one on top of the other. This creates a
parent-child relationship between the game objects. If the parent moves, the child follows, but the parent doesn't follow if the
child moves.

> The child's transform (position) will be relative to the parent, and parent's transform is relative to the world.

### Components & Transforms

**Components** are added to Game Objects to define their features, like behaviors or appearances.
**Transforms** are added to Game Objects to define their position, rotation, and scale values.

Basic Components:

* Rigid Body - Applies basic physics to the object (gravity, collision, drag, etc).
* Material - Applies a look to the object (colors, textures, etc).

### Scripts

Default script:

```c#
using UnityEngine;
using System.Collections;

public class PlayerMovement : MonoBehaviour {

    // Use this for initialization
    void Start () {

    }

    // Update is called once per frame
    void Update () {

    }
}
```

Making fields public allow Unity to see them, and make them editable in the Unity editor.

* FixedUpdate() - smoother rendering for physics-based updates

### Prefabs

Prefabs, or prefabricated game objects, are user defined game objects. When creating
a game object with components and child game objects, you can drag the parent into the
Project window to create what is known as a _Prefab_. This allows us to recreate multiple
instances of that game object. Clicking on the prefab and altering values alters all objects
created from that prefab.

Individual instance's values can also be altered, in order to reflect that change to other prefab objects,
you would have to right-click the altered value and hit **Apply**.

> Prefabs are highlighted blue in the Hierachy window.

## Workflow

## Advance Use

## Other
