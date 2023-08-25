from core.utils.b64decode.decode import Decode

class Store:

    @staticmethod
    def store(filename:str,fileobj:object):
        try:
            with open(f'media/{filename}','wb') as f:
                f.write(Decode.decode(fileobj))
                f.close()
        except Exception as e:
            raise Exception(str(e))