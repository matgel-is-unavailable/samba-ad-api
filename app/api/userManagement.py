import string
import ldb
from samba import dsdb
import os

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

def deleteUser(username : string, samdb):
    try:
        samdb.transaction_start()
        samdb.deleteuser(username=username)
    except:
        samdb.transaction_cancel()
        raise
    else:
        samdb.transaction_commit()

    return 'User %s deleted' % username

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

def listUsers(samdb):
    try:
        samdb.transaction_start()
        search_dn = samdb.domain_dn()
        filter_expires = ""
        current_nttime = samdb.get_nttime()
        filter_expires = "(|(accountExpires=0)(accountExpires>=%u))" % (current_nttime)
        filter_disabled = "(!(userAccountControl:%s:=%u))" % (
            ldb.OID_COMPARATOR_AND, dsdb.UF_ACCOUNTDISABLE)

        filter = "(&(objectClass=user)(userAccountControl:%s:=%u)%s%s)" % (
            ldb.OID_COMPARATOR_AND,
            dsdb.UF_NORMAL_ACCOUNT,
            filter_disabled,
            filter_expires)

        lookup = samdb.search(search_dn,
                           scope=ldb.SCOPE_SUBTREE,
                           expression=filter,
                           attrs=["samaccountname"])

        if (len(lookup) == 0):
            return
        users = []
        for entry in lookup: 
            users.append("%s" % entry.get("samaccountname", idx=0))
    except:
        samdb.transaction_cancel()
        raise
    else:
        samdb.transaction_commit()

    return 'Users: %s' % users