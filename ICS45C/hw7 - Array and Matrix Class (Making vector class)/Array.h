#include <iomanip>
#include <iostream>
#include "Exception.h"
using namespace std;

template
    <typename Type>

class Array
{
private:
    int len;
    Type * buf;
public:
    Array(int newLen)
	: len(newLen), buf(new Type [newLen])
    {
    }
    Array (const Array & l)
	: len(l.len), buf(new Type [l.len])
    {
	for(int i = 0; i < l.len; ++i)
	    buf[i] = l.buf[i]; 
    }
    int length()
    {
	return len;
    }
    Type & operator [](int i)
	throw(IndexOutOfBoundsException)
    {
	if(!(0 <= i && i < len))
	    throw IndexOutOfBoundsException();
	return buf[i];
    }
    void print(ostream & out)
    {
	for(int i = 0; i < len; ++i)
	    out << setw(8) << setprecision(2) << fixed << right << buf[i];
	out << endl;
    }
    friend ostream & operator <<(ostream & out, Array & a)
    {
	a.print(out);
	return out;
    }
    friend ostream & operator <<(ostream & out, Array * ap)
    {
	ap->print(out);
	return out;
    }
    ~Array()
    {
	delete[] buf;
    }
};
