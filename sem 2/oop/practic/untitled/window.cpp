//
// Created by patri manciu on 26.06.2024.
//

// You may need to build the project (run Qt uic code generator) to get "ui_window.h" resolved

#include "window.h"
#include "ui_window.h"
#include <QMessageBox>
#include <QVBoxLayout>
#include <QTextEdit>

window::window(IdeaTableModel* model, Researcher& r, QWidget *parent) :
        model(model), researcher(r), QWidget(parent), ui(new Ui::window) {
    ui->setupUi(this);
    ui->setupUi(this);
    this->setWindowTitle(QString::fromStdString(researcher.getName()));
    this->ui->position->setText(QString::fromStdString(researcher.getPosition()));
    if (this->researcher.getPosition() != "senior"){
        this->ui->approveButton->hide();
    }
    this->ui->tableView->setModel(model);
    QObject::connect(this->ui->addButton,&QPushButton::clicked,this,&window::addIdea);
    QObject::connect(this->ui->approveButton,&QPushButton::clicked,this,&window::acceptIdea);
    QObject::connect(this->ui->developButton,&QPushButton::clicked,this,&window::develop);

}

void window::addIdea() {
    QString name = ui->nameLine->text();
    QString description = ui->descLine->text();
    QString res = QString::fromStdString(this->researcher.getName());
    int duration = ui->durationLine->text().toInt();
    Idea idea(name.toStdString(), description.toStdString(), "proposed", res.toStdString(), duration);
    this->model->addIdea(idea);
}

void window::acceptIdea() {
    int index = this->ui->tableView->currentIndex().row();
    try{
        model->reviseIdea(index);
    }catch(std::exception& e){
        QMessageBox::critical(this,"Error",e.what());
    }
}

window::~window() {
    delete ui;
}

void window::develop() {
    std::vector<Idea> ideas = model->acceptedIdeas(researcher);
    for (auto& idea : ideas) // Use const auto& to avoid copying ideas
    {
        QWidget* widget = new QWidget();
        QLayout* layout = new QVBoxLayout();
        QTextEdit* edit = new QTextEdit(QString::fromStdString(idea.getDescription()));
        edit->setObjectName("edit"); // Use a constant name for the QTextEdit
        layout->addWidget(edit);
        QPushButton* saveButton = new QPushButton("Save");
        layout->addWidget(saveButton);

        widget->setLayout(layout);
        widget->setObjectName(QString::fromStdString(idea.getName())); // Set the object's name to find it later
        widget->show();
    }
}
