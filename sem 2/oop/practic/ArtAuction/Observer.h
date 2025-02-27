//
// Created by patri manciu on 26.06.2024.
//

#ifndef ARTAUCTION_OBSERVER_H
#define ARTAUCTION_OBSERVER_H


class Observer {
public:
    Observer() {};
    virtual void update() = 0;
    virtual ~Observer() = default;
};


#endif //ARTAUCTION_OBSERVER_H
