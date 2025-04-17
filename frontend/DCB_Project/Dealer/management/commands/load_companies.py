import csv
from django.core.management.base import BaseCommand
from ProductManagement.models import InsuranceCompany

# class Command(BaseCommand):
#     help = 'Load insurance companies from a CSV file into the database'

#     def handle(self, *args, **kwargs):
#         with open('templates\Dealer\insurance\insurer.csv', newline='') as csvfile:
#             reader = csv.reader(csvfile)
#             for row in reader[1:]:
#                 company_id, name, founded_year, headquarters = row
#                 InsuranceCompany.objects.update_or_create(
#                     id=int(company_id),
#                     defaults={
#                         'name': name.strip(),
#                         'founded_year': int(founded_year),
#                         'headquarters': headquarters.strip()
#                     }
#                 )
#         self.stdout.write(self.style.SUCCESS('Successfully loaded insurance companies from CSV'))


class Command(BaseCommand):
    help = 'Load insurance companies from a CSV file'

    def handle(self, *args, **kwargs):
        with open('/home/dreamcar/DCB_Project/templates/Dealer/insurance/insurer.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            for row in reader:
                # Extracting the fields from the row
                company_id = int(row[0])  # Convert the first column to an integer (S NO)
                name = row[1]
                founded_year = int(row[2])  # Convert the year to an integer
                headquarters = row[3]

                # Create or update the company in the database
                InsuranceCompany.objects.update_or_create(
                    id=company_id,
                    defaults={
                        'name': name,
                        'founded_year': founded_year,
                        'headquarters': headquarters.strip()
                    }
                )

        self.stdout.write(self.style.SUCCESS('Successfully loaded insurance companies.'))