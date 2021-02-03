

# convertire les fichier mp4 en fichier mp3
###############################################################
def convertisseur () :

	import menu
	import moviepy.editor
	mp3 = '.mp3'
	mp4 = '.mp4'

	nom_fichier = menu.nom_fichier()
	chemin_fichier = menu.chemin_fichier()
	mp4_file = chemin_fichier+nom_fichier+mp4
	mp3_file = chemin_fichier+nom_fichier+mp3


	videoclip = moviepy.editor.VideoFileClip(mp4_file)
	audioclip = videoclip.audio
	audioclip.write_audiofile(mp3_file)
	audioclip.close()
	videoclip.close()
##################################################################