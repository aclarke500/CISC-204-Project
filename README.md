# CISC/CMPE 204 Modelling Project

Welcome to the major project for CISC/CMPE 204!

Change this README.md file to summarize your project, and provide pointers to the general structure of the repository. How you organize and build things (which files, how you structure things, etc) is entirely up to you! The only things you must keep in place are what is already listed in the **Structure** section below.

## Structure

* `documents`: Contains folders for both of your draft and final submissions. README.md files are included in both.
* `run.py`: General wrapper script that you can choose to use or not. Only requirement is that you implement the one function inside of there for the auto-checks.
* `test.py`: Run this file to confirm that your submission has everything required. This essentially just means it will check for the right files and sufficient theory size.



## Explanation

In the photos directory there is more in depth explanation. Our application attempts to determine if a given path on a two dimensional grid is legal, given the following propeties: Each coordinate is a node, which can either be a road, intersection, or block. Intersections, may have the ability for a car to travel in any one of the four cardinal directions depening on their neighbouring nodes. Roads can run East-West or North-South, but not anyway else. Meaning if a road runs north, then it cannot go east, for instance. Lastly there are blocks, which cannot be traveled to or from. In diagram.jpg there is a diagram with a 3x3 grid that showcases our current map. Orange is an intersection, grey is a road, and red is a block. This is a small map to make development / testing easy, but will be built dynamically to allow for more verstatility later on. Our application determines every possible reasonable path one could traverse to get from point A to point B on a 3x3 grid, analyzes all of them using logic to see if they are legal. Of the legal onees, the shortest path is returned as the best path. 