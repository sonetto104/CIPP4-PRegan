import os


def validate_image_size(value):
    
    max_size = 1024 * 1024 * 10  # 10 MB

    if value.size > max_size:
        raise ValidationError("File size exceeds the limit of 10 MB.")