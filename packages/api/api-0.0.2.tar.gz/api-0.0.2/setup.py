import setuptools

setuptools.setup(name='api',
                 version='0.0.2',
                 description='Consume an API from ReadMe Build',
                 long_description=open('README.rst').read().strip(),
                 author='ReadMe',
                 author_email='support@readme.io',
                 url='http://readme.build',
                 py_modules=['api'],
                 install_requires=[],
                 license='MIT License',
                 keywords='api readme')
