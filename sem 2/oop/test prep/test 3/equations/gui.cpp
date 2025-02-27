//
// Created by patri manciu on 24.05.2024.
//

// You may need to build the project (run Qt uic code generator) to get "ui_gui.h" resolved

#include "gui.h"
#include "ui_gui.h"
#include <QFont>


gui::gui(Service& serv, QWidget *parent) :
        QWidget(parent), ui(new Ui::gui) {
    this->service = serv;
    ui->setupUi(this);
    this->populate_list();

    QObject::connect(ui->equationsList, &QListWidget::itemClicked, this, &gui::listItemClickedHandler);
    QObject::connect(ui->updateButton, &QPushButton::clicked, this, &gui::update);
    QObject::connect(ui->solutionButton, &QPushButton::clicked, this, &gui::solution);
}

gui::~gui() {
    delete ui;
}

void gui::populate_list() {
    ui->equationsList->clear();
    for (auto eq : this->service.getAllEq()) {
        QString eqString = QString::fromStdString(eq.to_string());
        QListWidgetItem* item = new QListWidgetItem(eqString);
        if (eq.real_solutions()) {
            QFont font = item->font();
            font.setBold(true);
            item->setFont(font);
        }
        ui->equationsList->addItem(item);
    }
}

void gui::listItemClickedHandler() {
    int row = this->ui->equationsList->currentRow();
    Equations e = this->service.getAllEq()[row];
    this->ui->lineEditA->setText(QString::fromStdString(std::to_string(e.getA())));
    this->ui->lineEditB->setText(QString::fromStdString(std::to_string(e.getB())));
    this->ui->lineEditC->setText(QString::fromStdString(std::to_string(e.getC())));

}
void gui::update() {
    int row = this->ui->equationsList->currentRow();

    bool okA, okB, okC;
    int a = this->ui->lineEditA->text().toInt(&okA);
    int b = this->ui->lineEditB->text().toInt(&okB);
    int c = this->ui->lineEditC->text().toInt(&okC);

    if (!okA || !okB || !okC) {
        qDebug() << "One or more conversions failed";
        return;
    }

    Equations e = Equations(a, b, c);

    this->service.updateEquations(row, e);

    this->populate_list();
}

void gui::solution() {
    int row = this->ui->equationsList->currentRow();
    Equations e = this->service.getAllEq()[row];
    this->ui->solutionsLine->setText(QString::fromStdString(e.sol()));
}