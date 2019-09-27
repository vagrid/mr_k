
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

#
class Location(models.Model):
    """
    """
    name = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100, unique = True)

    #
    class Meta:
        """
        """
        ordering = ["name"]

    # 
    def __str__(self):
        """
        """
        return self.name 

#
class Mission(models.Model):
    """
    """ 
    title           = models.CharField(max_length = 100)
    slug            = models.SlugField(max_length = 100, unique = True) 
    location        = models.ForeignKey(Location, related_name = "city", on_delete = models.CASCADE)  
    description     = models.TextField() 
    picture         = models.ImageField(upload_to = "images")
    #
    difficulty      = models.IntegerField(default = 1, validators = [MaxValueValidator(5), MinValueValidator(1)])
    logic           = models.IntegerField(default = 1, validators = [MaxValueValidator(5), MinValueValidator(1)])
    handling        = models.IntegerField(default = 1, validators = [MaxValueValidator(5), MinValueValidator(1)])
    search          = models.IntegerField(default = 1, validators = [MaxValueValidator(5), MinValueValidator(1)])
    #
    success         = models.IntegerField(default = 1, validators = [MaxValueValidator(100), MinValueValidator(0)])
    min_players     = models.IntegerField(default = 1, validators = [MaxValueValidator(100), MinValueValidator(1)])
    max_players     = models.IntegerField(default = 1, validators = [MaxValueValidator(100), MinValueValidator(1)])
    min_age         = models.IntegerField(default = 1, validators = [MaxValueValidator(100), MinValueValidator(1)])
    max_age         = models.IntegerField(default = 1, validators = [MaxValueValidator(100), MinValueValidator(1)])
    duration        = models.IntegerField(default = 1, validators = [MaxValueValidator(180), MinValueValidator(5)])


    # 
    def __str__(self):
        """
        """
        return self.title




