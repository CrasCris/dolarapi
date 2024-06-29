import pandas as pd
from sodapy import Socrata
import os

try:
    MyAppToken=os.environ.get('token')
    client = Socrata("www.datos.gov.co",MyAppToken)
    results = client.get("mcec-87by", limit=10000)
except:
    print("No token api find, using without key")
    client = Socrata("www.datos.gov.co",None)
    results = client.get("mcec-87by", limit=10000)

# Convert to pandas DataFrame
def dolar_data():
    datos = pd.DataFrame.from_records(results)
    datos.drop("unidad", axis=1)
    datos['vigenciahasta'] = pd.to_datetime(datos['vigenciahasta'],format="%Y-%m-%dT%H:%M:%S.%f")
    datos['vigenciadesde'] = pd.to_datetime(datos['vigenciadesde'],format="%Y-%m-%dT%H:%M:%S.%f")
    datosOrd=datos.sort_values(by='vigenciahasta', ascending=False)
    date_ranges = []
    for index, row in datosOrd.iterrows():
        trm = row['valor']
        fecha_desde = row['vigenciadesde']
        fecha_hasta = row['vigenciahasta']
        date_range = pd.date_range(start=fecha_desde, end=fecha_hasta, freq='D')
        for fecha in date_range:
            date_ranges.append({'valor': trm, 'Fecha': fecha})
    new_df = pd.DataFrame(date_ranges)
    Serie = new_df.sort_values(by='Fecha', ascending=True)
    Serie.rename(columns={'valor': 'Serie'}, inplace=True)
    Serie.set_index('Fecha', inplace=True)
    Serie.index = Serie.index.strftime('%Y-%m-%d')
    dictt = Serie.to_dict()
    return dictt