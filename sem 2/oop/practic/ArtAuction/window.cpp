//
// Created by patri manciu on 26.06.2024.
//

// You may need to build the project (run Qt uic code generator) to get "ui_Window.h" resolved

#include "window.h"
#include "ui_Window.h"

#include <QMessageBox>
#include <QDate>

Window::Window(std::string name, int ID, Session& s, QWidget *parent) :
        QWidget(parent), ui(new Ui::Window), session{s}, name{name}, ID{ID} {
    ui->setupUi(this);
    this->setWindowTitle(QString::fromStdString(this->name));
    session.registerObserver(this);
    this->isCollector = false;
    this->setIfCollector();
    if (this->isCollector) {
        ui->addButton->hide();
        ui->nameLine->hide();
        ui->priceLine->hide();
        ui->categoryLine->hide();
    }
    this->populateItems();
    this->populateCategory();
    QObject::connect(ui->categoryComboBox, &QComboBox::currentTextChanged, this, &Window::categorySelected);
    QObject::connect(ui->addButton, &QPushButton::clicked, this, &Window::addItem);
    QObject::connect(ui->itemsList, &QListWidget::itemSelectionChanged, this, &Window::populateOffers);
    QObject::connect(ui->bidButton, &QPushButton::clicked, this, &Window::bid);
}

void Window::setIfCollector() {
    this->ui->collectorLabel->setText(QString ::fromStdString("NOT"));
    for (auto &user : this->session.getUsers()) {
        if (user.getName() == this->name && user.getType() == "collector") {
            this->isCollector = true;
            this->ui->collectorLabel->setText(QString::fromStdString("Collector"));
            break;
        }
    }
}

Window::~Window() {
    this->session.save();
    delete ui;
}

void Window::populateItems() {
    this->ui->itemsList->clear();
    for (int i = 0; i < this->session.getItems().size(); ++i) {
        for (int j = i + 1; j < this->session.getItems().size(); ++j) {
            if (this->session.getItems()[i].getCurrentPrice() < this->session.getItems()[j].getCurrentPrice()) {
                Item aux = this->session.getItems()[i];
                this->session.getItems()[i] = this->session.getItems()[j];
                this->session.getItems()[j] = aux;
            }
        }
    }
    for (auto &item: this->session.getItems())  {
        QListWidgetItem* it = new QListWidgetItem(QString::fromStdString(item.itemToString()));
        ui->itemsList->addItem(it);
    }
}

void Window::populateCategory() {
    this->ui->categoryComboBox->clear();
    this->ui->categoryComboBox->addItem(QString::fromStdString("All"));
    for (auto &category : this->session.getCategories()) {
        this->ui->categoryComboBox->addItem(QString::fromStdString(category));
    }
    this->ui->categoryComboBox->setCurrentText("All");
}

void Window::categorySelected() {
    std::string cat = this->ui->categoryComboBox->currentText().toStdString();
    this->ui->itemsList->clear();
    if (cat == "All") {
        this->populateItems();
        return;
    }
    for (auto &item : this->session.getItems()) {
        if (item.getCategory() == cat) {
            QListWidgetItem* it = new QListWidgetItem(QString::fromStdString(item.itemToString()));
            ui->itemsList->addItem(it);
        }
    }
}

void Window::update() {
    std::cout << "update " << this->name << std::endl;
    this->populateItems();
}

void Window::addItem() {
    if (this->isCollector) {
        QMessageBox::critical(this, "Error", "You are not admin");
        return;
    }
    std::string name = this->ui->nameLine->text().toStdString();
    std::string category = this->ui->categoryLine->text().toStdString();
    int price = this->ui->priceLine->text().toInt();
    if (name.empty() || category.empty() || price <= 0) {
        QMessageBox::critical(this, "Error", "Invalid data");
        return;
    }
    Item i{name, category, price};
    this->session.addItem(i);
}

void Window::populateOffers() {
    this->ui->offersList->clear();
    std::string selected = this->ui->itemsList->currentItem()->text().toStdString();
    for (auto &item : this->session.getItems()) {
        if (item.itemToString() == selected) {
            for (auto &offer : item.getOffersListString()) {
                QListWidgetItem* it = new QListWidgetItem(QString::fromStdString(offer));
                this->ui->offersList->addItem(it);
            }
            break;
        }
    }
}

void Window::bid() {
    if (!this->isCollector) {
        QMessageBox::critical(this, "Error", "You are not collector");
        return;
    }
    std::string selected = this->ui->itemsList->currentItem()->text().toStdString();
    for (auto &item : this->session.getItems()) {
        if (item.itemToString() == selected) {
            int price = this->ui->bidLine->text().toInt();
            if (price <= item.getCurrentPrice()) {
                QMessageBox::critical(this, "Error", "Invalid price");
                return;
            }
            QDate date = QDate::currentDate();
            Offer o{this->ID, date.day(), date.month(), date.year(), price};
            item.addOffer(o);
            this->session.updateItem(item);
            return;
        }
    }
}

