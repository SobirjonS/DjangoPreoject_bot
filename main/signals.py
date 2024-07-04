from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Test, Evaluation

@receiver(pre_delete, sender=Test)
def set_default_test_title(sender, instance, **kwargs):
    evaluations = Evaluation.objects.filter(test=instance)
    for evaluation in evaluations:
        evaluation.test = None
        evaluation.save()
