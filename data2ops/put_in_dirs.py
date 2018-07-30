import os
from shutil import copy2
from data2ops import files2ops

def movefiles(file_name):
	speck_file = file_name + ".speck"
	asset_file = file_name + ".asset"
	
	start_path_OS = 'C:/Users/archiekinnane/Documents/' # input("Write the path to OpenSpace here. e.g C:/Users/akinnane/Desktop/OpenSpace-0.12.0/ ")
	start_path_me = os.getcwd() 
	start_path_files = files2ops.__file__[:-12]
	initial_speck_path = os.path.join(start_path_OS, "sync/http/")

	if os.path.isfile(os.path.join(start_path_me, speck_file)):
		final_path_speck = os.path.join(initial_speck_path, "adlerplanetarium_" + speck_file[:-6] + "_speck/1")
		if not os.path.isdir(final_path_speck):
			os.makedirs (final_path_speck)
			if not os.path.isfile(os.path.join(final_path_speck, speck_file)):
				copy2(os.path.join(start_path_me, speck_file), final_path_speck)
				os.remove(os.path.join(start_path_me, speck_file))
			if not os.path.isfile(os.path.join(final_path_speck[:-1], "1.ossync")):
				copy2(os.path.join(start_path_files, "1.ossync"), final_path_speck[:-1])
				
		final_path_textures = os.path.join(initial_speck_path, "adlerplanetarium_" + file_name + "_textures/1")
		if not os.path.isdir(final_path_textures):
			os.makedirs (final_path_textures)
			if not os.path.isfile(os.path.join(final_path_textures, "point3.png")):
				copy2(os.path.join(start_path_files, "point3.png"), final_path_textures)
			if not os.path.isfile(os.path.join(final_path_textures[:-1], "1.ossync")):
				copy2(os.path.join(start_path_files, "1.ossync"), final_path_textures[:-1])
	else:
		print ("Speck file not found in your directory")
			
	asset_path = os.path.join(start_path_OS, "data/assets/scene/digitaluniverse/")

	if os.path.isfile(os.path.join(start_path_me, asset_file)):
		if not os.path.isfile(os.path.join(asset_path, asset_file)):
			copy2(os.path.join(start_path_me, asset_file), asset_path)
			os.remove(os.path.join(start_path_me, asset_file))
	else:
		print ("Asset file not found in your directory")
