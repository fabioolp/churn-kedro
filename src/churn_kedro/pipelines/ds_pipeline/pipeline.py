from kedro.pipeline import Pipeline, node

from .nodes import ds_preprocessing_data, ds_feature_engineering, model_training

def create_pipeline(**kwargs):
    """
    Uma função para criar um pipeline Kedro
    
    Params: None
    Return: Um objeto Pipeline com uma lista de nós
    """
    return Pipeline(
        [
            node(
                func=ds_preprocessing_data,
                inputs=["database_train", "params:columns_to_drop"],
                outputs=["X", "y"],
                name="ds_preprocessing_data",
            ),
            node(
                func=ds_feature_engineering,
                inputs=["X", "params:fe_ratio_list", "params:fe_ratio", "params:features_cont_list",
                        "params:new_features_cont_list"],
                outputs="ds_fe_data",
                name="ds_feature_engineering",
            ),
            node(
                func=model_training,
                inputs=["ds_fe_data", "y", "params:rf_parameters"],
                outputs="rf_model",
                name="model_training",
            )
        ]
    )