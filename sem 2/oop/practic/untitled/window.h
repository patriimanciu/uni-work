//
// Created by patri manciu on 26.06.2024.
//

#ifndef RESEARCH2_WINDOW_H
#define RESEARCH2_WINDOW_H

#include <QWidget>
#include "IdeaTableModel.h"

QT_BEGIN_NAMESPACE
namespace Ui { class window; }
QT_END_NAMESPACE

class window : public QWidget {
Q_OBJECT

public:
    explicit window(IdeaTableModel* model, Researcher& r, QWidget *parent = nullptr);
    void addIdea();
    void acceptIdea();
    void develop();
    ~window() override;

private:
    Ui::window *ui;
    IdeaTableModel* model;
    Researcher& researcher;
};


#endif //RESEARCH2_WINDOW_H
