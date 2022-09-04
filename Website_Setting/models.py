from django.db import models
from django.core.exceptions import ValidationError
def validate_images(image):
    file_size = image.file.size
    limit_kb = 20
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb)
class Homepage_animated_line(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Animated Line'
        verbose_name_plural = 'Animated Line'
    Animated_line = models.CharField(max_length=500, verbose_name= "Animated Line",help_text=("please enter text which moving in Home page"))
    
class website_logo(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Website logo'
        verbose_name_plural = 'Website Logo'
    logo = models.ImageField(upload_to ='logo/',validators=[validate_images],verbose_name="Website Logo",help_text=("our recommended size 20 KB MAX"))