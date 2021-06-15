# Super Triangulation 
Super Triangulation is a method that leverages Alphapose (or Detectron+OpenPose) 2D detections and pose estimation, SuperGlue player pose correspondences and the classical triangulation method for multi-view 3D pose reconstruction

In the following repository you might find source code from other Github repositories. Mainly from [Detectron](https://github.com/facebookresearch/Detectron), [Alphapose](https://github.com/MVIG-SJTU/AlphaPose), [SuperGlue](https://github.com/magicleap/SuperGluePretrainedNetwork), [Openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose), AlphaPose and Detectron (See reference section for more details). Nevertheless all source code has been modified to suit the needs of the project. The jupyter notebook gives a step by step guide through the whole Super Tringulation method implementation.
The jupyter notebook belongs to Christos Antoniou and code can be used under the classis source code license.
Make sure that all files in the repository are present when executing the notebook cells. It is of prime importance that the ````3d.py```` file is included in the repository, in order to succesfully visualize the results. The visualization python file might not be eligible for execution directly from the notebook, so please run independently if any errors occur. The code for both the visualization python part and the main Super Triangulation implementation in Jupyter, is documented with a plethora of comments.

![Alt text](./cam1_view_frame0_detection0.png?raw=true "Title")
![Alt text](./right_view_frame0_detection0.png?raw=true "Title")
![Alt text](./3Dskeleton.png?raw=true "Title")



##  Quick Start
1. Make sure you have installed the conda environment ````super_triangulation.yml````
2. Open the Jupyter Notebook ````demo.ipynb ```` and start executing the cells
3. The ````demo_superglue.py```` and the ````match_pairs.py```` initially adapted from the SuperGlue repository have been modified to suit the projects' needs
4. Follow instructions on ````demo.ipynb```` notebook

## Environment
In order to run the notebook file, make sure you have installed all packages necessary. This can be done with 2 ways, by opening a terminal on the repository root and executing:
* ````pip install requirements.txt````
 or 
* ````conda env create --file super_triangulation.yml````


## Acknowledgments
I would like to thank Salmane El Mesoussi, Mert Cokmez and Aly El Hakie for their support and souce code contribution.
Special thanks to Salmane for his ideas and code contribution for the color pitch mask and camera calibration.
Special thanks to Mert for his classic triangulation baseline code that was later adapted.
Special thanks to Aly for producing the Alphapose 2D joint detection and & estimation and storing them to appropriate JSON files

## References
Code has been adapted from the following Github pages:
* [Openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
* [Detectron](https://github.com/facebookresearch/Detectron)
* [Alphapose](https://github.com/MVIG-SJTU/AlphaPose)
* [SuperGlue](https://github.com/magicleap/SuperGluePretrainedNetwork)
