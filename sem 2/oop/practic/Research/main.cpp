#include <QApplication>
#include <QPushButton>
#include "Data.h"
#include "seniorwindow.h"
#include "juniorwindow.h"

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);
    Data *data = new Data();
    for (auto res : data->getResearchers()) {
        if (res->getPosition() == "senior") {
            // senior window opened
            SeniorWindow *s = new SeniorWindow(data, res);
            s->show();
        } else {
            // junior window opened
            JuniorWindow *j = new JuniorWindow(data, res);
            j->show();
        }
    }

    return QApplication::exec();
}
