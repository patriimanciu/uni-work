#include <QApplication>
#include <QPushButton>
#include "gui.h"

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);
    Service service = Service();
    GUI g(service);
    g.show();
    return QApplication::exec();
}
