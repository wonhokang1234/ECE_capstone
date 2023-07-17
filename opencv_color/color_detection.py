import scipy.cluster
import sklearn.cluster
import numpy
from PIL import Image
import matplotlib.image as img
import sys


def dominant_colors(image):  # PIL image input

    ar = numpy.asarray(image)
    shape = ar.shape
    ar = ar.reshape(numpy.product(shape[:2]), shape[2]).astype(float)

    kmeans = sklearn.cluster.MiniBatchKMeans(
        n_clusters=10,
        init="k-means++",
        max_iter=20,
        random_state=1000
    ).fit(ar)
    codes = kmeans.cluster_centers_

    vecs, _dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
    counts, _bins = numpy.histogram(vecs, len(codes))    # count occurrences

    colors = []
    for index in numpy.argsort(counts)[::-1]:
        colors.append(tuple([int(code) for code in codes[index]]))
    
    with open("output.txt", 'w') as sys.stdout:
    	print(colors[0])
    return colors                    # returns colors in order of dominance

picture = img.imread('/home/d4/myflection/opencv_color/cropped_image.jpg')
dominant_colors(picture)
