//
// Created by patri manciu on 26.06.2024.
//

#include "BacteriaTable.h"
#include "Bacterium.h"

int BacteriaTable::rowCount(const QModelIndex &parent) const {
    return this->service.getBacteria().size();
}

int BacteriaTable::columnCount(const QModelIndex &parent) const {
    return 4;
}

QVariant BacteriaTable::data(const QModelIndex &index, int role) const {
    int row = index.row();
    int column = index.column();
    Bacterium currentBacteria = this->service.getBacteria()[row];

    if (role == Qt::DisplayRole) {
        switch (column) {
            case 0:
                return QString::fromStdString(currentBacteria.getName());
            case 1:
                return QString::fromStdString(currentBacteria.getSpecies());
            case 2:
                return QString::fromStdString(std::to_string(currentBacteria.getSize()));
            case 3:
                return QString::fromStdString(currentBacteria.getDiseasesStr());
            default:
                break;
        }
    }
    return QVariant();
}

QVariant BacteriaTable::headerData(int section, Qt::Orientation orientation, int role) const {
    if (role == Qt::DisplayRole && orientation == Qt::Horizontal) {
        switch (section) {
            case 0:
                return "Name";
            case 1:
                return "Species";
            case 2:
                return "Size";
            case 3:
                return "Diseases";
            default:
                break;
        }
    }
    return QVariant();
}

