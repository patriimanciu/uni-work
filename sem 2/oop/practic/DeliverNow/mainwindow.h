//
// Created by patri manciu on 25.06.2024.
//

#ifndef DELIVERNOW_MAINWINDOW_H
#define DELIVERNOW_MAINWINDOW_H

#include <QWidget>
#pragma once
#include "DataManager.h"
#include "CourierWindow.h"


QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QWidget {
Q_OBJECT

public:
    explicit MainWindow(DataManager& dataManager, QWidget *parent = nullptr);
    void populateCouriers();
    void populatePackages();
    void addCourier();
    void addNewPackage();
    ~MainWindow() override;

private:
    Ui::MainWindow *ui;
    DataManager &dataManager;
    std::vector<CourierWindow *> courierWindows = {};

    void showMap();
};


#endif //DELIVERNOW_MAINWINDOW_H
