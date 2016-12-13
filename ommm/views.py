from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.schemas import SchemaGenerator
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer


# Import all models views

from ommm.viewsDirectory.userViews import *
from ommm.viewsDirectory.favsViews import *
from ommm.viewsDirectory.exercisesViews import *
from ommm.viewsDirectory.sessionViews import *
from ommm.viewsDirectory.subscriptionsViews import *
from ommm.viewsDirectory.tagsViews import *
from ommm.viewsDirectory.typeViews import *


# the documentation view
class SwaggerSchemaView(APIView):
    renderer_classes = [OpenAPIRenderer, SwaggerUIRenderer]

    def get(self, request):

        generator = SchemaGenerator()
        schema = generator.get_schema(request=request)

        return Response(schema)
