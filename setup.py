import os.path
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(
    name='wwsclient',
    version='0.0.0.4',
    description='This script will be expose all workday webservice operations',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/hikmat30ce/Workday-Webservices-Client.git',
    author='Hikmat Ullah',
    author_email='me@hikmatu.com',
    license='MIT',
    packages=['wwsclient'],
    include_package_data=True,
    install_requires=[
        'appdirs==1.4.4',
        'attrs==20.3.0',
        'cached-property==1.5.2',
        'certifi==2020.12.5',
        'chardet==4.0.0',
        'defusedxml==0.7.0',
        'idna==2.10',
        'isodate==0.6.0',
        'lxml==4.6.2',
        'pytz==2021.1',
        'requests==2.25.1',
        'requests-file==1.5.1',
        'requests-toolbelt==0.9.1',
        'six==1.15.0',
        'urllib3==1.26.3',
        'xmltodict==0.12.0',
        'zeep==4.0.0'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={"console_scripts": ["realpython=reader.__main__:main"]},

    # install_requires={
    #         "dist": [
    #             'appdirs==1.4.4',
    #             'attrs==20.3.0',
    #             'cached-property==1.5.2',
    #             'certifi==2020.12.5',
    #             'chardet==4.0.0',
    #             'defusedxml==0.7.0',
    #             'idna==2.10',
    #             'isodate==0.6.0',
    #             'lxml==4.6.2',
    #             'pytz==2021.1',
    #             'requests==2.25.1',
    #             'requests-file==1.5.1',
    #             'requests-toolbelt==0.9.1',
    #             'six==1.15.0',
    #             'urllib3==1.26.3',
    #             'xmltodict==0.12.0',
    #             'zeep==4.0.0'
    #         ],
    #         "dev": [
    #             'appdirs==1.4.4',
    #             'attrs==20.3.0',
    #             'cached-property==1.5.2',
    #             'certifi==2020.12.5',
    #             'chardet==4.0.0',
    #             'defusedxml==0.7.0',
    #             'idna==2.10',
    #             'isodate==0.6.0',
    #             'lxml==4.6.2',
    #             'pytz==2021.1',
    #             'requests==2.25.1',
    #             'requests-file==1.5.1',
    #             'requests-toolbelt==0.9.1',
    #             'six==1.15.0',
    #             'urllib3==1.26.3',
    #             'xmltodict==0.12.0',
    #             'zeep==4.0.0'
    #         ]
    #     },
)
