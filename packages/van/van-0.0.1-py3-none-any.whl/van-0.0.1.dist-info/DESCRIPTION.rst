Van - Fanfou SDK
================

How to use
----------

.. code-block:: python

    from van import Fan, Config


    # 1. Subclass the ``Config`` class and offer your configs
    class MyConfig(Config):
        consumer_key = 'xxxx'
        consumer_secret = 'xxxx'


    # 2. Instancialize the ``Fan`` class
    me = Fan(MyConfig())
    # 3. call methods of ``me``
    me.update_status('你好啊，李银河！')

