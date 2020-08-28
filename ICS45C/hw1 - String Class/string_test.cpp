#include "String.h"

void test_assignment()
{
    cout << "----Testing assignment operator----" << endl;
    String first("First");
    String second("Second");
    cout << "String 1: " << first << endl  << "String 2: " << second << endl;
    cout << "String 1 = String 2" << endl;
    first = second;
    cout << "String 1: " << first << endl << "String 2: " << second << endl;
}

void test_index()
{
    cout << "----Testing index operator----" << endl;
    String index("ICS 45C is a fun class!");
    float in;
    cout << "Please enter a index for the string 'ICS 45C is a fun class!': ";
    cin >> in;
    cout <<  "The character at index " << in << " is " << index[in] << endl;
}

void test_size()
{
    cout << "----Testing size----" << endl;
    String random("Hi, welcome to Chili's!");
    cout << "String 'Hi, welcome to Chili's!' is size " << random.size() << endl;
}

void test_rev()
{
    cout << "----Testing reverse----" << endl;
    String test("Hello!");
    cout << "Original string: " << test << endl;
    cout << "Reverse: " << test.reverse() << endl;
}

void test_indexOfchar()
{
    char c;
    cout << "----Testing indexOf(char)----" << endl;
    String tester("The brown fox jumped over the brown barn.");
    cout << "String being tested:\n String1: " << tester << endl;
    cout << "Please enter a character to find index of: ";
    cin >> c;
    cout << "Character " << c << " is found in index " << tester.indexOf(c) << endl;
}

void test_indexOfpattern()
{
    cout << "----Testing indexOf(pattern)----" << endl;
    String haystack("The quick brown fox ran up the lazy log");
    String needle("ran");
    cout << "Strings being tested:\nString1: " << haystack << ", String2: " << needle << endl;
    cout << needle << " is found in index " << haystack.indexOf(needle) << endl;
}

void test_equality()
{
    cout << "----Testing equality----" << endl;
    String first("Hello");
    String second("World");
    String third("Hello");
    cout << "Strings being tested:\nString1: " << first << ", String2: " << second << ", String3: " << third << endl;
    cout << "String1 == String3: " << (first == third) << endl;
    cout << "String1 == String2: " << (first == second) << endl;
    cout << "String1 != String2: " << (first != second) << endl;
}

void test_relations()
{
    cout << "----Testing relational operators----" << endl;
    String first("Hello");
    String second("World");
    cout << "String being tested:'\nString1: " << first << ", String2: " << second << endl;
    cout << "String1 < String2: " << (first < second) << endl;
    cout << "String1 <= String2: " << (first <= second) << endl;
    cout << "String1 > String2: " << (first > second) << endl;
    cout << "String1 >= String2: " << (first >= second) << endl;
}

void test_addition()
{
    cout << "----Testing addtion operator----" << endl;
    String first("Hello");
    String second("World");
    cout << "Strings being tested:\nString1: " << first << ", String2: " << second << endl;
    cout << "String1 + String2: " << (first + second) << endl;
    cout << "Initial string left unmutated. String1: " << first << ", String2: " << second << endl;
}
void test_concatenation()
{
    cout << "----Testing concatenation operator----" << endl;
    String first("Hello");
    String second(" World");
    cout << "Strings being tested:\nString1: " << first << ", String2: " << second << endl;
    cout << "String1 += String2: " << (first += second) << endl;
    cout << "String1 is now mutated. String1: " << first << endl;
}

int main()
{
    cout << "~~~~Beginning tests.~~~~" << endl;
    test_assignment();
    test_index();
    test_size();
    test_rev();
    test_indexOfchar();
    test_indexOfpattern();
    test_equality();
    test_relations();
    test_addition();
    test_concatenation();
    cout << "~~~~Concluding tests.~~~~" << endl;
    return 0;
}
