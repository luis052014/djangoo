from django.db import models

# Create your models here.
from os import name
from django.db import models
from datetime import datetime

from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField


# Create your models here.
from app.core.erp.choices import gender_choices


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)



    def __str__(self) :
        return self.name
    
    class Meta:
        verbose_name='Categoria'
        verbose_name_plural = 'Categorias'
        #app_label = 'app.core.erp'
        ordering = ['id']


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=CASCADE)
    name = models.CharField(max_length=150, verbose_name='Nombre',unique=True)
    images = models.ImageField(upload_to='images /%Y/%m/%d',)
    price =  models.DecimalField(default=0.00, max_digits=9, decimal_places=2)




    def __str__(self) :
        return self.name
    
    class Meta:
        verbose_name='Producto'
        verbose_name_plural = 'Productos'
        
        ordering = ['id']


class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    last_names = models.CharField(max_length=150,verbose_name='Apellidos')
    dni=models.CharField(max_length=10, verbose_name='Dni',unique=True)
    date_birth=models.DateField(default=datetime.now, verbose_name= 'Fecha de nacimientos')
    address = models.CharField(max_length=300, verbose_name='Direccion')
    gender = models.CharField(max_length=10, choices= gender_choices, default=name, verbose_name='Sexo')


    def __str__(self) :
        return self.names
    
    class Meta:
        verbose_name='Cliente'
        verbose_name_plural = 'Clientes'
        
        ordering = ['id']


class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_sale = models.DateTimeField()
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)



    def __str__(self) :
        return self.client.names
    
    class Meta:
        verbose_name='Venta'
        verbose_name_plural = 'Ventas'
        
        ordering = ['id']


class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=CASCADE)
    product = models.ForeignKey(Product, on_delete=CASCADE)
    count = models.IntegerField()
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)






    def __str__(self) :
        return self.product.name
    
    class Meta:
        verbose_name='Detalle de venta'
        verbose_name_plural = 'Detalle de ventas'
        
        ordering = ['id']













