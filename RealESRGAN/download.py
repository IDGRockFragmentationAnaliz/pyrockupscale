import argparse
import contextlib
import datetime
import os
import six
import sys
import time
import unicodedata

import dropbox
ACCESS_TOKEN = ("sl.B-i4N8woC988uYigeLIy3muusuKWqnPnFYGcmRRqZ4_"
                "PJ6KdooXLebVsxq1bLmdge1QK1JDWmnn4ft6hbl1PrJPg2"
                "2yVjVkzq8rUM5YEV8_vlzdBYZ8bJq4gJJilGTGK-0Mnuag"
                "2B0vw")
link = "https://www.dropbox.com/scl/fi/fq4sxvr1q7vzawbeucm88/RealESRGAN_x2.pth?rlkey=v796lpud503gbdok7hc83xi79&st=xh9gyht1&dl=0"
#link = '/%s/%s/%s' % (folder, subfolder.replace(os.path.sep, '/'), name)

dbx = dropbox.Dropbox(ACCESS_TOKEN)
md, res = dbx.files_download(link)

def download(dbx, folder, subfolder, name):
    """Download a file.

    Return the bytes of the file, or None if it doesn't exist.
    """
    path = '/%s/%s/%s' % (folder, subfolder.replace(os.path.sep, '/'), name)
    while '//' in path:
        path = path.replace('//', '/')
    with stopwatch('download'):
        try:
            md, res = dbx.files_download(path)
        except dropbox.exceptions.HttpError as err:
            print('*** HTTP error', err)
            return None
    data = res.content
    print(len(data), 'bytes; md:', md)
    return data