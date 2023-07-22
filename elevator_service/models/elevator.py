from django.db import models
from elevator_service.models.base_model import BaseModel

class Elevator(BaseModel):

    STATUS_CHOICES = (
        (1, 'Operational'),
        (2, 'Maintenance'),
    )

    DIRECTION_CHOICES = (
        (1, 'Up'),
        (2, 'Down'),
        (3, 'Stop'),
    )

    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=1)
    direction = models.SmallIntegerField(choices=DIRECTION_CHOICES, default=3)
    current_floor = models.IntegerField(default=0)

    def __str__(self):
        return f'Elevator {self.id}'