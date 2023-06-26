# import os
# import cloudinary
# from cloudinary.uploader import upload
# if os.path.isfile('env.py'):
#     import env

# cloudinary.config(
#     cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
#     api_key=os.environ.get('CLOUDINARY_API_KEY'),
#     api_secret=os.environ.get('CLOUDINARY_API_SECRET')
# )


# def cloudinary_handler(file):
#     result = upload(file)

#     # Process the result and return relevant attachment information
#     attachment_url = result['secure_url']
#     attachment_format = result['format']
#     attachment_size = result['bytes']

#     return {
#         'url': attachment_url,
#         'format': attachment_format,
#         'size': attachment_size
#     }

