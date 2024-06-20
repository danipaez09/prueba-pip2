from setuptools import setup

readme = open("./README.md", "r")


setup(
    name='packaging_tutorial',
    packages=['packaging_tutorial'],  # this must be the same as the name above
    version='0.1',
    description='Esta es la descripcion de mi paquete, hacer pruebas',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author='Daniela Paez',
    author_email='daniela.paez09@gmail.com',
    # use the URL to the github repo
    url='https://github.com/nelsonher019/nelsonsaludo',
    download_url='https://github.com/nelsonher019/nelsonsaludo/tarball/0.1',
    keywords=['testing', 'pso', 'example'],
    classifiers=[ ],
    license='MIT',
    include_package_data=True
)