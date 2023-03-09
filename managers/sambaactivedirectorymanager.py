import string
import getpass
import ldb
from samba.auth import system_session
from samba.credentials import Credentials
from samba.dcerpc import security
from samba.dcerpc.security import dom_sid
from samba.ndr import ndr_pack, ndr_unpack
from samba.param import LoadParm
from samba.samdb import SamDB
from typing import List
from unittest import result

class SambaActiveDirectoryManager:
    lp = LoadParm()
    creds = Credentials()
    creds.guess(lp)
    samdb = SamDB(url='/var/lib/samba/private/sam.ldb', session_info=system_session(),credentials=creds, lp=lp)    
    def createUser(self, username : string, password : string):
        try:
            self.samdb.transaction_start()
            self.samdb.newuser(username=username,password=password)
        except:
            self.samdb.transaction_cancel()
            raise
        else:
            self.samdb.transaction_commit()

        return 'User %s created' % username

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
