class triangle:
  a,b,c = 0.0,0.0,0.0;
  Ad,Bd,Cd = 0.0,0.0,0.0;
  Ar,Br,Cr = 0.0,0.0,0.0;
  Apos,Bpos,Cpos = (0.0,0.0),(0.0,0.0),(0.0,0.0);
  perimeter = 0.0;
  area = 0.0;
  r = 0.0;
  areaC = 0.0;
  color = "black";
  solveable = False;
  sides = 0;
  angles = 0;
  x,y=0.0,0.0;
  rotater=0.0;
  def Triangle():
    import math;
    x,y=0.0,0.0;
    a,b,c = 0.0,0.0,0.0;    
    A,B,C = 0.0,0.0,0.0;
    Apos,Bpos,Cpos = (0.0,0.0),(0.0,0.0),(0.0,0.0);
    perimeter = 0.0;
    area = 0.0;
    r=0.0;
    areaC = 0.0;
  def isSolveable(triangle):
        
    if (triangle.a != 0.0):   
      triangle.sides += 1;   
    if (triangle.b != 0.0):    
      triangle.sides += 1;   
    if (triangle.c != 0.0):   
      triangle.sides += 1;
    if (triangle.a == 0):      
      if(triangle.Ad == 0.0):       
        triangle.angles +=1;
    if (triangle.b == 0.0):      
      if (triangle.Bd != 0.0):       
        triangle.angles += 1;
    if (triangle.c == 0):       
      if (triangle.Cd != 0.0):   
        triangle.angles += 1;
    if((triangle.sides + triangle.angles)<3):
      triangle.solveable = False;
      print("We need to know more to solve this triangle");
      print(triangle.triangle);
    if(triangle.a + triangle.b > triangle.c and triangle.b + triangle.c > triangle.a and triangle.c + triangle.a > triangle.b):
      triangle.solveable = True;
    else:
      print("The sides of this triangle make no sense ");
      print(triangle);
      triangle.solveable = False;
    return triangle.solveable;


    
  def sas(triangle):#this function solves the third side of a triangle when two of the sides and an aposeing angle have been set
    import math;
    if (triangle.a == 0.0):
      triangle.a = math.sqrt((triangle.b ** 2)+(triangle.c ** 2)- (2*triangle.b*triangle.c*math.cos(triangle.Ad)));
    elif(triangle.b == 0.0):
      triangle.b = math.sqrt((triangle.a ** 2)+(triangle.c ** 2)- (2*triangle.a*triangle.c*math.cos(triangle.Bd)));
    elif(triangle.c == 0.0):
      triangle.c = math.sqrt(triangle.b**2 + triangle.a**2 - 2 * triangle.b * triangle.a * math.cos(triangle.Cr));
    return triangle;
  def aas(triangle):
    import math;
    #this will set the missing sides off an aaas triangle
    if (triangle.c != 0.0):
      triangle.a = triangle.c * math.sin(triangle.Ar)/math.sin(triangle.Cr)
      triangle.b = triangle.c * math.sin(triangle.Br)/math.sin(triangle.Cr)
    elif(triangle.a != 0.0):
      triangle.c = triangle.a * math.sin(triangle.Cr)/math.sin(triangle.Ar)
      triangle.b = triangle.a * math.sin(triangle.Br)/math.sin(triangle.Ar)
    elif(triangle.b != 0.0):
      triangle.c = triangle.b * math.sin(triangle.Cr)/math.sin(triangle.Br)
      triangle.a = triangle.b * math.sin(triangle.Ar)/math.sin(triangle.Br)
    return triangle;

  def sss(triangle):
    import math;
   
    
    triangle.Cr = math.acos((triangle.a**2 + triangle.b**2 - triangle.c**2) / (2 * triangle.a * triangle.b))
    triangle.Br = math.acos((triangle.a**2 + triangle.c**2 - triangle.b**2) / (2 * triangle.a * triangle.c))
    triangle.Ar = math.pi - triangle.Cr - triangle.Br

    
    triangle.Ad = math.degrees(triangle.Ar);
    triangle.Bd = math.degrees(triangle.Br);
    triangle.Cd = math.degrees(triangle.Cr);
   
    return triangle;
    
  def findPerimeter(triangle):
    
    triangle.perimeter = triangle.a+triangle.b+triangle.c;
    return triangle;
  def findArea(triangle):
    
    triangle.area = triangle.perimeter/2.0;
    return triangle;

  def __str__(self):
    rstr =   "\nPerimeter:        " +  str(self.perimeter);
    rstr +=  "\nTriangle Area:    " +  str(self.area);
    rstr +=  "\nInradius:         " +  str(self.r);
    rstr +=  "\nCircle Area:      " +  str(self.areaC);
    rstr +=  "\nSide a,b,c :      " +  str(self.a) +" , " + str(self.b)+" , " + str(self.c);
    rstr +=  "\nAngles A,B,C d:   " +  str(self.Ad) +" , "+ str(self.Bd) + " , " + str(self.Cd);
    rstr +=  "\nAngles A,B,C r:   " +  str(self.Ar) +" , "+ str(self.Br) + " , " + str(self.Cr);
    return rstr;
  def solve(self):
    import math;
    if(self.isSolveable()):
      
      if (self.sides == 3):
        
        self = self.sss();
      elif (self.sides == 2):
        self.sas();
      elif (self.sides == 1):
        self.aas();
    
    self.findPerimeter();
    self.findArea();    
    self.sp = self.perimeter/2.0
    self.areaC = math.sqrt((self.sp*(self.sp-self.a)*(self.sp-self.b)*(self.sp-self.c)))
    self.r = 2.0*self.areaC/self.perimeter

  def draw(self,turtle):
    
    import math;
    
    self.color = nextcolor();
    turtle.penup();
    turtle.seth(self.rotater);
    turtle.setpos(self.x,self.y);
    turtle.pendown();
    
    turtle.color(self.color);
    self.Apos = turtle.pos();
    turtle.forward(self.c);
    turtle.left(180.0-self.Bd);
    self.Bpos = turtle.pos();  
    turtle.forward(self.a);
    
    self.Cpos = turtle.pos();
    self.CposHead = turtle.heading();
    turtle.left(180.0-self.Cd);

    turtle.forward(self.b);
    turtle.left(180.0-self.Ad);
  

  def drawInCircle(self,turtle):
    import math;
    intri = triangle();
    intri.rotater = self.rotater + 0.5 * self.Ad;
    intri.b = self.b;
    intri.Ad = self.Ad/2;
    intri.Cd = self.Cd/2;
    intri.Bd = 180 - intri.Ad - intri.Cd;
    intri.Ar = self.Ar/2;
    intri.Cr = self.Cr/2;
    intri.Br = math.pi - intri.Cr - intri.Ar;
    intri.x = self.x;
    intri.y = self.y;
    
    
    intri.aas();
    intri.solve();
    #intri.draw(turtle);
    
    
    turtle.penup();
    turtle.goto(self.Cpos[0],self.Cpos[1]);
    turtle.seth(self.CposHead);
    turtle.left(180-intri.Cd);
    turtle.forward(intri.a + self.r);
    turtle.left(90);
    turtle.pendown();
    turtle.circle(self.r);
    turtle.penup();
    
    return intri;

  
      
