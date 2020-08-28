#include <iostream>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <functional>
#include <fstream>
#include <iterator>
using namespace std;

int main()
{
    ifstream stops("stopwords.txt");
    ifstream doc("sample_doc.txt");
    ofstream freq_txt("frequency.txt");
    set<string> exclude;
    map<string, int> freq_map;
    // first lowers contents of stopwords.txt then stors into a set
    for_each( istream_iterator<string>(stops), istream_iterator<string>(), [&](string s)
    {
	transform( s.begin(), s.end(), s.begin(), ::tolower );
	exclude.insert(s);
    } );
    // first lowers the contents of sample_doc.txt then checks to see if the word is within the exclude set
    // if not, increment the int value within the map
    for_each( istream_iterator<string>(doc), istream_iterator<string>(), [&](string s)
    {
	transform( s.begin(), s.end(), s.begin(), ::tolower );
	if( exclude.find(s) == exclude.end() )
	    ++freq_map[s];
    } );
    // iterates through the freq_map and copies its contents into a file
    for_each( begin(freq_map), end(freq_map), [&](std::pair<string, int> output)
    {
	freq_txt << output.first << ": " << output.second << "\n";
    } );
    return 0;
}
