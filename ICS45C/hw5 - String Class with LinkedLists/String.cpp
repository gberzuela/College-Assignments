#include "String.h"

// Public definitions
String :: String(const char * s)
    : head(String :: ListNode :: stringToList(s))
{
}
String :: String(const String & s)
    : head(String :: ListNode :: copy(s.head))
{
}
String String :: operator =(const String & s)
{
    String :: ListNode :: deleteList(head);
    head = String :: ListNode :: copy(s.head);
    return *this;
}
char & String :: operator [](const int index)
{
    String :: ListNode* temp = head;
    if (inBound(index))
    {
	for(int count = 0; temp != nullptr; temp = head->next)
	{
	    if (count == index)
		return temp->info;
	    else
		++count;
	}
    }
    else
    {
	cout << "Index out of range. In order to continue, index will be set to 0." << endl;
	return head->info;
    }
}
int String :: size() const
{
    return String :: ListNode :: length(head);
}
int String :: indexOf(char c) const
{
    int count = 0;
    for(ListNode * p = head; p != nullptr; p = p->next)
    {
	if(p->info == c)
	    return count;
	++count;
    }
    cout << "Character " << c << " was not found in the string." << endl;
    return 0;
}
bool String :: operator ==(const String & s) const
{
    return String :: ListNode :: compare(head, s.head) == 0;
}
bool String :: operator <(const String & s) const
{
    return String :: ListNode :: compare(head, s.head) != 0;
}
String String :: operator +(const String & s) const
{
    String result;
    String :: ListNode :: deleteList(result.head);
    String :: ListNode* temp = String :: ListNode :: copy(head);
    result.head = String :: ListNode :: append(temp, s.head);
    String :: ListNode :: deleteList(temp);
    return result;
}
String String :: operator +=(const String & s)
{
    String :: ListNode* temp = String :: ListNode :: copy(head);
    String :: ListNode :: deleteList(head);
    head = String :: ListNode :: append(temp, s.head);
    String :: ListNode :: deleteList(temp);
    return *this;
}
String String :: reverse() const
{
    String result;
    String :: ListNode :: deleteList(result.head);
    String :: ListNode* temp = String :: ListNode :: copy(head);
    result.head = String :: ListNode :: reverse(temp);
    String :: ListNode :: deleteList(temp);
    return result;
}
void String :: print(ostream & out) const
{
    for(ListNode * p = head; p != nullptr; p = p->next)
	out << p->info;
}
void String :: read(istream & in)
{
    char temp[256];
    in.getline(temp, 256);
    String :: ListNode :: deleteList(head);
    head = String :: ListNode :: stringToList(temp);
}
String :: ~String()
{
    String :: ListNode :: deleteList(head);
}
// Private definitions
bool String :: inBound(int i)
{
    return i >= 0 && i < size();
}
String :: ListNode :: ListNode(char newInfo, ListNode * newNext)
    : info(newInfo), next(newNext)
{
}
String :: ListNode* String :: ListNode :: stringToList(const char * s)
{
    return !*s ? 0 : new ListNode(*s, stringToList(s+1));
}
String :: ListNode* String :: ListNode :: copy(ListNode * L)
{
    return L == nullptr ? nullptr : new ListNode(L->info, copy(L->next));
}
String :: ListNode* String :: ListNode :: reverse(ListNode * L)
{
    ListNode * result = nullptr;
    for(ListNode * p = L; p != nullptr; p = p->next)
	result = new ListNode(p->info, result);
    return result;
}
String :: ListNode* String :: ListNode :: append(ListNode * L1, ListNode * L2)
{
    return L1 == nullptr ? copy(L2) : new ListNode(L1->info, append(L1->next, L2));
}
int String :: ListNode :: compare(ListNode * L1, ListNode * L2)
{
    return L1 == nullptr || L2 == nullptr ? L1 == L2 : L1->info == L2->info && compare(L1->next, L2->next);
}
void String :: ListNode :: deleteList(ListNode * L)
{
    if (L != nullptr)
    {
	deleteList(L->next);
	delete L;
    }
}
int String :: ListNode :: length(ListNode * L)
{
    return !L ? 0 : 1 + length(L->next);
}
// iostream
ostream & operator <<(ostream & out, String str)
{
    str.print(out);
    return out;
}
istream & operator >>(istream & in, String & str)
{
    str.read(in);
    return in;
}

