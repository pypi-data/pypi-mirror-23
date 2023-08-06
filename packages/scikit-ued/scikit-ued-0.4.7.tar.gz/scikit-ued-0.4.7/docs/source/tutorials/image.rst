.. include:: ../references.txt

.. _image_analysis_tutorial:

***********************
Image Analysis Tutorial
***********************

Diffraction patterns analysis is essentially specialized image processing. This tutorial
will show some of the image processing and analysis techniques that are part of the :mod:`skued.image` module.

Contents
========

* :ref:`streaming`
* :ref:`alignment`
* :ref:`symmetry`
* :ref:`powder`

.. _streaming:

Streaming Image Processing
==========================

Diffraction datasets can be large, much larger than a machine can handle
in-memory. In this case, it makes sense to assemble processing pipelines instead
of working on the data all at once.

Consider the following snippet to combine 50 images 
from an iterable :data:`source`::

	import numpy as np

	images = np.empty( shape = (2048, 2048, 50) )
	from index, im in enumerate(source):
	    images[:,:,index] = im
	
	avg = np.average(images, axis = 2)

If the :data:`source` iterable provided 1000 images, the above routine would
not work on most machines. Moreover, what if we want to transform the images 
one by one before averaging them? What about looking at the average while it 
is being computed?

Scikit-ued provides some functions that can make streaming processing possible. These
function will have an 'i' prefix (for :func:`iter`). Let's look at an example::

	import numpy as np
	from skued.image import ialign, iaverage
	from skimage.io import imread

	stream = map(imread, list_of_filenames)
	aligned = ialign(stream)
	averaged = iaverage(aligned)

At this point, the generators :func:`map`, :func:`ialign`, and :func:`iaverage` are 'wired'
but will not compute anything until it is requested. We can use the function
:func:`last` to get at the final average, but we could also look at the average
step-by-step by calling :func:`next`::

	from skued import last

	avg = next(averaged) # only one images is loaded, aligned and added to the average
	total = last(averaged) # average of the entire stream

An important advantage of processing images in a streaming fashion is the lower
memory usage; this allows the use of multiple processes in parallel::

	from skued import pmap

	def align_and_avg(filenames):
	    stream = map(imread, filenames)
	    aligned = ialign(stream)
	    return last(iaverage(aligned))
	
	batches = [list_of_filenames1, list_of_filenames2, list_of_filenames3]
	
	for avg in pmap(align_and_avg, batches, processes = 3):
	    # write to disk of display
	    pass

Scikit-ued provides a few streaming statistical functions (:func:`ivar`, :func:`istd`, 
:func:`isem`, :func:`iaverage`) which are tested to have exact same results are the familiar
:mod:`numpy` and :mod:`scipy` equivalents. You can also find more specialized streaming functions (e.g. :func:`ialign`).

Example: averaging with error
------------------------------

It is possible to combine :func:`iaverage` and :func:`isem` into a single stream using :func:`itertools.tee`. 
Here is a recipe for it::

	def iaverage_with_error(images, weights):    
	    """ 
	    Combined streaming average and standard error of diffraction images. 
		
	    Parameters
	    ----------
	    images : iterable of ndarrays
	    	Images to be averaged. This iterable can also a generator.
	    weights : iterable of ndarray, iterable of floats, or None, optional
	    	Array of weights. See `numpy.average` for further information. If None (default), 
	    	total picture intensity of valid pixels is used to weight each picture.
	    
	    Yields
	    ------
	    avg : `~numpy.ndarray`
	    	Weighted average. 
	    sem : `~numpy.ndarray`
	    	Standard error in the mean
	    """
	    stream1, stream2 = itertools.tee(images, 2)
	    averages = iaverage(stream1, weights = weights)
	    errors = isem(stream2)
	    yield from zip(averages, errors)

.. _alignment:

Diffraction pattern alignment
=============================

Diffraction patterns can drift over a period of a few minutes, and for reliable data synthesis
it is important to align patterns to a reference.

The procedure of detecting, or registering, the translation between two similar images is usually
done by measuring the cross-correlation between images. When images are very similar, this procedure
is fine; take a look at scikit-image's :func:`skimage.feature.register_translation` for example. 

However, diffraction patterns all have a fixed feature: the position of the beam-block. Therefore, some pixels 
in each diffraction pattern must be ignored in the computation of the cross-correlation. 

Setting the 'invalid pixels' to 0 will not work, at those will correlate with the invalid pixels from the reference. One must use
the **masked normalized cross-correlation** through scikit-ued's :func:`mnxc2`.

