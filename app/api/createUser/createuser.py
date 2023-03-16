import string
def createUser():
    try:
        args = request.args.to_dict()
        username = args.get("username")
        password = args.get("password")
        #rdata = createUser(username, password)
        rdata = self.auth.test
        print(rdata)

        #resp = jsonify(rdata)   # jsonify provides us with a full response
        #resp.headers.add('Access-Control-Allow-Origin', '*')
        resp = "bladi" 
        return resp

    except Exception as e: 
        raise e
        # 500 error
        return HttpResponse.getDefault(False)
pass

def createUser(self, username : string, password : string):
    try:
        samdb.newuser(username=username,password=password)
    except:
        samdb.transaction_cancel()
        raise
    else:
        samdb.transaction_commit()

    return 'User %s created' % username