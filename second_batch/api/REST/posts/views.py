from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(http_method_names=["GET", "POST"])
def homepage(request: Request):
    if request.mthod == "POST":
        data = request.data
        response = {"message": "Hello World"}
        return Response(data=data)
    response = {"message": "Hello World"}
    return Response(data=response, status=status.HTTP_200_OK)
