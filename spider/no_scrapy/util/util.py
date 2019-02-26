#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 2019/2/26
import os

def mkdirs_if_not_exists(directory_):
    """
    create a new folder if it does not exist
    """
    if not os.path.exists(directory_) or not os.path.isdir(directory_):
        os.makedirs(directory_)