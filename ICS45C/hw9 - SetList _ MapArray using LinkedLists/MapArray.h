#include <iostream>
//#include <algorithm>
//#include <iterator>
using namespace std;

template
    < typename Index, typename Value >
class MapArray{
    int count;
    pair<Index, Value> *buf;
public:
    struct iterator{
	// Iterator traits
	typedef random_access_iterator_tag iterator_category;
	typedef iterator self_type;
	typedef pair<Index, Value> value_type;
	typedef pair<Index, Value>& reference;
	typedef pair<Index, Value>* pointer;
	typedef ptrdiff_t difference_type;
    private:
	pointer ibuf;
    public:
	iterator( pointer ptr )
	    : ibuf(ptr){}
	self_type operator ++(){
	    ++ibuf;
	    return *this;
	}
	self_type operator ++( int postfix ){
	    self_type cpy = *this;
	    ibuf++;
	    return cpy;
	}
	reference operator *(){
	    return *ibuf;
	}
	pointer operator ->(){
	    return ibuf;
	}
	bool operator ==( const self_type &rhs) const{
	    return ibuf == rhs.ibuf;
	}
	bool operator !=( const self_type &rhs) const{
	    return ibuf != rhs.ibuf;
	}
    };

    MapArray()
	: count(0), buf(new pair<Index, Value> [1000]){}
    iterator begin(){
	return iterator(buf);
    }
    iterator end(){
	return iterator(buf + count);
    }
    Value find( Index index ){
	for( int i = 0; i <= count; i++ ){
	    if( buf[i].first == index ){
		return i;
	    }
	}
	return -1;
    }
    Value& operator []( Index index ){
	if( find(index) == -1 ){
	    buf[count++] = pair<Index, Value>(index, 0);
	    sort( buf, buf + count );
	    return buf[find(index)].second;
	}	
	else{
	    sort( buf, buf + count );
	    return buf[find(index)].second;
	}
    }
    ~MapArray(){
	//for( int i = 0; i <= count; i++ )
	delete [] buf;
    }
};
