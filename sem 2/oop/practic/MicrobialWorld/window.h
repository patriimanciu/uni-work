//
// Created by patri manciu on 26.06.2024.
//

#ifndef MICROBIALWORLD_WINDOW_H
#define MICROBIALWORLD_WINDOW_H

#include <QWidget>
#include "BacteriaTable.h"


QT_BEGIN_NAMESPACE
namespace Ui { class Window; }
QT_END_NAMESPACE

class Window : public QWidget {
Q_OBJECT

public:
    explicit Window(QAbstractItemModel* proxyModel, Biologist b, QWidget *parent = nullptr);
    void combo(const QString& species);
    ~Window() override;

private:
    Ui::Window *ui;
    QAbstractItemModel* model;
};


#endif //MICROBIALWORLD_WINDOW_H