def findDistance(x1,x2,y1,y2):
  import math;
  distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
  return distance

def callback_1(x,y):
  import math;
  xs.append(x);
  ys.append(y);  
  if(len(xs) >= 3):    
    c = findDistance(xs[0],xs[1],ys[0],ys[1]);
    rot = math.degrees(math.atan2(ys[0]-ys[1],xs[0]-xs[1]));    
    a = findDistance(xs[1],xs[2],ys[1],ys[2]);
    b = findDistance(xs[2],xs[0],ys[2],ys[0]);   
    
    tri = triangle();
    tri.a = a;
    tri.b = b;
    tri.c = c;
    tri.x = xs[0];
    tri.y = ys[0];
    tri.rotater = 180+rot;

    tri.solve();
  
    tri.draw(turtle_1);
    print("this");

    intri = tri.drawInCircle(turtle_1);
    
    print("pre pop")
    xs.pop();
    ys.pop();
    xs.pop();
    ys.pop();
    xs.pop();
    ys.pop();
    print("call back")
   
  
def getinput():
  mytri = triangle();

  print("You will be asked for a value if you dont have it enter 0")
  count = 0;
  sides = 0;
  angles = 0;
  mytri.a = float(input("a = "));
  if (mytri.a != 0.0):
    count += 1;
    sides += 1;
  mytri.b = float(input("b = "));
  if (mytri.b != 0.0):
    count += 1;
    sides += 1;
  mytri.c = float(input("c = "));
  if (mytri.c != 0.0):
    count += 1;
    sides += 1;

  if (mytri.a == 0):
    mytri.Ad = float(input("A = "));
    if(mytri.Ad == 0.0):
      count +=1;
      angles +=1;

  if (mytri.b == 0.0):
    mytri.Bd = float(input("B = "));
    if (mytri.Bd != 0.0):
      count += 1;
      angles += 1;

  if (mytri.c == 0): 
    mytri.Cd = float(input("C = "));
    if (mytri.Cd != 0.0):
      count += 1;
      angles += 1;
  mytri.rotater = float(input("Rotation in Degrees"));

  if(count <3):
    print("bad input detected we need three values to solve a trialge try agin")
    getinput();
    return;  
  if (sides == 0):
    print("bad input detected we need at least one side to solve a trialge try agin")
    getinput();
    return;  

  
  if (sides == 3):
    mytri.sss();
  elif (sides == 2):
    mytri.sas();
  elif (sides == 1):
    mytri.aas();
  print mytri;
  return mytri;
    
