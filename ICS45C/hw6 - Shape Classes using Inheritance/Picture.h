#ifndef PICTURE_H
#define PICTURE_H
#include "Shape.h"

typedef class ShapeLinkedListPair* ShapeLinkedList;
class ShapeLinkedListPair
{
public:
    Shape * info;
    ShapeLinkedList next;
    ShapeLinkedListPair(Shape * newInfo, ShapeLinkedList newNext)
	: info(newInfo), next(newNext)
    {
    }
    static void deleteList(ShapeLinkedList L)
    {
	if(L != nullptr)
	{
	    deleteList(L->next);
	    delete L->info;
	    delete L;
	}
    }
};

class Picture
{
private:
    ShapeLinkedList head;
public:
    Picture()
	: head(nullptr)
    {
    }
    void drawAll()
    {
	for(ShapeLinkedList p = head; p != nullptr; p = p->next)
	{
	    p->info->draw();
	}
    }
    double totalArea()
    {
	double total = 0;
	for(ShapeLinkedList p = head; p != nullptr; p = p->next)
	{
	    total += p->info->area();
	}
	return total;
    }
    void add(Shape * sp)
    {
	head = new ShapeLinkedListPair(sp, head);
    }
    ~Picture()
    {
	ShapeLinkedListPair :: deleteList(head);
    }
};

#endif
