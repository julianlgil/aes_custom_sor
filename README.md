Lista de endpoints:
1.  /validar_cliente_operativo
2.  /validar_mandato_RADIAN
3.  /validar_notas_credito
4.  /validar_endoso
5.  /validar_restricciones_representante_legal
6.  /validar_condonaciones_de_giro
7.  /validar_cotizacion_y_aceptacion
8.  /validar_monto_factura
9.  /validar_cuenta_de_transferencia
10. /validar_condiciones_propias_de_la_operacion
11. /validar_garantia_mobiliaria

Levantar proyecto:
docker-compose down;
docker-compose up --build -d;

Correr tests:
docker-compose exec validaciones bash -c "pytest test_endpoints.py"