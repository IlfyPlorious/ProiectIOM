import csv
import os
import uuid
from models.model import Tag, Image


def init_tags_csv(file='tags_database.csv'):
    with open(file, 'w', newline='') as csvfile:
        fieldnames = ['id', 'Name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()


def init_images_csv(file='images_database.csv'):
    with open(file, 'w', newline='') as csvfile:
        fieldnames = ['id', 'path', 'name', 'description', 'tags']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()


def read_tags_csv(file='tags_database.csv'):
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        tags = []
        for row in reader:
            tags.append(Tag(row['id'], row['Name']))

    return tags


def read_images_csv(file='images_database.csv'):
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        images = []
        for row in reader:
            images.append(
                Image(row['id'], row['path'], row['name'], row['description'], extract_array_from_string(row['tags'])))

    return images


def read_tag_by_id(file='tags_database.csv', tag_id=None):
    if tag_id is None:
        return None
    else:
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['id'] == tag_id:
                    return Tag(row['id'], row['Name'])
        csvfile.close()

    return 'Tag not found'


def read_image_by_id(file='images_database.csv', image_id=None):
    if image_id is None:
        return None
    else:
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['id'] == image_id:
                    return Image(row['id'], row['path'], row['name'], row['description'],
                                 extract_array_from_string(row['tags']))
        csvfile.close()

    return 'Image not found'


def write_tag_csv(file='tags_database.csv', tag=None):
    with open(file, 'a', newline='') as csvfile:
        fieldnames = ['id', 'Name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if tag is not None:
            writer.writerow({'id': tag.tag_id, 'Name': tag.name})


def write_image_csv(file='images_database.csv', image=None):
    with open(file, 'a', newline='') as csvfile:
        fieldnames = ['id', 'path', 'name', 'description', 'tags']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if image is not None:
            for i in range(0, len(image.tags)):
                image.tags[i] = image.tags[i].lower()
            writer.writerow(
                {
                    'id': image.image_id,
                    'path': image.path,
                    'name': image.name,
                    'description': image.description,
                    'tags': image.tags
                }
            )


def delete_tag_by_id(file='tags_database.csv', tag_id=None):
    if tag_id is None:
        print('Invalid tag id')
    else:
        lines = list()

        with open(file, 'r', newline='') as readfile:
            reader = csv.DictReader(readfile)
            for row in reader:
                if row['id'] != tag_id:
                    lines.append(row)

        with open(file, 'w', newline='') as writefile:
            fieldnames = ['id', 'Name']
            writer = csv.DictWriter(writefile, fieldnames)
            writer.writeheader()
            writer.writerows(lines)


def delete_image_by_id(file='images_database.csv', image_id=None):
    if image_id is None:
        print('Invalid image id')
    else:
        lines = list()

        with open(file, 'r', newline='') as readfile:
            reader = csv.DictReader(readfile)
            for row in reader:
                if row['id'] != image_id:
                    lines.append(row)

        with open(file, 'w', newline='') as writefile:
            fieldnames = ['id', 'Name']
            writer = csv.DictWriter(writefile, fieldnames)
            writer.writeheader()
            writer.writerows(lines)


def update_tag_by_id(file='tags_database.csv', tag_id=None, new_name=None):
    if tag_id is None:
        print('Invalid tag id')
    else:
        lines = list()

        with open(file, 'r', newline='') as readfile:
            reader = csv.DictReader(readfile)
            for row in reader:
                if row['id'] != tag_id:
                    lines.append(row)
                elif new_name is not None:
                    new_row = {
                        'id': tag_id,
                        'Name': new_name
                    }
                    lines.append(new_row)

        with open(file, 'w', newline='') as writefile:
            fieldnames = ['id', 'Name']
            writer = csv.DictWriter(writefile, fieldnames)
            writer.writeheader()
            writer.writerows(lines)


def update_image_by_id(file='images_database.csv', image_id=None, image_path=None, image_name=None,
                       image_description=None, image_tags=None):
    if image_id is None:
        print('Invalid tag id')
    else:
        lines = list()

        with open(file, 'r', newline='') as readfile:
            reader = csv.DictReader(readfile)
            for row in reader:
                if row['id'] != image_id:
                    lines.append(row)
                else:
                    new_row = {
                        'id': image_id,
                        'path': image_path if image_path is not None else row['path'],
                        'name': image_name if image_name is not None else row['name'],
                        'description': image_description if image_description is not None else row['description'],
                        'tags': image_tags if image_tags is not None else row['tags'],
                    }
                    lines.append(new_row)

        with open(file, 'w', newline='') as writefile:
            fieldnames = ['id', 'path', 'name', 'description', 'tags']
            writer = csv.DictWriter(writefile, fieldnames)
            writer.writeheader()
            writer.writerows(lines)


def delete_tags_for_image(file='images_database.csv', image_id=None):
    if image_id is None:
        print('Invalid tag id')
    else:
        lines = list()

        with open(file, 'r', newline='') as readfile:
            reader = csv.DictReader(readfile)
            for row in reader:
                if row['id'] != image_id:
                    lines.append(row)
                else:
                    new_row = {
                        'id': image_id,
                        'path': row['path'],
                        'name': row['name'],
                        'description': row['description'],
                        'tags': [],
                    }
                    lines.append(new_row)

        with open(file, 'w', newline='') as writefile:
            fieldnames = ['id', 'path', 'name', 'description', 'tags']
            writer = csv.DictWriter(writefile, fieldnames)
            writer.writeheader()
            writer.writerows(lines)


def add_tag_to_image(file='images_database.csv', image_id=None, tag: str = None):
    if tag is None:
        print('Tag is invalid')
    else:
        lines = list()

        with open(file, 'r', newline='') as readfile:
            reader = csv.DictReader(readfile)
            for row in reader:
                if row['id'] != image_id:
                    lines.append(row)
                else:
                    tags = extract_array_from_string(row['tags'])
                    tags.append(tag.lower())
                    new_row = {
                        'id': image_id,
                        'path': row['path'],
                        'name': row['name'],
                        'description': row['description'],
                        'tags': tags,
                    }
                    lines.append(new_row)

        with open(file, 'w', newline='') as writefile:
            fieldnames = ['id', 'path', 'name', 'description', 'tags']
            writer = csv.DictWriter(writefile, fieldnames)
            writer.writeheader()
            writer.writerows(lines)


def delete_tag_from_image(file='images_database.csv', image_id=None, tag=None):
    if tag is None:
        print('Tag is invalid')
    else:
        lines = list()

        with open(file, 'r', newline='') as readfile:
            reader = csv.DictReader(readfile)
            for row in reader:
                if row['id'] != image_id:
                    lines.append(row)
                else:
                    tags = extract_array_from_string(row['tags'])
                    if tag in tags:
                        tags.remove(tag)
                    new_row = {
                        'id': image_id,
                        'path': row['path'],
                        'name': row['name'],
                        'description': row['description'],
                        'tags': tags,
                    }
                    lines.append(new_row)

        with open(file, 'w', newline='') as writefile:
            fieldnames = ['id', 'path', 'name', 'description', 'tags']
            writer = csv.DictWriter(writefile, fieldnames)
            writer.writeheader()
            writer.writerows(lines)


def extract_array_from_string(string: str):
    split_string = string.split(',')
    string_array = []
    for split in split_string:
        split_copy = '' + split

        # if used to remove space that appears after ',' in csv
        if split_copy[0] == ' ':
            split_copy = split_copy[1:]

        # lines used to remove array string representation artifacts
        # csv library stores data as str(data); str(list<str>) = [ 'data' , 'data' ] so we need to remove [ ' and ]
        split_copy = split_copy.replace('[', '')
        split_copy = split_copy.replace(']', '')
        split_copy = split_copy.replace("'", "")

        string_array.append(split_copy)

    return string_array


def reload_images(path):  # in case we find a way to refresh the list of photos in case the user deletes one
    files = os.listdir(path)  # Detect in some way if changes appeared to current path
    for i in files:
        if i[-4:] != ".jpg":
            files.remove(i)

    for i in files:
        image_path = os.path.join(path, i).replace("\\", "/")
        img = Image(image_id=uuid.uuid4(), path=image_path, name=image_path.split("/")[-1])
        write_image_csv(file='images_database.csv', image=img)
