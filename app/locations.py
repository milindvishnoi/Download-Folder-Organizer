import os

# To specify all the locations, making location for every
# user dynamic produced unless they edit it
username = os.getcwd().split("/")[2]
download_location = "/Users/" + username + "/Downloads"
other_location = os.path.join(download_location, "others")
photo_location = os.path.join(download_location, "photos")
document_location = os.path.join(download_location, "documents")
folder_location = os.path.join(download_location, "folders")
music_location = os.path.join(download_location, "music")
zipfile_location = os.path.join(download_location, "zipFiles")
video_location = os.path.join(download_location, "videos")
