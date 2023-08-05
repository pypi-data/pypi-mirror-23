|PyPI Version| |GitHub tag| |DOI| |PyPI License|

|PyPI Wheel| |PyPI Format| |PyPI Pythons| |Python 3| |PyPI
Implementation| |PyPI Status|

|Build Status| |CircleCI|

|Dependency Status| |Updates|

|Coverage Status| |codecov|

|Code Issues| |Scrutinizer Code Quality| |Codacy Badge| |Code Climate|
|Issue Count|

pybotics |image21|
==================

Python Toolbox for Robotics

Usage
-----

Installation
~~~~~~~~~~~~

::

    pip install pybotics

Quick Start
~~~~~~~~~~~

.. code:: python

    import numpy as np
    import pybotics as pybot

    # classic planar robot from textbooks
    robot_model = np.array([
        [0, 0, 0, 0],
        [0, 10, 0, 0],
        [0, 20, 0, 0]
    ], dtype=np.float)
    planar_robot = pybot.Robot(robot_model)
    planar_robot.joint_angles = np.deg2rad([30, 60, 0])
    pose = planar_robot.fk() # forward kinematics, returns 4x4 pose transform    

    # modern, collaborative, 6-axis robot (UR10 from Universal Robots)
    robot_model = np.loadtxt('ur10-mdh.csv', delimiter=',')
    ur10_robot = pybot.Robot(robot_model)
    ur10_robot.random_joints()
    pose = ur10_robot.fk() # forward kinematics, returns 4x4 pose transform

Applications
~~~~~~~~~~~~

-  `Kinematics <https://github.com/nnadeau/pybotics/blob/master/examples/example_kinematics.ipynb>`__
-  `Calibration <https://github.com/nnadeau/pybotics/blob/master/examples/example_calibration.ipynb>`__
-  Trajectory and path planning

References
----------

-  Craig, John J. Introduction to robotics: mechanics and control. Vol.
   3. Upper Saddle River: Pearson Prentice Hall, 2005.
-  Corke, Peter. Robotics, vision and control: fundamental algorithms in
   MATLAB. Vol. 73. Springer, 2011.

--------------

.. raw:: html

   <div>

Logo made by Freepik from www.flaticon.com is licensed by CC 3.0 BY

.. raw:: html

   </div>

.. |PyPI Version| image:: https://img.shields.io/pypi/v/pybotics.svg
   :target: https://pypi.python.org/pypi/pybotics
.. |GitHub tag| image:: https://img.shields.io/github/tag/nnadeau/pybotics.svg?maxAge=2592000?style=flat-square
   :target: https://github.com/nnadeau/pybotics/releases
.. |DOI| image:: https://zenodo.org/badge/66797360.svg
   :target: https://zenodo.org/badge/latestdoi/66797360
.. |PyPI License| image:: https://img.shields.io/pypi/l/pybotics.svg
   :target: https://pypi.python.org/pypi/pybotics
.. |PyPI Wheel| image:: https://img.shields.io/pypi/wheel/pybotics.svg
   :target: https://pypi.python.org/pypi/pybotics
.. |PyPI Format| image:: https://img.shields.io/pypi/format/pybotics.svg
   :target: https://pypi.python.org/pypi/pybotics
.. |PyPI Pythons| image:: https://img.shields.io/pypi/pyversions/pybotics.svg
   :target: https://pypi.python.org/pypi/pybotics
.. |Python 3| image:: https://pyup.io/repos/github/nnadeau/pybotics/python-3-shield.svg
   :target: https://pyup.io/repos/github/nnadeau/pybotics/
.. |PyPI Implementation| image:: https://img.shields.io/pypi/implementation/pybotics.svg
   :target: https://pypi.python.org/pypi/pybotics
.. |PyPI Status| image:: https://img.shields.io/pypi/status/pybotics.svg
   :target: https://pypi.python.org/pypi/pybotics
.. |Build Status| image:: https://travis-ci.org/nnadeau/pybotics.svg?branch=master
   :target: https://travis-ci.org/nnadeau/pybotics
.. |CircleCI| image:: https://circleci.com/gh/nnadeau/pybotics/tree/master.svg?style=svg
   :target: https://circleci.com/gh/nnadeau/pybotics/tree/master
.. |Dependency Status| image:: https://www.versioneye.com/user/projects/57d87a4a7129660045cf3a58/badge.svg?style=flat-square
   :target: https://www.versioneye.com/user/projects/57d87a4a7129660045cf3a58
.. |Updates| image:: https://pyup.io/repos/github/nnadeau/pybotics/shield.svg
   :target: https://pyup.io/repos/github/nnadeau/pybotics/
.. |Coverage Status| image:: https://coveralls.io/repos/github/nnadeau/pybotics/badge.svg?branch=master
   :target: https://coveralls.io/github/nnadeau/pybotics?branch=master
.. |codecov| image:: https://codecov.io/gh/nnadeau/pybotics/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/nnadeau/pybotics
.. |Code Issues| image:: https://www.quantifiedcode.com/api/v1/project/9015d6abef024afea0981992c1041078/badge.svg
   :target: https://www.quantifiedcode.com/app/project/9015d6abef024afea0981992c1041078
.. |Scrutinizer Code Quality| image:: https://scrutinizer-ci.com/g/nnadeau/pybotics/badges/quality-score.png?b=master
   :target: https://scrutinizer-ci.com/g/nnadeau/pybotics/?branch=master
.. |Codacy Badge| image:: https://api.codacy.com/project/badge/Grade/9d4f77b167874a049e97731181e2b53a
   :target: https://www.codacy.com/app/nicholas-nadeau/pybotics?utm_source=github.com&utm_medium=referral&utm_content=nnadeau/pybotics&utm_campaign=Badge_Grade
.. |Code Climate| image:: https://codeclimate.com/github/nnadeau/pybotics/badges/gpa.svg
   :target: https://codeclimate.com/github/nnadeau/pybotics
.. |Issue Count| image:: https://codeclimate.com/github/nnadeau/pybotics/badges/issue_count.svg
   :target: https://codeclimate.com/github/nnadeau/pybotics
.. |image21| image:: logo/robotic-arm.png
