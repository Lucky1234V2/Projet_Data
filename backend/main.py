import io

import numpy as np
from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from tensorflow.keras.models import load_model

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autorise toutes les origines
    allow_credentials=True,
    allow_methods=["*"],  # Autorise toutes les méthodes
    allow_headers=["*"],  # Autorise tous les headers
)

# Charger le modèle
model = load_model("models/mnist_model.keras")


@app.post("/predict/")
async def predict_digit(file: UploadFile = UploadFile(...)):
    try:
        # Convertir l'image en format compatible
        image = Image.open(io.BytesIO(await file.read())).convert("L")
        image = image.resize((28, 28))

        # Inverser les couleurs
        image = Image.fromarray(255 - np.array(image))

        image_arr = np.array(image) / 255.0
        image_arr = image_arr.reshape(1, 28, 28, 1)

        # Prédiction
        prediction = model.predict(image_arr)
        predicted_label = np.argmax(prediction)

        return {"prediction": int(predicted_label)}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/")
async def root():
    return {"message": "Hello World"}
    # return render_template("index.html")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
