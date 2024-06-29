from src.models import Serie
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from src.utils import dolar_data

app = FastAPI()

@app.get("/")
async def read_root(req: Request):
    context = """
    <html>
	<head>
		<title>DOLAR API</title>
	</head>
    <body>Api simple que ordena la información de datos libres del dolar en una seríe de tiempo</body>
    </html>
    """
    return HTMLResponse(context)

@app.get("/dolar_data", response_model=Serie)
async def get_dolar():
    dolar_data_serie = dolar_data()
    return dolar_data_serie

@app.get("/dolar_predict")
async def dolar_predict():
    return "hi"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.0", port=8080, reload=True)
