#include "ExtraTest.h"
#include <assert.h>
#include "FixedCapBiMap.h"
#include "FixedCapBiMapIterator.h"
#include <utility>

void TestExtra() {
    FixedCapBiMap m(10);
    m.add(5,5);
    m.add(3,5);
    m.add(4,9);
    m.add(12,5);
    m.add(5,2);
    m.add(6,13);
    m.add(13,5);
    m.add(1,7);

    std::pair<TValue, TValue> res1 = m.removeKey(5);
    std::pair<TValue, TValue> ans1(5, 2);
    std::pair<TValue, TValue> res2 = m.removeKey(1);
    std::pair<TValue, TValue> ans2(7, NULL_TVALUE);
    std::pair<TValue, TValue> res3 = m.removeKey(2);
    std::pair<TValue, TValue> ans3(NULL_TVALUE, NULL_TVALUE);
    assert((res1 == ans1) || (res2 == ans2) || (res3 == ans3));
}