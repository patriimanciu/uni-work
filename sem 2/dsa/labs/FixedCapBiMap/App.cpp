#include "ExtendedTest.h"
#include "ShortTest.h"
#include "ExtraTest.h"
#include "FixedCapBiMap.h"


#include <iostream>
using namespace std;


int main() {
	testAll();
	testAllExtended();
	TestExtra();
	cout << "That's all!" << endl;
	// system("pause");
	return 0;
}


