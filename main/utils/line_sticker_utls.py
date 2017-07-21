class StickerUtils:
    URI_SCHEME = "sticker"

    @staticmethod
    def id_to_uri(package_id: str, sticker_id: str) -> str:
        """
        convert sticker id to a uri that can be easily store as a str.
        
        :param package_id: the package id of the sticker.
        :type  package_id: str
        
        :param sticker_id: the sticker id of the sticker.
        :type  sticker_id: str
        
        :return: a uri. e.g. 'sticker://{package_id}/{sticker_id}'
        """
        return StickerUtils.URI_SCHEME + "://" + package_id + "/" + sticker_id

    @staticmethod
    def uri_to_id(uri: str) -> (str, str):
        data = uri.replace(StickerUtils.URI_SCHEME, '').replace('://', '').split('/')
        return data[0], data[1]
