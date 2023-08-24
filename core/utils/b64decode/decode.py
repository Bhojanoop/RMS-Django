import base64

class Decode:
    @staticmethod
    def decode(encoded_str):
        try:
            return base64.b64decode(encoded_str)
        except Exception as e:
            raise Exception(str(e))