xcbuild
=======

External Xcode scheme build tool
--------------------------------

xcbuild is a minimal build tool to make building complex schemes easier. it was created with the intention of
 building projects that require nested aggregate targets and schemes that require specific ordering.
 
 
Install
-------

To install, run `python setup.py install` optionally add `--user` to install it to the user's python install rather than the system


How To Use
----------


	usage: xcbuild [-h] [-l] [-c CONFIG] [-a ACTION] filename

	Resolve target dependencies

	positional arguments:
	  filename                      path to xcodeproj or xcworkspace

	optional arguments:
	  -h, --help                    show this help message and exit
	  -l, --list                    list schemes
	  -c CONFIG, --config CONFIG    path to the build config file
	  -a ACTION, --action ACTION    action to perform: "build", "test", "launch", "profile", "analyze", or "archive"