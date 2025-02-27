//
// Created by patri manciu on 26.06.2024.
//

#include "IdeaTableModel.h"

IdeaTableModel::IdeaTableModel(Service& serv, QObject *parent) : service(serv), QAbstractTableModel(parent) {
}

int IdeaTableModel::rowCount(const QModelIndex &parent) const {
    return service.getIdeas().size();
}

QVariant IdeaTableModel::data(const QModelIndex &index, int role) const {
    if (role == Qt::DisplayRole) {
        if (index.column() == 0) {
            return QString::fromStdString(service.getIdeas()[index.row()].getName());
        }
        if (index.column() == 1) {
            return QString::fromStdString(service.getIdeas()[index.row()].getDescription());
        }
        if (index.column() == 3) {
            return QString::fromStdString(service.getIdeas()[index.row()].getResearcher());
        }
        if (index.column() == 4) {
            return QString::number(service.getIdeas()[index.row()].getDuration());
        }
        if (index.column() == 2) {
            return QString::fromStdString(service.getIdeas()[index.row()].getStatus());
        }
    }
    return QVariant();
}

QVariant IdeaTableModel::headerData(int section, Qt::Orientation orientation, int role) const {
    if (role == Qt::DisplayRole && orientation == Qt::Horizontal) {
        switch (section) {
            case 0: return "Title";
            case 1: return "Description";
            case 2: return "Status";
            case 3: return "Researcher";
            case 4: return "Duration";
        }
    }
    return QVariant();
}

void IdeaTableModel::addIdea(Idea &idea) {
    this->beginInsertRows(QModelIndex(), this->rowCount(), this->rowCount());
    this->service.addIdea(idea);
    this->endInsertRows();
}

void IdeaTableModel::reviseIdea(int indexOfIdea) {
    this->service.acceptIdea(indexOfIdea);
    QModelIndex topLeft = this->index(indexOfIdea, 0);
    QModelIndex bottomRight = this->index(indexOfIdea, 4);
    emit dataChanged(topLeft, bottomRight);
}

void IdeaTableModel::setDescription(int indexOfIdea, std::string description) {
    this->service.setDescription(indexOfIdea, description);
    QModelIndex topLeft = this->index(indexOfIdea, 1);
    QModelIndex bottomRight = this->index(indexOfIdea, 1);
    emit dataChanged(topLeft, bottomRight);

}
