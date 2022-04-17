from setuptools import setup

setup(
    name='cmdMoveFiles',
    version= '0.1.0',
    py_modules=['cmdMoveFiles'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts':[
            'cmdMoveFiles = cmdMoveFiles:moveFiles',
        ],
    },
)