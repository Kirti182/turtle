from setuptools import find_packages, setup

package_name = 'ugv_package'

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
    maintainer='props',
    maintainer_email='props@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    entry_points={
    'console_scripts': [
        'sensor_publisher = ugv_package.sensor_publisher:main',
        'sensor_subscriber = ugv_package.sensor_subscriber:main',
        ],
    },
)
