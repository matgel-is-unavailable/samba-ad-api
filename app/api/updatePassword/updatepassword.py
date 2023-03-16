import string
def updatePassword(username : string, password : string, samdb):
    try:
        samdb.transaction_start()
        samdb.setpassword('(sAMAccountName=%s)' % username, password, force_change_at_next_login=False, username=None)
    except:
        samdb.transaction_cancel()
        raise
    else:
        samdb.transaction_commit()

    return 'Password of the user %s is updated' % username