from fastapi import APIRouter
from stroke_api import filters

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API Stroke Prediction !"}

# TODO décommenter et compléter
#@router.get("/patients/")
#def get_patients(gender: str = None, stroke: int = None, max_age: float = None):
    #filtered_df = 
    #return filtered_df.to_dict(orient="records")

# TODO décommenter et compléter
#@router.get("/patients/{patient_id}")
    # Gérer le cas où l'id de patient passé en paramètre n'existe pas


# TODO Ajout de la route stats
