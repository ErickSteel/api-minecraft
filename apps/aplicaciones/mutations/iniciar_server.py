import graphene
import os

class IniciarServer(graphene.Mutation):
	estado = graphene.Boolean()
	minecraft_dir = graphene.String()

	def mutate(self, info):
		os.chdir('/home/erick/Escritorio/Server/')
		os.system('screen -dmS "minecraft" java -Xmx1024M -Xms1024M -jar server.jar --nogui --world ewe')
		return IniciarServer(estado=True, minecraft_dir='home/erick/Escritorio/Server/')