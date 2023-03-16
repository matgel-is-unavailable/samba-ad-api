import string
def updatePassword(self, username : string, password : string):
    try:
        self.samdb.transaction_start()
        self.samdb.setpassword('(sAMAccountName=%s)' % username, password, force_change_at_next_login=False, username=None)
    except:
        self.samdb.transaction_cancel()
        raise
    else:
        self.samdb.transaction_commit()
    return 'Password of the user %s is updated' % username