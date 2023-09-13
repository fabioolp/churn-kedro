import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split 
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score
)

def ds_preprocessing_data(abandono_clientes, columns_to_drop):
    # Remove colunas que não serão utilizadas
    df1 = abandono_clientes.drop(columns=columns_to_drop)

    # Separando as variaveis independentes e dependentes
    y = df1['Exited']
    X = df1.copy()
    X = df1.drop(columns='Exited')

    return X, y

def ds_feature_engineering(X, fe_ratio_list, fe_ratio, features_cont_list, new_features_cont_list):
    # Processamento das variáveis
    le = LabelEncoder()
    X['Gender'] = le.fit_transform(X['Gender'])
    ds_fe_data = pd.get_dummies(data=X, columns=['Geography'])

    # Feature Engineering
    for fe_ratio_col in fe_ratio_list:
        fe_ratio_current = fe_ratio[fe_ratio_col]
        ds_fe_data[fe_ratio_current[0]] = ds_fe_data[fe_ratio_current[1]] / ds_fe_data[fe_ratio_current[2]]

    # Acrescenta novas variáveis na lista
    for var_cont in new_features_cont_list:
        features_cont_list.append(var_cont)

    return ds_fe_data

def model_training(ds_fe_data, y, rf_parameters):
    # Separação dos dados de treino e teste
    test_size = 0.3
    x_train, x_test, y_train, y_test = train_test_split(ds_fe_data, y, test_size = test_size, random_state = 42)

    # Instancia modelo e treina
    rf_model = RandomForestClassifier(**rf_parameters)
    rf_model.fit(x_train, y_train)

    # Realiza predição
    y_pred_rf = rf_model.predict(x_test)

    # Calcula métricas
    accuracy = accuracy_score(y_test, y_pred_rf)
    print("Acurácia: ", round(accuracy, 2))

    precision = precision_score(y_test, y_pred_rf)
    print("Precision:", round(precision, 2))

    recall = recall_score(y_test, y_pred_rf)
    print("Recall:   ", round(recall, 2))

    return rf_model