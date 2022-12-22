import matplotlib.pyplot as plt


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

    def __str__(self) -> str:
        return f'Image no.{self.image_id}\tName:{self.name}\n{self.description}'

    def display_image(self):
        image = plt.imread(self.path)
        plt.figure()
        plt.title(self.name)
        plt.imshow(image)
        plt.show()