
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication


from .models import User
from .serializers import UserSerializer


class UserAPI(APIView):

    authentication_classes = [SessionAuthentication]
    permission_classes     = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        data = request.data  # this is parsed data

        id   = data.get('id', None)


        if id is None:
            all_user = User.objects.all()
            serializer = UserSerializer(all_user, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # if user id is not None
            try:

                user = User.objects.get(pk = id)
                print(user)
            except User.DoesNotExist :
                error = {
                    'Not Exists:': 'User does not exists with Id'
                }
                return Response( error, status=status.HTTP_404_NOT_FOUND)
            else:
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
             
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = {'Inserted Successfuly': serializer.data}
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, format=None):
        id   = request.data.get('id', None)

        

        if id is not None:
            try:
                user = User.objects.get(pk = id)
            
            except:
                pass

            else:
                old_user = UserSerializer(user)

                response= {
                    'Old User data:': old_user.data # old data just for response only
                }
                serializer = UserSerializer(user, data = request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    response['update data'] = serializer.data

                    return Response(response, status=status.HTTP_200_OK)
                
        return Response({'Error': 'Id is required'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):

        id = request.data.get('id', None)

        if id is not None:

            try:
                user = User.objects.get(pk = id)
            except:
                response = {'Error': 'User DoestNotExis'}
            else:
                user.delete()
                response = {'Deleted': 'User Deleted Successfuly'}     
                return Response(response, status=status.HTTP_200_OK)
        return Response({'Error': 'Id is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)


