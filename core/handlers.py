import secrets


def file_upload_handler(instance, filename):
    extension = filename.split(".")[-1]
    filename = "%s.%s" % (secrets.token_hex(10), extension)
    return "%s/%s" % (extension, filename)
