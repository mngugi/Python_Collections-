import vtk

def func_to_calculate(x, y):
    # Define your own function to calculate z value based on x and y coordinates
    # Replace this with your actual calculation
    return x * x + y * y

def get_id(i, j):
    # Define your own function to calculate the point ID based on indices i and j
    # Replace this with your actual calculation
    return i + j * (X + 1)

x0 = -7  # X domain low end
y0 = -7  # Y domain low end
x_max = 7  # X domain high end
y_max = 7  # Y domain high end
X = 100  # Resolution in x direction. Integer
Y = 100  # Resolution in y direction. Integer

deltax = (x_max - x0) / float(X)
deltay = (y_max - y0) / float(Y)

points = vtk.vtkPoints()
cells = vtk.vtkCellArray()

zvals = []
for j in range(Y + 1):
    for i in range(X + 1):
        x = x0 + deltax * i
        y = y0 + deltay * j

        z_val = func_to_calculate(x, y)
        zvals.append(z_val)
        coord = x, y, z_val
        points.InsertNextPoint(coord)

for j in range(Y):
    for i in range(X):
        quad = vtk.vtkQuad()
        corner_id = get_id(i, j)

        quad.GetPointIds().SetId(0, corner_id)
        quad.GetPointIds().SetId(1, corner_id + 1)
        quad.GetPointIds().SetId(2, corner_id + (X + 2))
        quad.GetPointIds().SetId(3, corner_id + (X + 1))
        cells.InsertNextCell(quad)

mesh = vtk.vtkPolyData()
mesh.SetPoints(points)
mesh.SetPolys(cells)

point_data = vtk.vtkDoubleArray()
point_data.SetNumberOfComponents(1)

for zval in zvals:
    point_data.InsertNextTuple([zval])

mesh.GetPointData().SetScalars(point_data)

norms_generator = vtk.vtkPolyDataNormals()
norms_generator.SetInputData(mesh)

# Create a renderer, render window, and interactor
renderer = vtk.vtkRenderer()
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Add the norms_generator output to the renderer
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(norms_generator.GetOutputPort())
actor = vtk.vtkActor()
actor.SetMapper(mapper)
renderer.AddActor(actor)

# Create cube axes
axes = vtk.vtkCubeAxesActor2D()
axes.SetInputConnection(norms_generator.GetOutputPort())
axes.SetCamera(renderer.GetActiveCamera())
axes.SetLabelFormat("%1.1g")

# Create an outline filter
outline_filter = vtk.vtkOutlineFilter()
outline_filter.SetInputConnection(norms_generator.GetOutputPort())

# Add the outline and cube axes to the renderer
outline_mapper = vtk.vtkPolyDataMapper()
outline_mapper.SetInputConnection(outline_filter.GetOutputPort())
outline_actor = vtk.vtkActor()
# ...

# Add the outline and cube axes to the renderer
outline_mapper = vtk.vtkPolyDataMapper()
outline_mapper.SetInputConnection(outline_filter.GetOutputPort())
outline_actor = vtk.vtkActor()
outline_actor.SetMapper(outline_mapper)
renderer.AddActor(outline_actor)

# ...
# ...

# Create a renderer, render window, and interactor
renderer = vtk.vtkRenderer()
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Add the norms_generator output to the renderer
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(norms_generator.GetOutputPort())
actor = vtk.vtkActor()
actor.SetMapper(mapper)
renderer.AddActor(actor)

# Create cube axes
axes = vtk.vtkCubeAxesActor2D()
axes.SetInputConnection(norms_generator.GetOutputPort())
axes.SetCamera(renderer.GetActiveCamera())
axes.SetLabelFormat("%1.1g")

# Create an outline filter
outline_filter = vtk.vtkOutlineFilter()
outline_filter.SetInputConnection(norms_generator.GetOutputPort())

# Add the outline and cube axes to the renderer
outline_mapper = vtk.vtkPolyDataMapper()
outline_mapper.SetInputConnection(outline_filter.GetOutputPort())
outline_actor = vtk.vtkActor()
outline_actor.SetMapper(outline_mapper)
renderer.AddActor(outline_actor)

# Set up camera and render window
renderer.ResetCamera()
render_window.Render()

# Initialize interactor and start the event loop
interactor.Initialize()
interactor.Start()



