import os
from io import BytesIO

import logging
import typing
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter

from preview_generator import file_converter

from preview_generator.factory import PreviewBuilderFactory


class PreviewBuilderInterface(object):
    pass


class PreviewBuilderMeta(type):
    def __new__(mcs, *args: str, **kwargs: int) -> typing.Type[
        'PreviewBuilder']:
        cls = super().__new__(mcs, *args, **kwargs)
        cls = typing.cast(typing.Type['PreviewBuilder'], cls)
        cls.register()
        return cls


class PreviewBuilder(object, metaclass=PreviewBuilderMeta):
    mimetype = []  # type: typing.List[str]

    def __init__(
            self,
    ) -> None:
        logging.info('New Preview builder of class' + str(self.__class__))

    @classmethod
    def get_mimetypes_supported(
            cls,
    ) -> typing.List[str]:
        return cls.mimetype

    def get_page_number(self, file_path: str, preview_name: str,
                        cache_path: str) -> int:
        """
        Get the number of page of the document
        """
        raise Exception(
            'Number of pages not supported for this kind of Preview'
            ' Builder. Your preview builder must implement a '
            'get_page_number method with the same signature as in'
            'PreviewBuilder'
        )

    def build_jpeg_preview(self, file_path: str, preview_name: str,
                           cache_path: str, page_id: int,
                           extension: str = '.jpg',
                           size: typing.Tuple[int, int] = (256, 256)) -> None:
        """
        generate the jpg preview
        """
        raise Exception("Not implemented for this kind of document")

    def build_pdf_preview(self, file_path: str, preview_name: str,
                          cache_path: str, extension: str = '.pdf',
                          page_id: int = -1) -> None:
        """
        generate the jpeg preview
        """
        raise Exception("Not implemented for this kind of document")

    def build_html_preview(self, file_path: str, preview_name: str,
                           cache_path: str, extension: str = '.html') -> None:
        """
        generate the html preview
        """
        raise Exception("Not implemented for this kind of document")

    def build_json_preview(self, file_path: str, preview_name: str,
                           cache_path: str, page_id: int = 0,
                           extension: str = '.json') -> None:
        """
        generate the json preview
        """
        raise Exception("Not implemented for this kind of document")

    def build_text_preview(self, file_path: str, preview_name: str,
                           cache_path: str, page_id: int = 0,
                           extension: str = '.txt') -> None:
        """ 
        return file content from the cache
        """
        raise Exception("Not implemented for this kind of document")

    def get_original_size(self, file_path: str, page_id: int=-1) -> typing.Tuple[int, int]:
        raise Exception("Not implemented for this kind of document")

    @classmethod
    def register(cls) -> None:
        PreviewBuilderFactory.get_instance().register_builder(cls)




class OnePagePreviewBuilder(PreviewBuilder):
    '''
    Generic preview handler for single page document
    '''

    def get_page_number(self, file_path: str, preview_name: str,
                        cache_path: str) -> int:
        return 1


class ImagePreviewBuilder(OnePagePreviewBuilder):
    '''
    Generic preview handler for an Image (except multi-pages images)
    '''

    def build_json_preview(self, file_path: str, preview_name: str,
                           cache_path: str, page_id: int = 0,
                           extension: str = '.json') -> None:
        """
        generate the json preview
        """

        with open(file_path, 'rb') as img:
            result = file_converter.image_to_json(img)
            with open(cache_path + preview_name + extension, 'wb') as jpeg:
                buffer = result.read(1024)
                while buffer:
                    jpeg.write(buffer)
                    buffer = result.read(1024)
