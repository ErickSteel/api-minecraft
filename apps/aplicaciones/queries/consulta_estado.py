import graphene
import os

class EstadoServidor(graphene.ObjectType):
    process = graphene.String()

    def resolve_process(self, info):
        result = str(os.popen("ps -ef | grep server.jar | grep -v grep | awk '{printf $2}'").read())
        result = result.replace('\n', ' ')
        return result