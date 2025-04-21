from setuptools import setup

package_name = 'obstacle_avoidance'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your@email.com',
    description='ROS2 node for basic obstacle avoidance',
    license='MIT',
    entry_points={
        'console_scripts': [
            'bot_controller = obstacle_avoidance.bot_controller:main',
        ],
    },
)

