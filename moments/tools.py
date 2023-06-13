import os
import shutil
import sys
import json
from jina import Document, DocumentArray
from config import RANDOM_SEED


def prep_docs(input_file, num_docs=None, shuffle=True):
    docs = DocumentArray()
    memes = []
    print(f"Processing {input_file}")
    with open(input_file, "r") as file:
        raw_json = json.loads(file.read())

    for template in raw_json:
        for meme in template["generated_memes"]:
            meme["template"] = template["name"]
        memes.extend(template["generated_memes"])

    if shuffle:
        import random

        random.seed(RANDOM_SEED)
        random.shuffle(memes)

    for meme in memes[:num_docs]:
        doctext = f"{meme['template']} - {meme['caption_text']}"
        doc = Document(text=doctext)
        doc.tags = meme
        doc.tags["uri_absolute"] = "http" + doc.tags["image_url"]
        docs.extend([doc])

    return docs

def write_list(save_path, list_file):
    with open(save_path, "w", encoding='utf8') as file:
        for singleton in list_file:
            file.write(json.dumps(singleton, ensure_ascii=False) + "\n")
    return 

def make_dir(save_path : str):
  isExist = os.path.exists(save_path)
  if not isExist:
    os.makedirs(save_path)
    print("The new directory is created!")