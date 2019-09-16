# Gemini Observatory Community TOM Broker Modules

The [TOM Toolkit](https://github.com/TOMToolkit) comes with a basic module for 
submitting observations to the [Gemini Observatory](https://www.gemini.edu/) Phase 2 
system.  This module adds enhanced support to the TOM
Toolkit for requesting Gemini observations and is a common area for community development. 
For example, using this module TOMs can search for guide stars using 
[GSselect](https://github.com/bryanmiller/gsselect) and then submit observations.  

## Installation:

Install the module into your TOM environment:

    pip install tom-gemini-community

Add the name of the module that you want to use, 
e.g. `tom_gemini_community.gemini.gemini_gsselect`, to the `TOM_FACILITY_CLASSES` 
in your TOM's `settings.py`:

	TOM_FACILITY_CLASSES = [
		'tom_observations.facilities.lco.LCOFacility',
		'tom_observations.facilities.soar.SOARFacility',
		...
		'tom_gemini_community.gemini_gsselect.GEMFacility',
	]
