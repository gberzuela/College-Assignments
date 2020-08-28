#include "String.h"

void test_constructor()
{
    cout << "----Testing constructors and assignment----" << endl;
    String test1("Hello");
    String test2("World");
    cout << "Strings: " << test1 << " and " << test2 << endl;
    test1 = test2;
    cout << "test1=test2: " << test1 << " and " << test2 << endl; 
}

void test_indexOp()
{
    cout << "------Testing index operator------" << endl;
    String test("ICS 45c is a fun class!");
    float in;
    cout << "Please enter an index to find a character in 'ICS 45c is a fun class!': ";
    cin >> in;
    cout << "The character at index " << in << " is " << test[in] << endl;
}

void test_size()
{
    cout << "------Testing size------" << endl;
    String test("Hi, how's it going?");
    cout << "The size of the string '" << test << " is: " << test.size() << endl;
}

void test_indexOfChar()
{
    cout << "------Testing indexOfChar------" << endl;
    String test("The brown fox jumped over the lazy log.");
    cout << "Given string: " << test << "'\nThe character 'j' is found at index " << test.indexOf('j') << endl;
}

void test_relation()
{
    cout << "------Testing relations == and <------" << endl;
    String test1("Hello");
    String test2("World");
    String test3("Hello");
    cout << "Given strings: '" << test1 << "' and '" << test2 << "' and '" << test3 << "'" <<endl;
    cout << "'Hello'=='Hello': " << (test1 == test3) << endl;
    cout << "'Hello'<'World': " << (test1 < test2) << endl;
}

void test_add()
{
    cout << "------Testing addition------" << endl;
    String test1("Hello");
    String test2(" World");
    cout << "Given strings: '" << test1 << "' and '" << test2 << "'" << endl;
    cout << "+: " << test1 + test2 << endl;
    cout << "Final strings: '" << test1 << "' and '" << test2 << "'" << endl;
}

void test_cat()
{
    cout << "------Testing concatenation------" << endl;
    String test1("Hello");
    String test2(" World");
    cout << "Given strings: '" << test1 << "' and '" << test2 << "'" << endl;
    test1 += test2;
    cout << "+=: " << test1 << endl;
    cout << "Final strings: '" << test1 << "' and '" << test2 << "'" << endl;
}

void test_reverse()
{
    cout << "------Testing reverse------" << endl;
    String test("Hello world");
    cout << "Given string: " << test << endl;
    cout << "Reversed: " << test.reverse() << endl;
    cout << "Final string (to show string is unchanged): " << test << endl;
}

int main()
{
    cout << "~~~~~~Beginning tests for String class using ListNodes~~~~~~" << endl;
    test_constructor();
    test_indexOp();
    test_size();
    test_indexOfChar();
    test_relation();
    test_add();
    test_cat();
    test_reverse();
    cout << "~~~~~~Ending tests for String class using ListNodes~~~~~~" << endl;
    return 0;
}
