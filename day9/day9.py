import math
class Point:
    def __init__(self,x,y,z=0):
      self.x=x
      self.y=y
      self.z=z
      print(f"创建了Point({self.x},{self.y},{self.z})")


    def __del__(self):
      print(f"销毁了Point({self.x},{self.y},{self.z})")
    def __str__(self):
      return f"Point({self.x},{self.y},{self.z})"
    def __add__(self,other):
        if isinstance(other,Vector):
            return Point(self.x+other.x,self.y+other.y,self.z+other.z)
        else:
            raise TypeError("Point类只能与Vector类相加")
    def __sub__(self,other):
        if isinstance(other,Vector):
            return Point(self.x-other.x,self.y-other.y,self.z-other.z)
        elif isinstance(other,Point):
            return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
        else:
            raise TypeError("Point类只能与Vector类相减或与Point类相减")
    def __lt__(self,other):
        if isinstance(other,Point):
            dist_self=math.sqrt(self.x**2+self.y**2+self.z**2)
            dist_other=math.sqrt(other.x**2+other.y**2+other.z**2)
            return dist_self < dist_other
        else:
            return False
class Vector:
        def __init__(self,x,y,z=0):
            self.x = x
            self.y = y
            self.z = z
            print(f"创建了Vector({self.x},{self.y},{self.z})")

        def __del__(self):
            print(f"销毁了Vector({self.x},{self.y},{self.z})")

        def __str__(self):
            return f"Vector({self.x},{self.y},{self.z})"

        def __add__(self, other):
            if isinstance(other, Vector):
                return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
            else:
                raise TypeError("Vector类只能与Vector类相加")

        def __sub__(self, other):
            if isinstance(other, Vector):
                return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

            else:
                raise TypeError("Vector类只能与Vector类相减")
        def __mul__(self,x):
            rad=math.radians(x)
            cos_val=math.cos(rad)
            sin_val=math.sin(rad)
            new_x=self.x*cos_val-self.y*sin_val
            new_y=self.x*sin_val+self.y*cos_val
            return Vector(new_x,new_y,self.z)
        def __truediv__(self, x):
            rad=math.radians(x)
            cos_val=math.cos(rad)
            sin_val=math.sin(rad)
            new_x=self.x*cos_val+self.y*sin_val
            new_y=-self.x*sin_val+self.y*cos_val
            return Vector(new_x,new_y,self.z)
        def __eq__(self,other):
            if isinstance(other,Vector):
                return self.x == other.x and self.y==other.y and self.z==other.z
            else:
                return False
p1=Point(1,2)
p2=Point(3,4,5)
v1=Vector(1,1,1)
v2=Vector(2,2,2)
a=p1+v1
b=p1+p2
print(b)