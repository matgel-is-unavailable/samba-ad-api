import json
import string

class HttpResponse:
    @staticmethod
    def getDefault(success : bool) -> string:
        code = 500
        if success:
            code = 200
        return json.dumps({'success': success}), code, {'ContentType':'application/json'} 