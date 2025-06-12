from setuptools import setup, find_packages

setup(
    name='mkpipe-loader-mysql',
    version='0.2.0',
    license='Apache License 2.0',
    packages=find_packages(exclude=['tests', 'scripts', 'deploy']),
    install_requires=['mkpipe'],
    include_package_data=True,
    entry_points={
        'mkpipe.loaders': [
            'mysql = mkpipe_loader_mysql:MysqlLoader',
        ],
    },
    description='MySQL loader for mkpipe.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Metin Karakus',
    author_email='metin_karakus@yahoo.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
    ],
    python_requires='>=3.8',
)
