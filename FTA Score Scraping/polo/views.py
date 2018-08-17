from django.shortcuts import render
from tablib import Dataset


def simple_upload(request):
    if request.method == 'POST':
        competition_resource = CompetitionResource()
        dataset = Dataset()
        new_competition = request.FILES['myfile']

        imported_data = dataset.load(new_competition.read())
        result = competition_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            competition_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'simple_upload.html')
