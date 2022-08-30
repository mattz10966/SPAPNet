#!/usr/bin/env python
import argparse
import sys
import os
# torchlight
import torchlight
from torchlight import import_class

if __name__ == '__main__':
    print('Trainning with an example data on multiclass classification task')
    print('=========Val set:01,  Result=========')
    os.system('python main.py recognition -c config/train.yaml')




