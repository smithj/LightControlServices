from django.db import models


# Create your models here.
class Light(models.Model):
    light_id = models.IntegerField(default=0)
    controller = models.ForeignKey('Controller')
    bus = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=128)
    on = models.BooleanField(default=False)
    color = models.PositiveIntegerField(default=0)
    brightness = models.PositiveSmallIntegerField(default=0)
    delay = models.PositiveSmallIntegerField(default=0)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        """
   #     Send the attribute to the arduino before db save
        """
        print args
        print self.controller.path
        print self.color
        print self.on

        super(Light, self).save(*args, **kwargs)



class Controller(models.Model):
    path = models.CharField(max_length=255)
    description = models.CharField(max_length=128)

    SER = 'SER'
    INTERFACE_TYPE_CHOICES = (
        (SER, 'Serial'),
    )
    interface_type = models.CharField(max_length=3,
                                      choices=INTERFACE_TYPE_CHOICES,
                                      default=SER)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.path


