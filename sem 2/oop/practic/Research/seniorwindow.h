//
// Created by patri manciu on 26.06.2024.
//

#ifndef RESEARCH_SENIORWINDOW_H
#define RESEARCH_SENIORWINDOW_H

#include <QWidget>
#include <QAbstractTableModel>
#include "Data.h"
#include "Observer.h"

class ResearcherModel : public QAbstractTableModel {
Q_OBJECT
private:
    Researcher *researcher;
    Data* dataList;

public:
    ResearcherModel(Data* data, Researcher *researcher, QObject *parent = nullptr);
    int rowCount(const QModelIndex &parent = QModelIndex()) const override;
    int columnCount(const QModelIndex &parent = QModelIndex()) const override { return 5; }
    QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const override;
    QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override;
    void addIdea(Idea *idea);
    void update();
};


QT_BEGIN_NAMESPACE
namespace Ui { class SeniorWindow; }
QT_END_NAMESPACE

class SeniorWindow : public QWidget {
Q_OBJECT

public:
    explicit SeniorWindow(Data *data, Researcher *researcher, QWidget *parent = nullptr);
    void addIdea();
    void acceptIdea();
    ~SeniorWindow() override;

private:
    Ui::SeniorWindow *ui;
    Data *data;
    Researcher *researcher;
    ResearcherModel *model;
};

#endif //RESEARCH_SENIORWINDOW_H
