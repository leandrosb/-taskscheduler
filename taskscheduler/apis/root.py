from flask_restplus import Namespace, Resource

ns_root = Namespace('/', description='Endpoints root')


@ns_root.route('/healthz')
class HealthCheck(Resource):
    @classmethod
    def get(cls):
        """
        Chamada para verificar status da aplicacao
        """
        return {'status': 'Ok'}, 200
