#include "Shape.h"
#include <math.h>

class Circle
    : public Shape
{
protected:
    double radius;
    double pi = 3.14159265359;
    string name;
public:
    Circle(double newRadius, double rand, string newName)
	: Shape(newRadius, rand, newName), radius(newRadius), name(newName)
    {
    }
    virtual double area()
    {
	return pi * (radius * radius);
    }
    virtual void draw()
    {
	for(int y = -radius; y <= radius; ++y)
	{
	    for(int x = -(4/3)*radius; x <= (4/3)*radius; ++x)
	    {
		float distance = (x/((4/3)*radius))*(x/((4/3)*radius)) + (y/radius)*(y/radius);
		if(distance > 0.90 && distance < 1.1)
		{
		    cout << '*';
		}
		else
		{
		    cout << ' ';
		}
	    }
	    cout << endl;
	}
    }
    ~Circle() {}
};
