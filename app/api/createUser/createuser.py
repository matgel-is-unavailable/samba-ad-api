import string
def createUser(username : string, password : string, samdb):
    try:
        samdb.transaction_start()
        samdb.newuser(username=username,password=password)
    except:
        samdb.transaction_cancel()
        raise
    else:
        samdb.transaction_commit()

    return 'User %s created' % username