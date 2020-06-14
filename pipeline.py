import logging
import os
import shutil
logging.basicConfig(level=logging.INFO)
import subprocess


logger = logging.getLogger(__name__)
news_sites_uids = ['elpais']


def main():
    _extract()
    _transform()
    _load()


def _extract():
    logger.info('Starting extract process')
    files = os.listdir('./extract')
    for news_site_uid in news_sites_uids:
        subprocess.run(['python', 'main.py', news_site_uid], cwd='./extract')
        #subprocess.run(['mv', '{}', '../transform/{}.csv'.format(news_site_uid), ';'], cwd='./extract')
    for i in range(len(files)):
        if ".csv" in files[i]:
            shutil.move(os.getcwd()+os.sep+'extract'+os.sep+files[i],os.getcwd()+os.sep+'transform')


def _transform():
    logger.info('Starting transform process')
    files = os.listdir('./transform')
    print(files)
    for file in files:
        if '.csv' in file:
            dirty_data_filename = file
            clean_data_filename = 'clean_{}'.format(dirty_data_filename)
            subprocess.run(['python', 'main.py', dirty_data_filename], cwd='./transform')
            #os.remove(file)
    files2 = os.listdir('./transform')
    for i in range(len(files2)):
        if "clean" in files2[i]:
            shutil.move(os.getcwd()+os.sep+'transform'+os.sep+files2[i],os.getcwd()+os.sep+'load')

def _load():
    logger.info('Starting load process')
    files = os.listdir('./load')
    print(files)
    for file in files:
        if '.csv' in file:
            clean_data_filename = file
            subprocess.run(['python', 'main.py', clean_data_filename], cwd='./load')
        
  # files = os.listdir('./load')
  # for i in range(len(files)):
  #     if ".csv" in files[i]:
  #         os.remove(files[i])


if __name__ == '__main__':
    main()