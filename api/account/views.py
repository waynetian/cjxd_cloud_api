from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


#class PasswordView(APIView):

class AuthView(APIView):
    def get(self, request, *args, **kwargs):
        q = request.query_params 
        email = q['email']
        password = q['password']

        try:
            username = User.objects.get(email=email)
        except ObjectDoesNotExist:
            raise Http404
    
        user = authenticate(username=username, password=password)
        if user is not None:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            raise Http404
    
    def put(self, request, *args, **kwargs):
        data = request.data
        email = data['email'] 
        password = data['password']
        try: 
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            raise Http404
        user.set_password(password)
        user.save()
        return Response()


        #    snippets = Snippet.objects.all()
        #    serializer = SnippetSerializer(snippets, many=True)
        #    return Response(serializer.data)

        #def post(self, request, format=None):
        #    serializer = SnippetSerializer(data=request.DATA)
        #    if serializer.is_valid():
        #        serializer.save()
        #        return Response(serializer.data, status=status.HTTP_201_CREATED)
        #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrgSetView(APIView):
    def get(self, request, *args, **kwargs):
        q = request.query_params 
        org_id = q['org_id']

        org = Organization.objects.get(id=org_id)
        result = [{b'text':org.name.encode('utf8'), b'org_id':org_id.encode('utf8'), b'nodes':[], b'name':'abc'}, ]
        
        self.RecursiveQuery(int(org_id), result[0]['nodes'])
        print result
        import json
        data = json.dumps(result)
        print data
        from django.http import HttpResponse
 
        return Response(data)

    def RecursiveQuery(self, org_id, result):
        res = Organization.objects.filter(parent_id=org_id)
        for i in res:
            item = {'text': i.name, 'org_id':i.id}
            item['nodes'] = [] 
            result.append(item) 
            self.RecursiveQuery(i.id, item['nodes'])  



class UserInfoView(APIView):
    def get(self, request, *args, **kwargs):
        q = request.query_params 
        user_id = q['user_id']
        try:
            base_info = UserBaseInfo.objects.get(user=user_id)
            
            serializer = UserBaseInfoSerializer(base_info)
            return Response(serializer.data)
  
        except ObjectDoesNotExist:
            raise Http404
    
    def post(self, request, *args, **kwargs):
        pass


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        ''' create a new user '''
        data = request.data
        
        # random generate uuid, max length 30 char
        import uuid
        #username = str(uuid.uuid4())[:-2])
        username = str(uuid.uuid4())[:-6]
        print 'username length is', len(username)
        email = data['email']
        password = data['password']
        try:
            user = User.objects.create_user(username, email, password)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except Exception, e:
            return Response(str(e))    

    #def partial_update(self, request, *args, **kwargs):
    #    ''' '''

    
    #def destroy(self, request, *args, **kwargs):
    #    ''' delete a new user '''
    #    data = request.data
    #    print '*******************'
    #    return Response("delete user")


    #def list(self, request, *args, **kwargs):
    #    ''' delete a new user '''
    #    #data = request.data
    #    print '*******************'
    #    return Response("list user")


class UserBaseInfoViewSet(viewsets.ModelViewSet):
    queryset = UserBaseInfo.objects.all()
    serializer_class = UserBaseInfoSerializer

    def retrieve(self, request, *args, **kwargs):
        user_id = kwargs['pk']
        try:
            base_info = UserBaseInfo.objects.get(user=user_id)
            serializer = UserBaseInfoSerializer(base_info)
            return Response(serializer.data)
  
        except ObjectDoesNotExist:
            raise Http404
 

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        org = Organization()
        org.name = data['name']
        org.short_name = data['short_name'] 
        org.type = data['type'] 
        org.parent_id = int(data['parent_id'])
        org.save()
        if org.parent_id != 0:
            parent_id = org.parent_id
            parent_org =  Organization.objects.get(id=parent_id)
            org.org_id_seq = "%s%s/" %(parent_org.org_id_seq, org.id)
        else:
            org.org_id_seq = "/%s/" %(org.id)
            print org.org_id_seq
        org.save()
        serializer = OrganizationSerializer(org)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        org_id = int(kwargs['pk'])
        
        ret = self.RecursiveDestroy(org_id)
        i = Organization.objects.get(id=org_id)
        i.delete()

        if ret == 0:
            return Response('ok')
 
        return Response('error')

    def RecursiveDestroy(self, org_id):
        ret = 0
        res = Organization.objects.filter(parent_id=org_id)
        for i in res:
            # user exist check
            print i.id
            ret = self.RecursiveDestroy(i.id)
            i.delete()
        return ret



class OrganizationInfoViewSet(viewsets.ModelViewSet):
    queryset = OrganizationInfo.objects.all()
    serializer_class = OrganizationInfoSerializer



    '''
    def list(self, request, *args, **kwargs):
        print '***************************'
        q = request.query_params 
        org_id = q['org_id']
        try:
            base_info = OrganizationInfo.objects.get(org=org_id)
            serializer = OrganizationInfoSerializer(base_info)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            raise Http404
 
    '''

'''
class OrganizationInfoView(APIView):
    def get(self, request, *args, **kwargs):
        q = request.query_params 
        org_id = q['org_id']
        try:
            base_info = OrganizationInfo.objects.get(org=org_id)
            serializer = OrganizationInfoSerializer(base_info)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            raise Http404
    
'''

        

