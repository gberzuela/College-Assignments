CXXFLAGS=-std=c++11 -Wpedantic -Wall -Wextra -Werror -Wzero-as-null-pointer-constant
CFLAGS=-std=c99 -pedantic -Wall -Wextra -Werror -ansi -Wwrite-strings

make: standard_main.cpp string_test.cpp String.cpp
	echo ----------Compiling test_string and String.cpp to create executable program main----------
	g++ String.cpp string_test.cpp -std=c++11 -o my_main
	g++ String.cpp standard_main.cpp -std=c++11 -o main
clean:
	echo ----------Removing executable program main----------
	/bin/rm my_main
	/bin/rm main
