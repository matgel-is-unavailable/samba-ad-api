#!/bin/bash
docker build -t samba-ad-api:test -f docker/Dockerfile .
docker build -t samba-activedirectory:test -f /mnt/dev/docker/images/samba-activedirectory/Dockerfile /mnt/dev/docker/images/samba-activedirectory
bash dev_restart.sh