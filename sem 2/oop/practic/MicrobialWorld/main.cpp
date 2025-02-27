#include <QApplication>
#include <QPushButton>
#include "Service.h"
#include "BacteriaTable.h"
#include "window.h"
#include <QSortFilterProxyModel>
#include <QRegularExpression>

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);
    Service s;
    BacteriaTable* model = new BacteriaTable{s};

    for (auto b : s.getBiologists()) {
        QSortFilterProxyModel* proxyModel = new QSortFilterProxyModel{};
        proxyModel->setSourceModel(model);
        proxyModel->setDynamicSortFilter(true);
        proxyModel->filterRegularExpression(QRegularExpression { "b.getName()", QRegularExpression::CaseInsensitiveOption, } );
        Window* w = new Window{model, b};
        w->show();
    }
    return QApplication::exec();
}
