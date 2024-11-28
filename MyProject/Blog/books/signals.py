from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Book
import uuid  # For generating a unique hex code

# Function to generate a random hex code
def generate_unique_hex():
    return uuid.uuid4().hex[:6].upper()  # 6-character uppercase hex code

@receiver(pre_save, sender=Book)
def add_unique_hex_code(sender, instance, **kwargs):
    hex_code = generate_unique_hex()
    print(hex_code)
