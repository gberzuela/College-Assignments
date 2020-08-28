/// String.cpp; definitions of String class
#include "String.h"

/// Start of public definitions
String :: String(const char * s)
    : buf(strdup(s))
{
}

String :: String(const String & s)
    : buf(strdup(s.buf))
{
}

String String :: operator =(const String & s)
{
    delete_char_array(buf);
    buf = strdup(s.buf);
    return *this;
}

char & String :: operator [](int index)
{
    if (inBound(index))
	return buf[index];
    cerr << "Index is out of bounds. In order to continue, index will be set to 0." << endl;
    return buf[0];
}

int String :: size()
{
    return strlen(buf);
}

String String :: reverse()
{
    char *cpy;
    cpy = strdup(buf);
    reverse_cpy(cpy, buf);
    String copy(cpy);
    delete_char_array(cpy);
    return copy;
}

int String :: indexOf(const char s)
{
    char *point = strchr(buf, s);
    if (point != nullptr)
	return point - buf;
    else if (point == nullptr)
	return -1;
}

int String :: indexOf(const String pattern)
{
    char *point = strstr(buf, pattern.buf);
    if (point != nullptr)
	return point - buf;
    else if (point == nullptr)
	return -1;
}

bool String :: operator ==(const String s)
{
    return strcmp(buf, s.buf) == 0;
}

bool String :: operator !=(const String s)
{
    return strcmp(buf, s.buf) != 0;
}

bool String :: operator >(const String s)
{
    return strcmp(buf, s.buf) > 0;
}

bool String :: operator <(const String s)
{
    return strcmp(buf, s.buf) < 0;
}

bool String :: operator <=(const String s)
{
    return strcmp(buf, s.buf) <= 0;
}

bool String :: operator >=(const String s)
{
    return strcmp(buf, s.buf) >= 0;
}

String String :: operator +(const String s)
{
    char *cpy = new_char_array(strlen(buf) + strlen(s.buf) +  1);
    strcpy(cpy, buf);
    strcat(cpy, s.buf);
    String copy(cpy);
    delete_char_array(cpy);
    return copy;
}

String String :: operator +=(const String s)
{
    char *cpy = new_char_array(strlen(buf) + strlen(s.buf) + 1);
    strcpy(cpy, buf);
    strcat(cpy, s.buf);
    delete_char_array(buf);
    buf = strdup(cpy);
    delete_char_array(cpy);
    return *this;
}

void String :: print(ostream & out)
{
    out << buf;
}

void String :: read(istream & in)
{
    char a[256];
    in.getline(a, 256);
    delete_char_array(buf);
    buf = strdup(a);
}

void String :: final_report_on_allocations()
{
   if (allocations > 0)
	error("Memory leak in class String");
   if (allocations < 0)
	error("Too many delete[]s in class String");
   if (allocations == 0)
	cout << "Allocations & deallocations match\n";
}

String :: ~String()
{
    delete_char_array(buf);
}

/// Start of private definitions
bool String :: inBound(int i)
{
    return i >= 0 && i < strlen(buf);
}

int String :: strlen(const char * s)
{
    int len;
    for (int i = 0; s[i] != '\0'; ++i)
	++len;
    return len;
}

char * String :: strcpy(char * dest, const char * src)
{
    int i;
    for (i = 0; src[i] != '\0'; ++i)
	dest[i] = src[i];
    dest[i] = '\0';
    return dest;
}

char * String :: strcat(char * dest, const char * src)
{
    strcpy(dest + strlen(dest), src);
    return dest;
}

int String :: strcmp(const char * left, const char * right)
{
    for (int i = 0; left[i] != '\0'; ++i)
    {
	if ((left[i] != right[i]) || left[i] == '\0' || right[i] == '\0')
	    return left[i] - right[i];
    }
    return 0;
}

int String :: strncmp(const char * left, const char * right, int n)
{
    for (int i = 0; left[i] != '\0' && i <= n; ++i)
    {
	if ((left[i] != right[i]) || left[i] == '\0' || right[i] == '\0')
	    return left[i] - right[i];
    }
    return 0;
}

char * String :: strchr(char * str, int c)
{
    for (int i = 0; str[i] != '\0'; ++i)
    {
	if (str[i] == c)
	    return str + i;
    }
    return nullptr;
}

const char * String :: strstr(const char * haystack, const char * needle)
{
    return const_cast < char * > (strstr(const_cast < char * > (haystack), const_cast < char * > (needle)));
}

char * String :: strstr(char * haystack, const char * needle)
{
    int len = strlen(needle);
    char *s = haystack;
    char *p;
    while (s != '\0')
    {
	p = strchr(s, needle[0]);
	if (p == nullptr)
	    return nullptr;
	else if (strncmp(p, needle, len) == 0)
	    return p;
	else
	    s = p + 1;
    }
    return nullptr;
}
void String :: reverse_cpy(char * dest, const char *src)
{
    int len = strlen(src);
    for (int i = len - 1; i >= 0; --i)
	dest[len-i-1] = src[i];
    dest[len] = '\0';
}

char * String :: strdup(const char *src)
{    
    return strcpy(new_char_array(strlen(src)+1), src);
}

int String :: allocations = 0;

char * String :: new_char_array(int n_bytes)
{
    ++allocations;
    return new char[n_bytes];
}

void String :: delete_char_array(char * p)
{
    --allocations;
    if (allocations < 0)
	error("More delete[] than new[]");
    delete [] p;
}

void String :: error(const char * p)
{
    cerr << "Error (class String): " << p << endl;
}

/// Operator << and >> overload
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
