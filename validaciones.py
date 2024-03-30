from typing import List, Any, Dict

from fastapi import FastAPI
import random

app = FastAPI()

@app.post("/cargar_facturas_creditrisk")
def cargar_facturas_creditrisk(payload: Dict[str, Any]):
    print(payload)
    return {"resultado": True if payload.get('facturas') else False}


@app.get("/validar_score_riego")
def validar_score_riego():
    return {"resultado": True}

@app.post("/ceder_facturas")
def ceder_facturas(payload: Dict[str, Any]):
    print(payload)
    return {"resultado": True if payload.get('facturas') else False}

@app.get("/validar_cliente_operativo")
def validar_cliente_operativo():
    return {"resultado": random.choice([True, False])}

@app.get("/validar_mandato_RADIAN")
def validar_mandato_RADIAN():
    return {"resultado": random.choice([True, False])}

@app.get("/validar_notas_credito")
def validar_notas_credito():
    return {"resultado": random.choice([True, False])}

@app.get("/validar_endoso")
def validar_endoso():
    return {"resultado": random.choice([True, False])}

@app.get("/validar_restricciones_representante_legal")
def validar_restricciones_representante_legal():
    return {"resultado": random.choice([True, False])}

@app.get("/validar_condonaciones_de_giro")
def validar_condonaciones_de_giro():
    return {"resultado": random.choice([True, False])}

@app.get("/validar_cotizacion_y_aceptacion")
def validar_cotizacion_y_aceptacion():
    return {"resultado": random.choice([True, False])}

@app.get("/validar_monto_factura")
def validar_monto_factura():
    return {"resultado": random.choice([True, False])}

@app.get("/validar_cuenta_de_transferencia")
def validar_cuenta_de_transferencia():
    return {"resultado": random.choice([True, False])}

@app.get("/validar_condiciones_propias_de_la_operacion")
def validar_condiciones_propias_de_la_operacion():
    return {"resultado": random.choice([True, False])}

@app.get("/validar_garantia_mobiliaria")
def validar_garantia_mobiliaria():
    return {"resultado": random.choice([True, False])}
