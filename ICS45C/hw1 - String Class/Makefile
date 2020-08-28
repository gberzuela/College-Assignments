CXXFLAGS=-std=c++11 -Wpedantic -Wall -Wextra -Werror -Weffc++ -Wzero-as-null-pointer-constant
CFLAGS=-std=c99 -pedantic -Wall -Wextra -Werror -ansi -Wwrite-settings

main: string_test.cpp standard_main.cpp
	echo ------------compiling String.h to create executable program main------------
	g++ -ggdb -std=c++11 string_test.cpp -o test_main
	g++ -ggdb -std=c++11 standard_main.cpp -o main

clean:
	echo ------------removing executable program main------------
	/bin/rm test_main
	/bin/rm main
