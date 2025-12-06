from setuptools import find_packages, setup

package_name = 'pkg04_service_py'

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
    maintainer='fcs',
    maintainer_email='fcs@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'demo01_server_py = pkg04_service_py.demo01_server_py:main',
            'demo01_client_py = pkg04_service_py.demo01_client_py:main',
        ],
    },
)
