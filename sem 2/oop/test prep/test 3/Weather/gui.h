//
// Created by patri manciu on 28.05.2024.
//

#ifndef WEATHER_GUI_H
#define WEATHER_GUI_H

#include <QWidget>
#include "Service.h"

QT_BEGIN_NAMESPACE
namespace Ui { class GUI; }
QT_END_NAMESPACE

class GUI : public QWidget {
Q_OBJECT

public:
    explicit GUI(Service &serv, QWidget *parent = nullptr);

    ~GUI() override;

private:
    Ui::GUI *ui;
    Service service;
    void populate_list();
    void filter();
    void filterDescription();
};


#endif //WEATHER_GUI_H
