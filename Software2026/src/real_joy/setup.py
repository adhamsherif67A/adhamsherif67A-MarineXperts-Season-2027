from setuptools import setup

package_name = 'RealJoy'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'PyQt5', 'numpy'],
    zip_safe=True,
    maintainer='boda',
    maintainer_email='boda@todo.todo',
    description='TODO: Package description',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'zed_to_mavros_pose = RealJoy.zed_to_mavros_pose:main',
'rov_gui_gst = rov_gui_gst.main',
        ],
    },
)

