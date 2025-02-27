#include <QApplication>
#include <QPushButton>
#include "Service.h"
#include "IdeaTableModel.h"
#include "window.h"

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);
    Service s;
    IdeaTableModel tm(s);
    for (auto res : s.getResearchers()) {
        window* rw = new window(&tm, res);
        rw->show();
    }
    return QApplication::exec();
}
