import io
import csv
import unittest
from Scene import Scene,Color
from SceneObject import Disc
from Serialize import *

class TestSceneToCsv(unittest.TestCase):
    def test_listobject(self):
        # Create a scene with some objects
        scene = Scene()
        scene.set_BgdColor(Color(102,204,255))
        scene.set_Size(1100,1100)

        scene.listObject.append(Disc(0,216, Color(255,0,0,), 250))
        scene.listObject.append(Disc(-250,-216, Color(0, 255, 0), 250))
        scene.listObject.append(Disc(250,-216, Color(0, 0, 255), 250))

        
        self.assertEqual(scene.listObject[0].csv_row(), [0 ,0  , 102, 204, 255,1100,1100, 'viewport'])
        self.assertEqual(scene.listObject[1].csv_row(), [0 ,216, 255, 0  , 0  , 250 , 0  , 'disc'    ])
        self.assertEqual(scene.listObject[2].csv_row(), [-250, -216, 0  , 255, 0  , 250 , 0  , 'disc'    ])
        self.assertEqual(scene.listObject[3].csv_row(), [250, -216, 0  , 0  , 255, 250, 0  , 'disc'    ])

if __name__ == "__main__":
    unittest.main()