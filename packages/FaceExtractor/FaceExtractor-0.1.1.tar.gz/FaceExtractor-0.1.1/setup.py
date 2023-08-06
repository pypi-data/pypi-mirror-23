from setuptools import setup

setup(name='FaceExtractor',
      version='0.1.1',
      description='Extract faces from images with OpenCV',
      url='https://github.com/ducthienbui97/FaceExtractor',
      author='Thien Bui',
      author_email='thienbui797@gmail.com',
      license='BSD-3-Clause',
      packages=['face_extractor'],
      install_requires=['opencv-python'],
      package_data={'face_extractor':['data/*.xml']},
      setup_requires=['setuptools-markdown'],
      long_description_markdown_filename='README.md',
)