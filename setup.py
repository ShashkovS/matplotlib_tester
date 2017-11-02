#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='matplotlib_tester',
    version='0.0.1',
    description='Функция для тестирования задач по matplotlib',
    long_description='Функция для тестирования задач по matplotlib',
    author='Sergey Shashkov',
    author_email='sh57@yandex.ru',
    url='https://github.com/ShashkovS/matplotlib_tester',
    py_modules=['matplotlib_tester'],
    install_requires=['numpy', 'matplotlib'],
    include_package_data=True,
    license='MIT'
)
