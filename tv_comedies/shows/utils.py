from .models import Writer

def create_writer(name, bio):
    writer = Writer()
    writer.name = name
    writer.bio = bio
    writer.save()
