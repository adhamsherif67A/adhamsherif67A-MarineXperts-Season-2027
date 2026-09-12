from setuptools import find_packages, setup

package_name = 'mavros_autotune'

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
    maintainer='boda',
    maintainer_email='a.ibrahim03633@student.aast.edu',
    description='MAVROS Autotune Node for Position and Velocity Tuning',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'mavros_autotune = mavros_autotune.autotune_node:main'
        ],
    },
)
