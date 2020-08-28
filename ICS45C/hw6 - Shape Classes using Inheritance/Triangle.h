#include "Shape.h"

class Triangle
    : public Shape
{
protected:
    double height;
    double base;
    string name;
public:
    Triangle(double newHeight, double newBase, string newName)
	: Shape(newHeight, newBase, newName), height(newHeight), base(newBase), name(newName)
    {
    }
    virtual double area()
    {
	return (base * height) / 2.0;
    }
    virtual void draw()
    {
	for(int i = 1; i <= height; ++i)
	{
	    if(i == height)
	    {
		for(int j = 1; j <= base; ++j)
		    cout << '*';
		cout << endl;
	    }
	    else
	    {
	        for(int j = 1; j <= i; ++j)
		    cout << '*';
	        cout << endl;
	    }
	}
    }
    ~Triangle() {}
};

