from setuptools import find_packages, setup
from glob import glob

package_name = 'pkg03_topic_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name+'/launch', glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='fcs',
    maintainer_email='fcs@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'demo02_talker_py = pkg03_topic_py.demo02_talker_py:main',
            'demo02_listener_py = pkg03_topic_py.demo02_listener_py:main',
        ],
    },
)
