#include "String.h"

void test_constructor()
{
    cout << "------------Testing constructors------------" << endl;
    String test1("Hello");
    String test2("World");
    cout << "Starting strings:\nString1: " << test1 << "    String2: " << test2 << endl;
    test1 = test2;
    cout << "String1 = String2 now.\nString1: " << test1 << "    String2: " << test2 << "\n" << endl;
}

void test_index()
{
    cout << "------------Testing index operator------------" << endl;
    String index("ICS 45c is a fun class!");
    float in;
    cout << "Please enter an index for the string 'ICS 45c is a fun class!': ";
    cin >> in;
    cout << "The character at index " << in << " is " << index[in] << "\n" << endl;
}

void test_size()
{
    cout << "------------Testing size------------" << endl;
    String random("Hi, welcome to Chili's!");
    cout << "String: '" << random << "' is size " << random.size() << "\n" << endl;
}

void test_rev()
{
    cout << "------------Testing reverse------------" << endl;
    String test("KONO DIO DA!");
    cout << "Original string: " << test << endl;
    cout << "Reverse: " << test.reverse() << "\n" << endl;
}

void test_indexOfchar()
{
    char ch;
    cout << "------------Testing indexOf(char)------------" << endl;
    String tester("The brown fox jumped over the brown barn.");
    cout << "String to test: " << tester << endl;
    cout << "Please enter a character to find index of: ";
    cin >> ch;
    cout << "Character " << ch << " is found at index " << tester.indexOf(ch) << "\n" << endl; 
}

void test_indexOfpattern()
{
    cout << "------------Testing indexOf(pattern)------------" << endl;
    String haystack("The quick brown fox ran up the lazy log.");
    cout << "String to test: " << haystack << endl;
    String needle("ran");
    cout << "String to find: " << needle << endl;
    cout << "'" << needle << "' is found at index " << haystack.indexOf(needle) << "\n" << endl;
}

void test_equality()
{
    cout << "------------Testing equality------------" << endl;
    String first("Hello");
    String second("world");
    String third("Hello");
    cout << "Strings being tested:\nString1: " << first << ", String2: " << second << ". String3: " << third << endl;
    cout << "String1 == String2: " << (first == third) << endl;
    cout << "String 1 == String2: " << (first == second) << endl;
    cout << "String1 != String2: " << (first != second) << "\n" << endl;
}

void test_relations()
{
    cout << "------------Testing relational operators------------" << endl;
    String first("Hello");
    String second("World");
    cout << "Strings being tested:\nString1: " << first << ", String2: " << second << endl;
    cout << "String1 < String2: " << (first < second) << endl;
    cout << "String1 <= String2: " << (first <= second) << endl;
    cout << "String1 > String2: " << (first > second) << endl;
    cout << "String1 >= String2: " << (first >= second) << "\n" << endl;
}

void test_addition()
{
    cout << "------------Testing addition operator------------" << endl;
    String first("Hello");
    String second("World");
    cout << "Strings being tested:\nString1: " << first << ", String2: " << second << endl;
    cout << "String1 + String2: " << (first + second) << endl;
    cout << "Initial strings left unmutated:\nString1: " << first << ", String2: " << second << "\n" << endl;
}

void test_concatenation()
{
    cout << "------------Testing concatenation operator------------" << endl;
    String first("Hello");
    String second("World");
    cout << "Strings being tested:\nString1: " << first << ", String2: " << second << endl;
    cout << "String1 += String2: " << (first += second) << endl;
    cout << "String1 is now mutated:\nString1: " << first << ", String2: " << second << "\n" << endl;
}

int main()
{
    cout << "~~~~~~~~~~~~Beginning tests for String class~~~~~~~~~~~~\n" << endl;
    test_constructor();
    test_index();
    test_size();
    test_rev();
    test_indexOfchar();
    test_indexOfpattern();
    test_equality();
    test_relations();
    test_addition();
    test_concatenation();
    String::final_report_on_allocations();
    return 0;
}
