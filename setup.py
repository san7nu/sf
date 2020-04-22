import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='sf',
     version='0.1',
     scripts=['sf/__init__.py'] ,
     author="sk",
     author_email="",
     description="",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )