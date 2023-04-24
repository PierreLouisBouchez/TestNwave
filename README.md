# Nwave Console

Welcome, this is a Python code for a command-line interface that allows you to create and manipulate simple 2D shapes on a scene. 


### Functionality

The available commands are:

- `add`: adds a new shape to the scene. The supported shapes are "disc" and "square". 

- `viewportsize`: modifies the size of the viewport, which is the area where the shapes are drawn.

- `bgdcolor`: modifies the background color of the scene.

- `render`: renders the scene into a file in PNG or JPG format.

- `serialize`: serializes the scene into a file in JSON or CSV format.

- `help`: shows the help panel with the list of available commands.

- `quit`: quits the program.

### Usage

Below is an example usage of the command line interface:

```python
bgdcolor 102 204 255
viewportsize 1100 1000
add disc   0    216 255 0 0  250
add disc -250  -216 0 255 0  250
add disc  250  -216 0 0 255  250
```

<img src="https://github.com/PierreLouisBouchez/TestNwave/blob/main/test.png" width="220" height="200" />

### Improving the Code

The current implementation of the library works well for circles. However, there are several ways in which the code can be improved to make it more flexible and extendable for other developers :

- Currently, the library only supports circles. Other shapes like squares, triangles, or polygons can be added to the SceneObject file .

- In addition to JSON and CSV serializers, other formats like XML or USD can be added in the class Serializer.

- In parallel to the PNG and JPG renderers, other formats such as HTML or PPM can be added in the Renderer class.


