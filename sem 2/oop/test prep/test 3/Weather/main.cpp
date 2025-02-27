#include <QApplication>
#include <QPushButton>
#include "Service.h"
#include "GUI.h"

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);
    Service serv = Service();
    GUI gui(serv);
    gui.show();
    return QApplication::exec();
}
