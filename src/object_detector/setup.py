from setuptools import find_packages, setup

package_name = 'object_detector'

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
    maintainer='kimu',
    maintainer_email='hellokimaya@gmail.com',
    description='Object detection using OpenCV and ROS 2',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['detect_color = object_detector.detect_color:main'
        ],
    },
)
