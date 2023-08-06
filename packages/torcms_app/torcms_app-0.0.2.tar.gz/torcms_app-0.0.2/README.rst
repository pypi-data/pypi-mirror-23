yunsuan
================

安装
-------------

源代码部署。


首次安装
----------------------

Building the environment


::

    ~/usr/python36/bin/python3 -m venv ~/vpy_yunsuan
    source ~/vpy_yunsuan/bin/activate
    pip3 install -r doc/requirements.txt
    git clone https://github.com/bukun/torcms_modules_bootstrap.git templates/modules




Database
----------------------

::

    \set dbname yunsuan
    CREATE USER :dbname WITH PASSWORD '131322' ; 
    CREATE DATABASE :dbname OWNER :dbname ;
    GRANT ALL PRIVILEGES ON DATABASE :dbname to :dbname ;
    \c :dbname ;
    create extension hstore;
    \q
