#ifndef SHAPE_H
#define SHAPE_H

#include <iostream>
using namespace std;

class Shape
{
protected:
    int x;
    int y;
    string name;
public:
    virtual double area() = 0;
    virtual void draw() = 0;
    Shape(int centerX, int centerY, string newName)
	: x(centerX), y(centerY), name(newName)
    {
    }
    virtual ~Shape() {}
};

#endif
