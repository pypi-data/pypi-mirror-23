BGmi
====
BGmi is a cli tool for subscribed bangumi.

|travis|
|pypi|

====
TODO
====
Empty as my wallet.

==========
Update Log
==========
+ Search / Download bangumi filter by regex
+ Download specified episode
+ Transmission-rpc support
+ Remove aria2 download method
+ Followed Bangumis Calendar for iOS / Android
+ Bugs fixed

=======
Feature
=======
+ Subscribe/unsubscribe bangumi
+ Bangumi calendar
+ Bangumi episode information
+ Download bangumi by subtitle group
+ Web page to view all subscribed bangumi
+ RSS feed for uTorrent
+ Play bangumi online with danmaku
+ Download bangumi by specified keywords (included and excluded).
+ **BGmi have supported Windows now**

.. image:: https://raw.githubusercontent.com/RicterZ/BGmi/master/images/bgmi.png
    :alt: BGmi
    :align: center
.. image:: https://raw.githubusercontent.com/RicterZ/BGmi/master/images/bgmi_http.png
    :alt: BGmi HTTP Service
    :align: center
.. image:: https://raw.githubusercontent.com/RicterZ/BGmi/master/images/bgmi_player.png
    :alt: BGmi HTTP Service
    :align: center

============
Installation
============
For **Mac OS X / Linux / Windows**:

.. code-block:: bash

    git clone https://github.com/RicterZ/BGmi
    cd BGmi
    python setup.py install

Or use pip:

.. code-block:: bash

    pip install bgmi

=============
Usage of bgmi
=============

Show bangumi calendar:

.. code-block:: bash

    bgmi cal all


Subscribe bangumi:

.. code-block:: bash

    bgmi add "Re:CREATORS" "夏目友人帐 陆" "进击的巨人 season 2"
    bgmi add "樱花任务" --episode 0


Unsubscribe bangumi:

.. code-block:: bash

    bgmi delete --name "Re:CREATORS"


Update bangumi database which locates at ~/.bgmi/bangumi.db defaultly:

.. code-block:: bash

    bgmi update --download
    bgmi update "从零开始的魔法书" --download 2 3
    bgmi update "时钟机关之星" --download


Set up the bangumi subtitle group filter and fetch entries:

.. code-block:: bash

    bgmi list
    bgmi fetch "Re:CREATORS"
    bgmi filter "Re:CREATORS" --subtitle "DHR動研字幕組,豌豆字幕组" --include 720P --exclude BIG5
    bgmi fetch "Re:CREATORS"
    # remove subtitle, include and exclude keyword filter and add regex filter
    bgmi filter "Re:CREATORS" --subtitle "" --include "" --exclude "" --regex
    bgmi filter "Re:CREATORS" --regex "(DHR動研字幕組|豌豆字幕组).*(720P)"
    bgmi fetch "Re:CREATORS"


Search bangumi and download:

.. code-block:: bash

    bgmi search '为美好的世界献上祝福！' --regex-filter '.*动漫国字幕组.*为美好的世界献上祝福！].*720P.*'
    # download
    bgmi search '为美好的世界献上祝福！' --regex-filter '.*合集.* --download


Modify bangumi episode:

.. code-block:: bash

    bgmi list
    bgmi mark "Re:CREATORS" 1


Manage download items:

.. code-block:: bash

    bgmi download --list
    bgmi download --list --status 0
    bgmi download --mark 1 --status 2

Status code:

+ 0 - Not downloaded items
+ 1 - Downloading items
+ 2 - Downloaded items

Show BGmi configure and modify it:

.. code-block:: bash

    bgmi config
    bgmi config ARIA2_RPC_TOKEN 'token:token233'

Fields of configure file:

BGmi configure:
+ :code:`BANGUMI_MOE_URL`: url of bangumi.moe mirror
+ :code:`BGMI_SAVE_PATH`: bangumi saving path
+ :code:`DOWNLOAD_DELEGATE`: the ways of downloading bangumi (aria2-rpc, transmission-rpc, xunlei)
+ :code:`MAX_PAGE`: max page for fetching bangumi information
+ :code:`BGMI_TMP_PATH`: just a temporary path
+ :code:`DANMAKU_API_URL`: url of danmaku api
+ :code:`CONVER_URL`: url of bangumi's cover
+ :code:`LANG`: language

Aria2-rpc configure:
+ :code:`ARIA2_RPC_URL`: aria2c deamon RPC url
+ :code:`ARIA2_RPC_TOKEN`: aria2c deamon RPC token("token:" for no token)

Xunlei configure:
+ :code:`XUNLEI_LX_PATH`: path of xunlei-lixian binary

Transmission-rpc configure:
+ :code:`TRANSMISSION_RPC_URL`: transmission rpc host
+ :code:`TRANSMISSION_RPC_PORT`: transmission rpc port


==================
Usage of bgmi_http
==================

Start BGmi HTTP Service bind on `0.0.0.0:8888`:

.. code-block:: bash

    bgmi_http --port=8888 --address=0.0.0.0

Configure tornado with nginx:

.. code-block:: bash

    server {
        listen 80;
        root /var/www/html/bangumi;
        autoindex on;
        charset utf8;
        server_name bangumi.example.com;

        location /bangumi {
            alias /var/www/html/bangumi;
        }

        location / {
            # reverse proxy to tornado listened port.
            proxy_pass http://127.0.0.1:8888;
        }
    }

Of cause you can use `yaaw <https://github.com/binux/yaaw/>`_ to manage download items if you use aria2c to download bangumi.

.. code-block:: bash

    ...
    location /bgmi_admin {
        auth_basic "BGmi admin (yaaw)";
        auth_basic_user_file /etc/nginx/htpasswd;
        alias /var/www/html/yaaw;
    }

    location /jsonrpc {
        # aria2c listened port
        proxy_pass http://127.0.0.1:6800;
    }
    ...

===================
DPlayer and Danmaku
===================

BGmi use `DPlayer <https://github.com/DIYgod/DPlayer>`_ to play bangumi.

First, setup nginx to access bangumi files. Second, choose one danmaku backend at `DPlayer#related-projects <https://github.com/DIYgod/DPlayer#related-projects>`_.

Use `bgmi config` to setup the url of danmaku api.

.. code-block:: bash

    bgmi config DANMAKU_API_URL http://127.0.0.1:1207/

... and enjoy :D

=======
License
=======
The MIT License (MIT)

Copyright (c) 2017 Ricter Zheng

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

.. |travis| image:: https://travis-ci.org/RicterZ/BGmi.svg?branch=master
   :target: https://travis-ci.org/RicterZ/BGmi

.. |pypi| image:: https://img.shields.io/pypi/v/bgmi.svg
   :target: https://pypi.python.org/pypi/bgmi
