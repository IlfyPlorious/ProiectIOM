import os
import time

from inout.io_operations import *
from models.model import Tag
import uuid

# tag1 = Tag(tag_id=uuid.uuid4(), name="Vulpe")
#
# # init_tags_csv()
# write_tag_csv(tag=tag1)
#
# tags = read_tags_csv()
# for tag in tags:
#     if tag.name == "Maimuta":
#         update_tag_by_id(tag_id=tag.tag_id, new_name="Ciocanitoare")
#
# tags = read_tags_csv()
# for tag in tags:
#     print(str(tag))

images = read_images_csv()

print(images[0].tags)
# add_tag_to_image(image_id=images[0].image_id, tag='Popcorn')
delete_tag_from_image(image_id=images[0].image_id, tag='Zburatoare')

images = read_images_csv()
print(images[0].tags)
