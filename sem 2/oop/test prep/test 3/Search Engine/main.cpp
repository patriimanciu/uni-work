#include <QApplication>
#include <QPushButton>
#include "gui.h"

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);
    Service service;
    GUI gui(service);
    gui.show();
    return a.exec();
}
