from re import S
from src.rubymarshal.classes import UserDef, RubyObject, registry
import src.rubymarshal.reader as reader
import src.rubymarshal.writer as writer
from typing import Type
from typing import Type
import struct

class Color(UserDef):
    def __init__(self, classname='Color', r=255, g=255, b=255, a=255):
        super().__init__(ruby_class_name=classname, attributes=None)
        self.red = r
        self.green = g
        self.blue = b
        self.alpha = a

    def _load(self, data: bytes):
        self.red, self.green, self.blue, self.alpha = struct.unpack("<dddd", data)

    def _dump(self) -> bytes:
        return struct.pack("<dddd", self.red, self.green, self.blue, self.alpha)

    def __repr__(self) -> str:
        return("Color(#%02x%02x%02x%02x)"%(int(self.red), int(self.green), int(self.blue), int(self.alpha)))

    def __str__(self) -> str:
        return self.__repr__()

class Tone(UserDef):
    def __init__(self, classname='Tone', r=0, g=0, b=0, gr=0):
        super().__init__(ruby_class_name=classname, attributes=None)
        self.red = r
        self.green = g
        self.blue = b
        self.grey = gr

    def _load(self, data: bytes):
        self.red, self.green, self.blue, self.grey = struct.unpack("<dddd", data)

    def _dump(self) -> bytes:
        return struct.pack("<dddd", self.red, self.green, self.blue, self.grey)

    def __repr__(self) -> str:
        return("Tone(#%02x%02x%02x%02x)"%(int(self.red), int(self.green), int(self.blue), int(self.grey)))

    def __str__(self) -> str:
        return self.__repr__()

class Table(UserDef):
    def __init__(self, classname='Table', elements=None, xsize = 1, ysize = 1, zsize = 1):
        super().__init__(ruby_class_name=classname, attributes=None)
        if (elements == None):
            self.elements = []
            for z in range(zsize):
                ydata = []
                for y in range(ysize):
                    xdata = []
                    for x in range(xsize):
                        xdata.append(0)
                    ydata.append(xdata)
                self.elements.append(ydata)
        else:
            self.elements = elements

        self.xsize = 0
        self.ysize = 0
        self.zsize = 0
        self.num_of_dimensions = 0

        self.calculate_variables(self.elements)

    def _load(self, data: bytes):
        num_of_dimensions, xsize, ysize, zsize, num_of_elements = struct.unpack("<IIIII", data[:20])
        # This might work or maybe not I don't know, I think it does?
        self.elements = []
        self.xsize = xsize
        self.ysize = ysize
        self.zsize = zsize
        self.num_of_dimensions = num_of_dimensions
        
        if (num_of_dimensions == 1):
            xdata = []
            xdata = list(
                    struct.unpack( "<" + "H"*xsize,
                        data[20:][:xsize*2]
                    )
                )

            self.elements = xdata
        elif (num_of_dimensions == 2):
            ydata = []
            for y in range(ysize):
                ydata.append(
                    list(
                       struct.unpack("<"+"H"*xsize, data[20+(y*xsize)*2:][:xsize*2])
                    )
                )
            self.elements = ydata
        elif (num_of_dimensions == 3):
            for z in range(zsize):
                ydata = []
                for y in range(ysize):
                    ydata.append(list(struct.unpack("<"+"H"*xsize, data[20+(z*ysize*xsize+y*xsize)*2:][:xsize*2])))
                self.elements.append(ydata)

        self.data = data
        return self
    
    def elements(self):
        return self.elements
    
    def xsize(self):
        return self.xsize
    
    def ysize(self):
        return self.ysize
    
    def zsize(self):
        return self.zsize
    
    def num_of_dimensions(self):
        return self.num_of_dimensions

    def x(self, x):
        return self.elements[x]
    
    def set_x(self, x, value):
        self.elements[x] = value
    
    def xy(self, x, y):
        return self.elements[y][x]
    
    def set_xy(self, x, y, value):
        self.elements[y][x] = value
    
    def xyz(self, x, y, z):
        return self.elements[z][y][x]

    
    def set_xyz(self, x, y, z, value):
        self.elements[z][y][x] = value

    def resize(self, x, y = 0, z = 0):
        new_table = Table('Table', None, x, y, z)
        assert x > 0
        # Logic taken from R48! Thanks 20kdc
        for i in range(self.xsize):
            if x <= i:
                break
            for j in range(self.ysize):
                if y <= j:
                    break
                for k in range(self.zsize):
                    if z <= k:
                        break
                    new_table.set_xyz(i, j, k, self.xyz(i, j, k))
        # It's up to you to set the table to the new table
        return new_table

    def calculate_variables(self, elements):
        xsize = len(elements)
        # Is there multiple lists in elements?
        if xsize > 0 and type(elements[0]) is list:
            # Correctly set xsize and ysize
            xsize = len(elements[0])
            ysize = len(elements)
            # Are there lists inside the lists inside the list?
            if ysize > 0 and type(elements[0][0]) is list:
                # Correctly set xsize and zsize
                xsize = len(elements[0][0])
                ysize = len(elements[0])
                zsize = len(elements)
                num_of_dimensions = 3
            else:
                zsize = 1
                num_of_dimensions = 2
        else:
            zsize = 1
            ysize = 1
            num_of_dimensions = 1
        self.xsize = xsize
        self.ysize = ysize
        self.zsize = zsize
        self.num_of_dimensions = num_of_dimensions
        
        

    def _dump(self) -> bytes:
        elements = self.elements
        self.calculate_variables(elements)
        if self.num_of_dimensions == 1:
            flat_list = elements
        
        flat_list = []
        for element in elements:
            if type(element) is list:
                for item in element:
                    if type(element) is list:
                        for item2 in item:
                            flat_list.append(item2)
                    else:
                        flat_list.append(item)
            else:
                flat_list.append(element)

        if len(flat_list) != self.xsize * self.ysize * self.zsize:
            raise(BaseException, "Table inproperly flattened?")

        return struct.pack(
            "<IIIII"+"H"*len(flat_list),
            self.num_of_dimensions, self.xsize, self.ysize, self.zsize,
            len(flat_list),
            *flat_list
        )

    def __repr__(self) -> str:
        return("Table(%s)"%(self.elements))

    def __str__(self) -> str:
        return self.__repr__()
