# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='deplicate',
    version=open('VERSION').read().strip(),
    description='Advanced Duplicate File Finder for Python. '
                'Nothing is impossible to solve.',
    long_description=open('README.rst').read(),
    keywords='duplicates dups',
    url='https://github.com/vuolter/deplicate',
    download_url='https://github.com/vuolter/deplicate/releases',
    author='Walter Purcaro',
    author_email='vuolter@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        # 'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: System',
        'Topic :: System :: Filesystems',
        'Topic :: Utilities'],
    platforms=['any'],
    packages=['duplicate'],
    include_package_data=True,
    install_requires=[
        'enum34;python_version<"3.4"',
        'psutil;os_name!="nt"',
        'pyobjc;sys_platform=="darwin"',
        'pypiwin32>=154;os_name=="nt"',
        'scandir;python_version<"3.5"',
        'wmi;os_name=="nt"',
        'xxhash>=1'],
    extras_require={
        'full': ['directio;os_name!="nt"']},
    python_requires='>=2.6,!=3.0,!=3.1,!=3.2',
    zip_safe=True)
