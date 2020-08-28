// String.h; defines and declares the String class
#include <iostream>
using namespace std;

#define MAXLEN 128
class String
{
public:
    /// Both constructors should construct this Strong from the parameter s
    explicit String(const char * s = "")
    {
	if (strlen(s) > MAXLEN)
	    cout << "Cannot construct String. String too large." << endl;
	else
	    strcpy(buf, s);
    }
    String(const String & s)
    {
	if (strlen(s.buf) > MAXLEN)
	    cout << "Cannot construct String. String too large." << endl;
	else
	    strcpy(buf, s.buf);
    }
    String operator = (const String & s)
    {
	String assign(strcpy(buf, s.buf));
	return assign;
    }
    char & operator [](int index)
    {
	if (inBounds(index))
	    return buf[index];
	cerr << "Index is out of bounds. In order to continue, index will be set to 0." << endl;
	return buf[0];
    }
    int size()
    {
	return strlen(buf);
    }
    String reverse() // does not modify this String
    {
	String copy;
	strcpy(copy.buf, buf);
	reverse_cpy(copy.buf, buf);
	return copy;
    }
    int indexOf(const char c)
    {
	char *point = strchr(buf, c);
	if (point != nullptr)
	    return point - buf;
	/*else if (point == nullptr)
	    return -1;*/
    }
    int indexOf(const String pattern)
    {
	char *point = strstr(buf, pattern.buf);
	if (point != nullptr)
	    return point - buf;
	/*else if (point == nullptr)
	    return -1;*/
    }
    bool operator ==(const String s)
    {
	return strcmp(this->buf, s.buf) == 0;
    }
    bool operator !=(const String s)
    {
	return strcmp(this->buf, s.buf) != 0;
    }
    bool operator >(const String s)
    {
	return strcmp(this->buf, s.buf) > 0;
    }
    bool operator <(const String s)
    {
	return strcmp(this->buf, s.buf) < 0;
    }
    bool operator <=(const String s)
    {
	return strcmp(this->buf, s.buf) <= 0;
    }
    bool operator >=(const String s)
    {
	return strcmp(this->buf, s.buf) >= 0;
    }
    /// concatenates this and s to return result
    String operator +(const String s)
    {
	String copy;
	strcpy(copy.buf, buf);
	strcat(copy.buf, s.buf);
	return copy;
    }
    // concatenates s onto end of this string
    String operator +=(const String s)
    {
	String cat(strcat(buf, s.buf));
	if (strlen(cat.buf) > MAXLEN)
	    cout << "Cannot concatenate. Produced String is too large." << endl;
	else
	    return cat;
    }
    void print(ostream & out)
    {
	out << buf;
    }
    void read(istream & in)
    {
	if (strlen(buf) > MAXLEN)
	    cout << "String too large." << endl;
	else
	    in >> buf;
    }
    ~String(){}
private:
    bool inBounds(int i)
    {
	return i >= 0 && i < strlen(buf);
    } // HINT: some C string primitives you should define and use
    static int strlen(const char * s)
    {
	int len = 0;
	for (int i = 0; s[i] != '\0'; ++i)
	    ++len;
	return len;
    }
    static char *strcpy(char *dest, const char *src)
    {
	int i;
	for (i = 0; src[i] != '\0'; ++i)
	    dest[i] = src[i];
	dest[i] = '\0';
	return dest;
    }
    static char *strcat(char *dest, const char *src)
    {
	strcpy(dest + strlen(dest), src);
	return dest;
    }
    static int strcmp(const char *left, const char *right)
    {
	for (int i = 0; left[i] != '\0'; ++i)
	{
	    if ((left[i] != right[i]) || left[i] == '\0' || right[i] == '\0')
		return left[i] - right[i];
	}
	return 0;
    }
    static int strncmp(const char *left, const char *right, int n)
    {
	for (int i = 0; left[i] != '\0' && i <= n; ++i)
	{
	    if ((left[i] != right[i]) || left[i] == '\0' || right[i] == '\0')
		return left[i] - right[i];
	}
	return 0;
    }
    static char *strchr(char *str, int c)
    {
	for (int i = 0; str[i] != '\0'; ++i)
	{
	    if (str[i] == c)
		return str + i;
	}
	return nullptr;
    }
    /* haystack "The quick brown fox ran up the lazy log"
       needle "ran" */
    static const char *strstr(const char *haystack, const char *needle)
    {
	return const_cast < char * > (strstr(const_cast < char * > (haystack), const_cast < char * > (needle)));
    }
    static char *strstr(char *haystack, const char *needle)
    {
	int len = strlen(needle);
	char *s = haystack;
	char *p;
	while (s != '\0')
	{
	    p = strchr(s, needle[0]);
	    if (p == nullptr)
		return nullptr;
	    else if (strncmp(p, needle, len) ==0)
		return p;
	    else
		s = p + 1;
	}
	return nullptr;
    }
    static void reverse_cpy(char *dest, const char *src)
    {
	int len = strlen(src);
	for (int i = len - 1; i >= 0; --i)
	    dest[len-i-1] = src[i];
	dest[len] = '\0';
    }
    char buf[MAXLEN]; // array for the character in this string
    // DO NOT store the 'logical' length of this string
    // use the null '\0' terminator to mark the end
    };
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
