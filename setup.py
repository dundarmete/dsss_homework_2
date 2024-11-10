from setuptools import setup, find_packages

setup(
    name="dsss_homework_2",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'math_quiz = dsss_homework_2.math_quiz:math_quiz',
        ],
    },
    author="Metehan Dündar",
    author_email="metehan.duendar@fau.de",
    description="A simple math quiz game",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/dundarmete/dsss_homework_2",  # GitHub or project URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9.6',
)
