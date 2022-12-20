from inout.io_operations import *
from models.model import Tag
import uuid

tag1 = Tag(tag_id=uuid.uuid4(), name="Vulpe")

# init_tags_csv()
write_tag_csv(tag=tag1)

tags = read_tags_csv()
for tag in tags:
    if tag.name == "Maimuta":
        update_tag_by_id(tag_id=tag.tag_id, new_name="Ciocanitoare")

tags = read_tags_csv()
for tag in tags:
    print(str(tag))
