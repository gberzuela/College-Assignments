#include <iostream>
using namespace std;

template
    < typename LType >

class ListNode{
public: 
    LType info;
    ListNode<LType>* next;
    ListNode<LType>( LType newInfo, ListNode* newNext )
	: info(newInfo), next(newNext){}
    static void deleteList( ListNode* L ){
	if( L != nullptr ){
	    deleteList( L->next );
	    delete L;
	}
    }
};

template
    < typename sType >

class SetList{
    ListNode<sType>* head;
public:
    struct iterator{
	// Iterator traits
	typedef forward_iterator_tag iterator_category;
	typedef iterator self_type;
	typedef ListNode<sType> value_type;
	typedef ListNode<sType>& reference;
	typedef ListNode<sType>* pointer;
	typedef ptrdiff_t difference_type;
    private:
	pointer ibuf;
    public:
	iterator( pointer ptr )
	    : ibuf(ptr){}
	/*self_type operator ++(){
	    ++ibuf;
	    return *this;
	}
	self_type operator ++( int postfix ){
	    self_type cpy = *this;
	    ibuf++;
	    return cpy;
	}*/
	reference operator*(){
	    return *ibuf;
	}
	pointer operator ->(){
	    return ibuf;
	}
	bool operator ==( const self_type &rhs) const{
	    return ibuf == rhs.ibuf;
	}
	bool operator !=( const self_type &rhs ) const{
	    return ibuf != rhs.ibuf;
	}
    };

    SetList()
	: head( nullptr ){}
    SetList( const sType s )
	: head( new ListNode<sType>(s, nullptr) ){}
    iterator begin(){
	return iterator(head);
    }
    iterator end(){
	return iterator(nullptr);
    }
    iterator insert( sType s ){
	head = new ListNode<sType>(s, head);
	return iterator(head);
    }
    iterator find( sType s ){
	for( ListNode<sType>* temp = head; temp != nullptr; temp = temp->next ){
	    if( temp->info == s )
		return iterator(temp);
	}
	return iterator(nullptr);
    }
    ~SetList(){
	ListNode<sType> :: deleteList(head);
    }
};
