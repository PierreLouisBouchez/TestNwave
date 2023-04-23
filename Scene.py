from Color import *
import SceneObject


class Scene:

    #Constructor method that initializes an empty list called "listObject" and adds a new SceneObject to represent the viewport
    def __init__(self):
        self.listObject = []
        self.listObject.append(SceneObject.SceneObject(0,0,Color(0, 0, 0),1000,1000,"viewport"))

    #Method to modify the brackground color of the object
    def set_BgdColor(self, c: Color):
        self.listObject[0].set_color(c)

    #Method to get the viewport object in the "listObject"
    def getViewportObject(self):
        return self.listObject[0]


    #Method that creates a dictionary representation of the scene.
    def to_dict(self):
        return {
            "listObject": [obj.to_dict() for obj in self.listObject]
        }
    
    #Method that modify the width and height attributes of the viewport
    def set_Size(self, width :int,height:int):
        self.listObject[0].width = width
        self.listObject[0].height = height
