#include <QApplication>
#include <QPushButton>
#include "Session.h"
#include "window.h"

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);
    Session s;
    for (auto u: s.getUsers()) {
        Window* w = new Window(u.getName(), u.getId(),s);
        w->show();
    }
    return QApplication::exec();
}
