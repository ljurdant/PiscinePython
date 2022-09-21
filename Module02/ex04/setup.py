from setuptools import setup, find_packages

setup(
    name="my-minipack",
    version="1.0.0",
    description="How to create a package python",
    home_page=None,
    author="ljurdant",
    author_email="ljurdant@student.42.fr",
    license="MIT",
    location="[PATH TO BOOTCAMP PYTHON]/module02/tmp_env/lib/python3.7/site-packages",
    requires="",
    required_by="",
    metadata_version="2.1",
    installer="pip",
    classifiers=[
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Intended Audience :: Students',
    'Topic :: Education',
    'Topic :: HowTo',
    'Topic :: Package',

    # Pick your license as you wish (should match "license" above)
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3 :: Only', 
],
)