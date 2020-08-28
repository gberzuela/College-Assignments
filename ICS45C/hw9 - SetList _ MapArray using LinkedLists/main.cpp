#include <iostream>
//#include <set>
#include "SetList.h"
//#include <map>
#include "MapArray.h"
#include <string>
#include <algorithm>
//#include <functional>
#include <fstream>
#include <iterator>
using namespace std;

int main() {
    ifstream stops("stopwords.txt");
    ifstream doc("sample_doc.txt");
    ofstream freq_text("frequency.txt");
    SetList<string> exclude;
    MapArray<string, int> freq_map;
    for_each( istream_iterator<string>(stops), istream_iterator<string>(), [&](string s)
    {
	transform( s.begin(), s.end(), s.begin(), ::tolower );
	exclude.insert(s);
    });
    for_each( istream_iterator<string>(doc), istream_iterator<string>(), [&](string s)
    {
	transform( s.begin(), s.end(), s.begin(), ::tolower );
	if( exclude.find(s) == exclude.end() )
	    ++freq_map[s];
    });
    for_each( freq_map.begin(), freq_map.end(), [&](pair<string, int> output)
    {
	freq_text << output.first << ": " << output.second << endl;
    });
    return 0;
}
