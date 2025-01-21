//
// Created by patri manciu on 05.04.2024.
//

#include "ExtraTest.h"
#include <iostream>

void Test() {
    Stack s;
    s.push(3);
    s.push(1);
    assert(s.search(3) == true);
    assert(s.search(2) == false);
    std::cout << "Extra Tests passed.\n";
}
