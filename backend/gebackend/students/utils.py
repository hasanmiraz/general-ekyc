from django.utils import timezone

def student_upload_path(instance, filename):
    return f"student_images/{instance.student.student_number}/{timezone.now():%Y/%m}/{filename}"