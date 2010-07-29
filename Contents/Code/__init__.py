from PMS import Plugin, Log, DB, Thread, XML, HTTP, JSON, RSS, Utils
from PMS.MediaXML import MediaContainer, DirectoryItem, PhotoItem
import re

PLUGIN_PREFIX   = "/photos/TheSartorialist"
RSS_FEED        = "http://feeds.feedburner.com/TheSartorialist"

####################################################################################################
def Start():
  Plugin.AddRequestHandler(PLUGIN_PREFIX, HandlePhotosRequest, "The Sartorialist", "icon-default.png", "art-default.jpg")
  Plugin.AddViewGroup("Pictures", viewMode="Pictures", contentType="photos")

####################################################################################################
def HandlePhotosRequest(pathNouns, count):
  dir = MediaContainer("art-default.jpg", "Pictures", "The Sartorialist")
  
  if count == 0:
    for item in RSS.Parse(RSS_FEED).entries:
      node = XML.ElementFromString(item.content[0].value, True)
      img = node.xpath("//img")[0].get('src')
      dir.AppendItem(PhotoItem(img, re.sub(r'[^.]+\.+', '', item.title), '', img))

  return dir.ToXML()
