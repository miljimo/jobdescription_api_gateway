import setuptools
long_description = "No descriptions";

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(name = "jimobama_postgres_service_gateway",
      version="0.0.1",
      description="Http gateway to called postgres functions/store_procedures.",
      long_description =long_description,
      url="https://github.com/miljimo/pgdataaccess_api_gateway.git",
      long_description_content_type="text/markdown",
      author="Obaro I. Johnson",
      author_email="johnson.obaro@hotmail.com",
      packages=setuptools.find_packages(),
      install_requires=[],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",         
    ],python_requires='>=3.6');