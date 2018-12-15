RESSOURCES_PATH = "ressources/"
IMAGES_PATH = RESSOURCES_PATH + "images/"


def get_image(name):
    """
    Get an image by is name
    :param name: name of the image
    :type name: str
    :return: path of the image
    :exception IOError
    """
    import os
    if not os.path.isfile(IMAGES_PATH + name):
        raise IOError("This image doesn't exist !")
    return IMAGES_PATH + name
