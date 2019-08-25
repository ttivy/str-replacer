from setuptools import setup

setup(
    name='str-replacer',
    version='0.1.0',
    description='',
    author='ttivy',
    author_email='25240747+ttivy@users.noreply.github.com',
    url='https://github.com/ttivy/str-replacer',
    license='MIT',
    packages=[
        'replacer',
    ],
    install_requires=[
        'pyahocorasick',
    ],
    test_suite='tests',
)
