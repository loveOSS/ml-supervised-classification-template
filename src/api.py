"""Basic REST API to expose the predictions of the ML app."""
import joblib
import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

import config

app = FastAPI()
model = joblib.load("{0}best_model.z".format(config.MODELS))


class Item(BaseModel):
    """The expected model from REST API request."""

    some_property: int


@app.post("/")
def predict(item: Item):
    """Return ML predictions, see /docs for more information.

    Args:
        item: (Item) the parsed data from user request

    Returns:
        A dictionnary with the predicted nutrigrade
        and the related probability
    """
    
    # @TODO: build the sample
    sample = {}
    
    prediction = model.predict([sample])[0]
    probability = model.predict_proba([sample]).argmax(1).item()

    return {"prediction": prediction, "probability": probability}


if __name__ == "__main__":
    uvicorn.run(
        "api:app",
        host=config.DOCKER_HOST,
        port=config.DOCKER_PORT,
        reload=True,
        debug=True,
        workers=3,
    )
