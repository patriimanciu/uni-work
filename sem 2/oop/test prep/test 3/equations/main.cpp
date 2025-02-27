#include <QApplication>
#include "gui.h"

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);
    Service service = Service();
    gui g(service);
    g.show();
    return a.exec();

}
