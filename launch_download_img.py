import os

import pandas as pd

from scraping import image
import tqdm

# Import data processed
path_conf_json = os.path.normpath(os.path.join(os.getcwd(), "data", "data_processed.csv"))
data = pd.read_csv(path_conf_json)
data["id"] = data.index

# Image Download
for id, url in tqdm.tqdm(zip(data.id, data.img_url)):
    image.download_save_img(url, id)
