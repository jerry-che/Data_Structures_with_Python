#  File: Geom.py

#  Description:

#  Student Name: Jerry Che

#  Student UT EID: jc78222

#  Course Name: CS 313E

#  Partner's Name: Terry Woodward Jr

#  Partner's UT EID: tgw466

#  Unique Number: 86325

#  Date Created: 06/18/18

#  Date Last Modified: 06/21/18


import math

class Point (object):
  # constructor 
  # x and y are floats
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get distance
  # other is a Point object
  def dist (self, other):
    return math.hypot((self.x - other.x), (self.y - other.y))

  # get a string representation of a Point object
  # takes no arguments
  # returns a string
  def __str__ (self):
    return '(' + str(self.x) + "," + str(self.y) + ")"

  # test for equality
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
    tol = 1.0e-16
    return ((abs (self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

class Circle (object):
  # constructor
  # x, y, and radius are floats
  def __init__ (self, radius = 1, x = 0, y = 0):
    self.radius = radius
    self.center = Point (x, y)

  # compute cirumference
  def circumference (self):
    return (2.0 * math.pi * self.radius)

  # compute area
  def area (self):
    return math.pi * self.radius * self.radius

  # determine if point is strictly inside circle
  def point_inside (self, p):
    return (self.center.dist(p) < self.radius)

  # determine if a circle is strictly inside this circle
  def circle_inside (self, c):
    distance = self.center.dist (c.center)
    return (distance + c.radius) < self.radius

  # determine if a circle c intersects this circle (non-zero area of overlap)
  # the only argument c is a Circle object
  # returns a boolean
  def does_intersect (self, c):
  	distance = self.center.dist(c.center)
  	return distance < self.radius + c.radius

   
  # determine the smallest circle that circumscribes a rectangle
  # the circle goes through all the vertices of the rectangle
  # the only argument, r, is a rectangle object
  def circle_circumscribes (self, r):
    x = (r.ul.x + r.lr.x) / 2
    y = (r.ul.y + r.lr.y) / 2
    center = Point(x,y)
    radius = center.dist(r.lr)
    smallest_circle = Circle(radius,x,y)
    return smallest_circle



  # string representation of a circle
  # takes no arguments and returns a string
  def __str__ (self):
    return "Radius: " + format(abs(self.radius),'.2f') + " Center: " "(" + str(self.center.x) + "," + str(self.center.y) + ')'

    
  # test for equality of radius
  # the only argument, other, is a circle
  # returns a boolean
  def __eq__ (self, other):
    tol = 1.0e-16
    same_radius = abs(self.radius - other.radius) < tol
    return same_radius

class Rectangle (object):
  # constructor
  def __init__ (self, ul_x = 0, ul_y = 1, lr_x = 1, lr_y = 0):
    if ((ul_x < lr_x) and (ul_y > lr_y)):
      self.ul = Point (ul_x, ul_y)
      self.lr = Point (lr_x, lr_y)
    else:
      self.ul = Point (0, 1)
      self.lr = Point (1, 0)

  # determine length of Rectangle (distance along the x axis)
  # takes no arguments, returns a float
  def length (self):
  	return abs(self.ul.x - self.lr.x)
 

  # determine width of Rectangle (distance along the y axis)
  # takes no arguments, returns a float
  def width (self):
  	return abs(self.ul.y - self.lr.y)

  # determine the perimeter
  # takes no arguments, returns a float
  def perimeter (self):

  	return (self.length() + self.width()) * 2
    
  # determine the area
  # takes no arguments, returns a float
  def area (self):
  	return (self.length() * self.width())

  # determine if a point is strictly inside the Rectangle
  # takes a point object p as an argument, returns a boolean
  def point_inside (self, p):
  	return(((p.x > self.ul.x) and (p.x < self.lr.x)) and ((p.y > self.lr.y) and (p.y < self.ul.y)))

  #if another Rectangle is strictly inside this Rectangle
  # takes a rectangle object r as an argument, returns a boolean
  # should return False if self and r are equal
  def rectangle_inside (self, r):
  	return (((r.ul.x > self.ul.x) and (r.ul.y < self.ul.y)) and ((r.lr.x > self.lr.x) and (r.lr.y > self.lr.y)))

  # determine if two Rectangles overlap (non-zero area of overlap)
  # takes a rectangle object r as an argument returns a boolean
  def does_intersect (self, other):
    if (self.ul.x > other.lr.x) or (self.lr.x < other.ul.x) or (self.ul.y > other.lr.y) or (self.lr.y < other.ul.y):
      return False
    return True

  	

  # determine the smallest rectangle that circumscribes a circle
  # sides of the rectangle are tangents to circle c
  # takes a circle object c as input and returns a rectangle object
  def rect_circumscribe (self, c):
    center_x = c.center.x
    center_y = c.center.y


    rect_ul_x = center_x - c.radius
    rect_ul_y = center_y + c.radius
    rect_lr_x = center_x + c.radius
    rect_lr_y = center_y - c.radius

    smallest_rect = Rectangle(rect_ul_x,rect_ul_y,rect_lr_x,rect_lr_y)

    return smallest_rect

  # give string representation of a rectangle
  # takes no arguments, returns a string
  def __str__ (self):
    return "Coordinates of Rectangle: " "(" + str(self.ul.x) + "," + str(self.ul.y) + ')' + " " +  "(" + str(self.lr.x) + "," + str(self.lr.y) + ')'

  # determine if two rectangles have the same length and width
  # takes a rectangle other as argument and returns a boolean
  def __eq__ (self, other):
    tol = 1.0e-16
    diff_length = abs(self.length() - other.length())
    diff_width = abs(self.width() - other.width ())

    return (diff_width < tol  and diff_length < tol)



def main():
  # open the file geom.txt
  cord_list = []
  geom_file = open('geom.txt','r')

  for line in geom_file:
    line = line.rstrip().split()
    cord_list.append(line)


  # create Point objects P and Q
  point_p = Point(float(cord_list[0][0]),float(cord_list[0][1]))
  point_q = Point(float(cord_list[1][0]),float(cord_list[1][1]))

  # print the coordinates of the points P and Q
  print("Point P:",point_p)
  print("Point Q:",point_q)

  # find the distance between the points P and Q
  print("Distance between P and Q:", format(point_q.dist(point_p),'.2f'))
 
  # create two Circle objects C and D
  circle_c = Circle(float(cord_list[2][2]),float(cord_list[2][0]),float(cord_list[2][1]))
  circle_d = Circle(float(cord_list[3][2]),float(cord_list[3][0]),float(cord_list[3][1]))
  # print C and D
  print("Circle C:",circle_c)
  print("Circle D:",circle_d)

  # compute the circumference of C
  print("Circumference of C: ", format(circle_c.circumference(),'.2f'))

  # compute the area of D
  print("Area of D:",format(circle_d.area(),'.2f'))

  # determine if P is strictly inside C
  if circle_c.point_inside(point_p) == True:
    print("P is inside C")
  else:
    print("P is not inside C")

  # determine if C is strictly inside D
  if circle_d.circle_inside(circle_c) == True:
    print("C is inside D")
  else:
    print("C is not inside D")

  # determine if C and D intersect (non zero area of intersection)
  if circle_c.does_intersect(circle_d) == True:
    print("C does intersect D")
  else:
    print("C does not intersect D")

  # determine if C and D are equal (have the same radius)
  if (circle_c == circle_d):
    print("C is equal to D")
  else:
    print("C is not equal to D")

  # create two rectangle objects G and H
  rect_g = Rectangle(float(cord_list[4][0]),float(cord_list[4][1]),float(cord_list[4][2]),float(cord_list[4][3]))
  rect_h = Rectangle(float(cord_list[5][0]),float(cord_list[5][1]),float(cord_list[5][2]),float(cord_list[5][3]))


  # print the two rectangles G and H
  print("Rectangle G:",rect_g)
  print("Rectangle H:",rect_h)

  # determine the length of G (distance along x axis)
  print("Length of G:",rect_g.length())

  # determine the width of H (distance along y axis)
  print("Width of H:",rect_h.width())

  # determine the perimeter of G
  print("Perimeter of G:",rect_g.perimeter())

  # determine the area of H
  print("Area of H:",rect_h.area())

  # determine if point P is strictly inside rectangle G
  if rect_g.point_inside(point_p) == True:
    print("P is inside G")
  else:
    print("P is not inside G")

  # determine if rectangle G is strictly inside rectangle H
  if rect_h.rectangle_inside(rect_g) == True:
    print("G is inside H")
  else:
    print("G is not inside H")

  # determine if rectangles G and H overlap (non-zero area of overlap)
  if rect_h.does_intersect(rect_g) == True:
    print("G does overlap H")
  else:
    print("G does not overlap H")

  # find the smallest circle that circumscribes rectangle G
  # goes through the four vertices of the rectangle
  print("Circle that circumscribes G: ", circle_c.circle_circumscribes(rect_g))

  # find the smallest rectangle that circumscribes circle D
  # all four sides of the rectangle are tangents to the circle
  print("Rectangle that circumscribes D:", rect_g.rect_circumscribe(circle_d))

  # determine if the two rectangles have the same length and width
  if (rect_g == rect_h):
    print("Rectangle G is equal to H")
  else:
    print("Rectangle G is not equal to H")

  # close the file geom.txt
  geom_file.close()


if __name__ == "__main__":
  main()