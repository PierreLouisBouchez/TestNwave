from PIL import Image, ImageDraw
from Scene import *

class Renderer:
    def draw(self,Scene):

        image = Image.new('RGB', (Scene.getViewportObject().width,Scene.getViewportObject().height ), Scene.getViewportObject().color.tuple() )
        draw = ImageDraw.Draw(image)
        
        for i in range (1,len(Scene.listObject)):   #draw shapes from the list of object
            Scene.listObject[i].drawShape(draw,Scene)

        return image
    
    def render_png(self,Scene):
        image = Renderer.draw(self,Scene)
        image.save("test.png", "png")

    def render_jpg(self,Scene):
        image = Renderer.draw(self,Scene)
        image.save("test.jpg", "jpeg")
