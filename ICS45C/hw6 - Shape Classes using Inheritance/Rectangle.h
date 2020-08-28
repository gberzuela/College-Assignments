#include "Shape.h"
#ifndef RECTANGLE_H
#define RECTANGLE_H

class Rectangle
    : public Shape
{
protected:
    double height;
    double base;
    string name;
public:
    Rectangle(double newHeight, double newBase, string newName)
	: Shape(newHeight, newBase, newName), height(newHeight), base(newBase), name(newName)
    {
    }
    virtual double area()
    {
	return base * height;
    }
    virtual void draw()
    {
	for(int i = 1; i <= height; ++i)
	{
	    if(i == 1 || i == height)
	    {
		for(int j = 1; j <= base + 1; ++j)
		    cout << '*';
		cout << endl;
	    }
	    else
	    {
		cout << '*';
		for(int j = 1; j < base; ++j)
		    cout << ' ';
		cout << '*' << endl;
	    }
	}
    }
    ~Rectangle() {}
};

#endif
