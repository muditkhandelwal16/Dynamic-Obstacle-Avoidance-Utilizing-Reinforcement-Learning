from setuptools import setup

package_name = 'bumperbot_motion'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mudit',
    maintainer_email='mudit@example.com',
    description='Motion planning for the bumperbot',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'a_star_planner = bumperbot_motion.a_star_planner:main',
            'pd_motion_planner = bumperbot_motion.pd_motion_planner:main',
        ],
    },
)
