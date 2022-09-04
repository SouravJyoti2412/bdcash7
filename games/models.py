from distutils.command.upload import upload
from django.db import models
from django.core.exceptions import ValidationError
def validate_images(image):
    file_size = image.file.size
    limit_kb = 200
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb)
def validate_image(image):
    file_size = image.file.size
    limit_kb = 250
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb)

class game1(models.Model):
    fontImage = models.ImageField(upload_to ="games_image",validators=[validate_image],verbose_name="Game Image For Home page",help_text=(" our recommended size  250 KB MAX"))
    game_name = models.CharField(max_length=30,help_text=("please enter Game name"))
    Image = models.ImageField(upload_to ="games_image",validators=[validate_images],verbose_name="Game Image",help_text=("Please use our recommended dimensions: 887 X 885px, 200 KB MAX"))
    rate = models.IntegerField(verbose_name="Winning Rate",help_text=("please enter how percent get customer"))
    
class game2(models.Model):
    fontImage = models.ImageField(upload_to ="games_image",validators=[validate_image],verbose_name="Game Image For Home page",help_text=(" our recommended size  250 KB MAX"))
    game_name = models.CharField(max_length=30,help_text=("please enter Game name"))
    Image = models.ImageField(upload_to ="games_image",validators=[validate_images],verbose_name="Game Image",help_text=("Please use our recommended dimensions: 887 X 885px, 200 KB MAX"))
    rate = models.IntegerField(verbose_name="Winning Rate",help_text=("please enter how percent get customer"))

class game3(models.Model):
    fontImage = models.ImageField(upload_to ="games_image",validators=[validate_image],verbose_name="Game Image For Home page",help_text=(" our recommended size  250 KB MAX"))
    game_name = models.CharField(max_length=30,help_text=("please enter Game name"))
    Image = models.ImageField(upload_to ="games_image",validators=[validate_images],verbose_name="Game Image",help_text=("Please use our recommended dimensions: 887 X 885px, 200 KB MAX"))
    rate = models.IntegerField(verbose_name="Winning Rate",help_text=("please enter how percent get customer"))

class game4(models.Model):
    fontImage = models.ImageField(upload_to ="games_image",validators=[validate_image],verbose_name="Game Image For Home page",help_text=(" our recommended size  250 KB MAX"))
    game_name = models.CharField(max_length=30,help_text=("please enter Game name"))
    Image = models.ImageField(upload_to ="games_image",validators=[validate_images],verbose_name="Game Image",help_text=("Please use our recommended dimensions: 887 X 885px, 200 KB MAX"))
    rate = models.IntegerField(verbose_name="Winning Rate",help_text=("please enter how percent get customer"))

class game5(models.Model):
    fontImage = models.ImageField(upload_to ="games_image",validators=[validate_image],verbose_name="Game Image For Home page",help_text=(" our recommended size  250 KB MAX"))
    game_name = models.CharField(max_length=30,help_text=("please enter Game name"))
    Image = models.ImageField(upload_to ="games_image",validators=[validate_images],verbose_name="Game Image",help_text=("Please use our recommended dimensions: 887 X 885px, 200 KB MAX"))
    rate = models.IntegerField(verbose_name="Winning Rate",help_text=("please enter how percent get customer"))


class game6(models.Model):
    fontImage = models.ImageField(upload_to ="games_image",validators=[validate_image],verbose_name="Game Image For Home page",help_text=(" our recommended size  250 KB MAX"))
    game_name = models.CharField(max_length=30,help_text=("please enter Game name"))
    Image = models.ImageField(upload_to ="games_image",validators=[validate_images],verbose_name="Game Image",help_text=("Please use our recommended dimensions: 887 X 885px, 200 KB MAX"))
    rate = models.IntegerField(verbose_name="Winning Rate",help_text=("please enter how percent get customer"))


   