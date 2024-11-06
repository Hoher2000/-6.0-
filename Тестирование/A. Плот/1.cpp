#include <iostream>

int main(){
	int x1, y1, x2, y2, x, y;
	std::cin >> x1 >> y1 >> x2 >> y2 >> x >> y;
	if (x1 <= x && 	x <= x2){
		std::cout << (std::abs(y - y1) < std::abs(y - y2)? "S" : "N");
    	return 0;
    }
	if (y1 <= y && y <= y2){
		std::cout << (std::abs(x - x1) < std::abs(x - x2)? "W" : "E");
    	return 0;
    }
	if (x < x1){
	std::cout << (y < y1 ? "SW" : "NW");
	return 0;
}
    std::cout << (y < y1 ? "SE" : "NE");
	return 0;
}
