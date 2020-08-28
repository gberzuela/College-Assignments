#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include <fstream>
#include <iterator>
using namespace std;

int main()
{
    ifstream nums("rand_numbers.txt");
    ofstream odds("odd.txt");
    ofstream evens("even.txt");
    vector<int> vecs;
    copy( istream_iterator<int>(nums), istream_iterator<int>(), back_inserter(vecs) );
    sort( begin(vecs), end(vecs) );
    for_each( begin(vecs), end(vecs), [&](int num)
    {
	if( num % 2 == 0 )
	    evens << num << "\n";
	else
	    odds << num << ' ';
    } );
    return 0;
}
