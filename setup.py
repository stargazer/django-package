from setuptools import setup

setup(
    name='django-package',
    packages=('package',),
    author='C. Paschalides',
    author_email='already.late@gmail.com',
    license='WTFPL',
    install_requires=(
        'Django',
    ),
    tests_require=(),
    test_suite='runtests.run',
    zip_safe=False,
)
