#include <iostream>

int main(){
	
	int a;
	int b;
	
	a = 56;
	b = 456;
	
	do {
		a = a + b;
	}
	while ( a < 5000 );
	
	std::cout << a << "\n";
	
}
