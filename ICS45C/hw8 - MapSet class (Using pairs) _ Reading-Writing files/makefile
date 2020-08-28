CXXFLAGS=-std=c++11 -std=gnu++11 -Wpedantic -Wall -Wextra -Werror  -Wzero-as-null-pointer-constant -ggdb
CFLAGS=-std=c99 -pedantic -Wall -Wextra -Werror -ansi -Wwrite-strings
mapset:mapset.cpp
	g++ $(CXXFLAGS) mapset.cpp -o mapset
nums:process_numbers.cpp
	g++ $(CXXFLAGS) process_numbers.cpp -o nums

clean:
	/bin/rm mapset
	/bin/rm nums 
