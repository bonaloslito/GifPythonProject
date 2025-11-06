import imageio.v3 as iio

filenames = [r'c:\Users\bonal\OneDrive\Documents\DataProjects\PythonJupyterNotebook\mustang.png', r'c:\Users\bonal\OneDrive\Documents\DataProjects\PythonJupyterNotebook\mustang2.png', r'c:\Users\bonal\OneDrive\Documents\DataProjects\PythonJupyterNotebook\mustang3.png']
images = [ ]


for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('mustang.gif', images, duration = 500, loop = 0)