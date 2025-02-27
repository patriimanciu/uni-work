//
// Created by patri manciu on 27.05.2024.
//

#ifndef SEARCH_ENGINE_GUI_H
#define SEARCH_ENGINE_GUI_H

#include <QWidget>
#include "service.h"

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
    void search();
    void best_matching();
};


#endif //SEARCH_ENGINE_GUI_H
