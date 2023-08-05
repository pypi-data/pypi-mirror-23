pybotics 
=========

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

-  Kinematics
-  Calibration
-  Trajectory and path planning

Development
-----------

-  All branches are deployed to PyPI's Test Site
-  Only tags on the ``master`` branch are deployed to PyPI

References
----------

-  Craig, John J. Introduction to robotics: mechanics and control. Vol.
   3. Upper Saddle River: Pearson Prentice Hall, 2005.
-  Corke, Peter. Robotics, vision and control: fundamental algorithms in
   MATLAB. Vol. 73. Springer, 2011.
