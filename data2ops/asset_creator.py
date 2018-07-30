# create Asset File   


def makeAsset(file_name, GUI_name ='default', GUI_path = 'default'):
	if GUI_name == 'default':
		GUI_name2 = input("What is the GUI name of your data? e.g. Sloan Digital Sky Survey ")
	else:
		GUI_name2 = GUI_name

	if GUI_path == 'default':
		GUI_path2 = input("What is the GUI path for your data? e.g. /Universe/Galaxies (use forward slashes) ")
	else:
		GUI_path2 = GUI_path

	f2 = open(file_name + ".asset","w+")
	f2.write(
	"local assetHelper = asset.require('util/asset_helper') \r\n \r\n \r\n \r\n" +
	"local textures = asset.syncedResource({\r\n" +
	"    Name = \"" + GUI_name2 + " Textures\",\r\n" +
	"    Type = \"HttpSynchronization\",\r\n" + 
	"    Identifier = \"adlerplanetarium_" + file_name + "_textures\",\r\n" + 
	"    Version = 1\r\n" + 
	"})\r\n \r\n" + 
	"local speck = asset.syncedResource({\r\n" +
	"    Name = \"" + GUI_name2 + " Speck Files\",\r\n" + 
	"    Type = \"HttpSynchronization\",\r\n" + 
	"    Identifier = \"adlerplanetarium_" + file_name + "_speck\",\r\n" + 
	"    Version = 1\r\n" + 
	"})\r\n \r\n" +
	"local object = {\r\n" +
	"    Identifier = \"" + GUI_name2 + "\",\r\n" +
	"    Renderable = {\r\n" + 
	"        Type = \"RenderableBillboardsCloud\",\r\n" +
	"        Enabled = false,\r\n" + 
	"        Color = { 0.8, 0.8, 1.0 },\r\n" + 
	"        Transparency = 1.0,\r\n" + 
	"        ScaleFactor = 507.88,\r\n" + 
	"        File = speck .. \"/" + file_name + ".speck\",\r\n" + 
	"        Texture = textures .. \"/point3.png\",\r\n" + 
	"        Unit = \"Mpc\",\r\n" + 
	"        -- Fade in value in the same unit as \"Unit\"\r\n" + 
	"        FadeInDistances = { 220.0, 650.0 },\r\n" + 
	"        BillboardMaxSize = 50.0,\r\n" + 
	"        BillboardMinSize = 0.0,\r\n" + 
	"        TextSize = 14.8,\r\n" + 
	"        TextMinSize = 10.0,\r\n" + 
	"        TextMaxSize = 50.0\r\n" + 
	"    },\r\n" + 
	"    GUI = {\r\n"
	"        Name = \"" + GUI_name2 + "\",\r\n" +
	"        Path = \"" + GUI_path2 + "\"\r\n" +
	"    }\r\n" +
	"}\r\n \r\n \r\n \r\n" + 
	"assetHelper.registerSceneGraphNodesAndExport(asset, { object })"  
	)
		
	f2.close()