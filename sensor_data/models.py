from django.db import models

class SensorData(models.Model):
    humidity = models.FloatField()
    temperature = models.FloatField()
    moisture_value = models.FloatField(default=0.0)
    moisture_percentage = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    motor_status = models.CharField(max_length=20,default="Unknown state")