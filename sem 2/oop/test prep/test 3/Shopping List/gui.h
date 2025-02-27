//
// Created by patri manciu on 28.05.2024.
//

#ifndef SHOPPING_LIST_GUI_H
#define SHOPPING_LIST_GUI_H

#include <QWidget>
#include "Service.h"


QT_BEGIN_NAMESPACE
namespace Ui { class GUI; }
QT_END_NAMESPACE

class GUI : public QWidget {
Q_OBJECT

public:
    explicit GUI(Service &service, QWidget *parent = nullptr);

    ~GUI() override;

private:
    Ui::GUI *ui;
    Service service;
    void populate_list();
    void search_bar();
    void filter();
};


#endif //SHOPPING_LIST_GUI_H
