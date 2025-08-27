from fastapi import APIRouter
from pydantic import Field
from stroke_api import filters
from typing import Literal, Annotated

router = APIRouter()


@router.get('/')
def read_root():
    return {'message': "Bienvenue sur l'API Stroke Prediction !"}


# TODO décommenter et compléter
@router.get('/patients/')
def get_patients(
    gender: Literal['male', 'female', 'other'] | None = None,
    stroke: Annotated[int, Field(ge=0, le=1)] | None = None,
    # stroke: int | None = None,
    max_age: float | None = None,
):
    result = filters.filter_patient(gender=gender, stroke=stroke, max_age=max_age)
    return result


# TODO décommenter et compléter
# Gérer le cas où l'id de patient passé en paramètre n'existe pas
@router.get('/patients/{patient_id}')
def get_patients_by_id(patient_id: int):
    result = filters.filter_patient_by_id(patient_id)
    return result


# TODO Ajout de la route stats
@router.get('/stats/')
def get_stats():
    df = filters.stroke_data.copy()
    output = {
        'total_patients': int(df['id'].count()),
        'average_age': float(round(df['age'].mean(), 2)),
        'stroke_rate': float(round(df['stroke'].mean(), 2)),
        'gender_rate': {
            i: float(
                (
                    (
                        (df['gender'].loc[df['gender'] == i].count())
                        / df['gender'].count()
                    )
                    * 100
                ).round(2)
            )
            for i in df['gender'].unique()
        },
    }
    return output
