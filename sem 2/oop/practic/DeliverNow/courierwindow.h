//
// Created by patri manciu on 25.06.2024.
//

#ifndef DELIVERNOW_COURIERWINDOW_H
#define DELIVERNOW_COURIERWINDOW_H

#include <QWidget>
#include <QListWidgetItem>
#include "DataManager.h"

QT_BEGIN_NAMESPACE
namespace Ui { class CourierWindow; }
QT_END_NAMESPACE

class CourierWindow : public QWidget {
Q_OBJECT

public:
    explicit CourierWindow(Courier &courier, DataManager& dataManager, QWidget *parent = nullptr);
    void populateDeliveries();
    void populateByStreet(QListWidgetItem *item);
    void populateStreets();
    void deliverPackage();
    ~CourierWindow() override;

private:
    Ui::CourierWindow *ui;
    Courier &courier;
    DataManager& dataManager;
    bool assigned(Package package);
};


#endif //DELIVERNOW_COURIERWINDOW_H
