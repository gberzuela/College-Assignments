CXXFLAGS=-std=c++11 -Wpedantic -Wall -Wextra -Werror -Wzero-as-null-pointer-constant
CFLAGS=-std=c99 -pedantic -Wall -Wextra -Werror -ansi -Wwrite-strings

main: String.cpp test_main.cpp standard_main.cpp
	echo --------compiling String.cpp, standard_main, and test_main.cpp to create executables------
	g++ -std=c++11 String.cpp test_main.cpp -o main
	g++ -std=c++11 String.cpp standard_main.cpp -o stand_main

clean:
	echo ------Removing executables------
	/bin/rm main
	/bin/rm stand_main
