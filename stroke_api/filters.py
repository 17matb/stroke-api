from typing import Literal, Annotated
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, TypeAdapter

app = FastAPI()

# Chargement des données (une fois)
stroke_data: pd.DataFrame = pd.read_parquet('./data/data.parquet')


class Patient(BaseModel):
    id: int
    gender: str
    age: float
    hypertension: int
    heart_disease: int
    ever_married: str
    work_type: str
    residence_type: str
    avg_glucose_level: float
    bmi: float
    smoking_status: str
    stroke: int


@app.get('/patients/', response_model=list[Patient])
def filter_patient(
    gender: Literal['male', 'female', 'other'] | None = None,
    stroke: Annotated[int, Field(ge=0, le=1)] | None = None,
    # stroke: int | None = None,
    max_age: float | None = None,
) -> list[Patient]:
    """
    Desc:       Filter patients
    Args:       gender: 'male' | 'female' | 'other' | None
                stroke: 0 | 1
                max_age: float >= 0 | None
    Returns:    list[Patient]
    """
    # if stroke not in (0, 1) and stroke is not None:
    #     raise HTTPException(status_code=422, detail='stroke should be 0 or 1')
    # if max_age is not None and max_age < 0:
    #     raise HTTPException(status_code=422, detail="max_age can't be less than zero")
    df: pd.DataFrame = stroke_data.copy()
    if gender is not None:
        df = df.loc[df['gender'] == gender]
    if stroke is not None:
        df = df.loc[df['stroke'] == stroke]
    if max_age != 0 and max_age is not None:
        df = df.loc[df['age'] <= max_age]
    # records = cast(list[dict[str, Any]], df.to_dict('records'))
    # result: list[Patient] = [Patient(**i) for i in records]
    records = df.to_dict('records')
    result: list[Patient] = TypeAdapter(list[Patient]).validate_python(records)
    return result


@app.get('/patients/{patient_id}')
def read_patient(patient_id: int):
    return {'patient_id': patient_id}


def filter_patient_by_id(patient_id: int) -> list[Patient]:
    df = stroke_data.copy()
    df = df.loc[df['id'] == patient_id]
    if df.empty:
        raise HTTPException(404, 'Patient ID not found')
    else:
        return df.to_dict('records')


# Tester l'app avec :
# poetry run fastapi dev stroke_api/main.py
# http://127.0.0.1:8000/docs : utiliser la fonctionnalité Try it out pour tester les routes

# Ajout des fonctions de filtrage des données cf notebook 1
# Ensuite faire appel à ces fonctions dans le fichier api.py où sont définies les routes.

# Ajouter les fonctions de filtrage pour les autres routes.
