from odoo import models, fields, api


class Cierre(models.Model):
    _name ='cierre'
    _description ='Cálculos pertinentes para dar cierrer a un dia de ventas'    
        
    producto_ids = fields.Many2many('producto', string ="Prodductos involucrados", help ='productos que tuvieron movimiento después del último cierre.' )
    # nombre-ids-delaotrclase = fields.One2many('nombre_oficial_de_la_clase_relacionada_' ) (termina en ids el nombre del campo)
    
    ganancia_total= fields.Float(string="Ganancia total", compute="compute_total_producto_ganancia", help="Ganancia detodos los productos vendidos.")
    total_productos=fields.Integer(string="Total de productos vendidos", compute="compute_total_producto_ganancia", help="Cantidad de productos vendidos.")
    fecha_cierre=fields.Datetime(required=True, string="Fecha", default=fields.Datetime.now, readonly=True, help="Fecha de creado del cierre." )
    pagar_a_compannias=fields.Text( string="Lista de Deudas", help="Cantidad de dinero a pagar por empresa.", compute="compute_deuda_empresa")
    
    
    @api.depends("producto_ids.compannia","producto_ids.ventas","producto_ids.precio_costo")
    def compute_deuda_empresa(self):
        for cierre in self:
            resultado= {}
            
            for producto in cierre.producto_ids:
                compannia= producto.compannia
                
                if compannia not in resultado:
                    resultado[compannia] = 0.0  
                    
                resultado[compannia] += (
                    producto.ventas * producto.precio_costo
                )
            print("RESULTADO:", resultado)
            cierre.pagar_a_compannias = resultado     
                      
    
    @api.depends('producto_ids.ganancia', 'producto_ids.ventas')
    def compute_total_producto_ganancia(self):
        
        
        for cierre in self:
            cierre.ganancia_total = 0.0
            cierre.total_productos = 0
        
            for producto in cierre.producto_ids:
                cierre.ganancia_total += ((producto.ganancia)*(producto.ventas))
                cierre.total_productos += producto.ventas
        
        
    
