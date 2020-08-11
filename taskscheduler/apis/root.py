from flask_restplus import Namespace, Resource

ns_root = Namespace('/', description='Endpoints root')


@ns_root.route('/healthz')
class HealthCheck(Resource):
    def get(self):
        """
        Chamada para verificar status da aplicacao
        """
        return {'status': 'Ok'}, 200
