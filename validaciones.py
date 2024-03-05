from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/validar_cliente_operativo")
def validar_cliente_operativo():
    return {"result": random.choice([True, False])}

@app.get("/validar_mandato_RADIAN")
def validar_mandato_RADIAN():
    return {"result": random.choice([True, False])}

@app.get("/validar_notas_credito")
def validar_notas_credito():
    return {"result": random.choice([True, False])}

@app.get("/validar_endoso")
def validar_endoso():
    return {"result": random.choice([True, False])}

@app.get("/validar_restricciones_representante_legal")
def validar_restricciones_representante_legal():
    return {"result": random.choice([True, False])}

@app.get("/validar_condonaciones_de_giro")
def validar_condonaciones_de_giro():
    return {"result": random.choice([True, False])}

@app.get("/validar_cotizacion_y_aceptacion")
def validar_cotizacion_y_aceptacion():
    return {"result": random.choice([True, False])}

@app.get("/validar_monto_factura")
def validar_monto_factura():
    return {"result": random.choice([True, False])}

@app.get("/validar_cuenta_de_transferencia")
def validar_cuenta_de_transferencia():
    return {"result": random.choice([True, False])}

@app.get("/validar_condiciones_propias_de_la_operacion")
def validar_condiciones_propias_de_la_operacion():
    return {"result": random.choice([True, False])}

@app.get("/validar_garantia_mobiliaria")
def validar_garantia_mobiliaria():
    return {"result": random.choice([True, False])}
