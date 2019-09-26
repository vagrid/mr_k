
from django.db import models


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
    location    = models.ForeignKey(Location, related_name = "city", on_delete = models.CASCADE)  
    description = models.TextField() 
    title       = models.CharField(max_length = 100)
    slug        = models.SlugField(max_length = 100, unique = True)

    # 
    def __str__(self):
        """
        """
        return self.title




