from setuptools import setup, find_packages
 
setup(
    name = 'nkueamis',
    version = '0.1.3',
    author = 'Wanpeng Zhang',
    author_email = 'zawnpn@gmail.com',
    keywords = ('NKU', 'eamis', 'Education'),
    url = 'https://github.com/zawnpn/nkueamis',
    description = 'A simple tool to help get information in NKU-EAMIS(NKU Education Affairs Management Information Ststem).',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
      ],
    license = 'MIT',
    packages = find_packages(),
    install_requires=['docopt', 'requests', 'bs4', 'prettytable'],
    entry_points={
        'console_scripts':[
            'nkueamis=nkueamis.nkueamis:main'
        ]
      },
)
