import os
import zipfile
import datetime


def pack():
    # Remove old archive
    for item in os.listdir('.'):
        if item.endswith(".zip"):
            os.remove(item)

    # Създай уникално име на архива
    dt = datetime.datetime.now().strftime('%H-%M_%d.%m.%y')
    with zipfile.ZipFile(f'submission-{dt}.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        excluded_dirs = ['.venv', 'venv', '.idea', '__pycache__', 'pycache', '__MACOS']

        for root, dirs, files in os.walk(os.getcwd()):
            # Филтрирай директориите на място, така че да не се обхождат
            dirs[:] = [d for d in dirs if not any(ex in d for ex in excluded_dirs)]

            for file in files:
                file_path = os.path.join(root, file)

                if not any(ex in file_path for ex in excluded_dirs):
                    archive_path = os.path.relpath(file_path, os.getcwd())
                    zipf.write(file_path, archive_path)

    print('Submission created!')


if __name__ == '__main__':
    pack()
