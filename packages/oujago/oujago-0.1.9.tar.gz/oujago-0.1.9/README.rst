
.. image:: https://readthedocs.org/projects/oujago/badge
   :target: http://oujago.readthedocs.io/en/latest
   :alt: Documentation Status

.. image:: https://img.shields.io/github/issues/oujago/oujago.svg
   :target: https://github.com/oujago/oujago



======
Oujago
======

Coding makes the life easier. This is a factory contains commonly used
algorithms and useful links.


Documentation
=============

Available online documents: `latest <http://oujago.readthedocs.io/en/latest/>`_
and `develop <http://oujago.readthedocs.io/en/develop/>`_.


Installation
============

Install ``oujago`` using pip:

.. code-block:: bash

    $> pip install oujago

Install from source code:

.. code-block:: bash

    $> python setup.py clean --all install


APIs
====


Natural Language Processing
---------------------------

Hanzi Converter
^^^^^^^^^^^^^^^

.. code-block:: shell

    >>> from oujago.nlp import FJConvert
    >>> FJConvert.to_tradition('繁简转换器')
    '繁簡轉換器'
    >>> FJConvert.to_simplify('繁簡轉換器')
    '繁简转换器'


Chinese Segment
^^^^^^^^^^^^^^^

Support ``jieba``, ``LTP`` etc. public segmentation methods, and support
``moran`` segmentation just for internal use.

.. code-block:: shell

    >>> from oujago.nlp import seg
    >>> seg("这是一个伸手不见五指的黑夜。")
    ['这是', '一个', '伸手不见五指', '的', '黑夜', '。']
    >>> seg("这是一个伸手不见五指的黑夜。", mode='ltp')
    ['这', '是', '一个', '伸手', '不', '见', '五', '指', '的', '黑夜', '。']
    >>> seg('我不喜欢日本和服', mode='jieba')
    ['我', '不', '喜欢', '日本', '和服']
    >>> seg('我不喜欢日本和服', mode='ltp')
    ['我', '不', '喜欢', '日本', '和服']


Part-of-Speech
^^^^^^^^^^^^^^

.. code-block:: shell

    >>> from oujago.nlp.postag import pos
    >>> pos('我不喜欢日本和服', mode='jieba')
    ['r', 'd', 'v', 'ns', 'nz']
    >>> pos('我不喜欢日本和服', mode='ltp')
    ['r', 'd', 'v', 'ns', 'n']


