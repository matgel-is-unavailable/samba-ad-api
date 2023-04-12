from samba.netcmd.gpo import *
import ldb
import json

def listGPO(samdb):
    # list in a list
    gpos = []
    msg = get_gpo_info(samdb, None)

    for m in msg:
        #print("DEBUG: " + str(m['name'][0]))
        gpo = {
         #str(m['name'][0]).split("'")[1::2]
            "gpo":str(m['name'][0]), "displayname":str(m['displayName'][0]), "path":str(m['gPCFileSysPath'][0]), "dn":str(m.dn), "version":str(attr_default(m, 'versionNumber', '0')), "flags":gpo_flags_string(int(attr_default(m, 'flags', 0)))
        }
        gpos.append(gpo)
    json.dumps(gpos)
    return gpos