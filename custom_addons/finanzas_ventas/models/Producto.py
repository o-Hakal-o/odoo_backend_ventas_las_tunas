from odoo import models, fields, api


class Producto (models.Model):
    _name = "producto"
    _description = "Crea tu producto modificando los diferentes parametros."
    cierre_ids = fields.Many2many('cierre', string = 'Cierres económicos', help="Cierres diarios en los que participó este producto" )
    #producto_ids = fields.Many2one('nombre_calse_padre)(termina en ids el nombre del campo)
    
    titulo = fields.Char(required = True, help = "Inserta el titulo de tu preoducto.", string = "Título", size = 24)
    numero_de_serie = fields.Char(required = False, help = "Inserta el número de serie de tu producto.", string = "Número de serie ")
    precio_costo = fields.Float(required = True, help ="Ingrese el precio de costo de su producto.", string = "Costo")
    precio_venta = fields.Float(required = True, help ="Ingrese el precio de venta de su producto.", string = "Precio")
    ganancia = fields.Float(help ="Ganacia por venta de este producto. ", string = "Ganancia", compute= "compute_ganancia")
    compannia = fields.Char(required = True, help  ="Ingrese el nombre de la compañia de donde proviene el producto.", string = "Nombre", size = 24 )
    ancho = fields.Float(required =False, help= "Inserta cuan ancho es tu producto en cm.", string = "Ancho")
    largo = fields.Float(required = False, help = "Inserta cuan largo es tu producto en cm.", string ="Largo")
    alto = fields.Float(required = False, help = "Inserta cuan alto es tu producto en cm.", string ="Alto")
    peso = fields.Float(required = False, help ="Inserta cuan pesado es tu producto en Kg.", string ="Peso")
    volumen_aprox = fields.Float(help = "Volumen aproximado del producto en metros cúbicos", string = "Volumen", compute ="_compute_volumen")
    imagen = fields.Image(required = False, string = "foto del producto", max_width = 1024, max_height = 1024)
    stock = fields.Boolean(required = True , help = "Marca si hay ejemplares de este producto en venta ahora mismo.")
    descripcion = fields.Char(required = False, size = 1000, string = "Descripción")
    ventas = fields.Integer(required = False, string ="Ventas", default = 0, help ="Ventas por cada producto")
    _sql_constraints = [
        ('ventas_positivas', 'CHECK(ventas >= 0)', 'El número de ventas no puede ser menor a 0.')
    ]
    
    
    @api.depends("precio_venta", "precio_costo")
    def compute_ganancia(self):
        for record in self:
            record.ganancia = ((record.precio_venta or 0.0) - (record.precio_costo or 0.0)) 
    
    
    
    @api.depends('ancho', 'largo', 'alto')
    def _compute_volumen(self):
        for record in self:
            record.volumen_aprox = ((record.ancho or 0.0) *(record.largo or 0.0) * (record.alto or 0.0))*(0.001)
            # aca se pone record.nombre_exacto_del_campo = (record.nombre_exacto_del campo or 0.0)    

    def action_incrementar(self):
        for record in self:
            record.ventas += 1
    
    def action_decrementar(self):
    
        for record in self:
            if record.ventas > 0:
                record.ventas -= 1