# from PIL import Image, ImageFilter
  
  
# # Opening the image (R prefixed to string
# # in order to deal with '\' in paths)
# image = Image.open(r"lenna.png")
  
# # Converting the image to grayscale, as edge detection 
# # requires input image to be of mode = Grayscale (L)
# image = image.convert("L")
  
# # Detecting Edges on the Image using the argument ImageFilter.FIND_EDGES
# image = image.filter(ImageFilter.FIND_EDGES)
  
# # Saving the Image Under the name Edge_Sample.png
# image.save(r"edge_lenna.png")


from PIL import Image, ImageFilter
  
img = Image.open(r"lenna.png")
  
# Converting the image to grayscale, as Sobel Operator requires
# input image to be of mode Grayscale (L)
img = img.convert("L")
  
# Calculating Edges using the passed laplican Kernel
# ImageFiler.Kernel is the double for loops (-1, -1, -1, -1, ...
final = img.filter(ImageFilter.Kernel((3, 3), (-1, -2, -1, -2, 12,
                                          -2, -1, -2, -1), 1, 0))
  
final.save("secondEdge_Lenna.png")