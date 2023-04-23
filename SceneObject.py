from Color import *
import Scene
from PIL import Image, ImageDraw

class SceneObject():
    def __init__(self,x,y,color,width,height,type):
        self.x = x              
        self.y = y             
        self.color = color      
        self.width = width      
        self.height = height    
        self.type = type        # type of the object (Viewport,Disc,Square...)
   
    def to_dict(self):
        #Return a dictionary containing the object's data
        return {
            "x": self.x,
            "y": self.y,
            "color": self.color.to_dict(),
            "width": self.width,
            "height": self.height,
            "type": self.type
        }
    
    def csv_row(self):
        #Return a list containing the object's data in csv format
        return [self.x, self.y] + self.color.csv_row() + [self.width, self.height, self.type]

    def set_position(self,x,y):                                    
        #Set the position of the object
        self.x = x              
        self.y = y

    def set_color(self,color):                                      
        #Set the color of the object
        self.color = color          

    def set_size(self,width,height):                               
        #Set the size of the object
        self.width = width
        self.height = height

    def drawShape(self, draw : ImageDraw):
        return NotImplemented 

    
class Disc(SceneObject):
    def __init__(self,x,y,color,width):
        super().__init__(x,y,color,width,0,"disc")                 
   
    def drawShape(self, draw : ImageDraw,scene : Scene):
        #Draws a disc using the ImageDraw library, taking into account the position and size of the viewport in the scene
        centerx=scene.getViewportObject().width/2 +self.x
        centery=scene.getViewportObject().height/2 +self.y *-1        

        draw.ellipse([(centerx - self.width,centery - self.width),(centerx +self.width ,centery+self.width )],fill=self.color.tuple())



    # Here we will be able to add new shapes