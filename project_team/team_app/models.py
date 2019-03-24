from django.db import models

class Teamlist(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length = 255)
    specialty = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ returns a readable string """
        return "{}".format(self.name)