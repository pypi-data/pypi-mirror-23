"""
setup
"""
import setuptools

setuptools.setup(
    name='inv_content_list',
    packages=['inv_content_list'], # this must be the same as the name above
    version='1.5',
    description='A random test lib11',
    author='Eric Chu',
    author_email='eric.chu@investopedia.com',
    url='https://github.com/peterldowns/mypackage', # use the URL to the github repo
    download_url='https://github.com/peterldowns/mypackage/archive/0.1.tar.gz', # I'll explain this in a second
    keywords=['testing', 'logging', 'example'], # arbitrary keywords
    include_package_data=True,
    install_requires=[
        'jinja2',
        'requests_oauth',
    ],
    classifiers=[],
)
