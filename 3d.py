import vispy
from vispy.scene import visuals, SceneCanvas
import numpy as np
import os
from vispy.color import ColorArray



class Visualizer():
    def __init__(self):
        self.canvas = SceneCanvas(keys='interactive', show=True)
        self.grid = self.canvas.central_widget.add_grid()
        self.view = vispy.scene.widgets.ViewBox(border_color='white',
                        parent=self.canvas.scene)
        self.grid.add_widget(self.view, 0, 0)


        # Player Visualization
        self.player_vis = visuals.Line()
        self.view.add(self.player_vis)
        self.connect = np.asarray([
                [0, 17], [0,1],[0, 2], [1, 3], [2, 4], [0,18],  # Head
                [5, 18], [6,18],[7, 5],[7,9], [8, 10], [8,6],
                [11, 19], [12,19],[11, 13],[12,14],
                [14, 16], [25, 16],  # Body
                [23, 25], [21, 25], [11, 13], [13, 15],
                [24,15],[24,20],[24,22]])
        
        # Pitch Visualizer
        self.pitch_vis = visuals.Line()
        self.view.add(self.pitch_vis)

        # Keypoint Visualizer
        self.keypoints_vis = visuals.Markers()
        fov = 60.

        #Set initial camera view
        #self.view.camera = vispy.scene.cameras.FlyCamera(fov=fov, roll=30)
        #self.view.camera = vispy.scene.cameras.TurntableCamera(fov=fov)
        #self.view.camera = vispy.scene.cameras.ArcballCamera(fov=fov)
        self.view.camera = vispy.scene.cameras.TurntableCamera(up='z', azimuth=90, roll=30)
        self.view.add(self.keypoints_vis) #add the keypoint markers in the scene
        visuals.XYZAxis(parent=self.view.scene)

       
        
         
    def update_players(self, player_points):
        '''
        :param player_points: player skeleton data
                        shape (N, 3)          
        '''
        #color = ColorArray(color,clip=True)
        #self.sem_vis.set_data(points,edge_color=color, size=3)
        print("Player 3D keypoints are",'\n',player_points)
        self.player_vis.set_data(player_points,
                              connect=self.connect,
                              width=2,
                              color=[0,1,0,1])

    def update_keypoints(self, keypoints):
    	self.keypoints_vis.set_data(keypoints,edge_color=[0,1,0], size=3)


    def update_pitch(self, pitch_points):
    	lines = np.asarray([[0,1],[0,2], [3,4],[3,5],[6,7],[6,8], [1,4], [2,5],[1,7],[2,8],[9,10]
    		,[11,12],[17,18],[10,16],[11,13],[12,14],[19,20],[21,22],[22,19],[23,24],[25,26],[23,26]])
    	self.pitch_vis.set_data(pitch_points,
                              connect=lines,
                              width=2,
                              color=[0,1,0,1])
   
        

if __name__ == '__main__': 
    all_player_points = np.load('2_view_points.npy')
    all_player_points_3_views = np.load('3_view_points.npy')
    pitch_points =np.load('pitch.npy') #load pitch points (0,0,0) is the center of the pitch
    keypoints_per_player = 26
    visualizer = Visualizer()
    num_players = 1#int(all_player_points_3_views.shape[0]/keypoints_per_player)

    #visualize just all 3D points of the first player
    visualizer.update_keypoints(all_player_points_3_views[0:26])

    #Visualize pitch
    visualizer.update_pitch(pitch_points)

    #Visualize the first player xtracted from 3 view cameras
    #visualizer.update_players(all_player_points_3_views)

    
    #for all players in 3D space
    
    for player_i in range(0,num_players):
    	player_points = all_player_points_3_views[player_i:(player_i+1)*26]
    	#visualizer.update_keypoints(player_points) #show keypoints for each player
    	visualizer.update_players(player_points) #draw skeleton for each player
        
    vispy.app.run()


