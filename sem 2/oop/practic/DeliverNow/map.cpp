//
// Created by patri manciu on 26.06.2024.
//

// You may need to build the project (run Qt uic code generator) to get "ui_map.h" resolved

#include "map.h"
#include "ui_map.h"
#include <QPainter>

map::map(DataManager &dataManager, QWidget *parent) :
        QWidget(parent), ui(new Ui::map), dataManager(dataManager) {
    ui->setupUi(this);
    setWindowTitle("Map");
}

map::~map() {
    delete ui;
}

void map::paintEvent(QPaintEvent *event) {
    QPainter painter(this);
    painter.setPen(QPen(Qt::lightGray, 1, Qt::SolidLine));
    int gridSize = 10;

    for (int x = 0; x <= width(); x += gridSize) {
        painter.drawLine(x, 0, x, height());
    }

    // Draw horizontal lines
    for (int y = 0; y <= height(); y += gridSize) {
        painter.drawLine(0, y, width(), y);
    }

    for (auto& package : this->dataManager.getPackages()) {
        if (!package.getStatus()) { // Only display undelivered packages
            QPointF position(package.getX(), package.getY());
            painter.setBrush(Qt::blue); // Set the color for circles
            painter.drawEllipse(position, 10, 10); // Draw circle with radius 10
        }
    }
}