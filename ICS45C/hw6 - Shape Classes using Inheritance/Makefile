CXXFLAGS=-std=c++11 -std=gnu+11 -Wpedantic -Wall -Wextra -Wzero-as-null-pointer-constant

main: standard_main.cpp Shape.h Triangle.h Rectangle.h
	echo ----------compiling main.cpp, Picture.h Shape.h, Rectangle.h, Square.h, Circle.h, and Triangle.h to create executable program main----------
	g++ -ggdb -std=c++11 standard_main.cpp Shape.h Rectangle.h Square.h Circle.h Triangle.h -o standard_main
	g++ -ggdb -std=c++11 main.cpp Picture.h Shape.h Rectangle.h Square.h Circle.h Triangle.h -o main

clean:
	echo ----------removing executable program main----------
	/bin/rm standard_main
	/bin/rm main
