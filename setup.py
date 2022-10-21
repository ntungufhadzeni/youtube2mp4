from setuptools import setup

setup(
    name='youtube2mp4',
    version='0.0.1',
    install_requires=["pytube==12.1.0"],
    packages=['youtube2mp4'],
    entry_points={
        'console_scripts': [
            'youtube2mp4 = youtube2mp4.youtube2mp4:main',
        ]
    }
    
)