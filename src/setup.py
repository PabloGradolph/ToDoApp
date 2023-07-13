from setuptools import setup


setup(
    name='todo_app',
    version='0.1.0',
    description='A minimal To-Do App',
    author='PabloGradolph',
    packages=['todoapp'],
    zip_safe=False,
    tests_require=['pytest'],
    install_requires=[
        'PyQt6'
    ]
)