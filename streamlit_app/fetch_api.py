from typing import Annotated, Literal

import pandas as pd
import requests
import streamlit as st
from pydantic import Field

URL = 'http://0.0.0.0:8000/patients'


@st.cache_data
def fetch_data(
    gender: Literal['male', 'female', 'other'] | None = None,
    stroke: Annotated[int, Field(ge=0, le=1)] | None = None,
    max_age: float | None = None,
) -> pd.DataFrame | None:
    try:
        params = {'gender': gender, 'stroke': stroke, 'max_age': max_age}
        response = requests.get(URL, params)
        fetched_data = response.json()
        df: pd.DataFrame = pd.DataFrame(fetched_data)
        return df
    except Exception as e:
        print(f'error: {e}')
        return None
