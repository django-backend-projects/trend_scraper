
from django.utils.timezone import make_aware
import openpyxl
from django.core.files.storage import default_storage


from app.core.models import ExcellAsanInfo


def upload_func():
    list_1 = [] 
    
    # Get the last record
    record = ExcellAsanInfo.objects.last()

    if record and record.file:
        # Open the Excel file using openpyxl
        file_path = default_storage.path(record.file.name)
        print("file_path", file_path)
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active

        # Assuming the headers are in the first row
        # headers = [cell.value for cell in next(sheet.iter_rows(values_only=True))]
        headers = [cell for cell in next(sheet.iter_rows(values_only=True))]

        # Verify if headers are present
        if all(header in headers for header in ["UserID", "FIN", "Pass"]):
            for row in sheet.iter_rows(min_row=2, values_only=True):
                list_1.append(
                    {
                        "UserID": row[headers.index("UserID")],
                        "FIN": row[headers.index("FIN")],
                        "Pass": row[headers.index("Pass")],
                    }
                )
        print("list_1", list_1)
        workbook.close()


upload_func()