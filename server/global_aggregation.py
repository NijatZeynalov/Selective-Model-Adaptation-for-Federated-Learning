
def weighted_average(models, weights):
    """Compute a weighted average of model parameters.
    
    Args:
        models: List of model parameters.
        weights: List of weights for each model.
    
    Returns:
        Averaged model parameters.
    """
    averaged_model = {}
    for key in models[0].keys():
        averaged_model[key] = sum(model[key] * weight for model, weight in zip(models, weights)) / sum(weights)
    return averaged_model
