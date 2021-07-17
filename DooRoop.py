import open3d as o3d
import numpy as np
trans_init = np.asarray([[1., 0., 0., .01],
                      [0., 1., 0., 0.],
                      [0., 0., 1., 0.],
                      [0., 0., 0., 1.]])


o3d.visualization.draw_geometries([o3d.io.read_point_cloud("D:\project_3d_recon\point_temp\compl.ply").transform(trans_init)])