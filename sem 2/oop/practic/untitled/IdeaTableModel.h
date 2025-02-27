//
// Created by patri manciu on 26.06.2024.
//

#ifndef RESEARCH2_IDEATABLEMODEL_H
#define RESEARCH2_IDEATABLEMODEL_H
#include <QAbstractTableModel>
#include "Service.h"
#include "Idea.h"

class IdeaTableModel : public QAbstractTableModel {
    Q_OBJECT
private:
    Service& service;

public:
    IdeaTableModel(Service& serv, QObject *parent = nullptr);
    int rowCount(const QModelIndex &parent = QModelIndex()) const override;
    int columnCount(const QModelIndex &parent = QModelIndex()) const override { return 5; }
    QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const override;
    QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override;
    void addIdea(Idea &idea);
    void reviseIdea(int indexOfIdea);
    void setDescription(int indexOfIdea, std::string description);
    std::vector<Idea> acceptedIdeas(Researcher researcher) { return this->service.getAcceptedIdeas(researcher.getName()); }
};


#endif //RESEARCH2_IDEATABLEMODEL_H