All of this is taken care of in scikit-ued's :func:`diff_register` function. Let's look at some polycrystalline Chromium:

.. plot::

	from skimage.io import imread
	import matplotlib.pyplot as plt

	ref = imread('Cr_1.tif')
	im = imread('Cr_2.tif')

	fig, (ax1, ax2, ax3) = plt.subplots(nrows = 1, ncols = 3, figsize = (9,3))
	ax1.imshow(ref, vmin = 0, vmax = 200)
	ax2.imshow(im, vmin = 0, vmax = 200)
	ax3.imshow(ref - im, cmap = 'RdBu_r')

	for ax in (ax1, ax2, ax3):
		ax.get_xaxis().set_visible(False)
		ax.get_yaxis().set_visible(False)

	ax1.set_title('Reference')
	ax2.set_title('Data')
	ax3.set_title('Difference')

	plt.tight_layout()
	plt.show()

From the difference pattern, we can see that the 'Data' pattern is shifted from 'Reference' quite a bit.
To determine the exact shift, we need to use a mask that obscures the beam-block and main beam::

	from skued.image import diff_register, shift_image
	import numpy as np

	ref = imread('Cr_1.tif')
	im = imread('Cr_2.tif')

	mask = np.zeros_like(ref, dtype = np.bool)
	mask[0:1250, 950:1250] = True

	shift = diff_register(im, reference = ref, mask = mask)
	im = shift_image(im, shift)

Let's look at the difference:

.. plot::

	from skimage.io import imread
	import matplotlib.pyplot as plt
	import numpy as np
	from skued.image import diff_register, shift_image

	ref = imread('Cr_1.tif')
	im = imread('Cr_2.tif')

	mask = np.zeros_like(ref, dtype = np.bool)
	mask[0:1250, 950:1250] = True

	shift = diff_register(im, ref, mask)
	shifted = shift_image(im, -shift)

	fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(nrows = 2, ncols = 3, figsize = (9,6))
	ax1.imshow(ref, vmin = 0, vmax = 200)
	ax2.imshow(im, vmin = 0, vmax = 200)
	ax3.imshow(ref - im, cmap = 'RdBu_r')
	ax4.imshow(mask, vmin = 0, vmax = 1, cmap = 'binary')
	ax5.imshow(shifted, vmin = 0, vmax = 200)
	ax6.imshow(ref - shifted, cmap = 'RdBu_r')

	for ax in (ax1, ax2, ax3, ax4, ax5, ax6):
		ax.get_xaxis().set_visible(False)
		ax.get_yaxis().set_visible(False)

	ax1.set_title('Reference')
	ax2.set_title('Data')
	ax3.set_title('Difference')
	ax4.set_title('Mask')
	ax5.set_title('Aligned data')
	ax6.set_title('Diff. after shift')

	plt.tight_layout()
	plt.show()

.. _symmetry:

Image processing involving symmetry
===================================

Rotational symmetry
-------------------
Diffraction patterns exhibit rotational symmetry based on the crystal structure. We can
take advantage of such symmetry to correct images in case of artifacts or defects. A useful
routine is :func:`nfold`, which averages portions of a diffraction pattern with itself based on
rotational symmetry.

.. plot::

    import matplotlib.pyplot as plt
    from skimage.io import imread
    from skued.image import nfold
    import numpy as np

    center = (1010, 1111)

    mask = np.zeros((2048, 2048), dtype = np.bool)
    mask[1100::, 442:480] = True # Artifact line
    mask[0:1260, 900:1140] = True # beamblock

    image = imread('graphite.tif')
    av = nfold(image, mod = 6, center = center, mask = mask)

    fig , (ax1, ax2, ax3) = plt.subplots(1,3, figsize = (9,3))
    ax1.imshow(image, vmin = 0, vmax = 150)
    ax2.imshow(mask, vmin = 0, vmax = 1)
    ax3.imshow(av, vmin = 0, vmax = 150)

    for ax in (ax1, ax2, ax3):
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)

    ax1.set_title('Graphite')
    ax2.set_title('Mask')
    ax3.set_title('Averaged')

    plt.tight_layout()
    plt.show()

To use :func:`nfold`, all you need to know is the center of the diffraction pattern::

    from skued.image import nfold
    from skimage.io import imread

    im = imread('graphite.tif')
    av = nfold(im, mod = 6, center = center)    # mask is optional

.. _powder:

Image analysis on polycrystalline diffraction patterns
======================================================

