import urllib
import requests
from PIL import Image
from io import BytesIO
import numpy as np

def download_img_to_array(url, img_size = (224,224)):
    """Extract image from a image url

    Parameters
    ----------
    url : str
    img_size : tuple of pixel number

    Returns
    -------
    numpy array : image in a numpy array
    """
    #
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = np.array(img.resize(img_size))
    img = img.astype('float16')/255
    return img

def download_save_img(url, id):
    """Download and save image

    Parameters
    ----------
    url : str
    img_size : tuple of pixel number

    Returns
    -------
    numpy array : image in a numpy array
    """
    path_img = "data/images/image_{}.jpg".format(id)
    urllib.request.urlretrieve(url, path_img)



