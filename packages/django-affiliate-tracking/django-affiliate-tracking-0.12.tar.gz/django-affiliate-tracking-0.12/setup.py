"""Setup for the affiliations application"""

from setuptools import setup


setup(
    name='django-affiliate-tracking',
    packages=['affiliations'],
    include_package_data=True,
    package_data={},
    version='0.12',
    description='A Django app providing mechanisms to track users and '
                'actions, to know when certain conditions are met.',
    long_description=open('README.rst', 'rt').read(),
    license='BSD License 2.0',
    author='Saxo Publish',
    author_email='publish@saxo.com',
    url='https://saxo.githost.io/publish/django-affiliate-tracking/',
    keywords=['django', 'affiliations'],
    zip_safe=False,
    install_requires=[
        'django>=1.9',
        'django-tls>=0.0.2',
        'mock>=2.0.0',
        'requests>=2.13.0',
    ],
    classifiers=[
      'Framework :: Django',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 3'
    ],
)
