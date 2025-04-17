from django.db import models
from UserManagement.models import *

class SpamReport(models.Model):
    draft_id = models.CharField(max_length=255)  # or ForeignKey to your model
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Link to User models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    remarks = models.CharField(max_length=255)  # Store the specific remark

    class Meta:
        unique_together = ('user', 'draft_id')  # Ensure a user can only report once per draft

    def __str__(self):
        return f"Spam Report for {self.draft_id} by {self.user.get_full_name()}"
