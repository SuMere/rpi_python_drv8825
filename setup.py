from distutils.core import setup
setup(
  name = 'rpi_python_drv8825',
  packages = ['rpi_python_drv8825'],
  version = '0.3',
  license='gpl-3.0',
  description = 'Python library to controll a stepper motor with a HR8825 driver',
  author = 'Riccardo Mereu',
  author_email = 'rmereu.dev@gmail.com',
  url = 'https://github.com/SuMere/rpi_python_drv8825',
  download_url = 'https://github.com/SuMere/rpi_python_drv8825/archive/refs/heads/master.zip',
  keywords = ['HR8825', 'control', 'steppermotor', 'stepper', 'motor', 'Raspberry', 'Pi'],
  install_requires=[
          'periphery.GPIO',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
