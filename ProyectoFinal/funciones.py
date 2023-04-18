import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.ensemble import (RandomForestClassifier,
                              GradientBoostingClassifier,
                              GradientBoostingRegressor)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    roc_auc_score,
    mean_squared_error,
    confusion_matrix)


from sklearn.neighbors import KNeighborsClassifier
from sklearn.experimental import enable_halving_search_cv  # noqa

from sklearn.model_selection import (
    KFold,
    cross_validate,
    cross_val_score,
    train_test_split,
    GridSearchCV,
    RandomizedSearchCV,
    HalvingGridSearchCV,
    StratifiedKFold)

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
from sklearn.preprocessing import StandardScaler, RobustScaler
from scipy import stats
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import random
import subprocess

# DEFINICION DE FUNCIONES
def parejas(df):
    '''Obtiene diagonal inferior de parejas en matriz de correlacion'''
    pairs_to_drop = set()
    cols = df.columns
    for i in range(0, df.shape[1]):
        for j in range(0, i+1):
            pairs_to_drop.add((cols[i], cols[j]))
    return pairs_to_drop

def correlaciones(data, n=5,metodo='pearson'):
    au_corr = data.corr(method=metodo).abs().unstack()
    labels_to_drop = parejas(data)
    au_corr = au_corr.drop(labels=labels_to_drop).sort_values(ascending=False)
    return au_corr[0:n]

def hist_box(variable,agrupado):
    fig,axes = plt.subplots(2,1,figsize=(15,10),
                            sharex = True,
                            gridspec_kw={'height_ratios':[1,3]})
    sns.boxplot(ax = axes[0],
                data = bank_df,
                x = variable,
                y = agrupado
                )
    sns.histplot(ax = axes[1],
                 data  =bank_df,
                 x = variable,
                 hue = agrupado,
                 kde = True,
                 )
    if agrupado == None:
        plt.axvline(x=bank_df[variable].mean(),
                   color = "red",
                   linestyle = "--",
                   label = "mean")
        plt.axvline(x=bank_df[variable].median(),
                   color = "green",
                   linestyle = "--",
                   label = 'median')
        plt.legend(loc = 1)
        titulo = (f'HISTOGRAMA + BOXPLOT DE: {variable}')
    else:
        titulo = (f'HISTOGRAMA + BOXPLOT DE: {variable} SEGUN TARGET')
    plt.suptitle(titulo,fontsize=16,y = 0.9)
    axes[0].set(xlabel=None, ylabel=None)
    fig.set_facecolor('white')
    return(plt.show())

def graf_cat(variable):
    titulo = (f'Barras variables no numericas: {variable}')
    fig,axes = plt.subplots(1,2,figsize=(12,5),
                            sharex = True)
    sns.histplot(ax = axes[0],
                data = bank_df,
                x = variable
                )
    sns.histplot(ax = axes[1],
                 data  =bank_df,
                 x = variable,
                 hue = "Attrition_Flag",
                 multiple = 'fill'
                 )
    plt.suptitle(titulo,fontsize=16,y = 0.97)
#     ax.set(xlabel='common xlabel', ylabel='common ylabel')
    axes[0].set_title('Histograma')
    axes[0].set(xlabel=None, ylabel='count')
    axes[0].tick_params(axis='x', rotation=90)
    axes[1].set_title('Barras 100%')
    axes[1].set(xlabel=None, ylabel='%')
    axes[1].tick_params(axis='x', rotation=90)
    fig.set_facecolor('white')
    return(plt.show())

def mat_conf(y_test,y_pred):
  cf_matrix = confusion_matrix(y_test, y_pred)
  ax = sns.heatmap(cf_matrix, annot=True, cmap='Blues',fmt='.1f')
  ax.set_title('Matriz de confusion con labels\n\n');
  ax.set_xlabel('\nValores predichos')
  ax.set_ylabel('Valores reales ');
  ax.xaxis.set_ticklabels(['False','True'])
  ax.yaxis.set_ticklabels(['False','True'])
  return(plt.show())


# Funcion para devolver el train_score de cross_validate en un DataFrame.
# Con opcion de seleccionar todos los valores 'all', solo los de
# entrenamiento con 'train' o los de test con 'test'

def resultados_train_scores_cv(train_score, opcion='all'):
    df = pd.DataFrame(train_score).T
    df['mean'] = df.mean(axis=1)
    df['max'] = df.max(axis=1)
    df['min'] = df.min(axis=1)
    df['std'] = np.std(df, axis=1)

    if opcion == 'all':
        return (print(df.round(3)))
    if opcion == 'test':
        return (df.filter(regex='^test', axis=0).round(3))
    if opcion == 'train':
        return (df.filter(regex='^train', axis=0).round(3))

# CARGA DE DATOS

bank_df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSz3Yx52trZcGRODnR1-aMr8bTTKZDGsZbJj1kw5ms_H5ZOypBXNd2Hyx1bn1A8sznMTQOtCUniEnvJ/pub?output=csv")

# Quitamos columnas que sugieren en Kaggle
bank_df = bank_df.drop(columns=["CLIENTNUM","Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1","Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2"])

client_count = bank_df['Total_Trans_Amt'].groupby(bank_df['Attrition_Flag']).count()
plt.subplots(figsize = (7,9))
plt.title("CUSTOMER CHRUN RATE")
plt.pie(client_count,
        labels = [client_count.index[0] + "\n" + (str(round((client_count[0]/(client_count[1]+client_count[0]))*100,2))) + "%",
                  client_count.index[1]+ "\n" + (str(round((client_count[1]/(client_count[1]+client_count[0]))*100,2))) + "%"],
        colors = (sns.color_palette('pastel')[1],sns.color_palette('pastel')[0]),
        labeldistance=0.3)

plt.show()