from setuptools import setup, find_packages

package_name = 'orca_core'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['tests']), # 自动查找所有包
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'numpy',
        'pyyaml',],
    zip_safe=True,
    maintainer='xingyi',
    maintainer_email='peiguorui2006@outlook.com',
    description='The orca_core package',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
