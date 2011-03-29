import re
PLUGIN_PREFIX   = "/photos/TheSartorialist"
RSS_FEED        = "http://feeds.feedburner.com/TheSartorialist"

####################################################################################################
def Start():
	Plugin.AddPrefixHandler(PLUGIN_PREFIX, MainMenu, "The Sartorialist", "icon-default.png", "art-default.jpg")
	Plugin.AddViewGroup("Pictures", viewMode="Pictures", mediaType="photos")
	MediaContainer.art = R('art-default.jpg')
	MediaContainer.viewGroup = 'Pictures'

####################################################################################################
def MainMenu():
	dir = MediaContainer(title1="The Sartorialist")
	for item in RSS.FeedFromURL(RSS_FEED).entries:
		title = item.title
		node = HTML.ElementFromString(item.content[0].value)
		img = node.xpath("//img")[0].get('src')
		dir.Append(PhotoItem(img, re.sub(r'[^.]+\.+', '', item.title), '', img))

	return dir
