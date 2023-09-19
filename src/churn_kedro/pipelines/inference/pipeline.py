from kedro.pipeline import Pipeline, node

from .nodes import preprocessing_data, feature_engineering, prediction

def create_pipeline(**kwargs):
    """
    Uma função para criar um pipeline Kedro
    
    Params: None
    Return: Um objeto Pipeline com uma lista de nós
    """
    return Pipeline(
        [
            node(
                func=preprocessing_data,
                inputs=["database_test", "params:columns_to_drop"],
                outputs="df_pre",
                name="preprocessing_data",
            ), 
            node(
                func=feature_engineering,
                inputs=["df_pre", "params:fe_ratio_list", "params:fe_ratio", "params:features_cont_list", "params:new_features_cont_list"],
                outputs="fe_data",
                name="feature_engineering",
            ), 
            node(
                func=prediction,
                inputs=["rf_model", "database_test", "fe_data"],
                outputs="predicted_data",
                name="prediction_node",
            ),
        ]
    )