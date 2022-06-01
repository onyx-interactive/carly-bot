from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    # TODO: Adjust your project information here
    name='Carly',
    version='1.0.0',
    description='A little bot',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/onyx-interactive/carly-bot',
    author='isahsan',
    author_email='isahsan@icloud.com',

    project_urls={
        'Bug Reports': 'https://github.com/onyx-interactive/carly-bot/issues',
        'Source': 'https://github.com/https://github.com/onyx-interactive/carly-bot',
    },

    keywords='carly-bot',

    python_requires='>=3.8, <4',

    install_requires='discord.py ~= 1.7.2',

    classifiers=[

        'Development Status :: 5 - Production/Stable',

        'Environment :: Console',

        'Intended Audience :: Other Audience',
        'Topic :: Communications :: Chat',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',

        'Typing :: Typed',
    ],

    package_dir={'': 'src/'},

    packages=find_packages(where='src/'),

    entry_points={
        'console_scripts': [
            'discord-bot=bot:main',
        ],
    },
)
