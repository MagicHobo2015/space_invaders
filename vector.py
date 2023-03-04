from math import sqrt
from copy import copy


class Vector:
    '''Simple 2d vector class for handling velocity, position, and acceleration 
       of game objects
       Double underscore methods like __add__ are the equivalent of operator+ in C++
                         methods like __eq__ and __ne__ are the equivalent of operator==
                         and operator!= in C++
                         Note: make *** SURE ** you have 2 underscores before and after
                             or Python will not recognize the methods
                             
        TODO:  fill in the missing methods, 
               uncomment the lines that test the class
               and make sure that all assertions pass
    '''
    def __init__(self, x=0, y=0): self.x, self.y = x, y
    def __str__(self): return f'Vector({self.x},{self.y})'

            # arithmetic operators
    def __add__(self, o): return Vector(self.x + o.x, self.y + o.y)
    def __neg__(self): return Vector(-self.x, -self.y)
    def __sub__(self, o): return self + -o
    def __mul__(self, k): return Vector(k * self.x, k * self.y)
    def __rmul__(self, k): return self * k
    def __truediv__(self, k): return 1.0 / k * self
    
            # logical operators
    def __eq__(self, o): return self.x == o.x and self.y == o.y

    def __ne__(self, o): return not self == o
    
            # vector-vector operators
    def dot(self, o): return self.x * o.x + self.y * o.y 
    def cross(self, o): return Vector(self.x * o.y - self.y * o.x) 

            # vector methods
    def norm(self): return self / self.mag()

    def mag(self): return sqrt(self.x ** 2 + self.y ** 2)
    
            # tests
    @staticmethod
    def run_tests():
        print('\n...........BEGINNING Vector.run_tests()..........')
                # don't put multiple statement on same line in general;  education example to conserve space
        v = Vector();               print(f'v  is: {v}')
        v2 = Vector(1, 2);          print(f'v2 is: {v2}\n')
        v3 = Vector(-2, 1);         print(f'v3 is: {v3}')
        
        print(f'-{v2} is: {-v2}')
        print(f'{v} + {v2} is: {v + v2}')
        print(f'{v} - {v2} is: {v - v2}')
        print(f'{v2} * 3 is: {v2 * 3}')
        print(f'3 * {v2} is: {3 * v2}')
        print(f'{v2} / 2.0 is: {v2 / 2.0}\n')
        
            # TODO: uncomment after you have filled in __eq__ and __ne__
        # print(f'*** assert {v2} + {v3} - {v3} == {v2}\n');       assert(v2 + v3 - v3 == v2)
        # print(f'*** assert 4.0 * {v2} / 4.0 == {v2}\n');         assert(4.0 * v2 / 4.0 == v2)
        
        print(f'{v2}.dot({v2}) is: {v2.dot(v2)}');       
        print(f'{v2}.dot({v3}) is: {v2.dot(v3)}')
        print(f'{v3}.dot({v3}) is: {v3.dot(v3)}\n')
        
            # TODO: uncomment after you have filled in mag() and norm()
        # print(f'v2.mag() is: {v2.mag()}')
        # print(f'v2.mag() ** 2 is: {round(v2.mag() ** 2, 5)}')
        # print(f'\n*** assert v2.dot(v2) == v2.mag() ** 2\n');   assert(v2.dot(v2) == round(v2.mag() ** 2, 5))
        
        # print(f'norm of v2 is: {v2.norm()}, and its length is: {round(v2.norm().mag(), 5)}\n')
        
        print(f'{v2}.cross({v3}) is: {v2.cross(v3)}')
        print(f'{v3}.cross({v2}) is {v3.cross(v2)}')
        print(f'-({v3}.cross({v2}) is {-(v3.cross(v2))}')
            # TODO: uncomment after you have filled in __eq__ and __ne__
        # print(f'\n*** assert v2.cross(v3) == -(v3.cross(v2)))');       assert(v2.cross(v3) == -v3.cross(v2))        
        # print(f'\n*** assert (Vector(1, 1) == Vector(1, 1))');         assert(Vector(1, 1) == Vector(1, 1))

        print('\n>>>>> Congratulations! All Vector assertions passed! <<<<< \n')
        print('...........ENDING Vector.run_tests().............\n')
 
        
def main():  # NOTE: three single quotes are how you mark a multi-line comment
    ''' ALL assertions need to pass...
            if ANY assertion fails, add additional statements to see what the 
            left and right side of the assertion were
            that caused it to fail...
    '''
    Vector.run_tests()    
        

if __name__ == '__main__':
    main()