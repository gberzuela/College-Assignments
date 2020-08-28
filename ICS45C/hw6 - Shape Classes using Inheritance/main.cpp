#include "Shape.h"
#include "Rectangle.h"
#include "Square.h"
#include "Circle.h"
#include "Triangle.h"
#include "Picture.h"

int main()
{ 
    Picture p;
    p.add(new Triangle(5, 5, "one"));
    p.add(new Triangle(4, 3, "two"));

    p.add(new Circle(5, 0, "three"));
    p.add(new Circle(10, 0, "four"));

    p.add(new Square(5, 0, "five"));
    p.add(new Square(10, 0, "six"));

    p.add(new Rectangle(4, 8, "seven"));
    p.add(new Rectangle(8, 4, "eight"));

    p.drawAll();
    cout << "Total area of all the shapes is: " << p.totalArea() << endl;
    return 0;
}
