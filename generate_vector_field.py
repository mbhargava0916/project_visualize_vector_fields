import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_3d_points(surface_type='flat_torus', grid_size=50, R=1, r = 0.3):
    u = np.linspace(0, 2 * np.pi, grid_size)
    v = np.linspace(0, 2 * np.pi, grid_size)
    U, V = np.meshgrid(u, v)

    if surface_type == 'flat torus':
        R = 1  
        r = 0.3 
        X = (R + r * np.cos(V)) * np.cos(U)
        Y = (R + r * np.cos(V)) * np.sin(U)
        Z = r * np.sin(V)
    elif surface_type == 'flat cylinder':
        X = np.cos(U)
        Y = np.sin(U)
        Z = V - np.pi
    elif surface_type == 'octagon':
        X = np.cos(U) * np.cos(V)
        Y = np.sin(U) * np.cos(V)
        Z = np.sin(V)
    elif surface_type == 'hyperbolic':
        X = U
        Y = V
        Z = U**2 - V**2
    elif surface_type == 'cone points':
        R = np.sqrt(U)
        Theta = V
        X = R * np.cos(Theta)
        Y = R * np.sin(Theta)
        Z = R
    
    return X, Y, Z

def plot_3d_surface(X, Y, Z, title='3D Surface Visualization'):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, edgecolor = 'k')
    ax.set_title(title)
    plt.show()

if __name__ == "__main__":
    surfaces = ['flat torus', 'flat cylinder', 'octagon', 'hyperbolic', 'cone points']
    surface_type = input("Enter the type of translation surface (e.g., 'flat torus'): ").strip()
    if surface_type.lower() in surfaces:
        grid_size = int(input("Enter the grid size: ").strip())
    else:
        raise ValueError("Cannot generate vector field for this entry")
    
    if surface_type.lower() == 'flat torus':
        R = float(input("Enter Major Axis: ").strip())
        r = float(input("Enter Minor Axis: ").strip())
        X, Y, Z = generate_3d_points(surface_type=surface_type, grid_size=grid_size, R=r, r=r)
    else:
        X, Y, Z = generate_3d_points(surface_type=surface_type, grid_size=grid_size)
    plot_3d_surface(X, Y, Z, title=f'3D Surface of {surface_type}')