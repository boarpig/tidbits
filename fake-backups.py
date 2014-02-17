#!/usr/bin/python
# 
# this script generates few years worth of "fake" backup file names which you
# can 'touch' into files
# 
# for i in "$(fake-backup.py)"; do
# touch "$i"
# done
#
# on command line. This was written to test my backup smart purge utility

prefix = "backup"
suffix = "tar.gz"

for year in range(2000, 2015):
    for month in range(1, 13):
        for day in range(1, 28):
            name = "{}-{}-{:0=2d}-{:0=2d}.{suffix}".format(prefix, year, month,
                                                           day, suffix)
            print(name)

