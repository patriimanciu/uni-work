//
// Created by patri manciu on 26.06.2024.
//

#ifndef MICROBIALWORLD_BACTERIATABLE_H
#define MICROBIALWORLD_BACTERIATABLE_H
#include <QAbstractTableModel>
#include "Service.h"
#include <QSortFilterProxyModel>


class BacteriaTable : public QAbstractTableModel {
private:
    std::vector<Bacterium> bacteria;
public:
    Service& service;
    BacteriaTable(Service& service, QObject *parent = nullptr): service{service}{};
    int rowCount(const QModelIndex &parent = QModelIndex()) const override;
    int columnCount(const QModelIndex &parent = QModelIndex()) const override;
    QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const override;
    QVariant headerData(int section, Qt::Orientation orientation, int role) const override;
    void setBacteria(const std::vector<Bacterium>& newBacteria);
    ~BacteriaTable() override = default;
};


#endif //MICROBIALWORLD_BACTERIATABLE_H
