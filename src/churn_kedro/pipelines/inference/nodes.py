# Bibliotecas
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocessing_data(database_test, columns_to_drop):
    # Remove colunas que não serão utilizadas
    df_pre = database_test.drop(columns=columns_to_drop)

    return df_pre

def feature_engineering(df_pre, fe_ratio_list, fe_ratio, features_cont_list, new_features_cont_list):
    # Processamento das variáveis
    le = LabelEncoder()
    df_pre['Gender'] = le.fit_transform(df_pre['Gender']) 
    fe_data = pd.get_dummies(data=df_pre, columns=['Geography'])

    # Feature Engineering
    for fe_ratio_col in fe_ratio_list:
        fe_ratio_current = fe_ratio[fe_ratio_col]
        fe_data[fe_ratio_current[0]] = fe_data[fe_ratio_current[1]] / fe_data[fe_ratio_current[2]]

    # Acrescenta novas variáveis na lista
    for var_cont in new_features_cont_list:
        features_cont_list.append(var_cont)

    return fe_data

def prediction(rf_model, database_test, fe_data):
    # Realiza predição
    database_test['predictedValues'] = rf_model.predict(fe_data)

    # Saida no formato solicitado no Case
    predicted_data = database_test[['RowNumber', 'predictedValues']]
    
    return predicted_data
