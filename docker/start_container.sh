#!/bin/bash
#port 80 is mapped to port 3000 inside the container
docker run -v ~/web1:/web1 -p 80:3000 -it web1 /bin/sh
