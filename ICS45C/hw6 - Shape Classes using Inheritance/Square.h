#include "Shape.h"
#include "Rectangle.h"

class Square
    : public Rectangle
{
protected:
    double side;
    string name;
public:
    Square(double newSide, double newHeight, string newName)
	: Rectangle(newSide, newHeight, newName), side(newSide), name(newName)
    {
    }
    virtual double area()
    {
	return side * side;
    }
    virtual void draw()
    {
	for(int i = 1; i <= side; ++i)
	{
	    if(i == 1 || i == side)
	    {
		for(int j = 1; j <= side + 2; ++j)
		    cout << '*';
		cout << endl;
	    }
	    else
	    {
		cout << '*';
		for(int j = 1; j <= side; ++j)
		    cout << ' ';
		cout << '*' << endl;
	    }
	}
    }
    ~Square() {}
};
