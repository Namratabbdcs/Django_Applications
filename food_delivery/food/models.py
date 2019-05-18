from django.utils import timezone
from django.db import models

# Create your models here.
class Food(models.Model):

    ASSIGN = 'yes'
    NOT_ASSIGN = 'free'
    STATUS_CHOICES = (
        (ASSIGN, 'yes'),
        (NOT_ASSIGN,'free')
    )

    HIGH_PRIORITY = "high"
    LOW_PRIORITY = "low"
    MEDIUM_PRIORITY = "medium"
    PRIORITY_CHOICES = (
        (HIGH_PRIORITY, "high"),
        (LOW_PRIORITY, "low"),
        (MEDIUM_PRIORITY, "medium")
    )

    NEW_TASK = "new"
    TASK_ACCEPTED = "accepted"
    TASK_DECLINED = "declined"
    CANCELLED = "cancelled"
    TASK_CHOICES = (
        (NEW_TASK, 'new'),
        (TASK_ACCEPTED, 'accepted'),
        (TASK_DECLINED, 'declined'),
        (CANCELLED,'cancelled')
    )

    order_no = models.CharField(max_length=128, primary_key=True, help_text='enter the order number')
    title = models.TextField(max_length=128, default='', null=False, help_text='enter the title')
    dt_created = models.DateTimeField(default=timezone.now(), blank=True)
    dt_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=128, choices=STATUS_CHOICES, default='NOT_ASSIGN', \
            help_text='deliverd or not delivered')
    priority = models.CharField(max_length=128, choices=PRIORITY_CHOICES, default='MEDIUM_PRIORITY',\
            help_text='priority can be high/low/medium')
    task = models.CharField(max_length=128, choices=TASK_CHOICES, default='NEW_TASK', \
            help_text='Accepts or not')