Center-finding
--------------
Polycrystalline diffraction patterns display concentric rings, and finding
the center of those concentric rings is important. Let's load a test image:

.. plot::

    from skimage.io import imread
    import matplotlib.pyplot as plt
    path = 'Cr_1.tif'

    im = imread(path, plugin = 'tifffile')
    mask = np.zeros_like(im, dtype = np.bool)
    mask[0:1250, 950:1250] = True

    im[mask] = 0
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.imshow(im, vmin = 0, vmax = 200)

    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    plt.show()

This is a noisy diffraction pattern of polycrystalline vanadium dioxide. 
Finding the center of such a symmetry pattern can be done with the 
:func:`powder_center` routine::
	
	from skued.image import powder_center
	ic, jc = powder_center(im, mask = mask)
	
	# Plotting the center as a black disk
	import numpy as np
	ii, jj = np.meshgrid(np.arange(im.shape[0]), np.arange(im.shape[1]),
	                     indexing = 'ij')
	rr = np.sqrt((ii - ic)**2 + (jj - jc)**2)
	im[rr < 100] = 0

	plt.imshow(im, vmax = 200)
	plt.show()

.. plot::

    from skimage.io import imread
    import numpy as np
    import matplotlib.pyplot as plt
    path = 'Cr_1.tif'
    im = imread(path, plugin = 'tifffile')
    from skued.image import powder_center
    mask = np.zeros_like(im, dtype = np.bool)
    mask[0:1250, 950:1250] = True
    ic, jc = powder_center(im, mask = mask)
    ii, jj = np.meshgrid(np.arange(im.shape[0]), np.arange(im.shape[1]),indexing = 'ij')
    rr = np.sqrt((ii - ic)**2 + (jj - jc)**2)
    im[rr < 100] = 1e6

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.imshow(im, vmin = 0, vmax = 200)

    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)

    plt.show()

Angular average
---------------

First, we create a test image::

	import numpy as np
	import matplotlib.pyplot as plt
	from skued import gaussian

	image = np.zeros( (256, 256) )
	xc, yc = image.shape[0]/2, image.shape[1]/2	# center

	extent = np.arange(0, image.shape[0])
	xx, yy = np.meshgrid(extent, extent)
	rr = np.sqrt((xx - xc)**2 + (yy-yc)**2)
	image += gaussian([xx, yy], center = [xc, yc], fwhm = 200)
	image[np.logical_and(rr < 40, rr > 38)] = 1
	image[np.logical_and(rr < 100, rr > 98)] = 0.5
	image /= image.max()	# Normalize max to 1
	image += np.random.random(size = image.shape)

	plt.imshow(image)
	plt.show()

.. plot::

    import numpy as np
    import matplotlib.pyplot as plt
    from skued import gaussian
    image = np.zeros( (256, 256) )
    xc, yc = image.shape[0]/2, image.shape[1]/2	# center
    extent = np.arange(0, image.shape[0])
    xx, yy = np.meshgrid(extent, extent)
    rr = np.sqrt((xx - xc)**2 + (yy-yc)**2)
    image += gaussian([xx, yy], center = [xc, yc], fwhm = 200)
    image[np.logical_and(rr < 40, rr > 38)] = 1
    image[np.logical_and(rr < 100, rr > 98)] = 0.5
    image /= image.max()	# Normalize max to 1
    image += np.random.random(size = image.shape)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.imshow(image)

    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    plt.show()


... and we can easily compute an angular average::
	
	from skued.image import angular_average

	radius, intensity = angular_average(image, (xc, yc))

	plt.plot(radius, intensity)

.. plot::
	
	from skued.image import angular_average
	from skued import gaussian
	import numpy as np
	import matplotlib.pyplot as plt
	from skued import gaussian
	image = np.zeros( (256, 256) )
	xc, yc = image.shape[0]/2, image.shape[1]/2	# center
	extent = np.arange(0, image.shape[0])
	xx, yy = np.meshgrid(extent, extent)
	rr = np.sqrt((xx - xc)**2 + (yy-yc)**2)
	image += gaussian([xx, yy], center = [xc, yc], fwhm = 200)
	image[np.logical_and(rr < 40, rr > 38)] = 1
	image[np.logical_and(rr < 100, rr > 98)] = 0.5
	image /= image.max()	# Normalize max to 1
	image += np.random.random(size = image.shape)
	radius, intensity = angular_average(image, (xc, yc))
	plt.plot(radius, intensity)
	plt.show()

:ref:`Return to Top <image_analysis_tutorial>`