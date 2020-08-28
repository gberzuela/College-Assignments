CXXFLAGS=-std=c++11 -Wpedantic -Wall -Wextra -Werr -Weffc++ -Wzero-as-null-pointer-constant
CFLAGS=-std=c99 -pedantic -Wall -Wextra -Werror -ansi -Wwrite-string

main: coins_main.cpp coins_menu.cpp
	echo ------------compiling coins_main.cpp and coins_menu.cpp to create executable programs------------
	g++ -ggdb -std=c++11 coins_main.cpp -o coins_main
	g++ -ggdb -std=c++11 coins_menu.cpp -o coins_menu

clean:
	echo ------------removing executable program main------------
	/bin/rm coins_main
	/bin/rm coins_menu
