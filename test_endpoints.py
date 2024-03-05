import requests
import pytest

ENDPOINTS = [
    "/validar_cliente_operativo",
    "/validar_mandato_RADIAN",
    "/validar_notas_credito",
    "/validar_endoso",
    "/validar_restricciones_representante_legal",
    "/validar_condonaciones_de_giro",
    "/validar_cotizacion_y_aceptacion",
    "/validar_monto_factura",
    "/validar_cuenta_de_transferencia",
    "/validar_condiciones_propias_de_la_operacion",
    "/validar_garantia_mobiliaria"
]

@pytest.mark.parametrize("endpoint", ENDPOINTS)
def test_endpoint(endpoint):
    response = requests.get(f"http://localhost:8000{endpoint}")
    assert response.status_code == 200
    data = response.json()
    assert "result" in data
    assert data["result"] in [True, False]

if __name__ == "__main__":
    pytest.main([__file__])
