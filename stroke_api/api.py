from fastapi import APIRouter
from stroke_api import filters

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API Stroke Prediction !"}

# TODO décommenter et compléter
@router.get("/patients/")
def get_patients(gender: str = None, stroke: int = None, max_age: float = None):
    result = filters.filter_patient(gender=gender, stroke=stroke, max_age=max_age)
    return result

# TODO décommenter et compléter
@router.get("/patients/{patient_id}")
def get_patients_by_id(patient_id: int = None):
    result = filters.filter_patient_by_id(patient_id)
    return result
# Gérer le cas où l'id de patient passé en paramètre n'existe pas

# TODO Ajout de la route stats
@router.get('/stats/')
def get_stats():
    # Fournit des statistiques agrégées sur les patients (ex. : nb total de patients, âge moyen, taux d’AVC, répartition hommes/femmes).
    df = filters.stroke_data.copy()

    output = {
        'total_patients': int(df['id'].count()),
        'average_age': float(df['age'].mean().round(2)),
        'stroke_rate': float(df['stroke'].mean().round(2)),
        'gender_rate': {i: float((((df['gender'].loc[df['gender'] == i].count())/df['gender'].count())*100).round(2)) for i in df['gender'].unique()}
    }
    return output