from setuptools import setup

setup(
    name='discord-ext-something',
    version='0.0.1',
    python_requires='>=3.10.0',
    install_requires=[
        'discord.py @ git+https://github.com/Rapptz/discord.py@6d494585f5d8e4023ff9ce0039571eadb11f4e19',
    ],
    extras_require={
        'dev': [
            'pytest'
        ]
    },
)
