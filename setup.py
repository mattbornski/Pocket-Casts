from setuptools import setup, find_packages

setup(
    name="pocketcasts-api",

    version='0.2.3',

    description='Unofficial API for pocketcasts.com',

    url='https://github.com/furgoose/Pocket-Casts',

    author='Fergus Longley',
    author_email='ferguslongley@live.com',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],

    packages=find_packages(exclude=['tests']),

    keywords='podcasts pocketcasts',

    install_requires=['requests'],
    extras_require={
        'test': ['pytest', 'vcrpy'],
    }
)
