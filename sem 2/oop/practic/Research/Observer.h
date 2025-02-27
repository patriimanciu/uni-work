#include <string>

class Observer {
public:
    Observer(){};
    virtual void update() = 0;
    virtual ~Observer() = default;

};