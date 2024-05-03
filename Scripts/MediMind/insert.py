import os
import django

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MediMind.settings')
django.setup()
from datetime import datetime, timedelta
from application.models import Appointment

# Define the appointment data
appointments_data = [
    {
        'doctor_name': 'Dr. Smith',
        'appointment_mood': 'Regular checkup',
        'appointment_time': datetime.now() + timedelta(days=1),  # Example: 1 day from now
        'appointment_length': 30  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Johnson',
        'appointment_mood': 'Follow-up',
        'appointment_time': datetime.now() + timedelta(days=5),  # Example: 5 days from now
        'appointment_length': 60  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Martinez',
        'appointment_mood': 'Regular checkup',
        'appointment_time': datetime.now() + timedelta(days=9),  # Example: 9 days from now
        'appointment_length': 45  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Lee',
        'appointment_mood': 'Follow-up',
        'appointment_time': datetime.now() + timedelta(days=13),  # Example: 13 days from now
        'appointment_length': 60  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Hernandez',
        'appointment_mood': 'Regular checkup',
        'appointment_time': datetime.now() + timedelta(days=17),  # Example: 17 days from now
        'appointment_length': 45  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Wang',
        'appointment_mood': 'Follow-up',
        'appointment_time': datetime.now() + timedelta(days=21),  # Example: 21 days from now
        'appointment_length': 60  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Nguyen',
        'appointment_mood': 'Regular checkup',
        'appointment_time': datetime.now() + timedelta(days=25),  # Example: 25 days from now
        'appointment_length': 30  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Garcia',
        'appointment_mood': 'Follow-up',
        'appointment_time': datetime.now() + timedelta(days=29),  # Example: 29 days from now
        'appointment_length': 60  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Gonzalez',
        'appointment_mood': 'Regular checkup',
        'appointment_time': datetime.now() + timedelta(days=33),  # Example: 33 days from now
        'appointment_length': 30  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Martinez',
        'appointment_mood': 'Follow-up',
        'appointment_time': datetime.now() + timedelta(days=37),  # Example: 37 days from now
        'appointment_length': 60  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Johnson',
        'appointment_mood': 'Regular checkup',
        'appointment_time': datetime.now() + timedelta(days=41),  # Example: 41 days from now
        'appointment_length': 60  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Lee',
        'appointment_mood': 'Follow-up',
        'appointment_time': datetime.now() + timedelta(days=45),  # Example: 45 days from now
        'appointment_length': 60  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Patel',
        'appointment_mood': 'Regular checkup',
        'appointment_time': datetime.now() + timedelta(days=49),  # Example: 49 days from now
        'appointment_length': 30  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Wang',
        'appointment_mood': 'Follow-up',
        'appointment_time': datetime.now() + timedelta(days=53),  # Example: 53 days from now
        'appointment_length': 60  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Nguyen',
        'appointment_mood': 'Regular checkup',
        'appointment_time': datetime.now() + timedelta(days=57),  # Example: 57 days from now
        'appointment_length': 45  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Hernandez',
        'appointment_mood': 'Follow-up',
        'appointment_time': datetime.now() + timedelta(days=61),  # Example: 61 days from now
        'appointment_length': 60  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Garcia',
        'appointment_mood': 'Regular checkup',
        'appointment_time': datetime.now() + timedelta(days=65),  # Example: 65 days from now
        'appointment_length': 30  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Martinez',
        'appointment_mood': 'Follow-up',
        'appointment_time': datetime.now() + timedelta(days=69),  # Example: 69 days from now
        'appointment_length': 60  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Johnson',
        'appointment_mood': 'Regular checkup',
        'appointment_time': datetime.now() + timedelta(days=72),  # Example: 72 days from now
        'appointment_length': 45  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Lee',
        'appointment_mood': 'Follow-up',
        'appointment_time': datetime.now() + timedelta(days=76),  # Example: 76 days from now
        'appointment_length': 60  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Hernandez',
        'appointment_mood': 'Regular checkup',
        'appointment_time': datetime.now() + timedelta(days=79),  # Example: 79 days from now
        'appointment_length': 45  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Wang',
        'appointment_mood': 'Follow-up',
        'appointment_time': datetime.now() + timedelta(days=82),  # Example: 82 days from now
        'appointment_length': 60  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Nguyen',
        'appointment_mood': 'Regular checkup',
        'appointment_time': datetime.now() + timedelta(days=86),  # Example: 86 days from now
        'appointment_length': 30  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Garcia',
        'appointment_mood': 'Follow-up',
        'appointment_time': datetime.now() + timedelta(days=90),  # Example: 90 days from now
        'appointment_length': 60  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Gonzalez',
        'appointment_mood': 'Regular checkup',
        'appointment_time': datetime.now() + timedelta(days=94),  # Example: 94 days from now
        'appointment_length': 30  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Martinez',
        'appointment_mood': 'Follow-up',
        'appointment_time': datetime.now() + timedelta(days=98),  # Example: 98 days from now
        'appointment_length': 60  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Johnson',
        'appointment_mood': 'Regular checkup',
        'appointment_time': datetime.now() + timedelta(days=102),  # Example: 102 days from now
        'appointment_length': 60  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Lee',
        'appointment_mood': 'Follow-up',
        'appointment_time': datetime.now() + timedelta(days=106),  # Example: 106 days from now
        'appointment_length': 60  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Patel',
        'appointment_mood': 'Regular checkup',
        'appointment_time': datetime.now() + timedelta(days=110),  # Example: 110 days from now
        'appointment_length': 30  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Wang',
        'appointment_mood': 'Follow-up',
        'appointment_time': datetime.now() + timedelta(days=114),  # Example: 114 days from now
        'appointment_length': 60  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Nguyen',
        'appointment_mood': 'Regular checkup',
        'appointment_time': datetime.now() + timedelta(days=118),  # Example: 118 days from now
        'appointment_length': 45  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Hernandez',
        'appointment_mood': 'Follow-up',
        'appointment_time': datetime.now() + timedelta(days=122),  # Example: 122 days from now
        'appointment_length': 60  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Garcia',
        'appointment_mood': 'Regular checkup',
        'appointment_time': datetime.now() + timedelta(days=126),  # Example: 126 days from now
        'appointment_length': 30  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Gonzalez',
        'appointment_mood': 'Follow-up',
        'appointment_time': datetime.now() + timedelta(days=130),  # Example: 130 days from now
        'appointment_length': 60  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Martinez',
        'appointment_mood': 'Regular checkup',
        'appointment_time': datetime.now() + timedelta(days=134),  # Example: 134 days from now
        'appointment_length': 45  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Johnson',
        'appointment_mood': 'Follow-up',
        'appointment_time': datetime.now() + timedelta(days=138),  # Example: 138 days from now
        'appointment_length': 60  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Lee',
        'appointment_mood': 'Regular checkup',
        'appointment_time': datetime.now() + timedelta(days=142),  # Example: 142 days from now
        'appointment_length': 60  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Patel',
        'appointment_mood': 'Follow-up',
        'appointment_time': datetime.now() + timedelta(days=146),  # Example: 146 days from now
        'appointment_length': 45  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Hernandez',
        'appointment_mood': 'Regular checkup',
        'appointment_time': datetime.now() + timedelta(days=150),  # Example: 150 days from now
        'appointment_length': 30  # Appointment length in minutes
    },
    {
        'doctor_name': 'Dr. Wang',
        'appointment_mood': 'Follow-up',
        'appointment_time': datetime.now() + timedelta(days=154),  # Example: 154 days from now
        'appointment_length': 60  # Appointment length in minutes
    }
]

# Create appointments
for data in appointments_data:
    Appointment.objects.create(
        doctor_name=data['doctor_name'],
        appointment_mood=data['appointment_mood'],
        appointment_time=data['appointment_time'],
        appointment_length=data['appointment_length']
    )
