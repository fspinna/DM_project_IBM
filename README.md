# DM_project_IBM

Preprocessing, clustering and sequential pattern mining della serie storica delle azioni IBM (open prices).


#### PREPROCESSING:
Data visualization e creazione delle matrici di distanza per DTW e CDM, creazione dei vettori feature-based.

#### CLUSTERING: 
La serie è stata divisa in sottoserie annuali, per le quali è stato effettuato il clustering attraverso gli algoritmi DBSCAN e Hierarchical utilizzando DTW e CDM come misure di distanza. Infine è stato applicato K-Means su vettori feature-based. I risultati migliori sono stati ottenuti con DTW.

#### SEQUENTIAL PATTERN MINING:
La serie è stata divisa in sottoserie mensili, che sono state discretizzate e formattate per poter essere importate all'interno del tool java SPMF. Attraverso l'algoritmo SPAM di SPMF si sono trovati i sequential pattern, che sono stati reimportati in Jupyter Notebook.
