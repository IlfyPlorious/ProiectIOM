import os


class Tag:
    def __init__(self, tag_id, name) -> None:
        self.tag_id = tag_id
        self.name = name

    def __str__(self) -> str:
        return f'No.{self.tag_id}\tName:{self.name}'


class Image:
    def __init__(self, image_id, path=None, name='Image', description=None, tags=None) -> None:
        if tags is None:
            tags = []
        self.image_id = image_id
        self.path = path
        self.name = name
        self.description = description
        self.tags = tags
        self.image_size_in_bytes = os.path.getsize(self.path)
        self.image_size_in_kilobytes = self.image_size_in_bytes / 1024
        self.image_size_in_megabytes = self.image_size_in_kilobytes / 1024

    def __str__(self) -> str:
        return f'Image no.{self.image_id}\tName:{self.name}\n{self.description}'

    def get_tags(self):
        tags_string = ''
        for tag in self.tags:
            tags_string += f', {tag}'

        tags_string = tags_string.replace(',', '', 1)
        tags_string = tags_string.replace(' ', '', 1)

        return tags_string

    def get_dimension(self, precision):
        if str(precision).lower() == 'mb':
            return '{:.2f} Mb'.format(self.image_size_in_megabytes)
        elif str(precision).lower() == 'kb':
            return '{:.2f} Kb'.format(self.image_size_in_kilobytes)
        else:
            return '{:.2f} bytes'.format(self.image_size_in_bytes)

#    def display_image(self, width=125, height=125):
#        global img
#        img = PIL.Image.open(str(self.path))
#        img = img.resize((width, height))
#        img = PIL.ImageTk.PhotoImage(img)
#        return img
