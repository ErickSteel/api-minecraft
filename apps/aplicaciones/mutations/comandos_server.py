import graphene
import os

class ComandosServer(graphene.Mutation):
	estado = graphene.Boolean()
	minecraft_dir = graphene.String()
	cmd = graphene.String()
	class Arguments:
		cmd = graphene.String()

	def mutate(self, info, cmd):
		os.system('screen -S minecraft -X stuff "{}\015"'.format(cmd))
		return ComandosServer(estado=False, minecraft_dir='home/erick/Escritorio/Server/', cmd=cmd)
