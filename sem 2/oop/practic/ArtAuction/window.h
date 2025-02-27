//
// Created by patri manciu on 26.06.2024.
//

#ifndef ARTAUCTION_WINDOW_H
#define ARTAUCTION_WINDOW_H

#include <QWidget>
#include "Observer.h"
#include "Session.h"

QT_BEGIN_NAMESPACE
namespace Ui { class Window; }
QT_END_NAMESPACE

class Window : public QWidget, public Observer {
Q_OBJECT

public:
    explicit Window(std::string name, int ID,Session &s, QWidget *parent = nullptr);
    void update() override;
    void populateItems();
    void populateCategory();
    void categorySelected();
    void populateOffers();
    void addItem();
    void bid();
    ~Window() override;

private:
    Ui::Window *ui;
    Session &session;
    std::string name;
    int ID;
    bool isCollector;
    void setIfCollector();
};


#endif //ARTAUCTION_WINDOW_H
