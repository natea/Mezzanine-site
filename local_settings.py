
DEV_SERVER = True
DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "sqlite3",
        "NAME": "mezzanine.db",
    }
}

if PACKAGE_NAME_FILEBROWSER in INSTALLED_APPS:
    FILEBROWSER_URL_FILEBROWSER_MEDIA = "/site_media/filebrowser"
    FILEBROWSER_PATH_FILEBROWSER_MEDIA = os.path.join(
              _package_path(PACKAGE_NAME_FILEBROWSER), "site_media", "filebrowser")

