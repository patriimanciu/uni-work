//
// Created by patri manciu on 26.06.2024.
//

#ifndef RESEARCH_JUNIORWINDOW_H
#define RESEARCH_JUNIORWINDOW_H

#include <QWidget>
#include "seniorwindow.h"
#include "Data.h"


QT_BEGIN_NAMESPACE
namespace Ui { class JuniorWindow; }
QT_END_NAMESPACE

class JuniorWindow : public QWidget {
Q_OBJECT

public:
    explicit JuniorWindow(Data *data, Researcher *researcher, QWidget *parent = nullptr);
    void addIdea();
    ~JuniorWindow() override;

private:
    Ui::JuniorWindow *ui;
    Data *data;
    Researcher *researcher;
    ResearcherModel *model;
};


#endif //RESEARCH_JUNIORWINDOW_H
