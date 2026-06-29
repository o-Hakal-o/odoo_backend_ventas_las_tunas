import json
from odoo import http
from odoo.http import request, Response


class ProductoAPI(http.Controller):

    @http.route(
        '/api/productos_activos',
        type='http',
        auth='public',
        methods=['GET', 'OPTIONS'],
        csrf=False
    )
    def get_productos(self, **kwargs):

        if request.httprequest.method == 'OPTIONS':
            return Response(
                status=200,
                headers=[
                    ('Access-Control-Allow-Origin', '*'),
                    ('Access-Control-Allow-Methods', 'GET, OPTIONS'),
                    ('Access-Control-Allow-Headers',
                     'Content-Type, ngrok-skip-browser-warning')
                ]
            )

        try:

            productos = request.env['producto'].sudo().search(
                [('stock', '=', True)],
                limit=10
            )

            data = []

            for p in productos:

                imagen = None

                if p.imagen:

                    # IMPORTANTE:
                    # En Odoo los Binary suelen venir ya codificados
                    if isinstance(p.imagen, bytes):
                        imagen = p.imagen.decode('utf-8')

                    elif isinstance(p.imagen, str):
                        imagen = p.imagen

                data.append({
                    'id': p.id,
                    'titulo': p.titulo or '',
                    'precio_venta': float(p.precio_venta or 0),
                    'descripcion': p.descripcion or '',
                    'imagen_base64': imagen
                })

            return Response(
                json.dumps({
                    'status': 'success',
                    'data': data
                }),
                status=200,
                headers=[
                    ('Content-Type', 'application/json'),
                    ('Access-Control-Allow-Origin', '*'),
                    ('Access-Control-Allow-Methods', 'GET, OPTIONS'),
                    ('Access-Control-Allow-Headers',
                     'Content-Type, ngrok-skip-browser-warning')
                ]
            )

        except Exception as e:

            return Response(
                json.dumps({
                    'status': 'error',
                    'message': str(e)
                }),
                status=500,
                headers=[
                    ('Content-Type', 'application/json'),
                    ('Access-Control-Allow-Origin', '*')
                ]
            )