#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 * Created by PyCharm.
 * User: Spkiddai
 * Date: 2021-3-10
"""

import subprocess,yaml

with open('sys_config.yaml', 'r', encoding='utf-8') as config_yaml:
    sys_config = yaml.load(config_yaml, Loader=yaml.FullLoader)


gencash = ['./'+sys_config['xray']['name'], 'genca']
gencasp = subprocess.Popen(gencash)
gencasp.communicate()