from __future__ import annotations

import os
import re
import time
from typing import Final

import cloudinary
from cloudinary.api import delete_resources
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

from src.utils.interfaces import ImageBase
from src.utils.util_functions import get_path_to_src

__all__ = ['Cloudnary']


def _parse_url(image_url: str):
    index = re.search('image/upload/(v\\d+/)?', image_url)
    if index is None:
        raise ValueError

    image_path = image_url[index.end():]
    if (index := re.search('/.+$', image_path)) is None:
        folder = None
        full_image_id = image_path
    else:
        index = index.start()
        folder = image_path[:index]
        full_image_id = image_path[index + 1:]

    try:
        index = full_image_id.index('.')
        image_id = full_image_id[:index]
    except ValueError:
        image_id = full_image_id

    return folder, image_id


# noinspection SpellCheckingInspection
class Cloudnary(ImageBase):
    class Image:
        def __init__(self, image_url: str):
            folder, image_id = _parse_url(image_url)
            self.folder: Final[str] = folder
            self.image_id: Final[str] = image_id

        def __str__(self) -> str:
            return f'{self.folder}/{self.image_id}'

    def __init__(self, cloud_name: str, api_key: int, api_secret: str):
        """
        :raises cloudinary.exceptions.AuthorizationRequired: if not valid
            `cloud_name` or `api_key` or `api_secret`
        """
        cloudinary.config(
            cloud_name=cloud_name,
            api_key=api_key,
            api_secret=api_secret
        )
        cloudinary.api.subfolders('/')  # check authorization

    def save(self, data: bytes, folder: str = None) -> str:
        filename = f'{get_path_to_src()}/utils/{int(time.time() * 10 ** 7)}.jpg'
        try:
            with open(filename, 'wb') as image:
                image.write(data)
            image_id = upload(
                filename,
                folder=folder
            )['public_id']
        except Exception:
            raise Exception  # TODO: log error
        finally:
            os.remove(filename)
        return cloudinary_url(image_id)

    def delete(self, url: str) -> None:
        try:
            image: Cloudnary.Image = self.Image(url)
            delete_resources(str(image))
        except ValueError:  # TODO: log error
            pass
