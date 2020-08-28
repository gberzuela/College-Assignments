#include "Shape.h"
#include "Triangle.h"
#include "Rectangle.h"
#include "Square.h"
#include "Circle.h"

void test_triangle()
{
    Triangle First(5, 5, "First");
    Triangle Second(4, 3, "Second");
    First.draw();
    Second.draw();
    cout << "First triangle area: " << First.area() << endl;
    cout << "Second triangle area: " << Second.area() << endl;
}

void test_rectangle()
{
    Rectangle First(4, 8, "First");
    Rectangle Second(8, 4, "Second");
    First.draw();
    Second.draw();
    cout << "First rectangle area: " << First.area() << endl;
    cout << "Second rectangle area: " << Second.area() << endl;
}

void test_square()
{
    Square First(5, 0, "First");
    Square Second(10, 0, "Second");
    First.draw();
    Second.draw();
    cout << "First square area: " << First.area() << endl;
    cout << "Second square area: " << Second.area() << endl;
}

void test_circle()
{
    Circle First(5, 0, "First");
    Circle Second(10, 0, "Second");
    First.draw();
    Second.draw();
    cout << "First circle area: " << First.area() << endl;
    cout << "Second circle area: " << Second.area() << endl;
}

int main()
{
    cout << "~~~~Testing Triangle~~~~" << endl;
    test_triangle();
    cout << "\n~~~~Testing Rectangle~~~~" << endl;
    test_rectangle();
    cout << "\n~~~~Testing Square~~~~" << endl;
    test_square();
    cout << "\n~~~~Testing Circle~~~~" << endl;
    test_circle();
    return 0;
}
