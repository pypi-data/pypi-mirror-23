========
PyOpenAL
========

PyOpenAL provides OpenAL bindings for python as well as an interface to them.

It even provides a simple way to open OGG Vorbis and OGG Opus files, if used together with `PyOgg <https://pypi.org/project/PyOgg/>`_.

PyOpenAL requires a dynamic OpenAL library (OpenAL32.dll). 
You can use the `official OpenAL library <http://www.openal.org/>`_ (deprecated) or the much better sounding `OpenAL Soft library <http://kcat.strangesoft.net/openal.html>`_, which is still actively developed (or any other OpenAL compatible library).

PyOpenAL provides OpenAL bindings, as you would find them in C++, meaning you can follow any `OpenAL C++ tutorial <http://www.openal.org/documentation/>`_ with Python.
OpenAL's methods expect C types as arguments, which means you will have to convert Python's types to C types using `ctypes <https://docs.python.org/3/library/ctypes.html>`_ if you want to use them directly.
Don't worry though, PyOpenAL can be used without the need to do that.

I removed the support for ALUT, because it is basically impossible to build nowadays. If you want ALUT support, please use the original `PyOpenAL from forrestv <https://github.com/forrestv/PyOpenAL>`_

Examples (with PyOgg)
=========================
Playing a file
--------------------

	from openal import * 
	
	# even though we use PyOgg, we don't have to import it ourselves, 
	# PyOpenAL does that for us (if it can find it)
	
	import time

	# open "test.opus"
	source = oalLoadFile("test.opus")

	source.play()

	while source.get_state() == AL_PLAYING:
		# wait until the file is done playing
		time.sleep(1)
		
	# release resources (don't forget this)
	oalQuit()
		
Streaming a file
----------------

	from openal import *

	# it is not required to do this, it's just to show off it exists
	pyoggSetStreamBufferSize(4096*4)
	oalSetStreamBufferCount(4)

	sourceStream = oalStreamFile("test.ogg")

	sourceStream.play()

	while sourceStream.get_state() == AL_PLAYING:
		# do stuff
		sourceStream.update()
		
	oalQuit()
	
Using OpenAL functions
----------------------

	# here we only import OpenAL's functions 
	# (in case you don't need / want PyOpenAL's functions / classes)
	from openal._al import *
	from openal._alc import *

	[...]
	
	# it's as simple as that:
	alDistanceModel(AL_INVERSE_DISTANCE_CLAMPED)
	
	# or a little more complicated, it really depends:
	alSourceUnqueueBuffers(source_id, 1, ctypes.pointer(ctypes.c_uint(buffer_ids[id])))
	
	[...]

To get a reference sheet, please visit `PyOpenAL's GitHub page <https://github.com/Zuzu-Typ/PyOpenAL>`_.
========================================================================================================
