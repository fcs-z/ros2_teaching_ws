from setuptools import find_packages, setup

package_name = 'pkg02_topic_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gcu68',
    maintainer_email='gcu68@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'demo01_talker_py = pkg02_topic_py.demo01_talker_py:main',
            'demo01_listener_py = pkg02_topic_py.demo01_listener_py:main',
        ],
    },
)
