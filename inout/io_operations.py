import csv

from models.model import Tag


def init_tags_csv(file='tags_database.csv'):
    with open(file, 'w', newline='') as csvfile:
        fieldnames = ['id', 'Name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()


def read_tags_csv(file='tags_database.csv'):
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        tags = []
        for row in reader:
            tags.append(Tag(row['id'], row['Name']))

    return tags


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


def write_tag_csv(file='tags_database.csv', tag=None):
    with open(file, 'a', newline='') as csvfile:
        fieldnames = ['id', 'Name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if tag is not None:
            writer.writerow({'id': tag.tag_id, 'Name': tag.name})


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
