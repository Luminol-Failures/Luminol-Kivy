from re import S
from rubymarshal.classes import UserDef, RubyObject, registry
import rubymarshal.reader as reader
import rubymarshal.writer as writer
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

    def _load(self, data: bytes):
        num_of_dimensions, xsize, ysize, zsize, num_of_elements = struct.unpack("<IIIII", data[:20])
        # This might work or maybe not I don't know, I think it does?
        self.elements = []
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

        # RKEVIN WHAT THE FUCK

        #assert num_of_dimensions != 2
        ## dirty hack
        #ysize = 1 if num_of_dimensions == 1 else ysize
        #zsize = 1 if num_of_dimensions < 3 else zsize
        #assert num_of_elements == xsize*ysize*zsize
        #assert num_of_elements*2+20 == len(data)
        ## extremely dirty hack by assuming there are always 3 dimensions
        #self.elements = []
        #for z in range(zsize):
        #    l = []
        #    for y in range(ysize):
        #        l.append(list(struct.unpack("<"+"H"*xsize, data[20+(z*ysize*xsize+y*xsize)*2:][:xsize*2])))
        #    self.elements.append(l)
        ## i feel so dirty for doing this but eh
        #if num_of_dimensions != 3:
        #    self.elements=self.elements[0]
        #if num_of_dimensions == 1:
        #    self.elements=self.elements[0]
        #self.data = data
        return self
    
    def elements(self):
        return self.elements

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

    def _dump(self) -> bytes:

        elements = self.elements
        # Set xsize to the length of the list
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
                zsize = len(elements)
                num_of_dimensions = 3
            else:
                zsize = 1
                num_of_dimensions = 2
        else:
            zsize = 1
            ysize = 1
            num_of_dimensions = 1
        
        if num_of_dimensions == 1:
            flat_list = elements
        
        flat_list = []
        for element in self.elements:
            if type(element) is list:
                for item in element:
                    if type(element) is list:
                        for item2 in item:
                            flat_list.append(item2)
                    else:
                        flat_list.append(item)
            else:
                flat_list.append(element)

        if len(flat_list) != xsize * ysize * zsize:
            raise(AttributeError, "Table inproperly flattened?")

        return struct.pack(
            "<IIIII"+"H"*len(flat_list),
            num_of_dimensions, xsize, ysize, zsize,
            len(flat_list),
            *flat_list
        )
        #return self.data
        #elements = self.elements
        #xsize = len(elements)
        #if xsize > 0 and type(elements[0]) is list:
        #    ysize = len(elements[0])
        #    if ysize > 0 and type(elements[0][0]) is list:
        #        zsize = len(elements[0][0])
        #        num_of_dimensions = 3
        #    else:
        #        zsize = -1
        #        num_of_dimensions = 2
        #else:
        #    ysize = -1
        #    zsize = -1
        #    num_of_dimensions = 1
        #if num_of_dimensions == 1:
        #    flattened = elements
        #elif num_of_dimensions == 2:
        #    flattened = [i for l in elements for i in l]
        #else:
        #    flattened = [i for l1 in elements for l2 in l1 for i in l2]
        #assert len(flattened) == xsize * (ysize if num_of_dimensions > 1 else 1) * (zsize if num_of_dimensions > 2 else 1)
        #return struct.pack("<IIIII"+"H"*len(flattened), num_of_dimensions, xsize, ysize, zsize, len(flattened), *flattened)

    def __repr__(self) -> str:
        return("Table(%s)"%(self.elements))

    def __str__(self) -> str:
        return self.__repr__()

#class RGSSRegistry(ClassRegistry):
#    def __init__(self):
#        self._registry = {
#            'Color': Color,
#            'Tone': Tone,
#            'Table': Table,
#        }
#
#    def get(self, ruby_class_name: str, default_cls: Type[RubyObject]):
#        if default_cls != RubyObject:
#            # we want to throw exceptions for unknown UserDefs and UsrMarshals
#            #default_cls = None
#            pass
#        return self._registry.get(ruby_class_name, default_cls)