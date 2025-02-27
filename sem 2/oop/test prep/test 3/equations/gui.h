//
// Created by patri manciu on 24.05.2024.
//

#ifndef EQUATIONS_GUI_H
#define EQUATIONS_GUI_H

#pragma once
#include <QApplication>
#include <QWidget>
#include "service.h"


QT_BEGIN_NAMESPACE
namespace Ui { class gui; }
QT_END_NAMESPACE

class gui : public QWidget {
Q_OBJECT

public:
    explicit gui(Service& serv, QWidget *parent = nullptr);

    ~gui() override;

private:
    Ui::gui *ui;
    Service service;
    void populate_list();
    void listItemClickedHandler();
    void update();
    void solution();
};


#endif //EQUATIONS_GUI_H
