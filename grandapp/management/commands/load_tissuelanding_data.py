from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from grandapp.models import Tissuelanding
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
        print("Loading tissue landing data!")
        for row in DictReader(open('./data/tissueslanding.csv')):
            tissuelanding = Tissuelanding()
            tissuelanding.tissue       = row['tissue']
            tissuelanding.tissueLink   = row['tissueLink']
            tissuelanding.tool         = row['tool']
            tissuelanding.netzoo       = row['netzoo']
            tissuelanding.netzooLink   = row['netzooLink']
            tissuelanding.netzooRel    = row['netzooRel']
            tissuelanding.network      = row['network']
            tissuelanding.ppi          = row['ppi']
            tissuelanding.ppiLink      = row['ppiLink']
            tissuelanding.motif        = row['motif']
            tissuelanding.motifDesc    = row['motifDesc']
            tissuelanding.expression   = row['expression']
            tissuelanding.expLink      = row['expLink']
            tissuelanding.tfs          = row['tfs']
            tissuelanding.genes        = row['genes']
            tissuelanding.refs         = row['refs']
            tissuelanding.refs2        = row['refs2']
            tissuelanding.refs3        = row['refs3']
            tissuelanding.samples      = row['samples']
            tissuelanding.reg          = row['reg']
            tissuelanding.script       = row['script']
            tissuelanding.save()
