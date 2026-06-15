from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Annotated, Literal
import joblib
import pandas as pd

app = FastAPI()
try:
    with open('models/model.pkl', 'rb') as f:
        model = joblib.load(f)
    with open('models/scaler.pkl', 'rb') as f:
        scaler = joblib.load(f)
except FileNotFoundError:
    raise HTTPException(status_code=500, detail="Model or scaler file not found")

class Input(BaseModel):
    latitude: Annotated[float, Field(..., description="Latitude of the listing")]
    longitude: Annotated[float, Field(..., description="Longitude of the listing")]
    accommodates: Annotated[int, Field(..., description="Number of guests the listing can accommodate")]
    bedrooms: Annotated[int, Field(..., description="Number of bedrooms in the listing")]
    beds: Annotated[int, Field(..., description="Number of beds in the listing")]
    minimum_nights: Annotated[int, Field(..., description="Minimum number of nights for a booking")]
    availability_365: Annotated[int, Field(..., description="Number of days the listing is available in a year")]
    room_type: Annotated[Literal["Entire home/apt", "Private room", "Shared room"], Field(..., description="Type of room (e.g., entire home/apt, private room, shared room)")]
    bathrooms: Annotated[float, Field(..., description="Number of bathrooms in the listing")]
    is_shared_bath: Annotated[bool, Field(..., description="Indicates if the bathroom is shared (True) or private (False)")]

@app.post('/predict')
def predict(data: Input):
    input_df = pd.DataFrame([data.dict()])

    cols_to_scale = ['accommodates', 'bedrooms', 'beds', 'bathrooms', 'minimum_nights', 'availability_365', 'latitude', 'longitude']
    input_df[cols_to_scale] = scaler.transform(input_df[cols_to_scale])

    input_df['is_shared_bath'] = input_df['is_shared_bath'].astype(int)

    input_df['room_type_Private room'] = 1 if data.room_type == "Private room" else 0
    input_df['room_type_Shared room'] = 1 if data.room_type == "Shared room" else 0

    input_df = input_df.drop(columns=['room_type'])

    expected_columns = model.feature_names_in_
    input_df = input_df.reindex(columns=expected_columns, fill_value=0)

    try:
        predict = model.predict(input_df)
        return {"Predicted Price": round(float(predict[0]), 2)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction Failed: {str(e)}")