#!/bin/bash
docker run --rm -it -v `pwd`:/docs -p 8000:8000 squidfunk/mkdocs-material