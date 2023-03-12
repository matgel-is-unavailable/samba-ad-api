#!/bin/bash
docker-compose -f docker/docker-compose.yml up -d
docker exec -it samba-ad-api bash