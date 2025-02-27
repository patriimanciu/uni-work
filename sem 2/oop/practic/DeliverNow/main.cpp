#include <QApplication>
#include <QPushButton>
#include "mainwindow.h"
#include "DataManager.h"

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);
    DataManager dataManager;
    MainWindow w = MainWindow(dataManager);
    w.show();
    return QApplication::exec();
}
