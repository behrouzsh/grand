from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from grandapp.models import Cancer
from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y %H:%M'

VACCINES_NAMES = [
    'Canine Parvo',
    'Canine Distemper',
    'Canine Rabies',
    'Canine Leptospira',
    'Feline Herpes Virus 1',
    'Feline Rabies',
    'Feline Leukemia'
]

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from pet_data.csv into our Pet model"

    def handle(self, *args, **options):
        print("Loading cancer data!")
        for row in DictReader(open('./data/cancer.csv')):
            cancer = Cancer()
            cancer.tissue    = row['cancer']
            cancer.nnets     = row['nnets']
            cancer.datasets  = row['datasets']
            cancer.types     = row['types']
            cancer.subtype   = row['subtype']
            cancer.save()
