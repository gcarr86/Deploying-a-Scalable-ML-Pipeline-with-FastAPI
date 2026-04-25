import pytest
import numpy as np
from ml.model import compute_model_metrics, inference, train_model



# TODO: implement the first test. Change the function name and input as needed
# Test 1: compute_model_metrics returns valid numbers
def test_compute_model_metrics():
    """
    Test that compute_model_metrics returns precision, recall, and fbeta
    and that all values are >= 0.
    """
    y_true = np.array([0, 1, 1, 0])
    y_pred = np.array([0, 1, 0, 0])

    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)

    assert precision >= 0
    assert recall >= 0
    assert fbeta >= 0

    pass


# TODO: implement the second test. Change the function name and input as needed
# Test 2: train_model returns a fitted model that can predict
def test_train_model_and_inference():
    """
    Test that train_model trains a model and inference returns predictions.
    """
    X = np.array([[0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1])

    model = train_model(X, y)
    preds = inference(model, X)

    assert len(preds) == len(y)
    assert set(preds).issubset({0, 1})


# TODO: implement the third test. Change the function name and input as needed
def test_inference_shape():
    """
    Test that inference returns the correct number of predictions.
    """
    X = np.array([[1, 2], [3, 4], [5, 6]])
    y = np.array([0, 1, 0])

    model = train_model(X, y)
    preds = inference(model, X)

    assert preds.shape[0] == X.shape[0]


    pass
