//
// Created by patri manciu on 26.06.2024.
//

#ifndef DELIVERNOW_MAP_H
#define DELIVERNOW_MAP_H

#include <QWidget>
#include "DataManager.h"


QT_BEGIN_NAMESPACE
namespace Ui { class map; }
QT_END_NAMESPACE

class map : public QWidget {
Q_OBJECT

public:
    explicit map(DataManager &dataManager, QWidget *parent = nullptr);
    void paintEvent(QPaintEvent *event) override;
    ~map() override;

private:
    Ui::map *ui;
    DataManager &dataManager;
};


#endif //DELIVERNOW_MAP_H
