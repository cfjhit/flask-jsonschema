"""
Flask-JsonSchema
----------

A Flask extension for validating JSON requets with jsonschema

"""
from setuptools import setup


setup(
    name='Flask-JsonSchema-All',
    version='0.1.1',
    url='https://github.com/cfjhit/flask-jsonschema',
    license='MIT',
    author='jay.chen',
    author_email='cfjhit@gmail.com',
    description='Flask extension for validating JSON requets',
    long_description=__doc__,
    py_modules=['flask_jsonschema'],
    test_suite='nose.collector',
    zip_safe=False,
    platforms='any',
    install_requires=['Flask>=0.9', 'jsonschema>=1.1.0'],
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
