from ..schema.file_schema import File

def Save(file):
    saveFile=File(
        path=file["path"],
        createdAt=file["createdAt"],
        filename=file["filename"],
        size=file["size"]
    )

    saveFile.save()

def Find(**kwargs):
    results=File.objects(**kwargs).to_json()
    return results