def main():
  
  turtle = Turtle();
  turtle.speed(tspeed);
  turtle.ht();
  while True:
    mytri = getinput();
    mytri.solve();
    mytri.draw(turtle);
    intri = mytri.drawInCircle(turtle);
    intri.drawInCircle();
    print(mytri);

def randomMain():
  while True:
    myRandomTri = randomtri();
    myRandomTri.draw(turtle_1);
    myRandomTri.drawInCircle(turtle_1);
    
    print(myRandomTri);



def nextcolor():
  global colorindex;
  colorindex += 1;
  if (colorindex > 20 ):
    colorindex = 0;
  
  return colors[colorindex];

def randomtri():
  import random;
  mytri = triangle();
  mytri.c = random.uniform(30,500)
  mytri.a = random.uniform(30,500)
  mytri.x = random.uniform(-600,400);
  mytri.y = random.uniform(-500,400);
  mytri.rotater =  random.uniform(-360,360)
  diff = abs(mytri.c-mytri.a);
  print diff;

  mytri.b = random.uniform(diff+1, mytri.c+mytri.a)
  mytri.sss();
  mytri.solve();

  return mytri;



def zoomMain():
  zoomtri = triangle();
  zoomtri.a = 600.0;
  zoomtri.b = 200.0;
  zoomtri.c = 600.0;
  zoomtri.sss();
  zoomtri.solve();
  zoomtri.draw(turtle_1);
  zoommode(zoomtri);

def zoommode(zoomtri):
  import math;
  rate = 4.0
  zoomtri.a -= rate;
  zoomtri.b -= rate;
  zoomtri.c -= rate;
  if (zoomtri.a <= 0 or zoomtri.b <= 0 or zoomtri.c <= 0):
    return;

  subtri = triangle();
  subtri.c = rate/2;
  subtri.Ad = zoomtri.Ad / 2.0;
  subtri.Ar = zoomtri.Ar / 2.0;
  subtri.Bd = 90;
  subtri.Br = math.pi/2;
  subtri.Cd = 180 - subtri.Ad - subtri.Bd;
  subtri.Cr = math.pi - subtri.Br - subtri.Ar;
  subtri.aas();
  subtri.sss();
  subtri.solve();



  zoomtri.x += rate/2;
  zoomtri.y += subtri.a;
  
  zoomtri.sss();
  zoomtri.solve();
  zoomtri.draw(turtle_1);
  #zoomtri.drawInCircle(turtle_1);
  
  
  zoommode(zoomtri);


colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ffffff', '#000000'];
colorindex = 0;
tspeed = 0;
from turtle import*;
xs = [];
ys = [];
turtle_1 = Turtle()
turtle_1.forward(1); 
turtle_1.speed(tspeed);


Screen().listen()  
Screen().bgcolor("black");
Screen().onclick(callback_1)
randomMain();
zoomMain();
#main();




