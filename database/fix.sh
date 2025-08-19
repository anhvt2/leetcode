#!/bin/bash
sqlfluff fix $1 --dialect mysql
# sqlfluff lint $1 --dialect mysql