#include <stdio.h>
#include <stdlib.h>

#define ORANGE "\e[0;33m"
#define END "\e[0m"

int main () {

	printf ("%sHello my own programm :)!%s\n", ORANGE, END);
	return EXIT_SUCCESS;
}
