#!/usr/bin/env python3
#
#

import os
import sys
import os.path

def j(*args):
    if not args: return
    todo = list(map(str, filter(None, args)))
    return os.path.join(*todo)

if sys.version_info.major < 3:
    print("you need to run evrm with python3")
    os._exit(1)

try:
    use_setuptools()
except:
    pass

try:
    from setuptools import setup
except Exception as ex:
    print(str(ex))
    os._exit(1)

target = "evrm"
upload = []

def uploadfiles(dir):
    upl = []
    if not os.path.isdir(dir):
        print("%s does not exist" % dir)
        os._exit(1)
    for file in os.listdir(dir):
        if not file or file.startswith('.'):
            continue
        d = dir + os.sep + file
        if not os.path.isdir(d):
            if file.endswith(".pyc") or file.startswith("__pycache"):
                continue
            upl.append(d)
    return upl

def uploadlist(dir):
    upl = []

    for file in os.listdir(dir):
        if not file or file.startswith('.'):
            continue
        d = dir + os.sep + file
        if os.path.isdir(d):   
            upl.extend(uploadlist(d))
        else:
            if file.endswith(".pyc") or file.startswith("__pycache"):
                continue
            upl.append(d)

    return upl

setup(
    name='evrm',
    version='35',
    url='https://bitbucket.org/thatebart/evrm',
    author='Bart Thate',
    author_email='bthate@dds.nl',
    description="Gif toedienende artsen de cel in !!".upper(),
    license='MIT',
    include_package_data=True,
    zip_safe=False,
    install_requires=["botlib"],
    scripts=["bin/evrm"],
    packages=['evrm', ],
    long_description='''

De patient heeft recht op zorg/verpleging zonder dat er strafbare feiten gepleegd worden, het slachtoffer heeft recht op vervolging van de gif toedienende arts.

| 1. direct bekend te maken dat deze medicatie gif zijn en ze van de markt af te halen.

| 2. direct een einde te zetten aan de vergiftigingen in de GGZ, gif toedienen is strafbaar.

| 3. direct de politie zelf bloedspiegels laten nemen om daarmee mishandeling bewijzen.

| 4. direct van alle nederlanders de medische dossiers opvragen om toediening van gif te kunnen vaststellen.

| 5. direct de noodzakelijke verpleging die deze slachtoffers van vergiftiging nodig hebben direct te leveren, ook in weekend en avonduren.

(1) Hersenweefselverlies door Haldol etc. - http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3476840/
(2) Europese Chemicals database voor de algemene bekendheid -  https://echa.europa.eu/search-for-chemicals

| email is bthate@dds.nl or thatebart@gmail.com 
| botfather on #dunkbots irc.freenode.net



''',
   data_files=[("docs", ["docs/conf.py","docs/index.rst"]),
               (j('docs', 'jpg'), uploadlist(j("docs","jpg"))),
               (j('docs', 'txt'), uploadlist(j("docs", "txt"))),
               (j('docs', '_templates'), uploadlist(j("docs", "_templates")))
              ],
   package_data={'': ["*.crt"],
                 },
   classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Utilities'],
)
