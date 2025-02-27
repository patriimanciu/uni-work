//
// Created by patri manciu on 25.06.2024.
//

// You may need to build the project (run Qt uic code generator) to get "ui_CourierWindow.h" resolved

#include "courierwindow.h"
#include "ui_CourierWindow.h"


CourierWindow::CourierWindow(Courier &courier, DataManager& dataManager, QWidget *parent) :
        QWidget(parent), ui(new Ui::CourierWindow), courier(courier), dataManager(dataManager){
    ui->setupUi(this);
    setWindowTitle(QString::fromStdString(courier.getName()));
    this->populateDeliveries();
    this->ui->zoneLabel->setText(QString::fromStdString(courier.getZone()));
    QObject::connect(ui->deliverButton, &QPushButton::clicked, this, &CourierWindow::deliverPackage);
}

CourierWindow::~CourierWindow() {
    delete ui;
}

void CourierWindow::populateDeliveries() {
    ui->deliveriesList->clear();
    for (auto& delivery : this->dataManager.getPackages()) {
        if (!delivery.getStatus() && this->assigned(delivery)){
            QListWidgetItem *item = new QListWidgetItem(QString::fromStdString(delivery.toString()));
            ui->deliveriesList->addItem(item);
        }
    }
}

bool CourierWindow::assigned(Package package) {
    for (auto& street: this->courier.getStreets()) {
        if (package.getStreet() == street) {
            return true;
        }
    }
    return false;
}

void CourierWindow::populateByStreet(QListWidgetItem *item) {
    ui->deliveriesList->clear();
    QListWidgetItem* sel = ui->streetsListWidget->currentItem();
    QString selectedStreet = sel->text();
    for (auto &delivery : this->dataManager.getPackages()) {
//        if (!delivery.getStatus() && this->assigned(delivery) &&
//            QString::fromStdString(delivery.getStreet()) == selectedStreet) {
         if (!delivery.getStatus() && this->assigned(delivery)) {
            std::cout << delivery.getStreet() << std::endl;
            QListWidgetItem *newItem = new QListWidgetItem(QString::fromStdString(delivery.toString()));
            ui->deliveriesList->addItem(newItem);
        }
    }
}

void CourierWindow::populateStreets() {
    ui->streetsListWidget->clear();
    for (auto& street : this->courier.getStreets()) {
        ui->streetsListWidget->addItem(QString::fromStdString(street));
    }
}

void CourierWindow::deliverPackage() {
    QListWidgetItem* sel = ui->deliveriesList->currentItem();
    std::string selectedDelivery = sel->text().toStdString();
    for (auto& delivery : this->dataManager.getPackages()) {
        if (delivery.toString() == selectedDelivery) {
            delivery.setStatus(true);
            this ->dataManager.updatePackage(delivery);
            this->populateDeliveries();
            return;
        }
    }
}
