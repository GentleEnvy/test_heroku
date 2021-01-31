from __future__ import annotations

import os
import re
import time
from logging import warning, exception
from typing import Final

import cloudinary
from cloudinary.api import delete_resources
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

from src.utils.interfaces import ImageBase
from src.utils.functions import get_path_to_src

# noinspection SpellCheckingInspection
__all__ = ['Cloudnary']


def _parse_url(image_url: str) -> tuple[str, str]:
    index = re.search('image/upload/(v\\d+/)?', image_url)
    if index is None:
        raise ValueError

    try:
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
    except Exception as e:  # FIXME: check raises
        exception(f'image_url = {image_url}')
        raise e


# noinspection SpellCheckingInspection
class Cloudnary(ImageBase):
    class Image:
        def __init__(self, image_url: str):
            folder, image_id = _parse_url(image_url)
            self.folder: Final[str] = folder
            self.image_id: Final[str] = image_id

        @property
        def id(self) -> str:
            if self.folder is None:
                return self.image_id
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

    def save(self, image_data, folder=None) -> str:
        filename = f'{get_path_to_src()}/utils/{int(time.time() * 10 ** 7)}.jpg'
        try:
            with open(filename, 'wb') as image:
                image.write(image_data)
            image_id = upload(
                filename,
                folder=folder
            )['public_id']
        except cloudinary.exceptions.Error:
            raise ValueError
        except:  # FIXME: check raises
            raise exception(f'{folder = }')
        finally:
            os.remove(filename)
        return cloudinary_url(image_id)[0]

    def delete(self, url) -> None:
        try:
            image: Cloudnary.Image = self.Image(url)
            delete_resources(image.id)
        except ValueError:
            warning(f'Couldn\'t parse url: {url}')
