from django.db import models

# Create your models here.
class Elementos(models.Model):
    id_elemento = models.CharField(primary_key=True, max_length=8, verbose_name="Identificador")
    descripcion_elemento = models.CharField(max_length=350,verbose_name="Descripción") 
    casillas_elemento = models.DecimalField(verbose_name="Casillas", max_digits=2,decimal_places=0)
    
    def __str__(self):
        fila_elemento = "Id: " + self.id_elemento + "  -  Descripción: " + self.descripcion_elemento 
        return fila_elemento

class Participantes(models.Model):
    id_participante = models.CharField(primary_key=True, max_length=6, verbose_name="Identificador del participante") 
    raci_participante = models.CharField(max_length=2, verbose_name="RACI")
    dn_participante = models.CharField(max_length=6, verbose_name="DN")
    sc_participante = models.CharField(max_length=30, verbose_name='Solution Center')
    nombres_participante = models.CharField(max_length=62, verbose_name='Nombres')
    apellido_pat_participante = models.CharField(max_length=62, verbose_name='Apellido Paterno')
    apellido_mat_participante = models.CharField(max_length=62, verbose_name='Apellido Materno')
    img_participante = models.ImageField(upload_to="imagenes/", null=True, verbose_name='Foto / Avatar')
    
    def __str__(self):
        fila_participantes = "Id: " + self.id_participante + "  -  Nombre completo: "
        fila_participantes += self.apellido_pat_participante + " " + self.apellido_mat_participante + ", "
        fila_participantes += self.nombres_participante 
        return fila_participantes
    
    def delete(self, using=None, keep_parents=False):
        self.img_participante.storage.delete(self.img_participante.name)
        super().delete()
    
    