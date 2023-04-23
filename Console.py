import cmd
from SceneObject import *
from Scene import Scene
from Render import Renderer
from Serialize import Serializer


class MyShell(cmd.Cmd):
    intro = "Welcome to my shell console. Type 'help' for the list of commands."
    prompt = ">> "

    def do_add(self, line):     
        #Add [shape] [x] [y] [red] [green] [blue] [size]->> Size can refer to either the radius or the two coordinates for a square, for example.
        args=line.split()        

        if len(args)>=6:
            if args[0]=="disc":
                try:
                    mainScene.listObject.append(Disc(int(args[1]),int(args[2]),Color(int(args[3]),int(args[4]),int(args[5])),int(args[6])))
                    print('Success')
                except :
                    print("add [shape] [x] [y] [red] [green] [blue] [size]")

        else:
            print("No enough arguments : add [shape] [x] [y] [red] [green] [blue] [size]")

    def do_viewportsize(self,line): 
        #Modify viewport size
        try:        
            args=line.split()

            x = int(args[0])
            y = int(args[1])
            mainScene.set_Size(x,y)

        except ValueError:
            print("Only integer excpected")
        except IndexError:
            print("No enough arguments : viewportsize [width] [length]")


    def do_bgdcolor(self,line):
        #Modify background color
        try:        
            args=line.split()

            red =   int(args[0])
            green = int(args[1])
            blue =  int(args[2])
            mainScene.set_BgdColor(Color(red,green,blue))
        except ValueError:
            print("Only integer excpected")
        except IndexError:
            print("No enough arguments : nbgdcolor [red] [green] [blue]")


    def do_render(self,line): 
        #Render the scene
        args=line.split()
        if len(args)==1:
            if args[0]=="png":
                Renderer.render_png(self,mainScene)
            if args[0]=="jpg":
                Renderer.render_jpg(self,mainScene)


    def do_serialize(self,line):
        #Serialize and export in the desired format       
        args=line.split()
        if len(args)==1:
            if args[0]=="json":
                Serializer.serializer_json(self,mainScene.to_dict(),"test.json")
            if args[0]=="csv":
                Serializer.serializer_csv(self,mainScene.listObject,"test.csv")
        
    def do_help(self, line):
        #Show help panel
        print("quit\nshow\nadd [shape] [x] [y] [red] [green] [blue] [size]\nviewportsize [width] [length]\nbgdcolor [red] [green] [blue]")

    def do_quit(self, line):
        #Quit
        return True


if __name__ == '__main__':
    mainScene = Scene()
    MyShell().cmdloop()


"""
Exemple code:

bgdcolor 102 204 255
viewportsize 1100 1000
add disc   0    216 255 0 0  250
add disc -250  -216 0 255 0  250
add disc  250  -216 0 0 255  250

"""