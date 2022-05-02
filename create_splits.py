import argparse
import glob
import os
import random

import numpy as np

from utils import get_module_logger

import shutil

def split(data_dir):
    """
    Create three splits from the processed records. The files should be moved to new folders in the 
    same directory. This folder should be named train, val and test.

    args:
        - data_dir [str]: data directory, /home/workspace/data/waymo
    """
    
    # TODO: Split the data present in `/home/workspace/data/waymo/training_and_validation` into train and val sets.
    # You should move the files rather than copy because of space limitations in the workspace.
    
    # I learnt how to use shutil on https://stackoverflow.com/questions/53074712/how-to-split-folder-of-images-into-test-training-validation-sets-with-stratified
    val_directory = data_dir+'/val'
    train_directory = data_dir+'/train'
    src = data_dir+'/training_and_validation'

    all_files = os.listdir(src)
    np.random.shuffle(all_files)
    
    source_len = int(len(all_files))
    train_FileNames, val_FileNames = np.split(np.array(all_files),[int(source_len*0.8)])
    
    train_FileNames = [src+'/'+ name for name in train_FileNames.tolist()]
    val_FileNames = [src+'/' + name for name in val_FileNames.tolist()]
    
    for name in train_FileNames:
        shutil.move(name, train_directory)

    for name in val_FileNames:
        shutil.move(name, val_directory)
    
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data-dir', required=True,
                        help='data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.data_dir)