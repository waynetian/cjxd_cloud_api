import json
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
            u = User.objects.get(username=username)
            print u.pk 
        except ObjectDoesNotExist:
            raise Http404
    
        user = authenticate(username=username, password=password)
        print user
        if user is not None:
            org2user = OrganizationToUser.objects.get(user=user.pk)
            base_info = UserBaseInfo.objects.get(user_id=user.pk)
            org = Organization.objects.get(id=org2user.org_id)
            role = Role.objects.get(role_id=org2user.role_id)
    
            serializer = OrgUserSerializer({'base_info':base_info,\
                                        'org':org, \
                                        'role':role, \
                                        'org2user':org2user})
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


 
class MultiOrgUserView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            q = request.data
            org_map = json.loads(q['org_map'])
            orguser_list = json.loads(q['orguser_list'])
            domain_id = int(q['domain_id'])
            domain_name = q['domain_name']
            
            #domain = Organization.objects.get(id=domain_id) 
            path = "/%s" %domain_name
            path_map = {path: domain_id}
            for k, v in org_map.items():
                if k in path_map:
                    continue
                self.RecursiveCreate(k, v , path_map, org_map)

            for q in orguser_list:
                try:
                    user_name = q['user_name']
                    email = q['email']
                    mobile_number = q['mobile_number'] 
                    id_number = q['id_number']
                    path = q['path']
                    org_id = path_map[path]
                    job_title = q['job_title']
                    job_type = int(q['job_type'])
                    role_id = int(q['role_id'])
                    domain_id = domain_id

                    import uuid
                    uid = str(uuid.uuid4())[:-6]
                    password = 'cjxd123'
                    user = User.objects.create_user(uid, email, password)
                    role = Role.objects.get(role_id=role_id) 
                    org = Organization.objects.get(id=org_id)
        
                    base_info = UserBaseInfo()
                    base_info.user = user
                    base_info.email = email
                    base_info.name = user_name 
                    base_info.id_number = id_number 
                    base_info.domain_id = domain_id
                    if mobile_number != '':
                        base_info.mobile_number = mobile_number
                    base_info.save()

                    org2user = OrganizationToUser()
                    org2user.user = base_info
                    org2user.org = org
                    org2user.role = role
                    org2user.job_type = job_type
                    org2user.job_title = job_title
                    org2user.save()
                except Exception, e:
                    print q, e
            return Response("ok")
        except Exception, e:
            import traceback
            traceback.print_exc()
            return Response("error")

 
    def RecursiveCreate(self, k, v, path_map, org_map):
        import os
        parent_path = os.path.dirname(k)
        if parent_path not in path_map:
            new_k = parent_path
            new_v = org_map[new_k]
            self.RecursiveCreate(new_k, new_v, path_map, org_map) 
        parent_id = path_map.get(parent_path)
        org = Organization()
        print v
        org.name = v['name']
        org.short_name = v['short_name'] 
        org.type = v['type']
        org.parent_id = parent_id
        org.save()
        path_map[k] = org.id
        if org.parent_id != 0:
            parent_id = org.parent_id
            parent_org =  Organization.objects.get(id=parent_id)
            org.org_id_seq = "%s%s/" %(parent_org.org_id_seq, org.id)
        else:
            org.org_id_seq = "/%s/" %(org.id)
        org.save()




class OrgUserView(APIView):
    def scope_query(self, request):
        q = request.query_params 
        org_id = int(q['org_id'])
        print org_id
        parent_org_list = []
        org = Organization.objects.get(id=org_id)
        parent_id_list = org.org_id_seq.split('/')
        for i in  parent_id_list:
            if i=="":
                continue
            ii = Organization.objects.get(id=i)
            parent_org_list.append({'name':ii.short_name, 'id':ii.id})
        #parent_org_list.append({'name':org.short_name, 'id':org.id})
            
        print 'aaa'
 
        result = []


        org_list = Organization.objects.filter(parent_id=org_id)
        for i in org_list: 
            result.append( {'text':i.short_name, 'org_id':i.id, 'org_id_seq': i.org_id_seq,  'icon':'glyphicon glyphicon-folder-close green', 'node_type':'org'})
        
        o2u_list=OrganizationToUser.objects.filter(org__id=org_id)
        
        for i in o2u_list:

            mobile = {'text': i.user.mobile_number,  'icon': "glyphicon glyphicon-earphone",'node_type':'mobile'}
            email =  {'text': i.user.email,  'icon': "glyphicon glyphicon-envelope", 'node_type':'email', }
            node = [mobile, email]
            job_title = i.job_title
            result.append({'text':i.user.name, 'nodes':node,'icon': "glyphicon glyphicon-user blue", 'node_type':'user', 'tags':[job_title] })

        rsp = {'parent_org_list':parent_org_list, 'result':result} 
        data = json.dumps(rsp)
        from django.http import HttpResponse
        return Response(data)



    def get(self, request, *args, **kwargs):
        q = request.query_params 
        if 'scope' in q:
            return self.scope_query(request)

        org_id = int(q['org_id'])
        page_num = int(q['page_num'])
        num_per_page = 15 

        page_start = (page_num - 1) * num_per_page
        page_end = page_num * num_per_page
          
        org = Organization.objects.get(id=org_id)

        org_id_seq = org.org_id_seq
        o2u_list=OrganizationToUser.objects.filter(org__org_id_seq__startswith=org_id_seq)[page_start: page_end]
       
        #org = OrganizationToUser.objects.filter(id__in=[54,66])
 
        result_list = []
        for i in o2u_list:
           result_list.append({'base_info':i.user,\
                                     'org':i.org, \
                                    'role':i.role, \
                                'org2user':i})

        #self.RecursiveGet(org_id, result_list)
        serializer = OrgUserSerializer(result_list, many=True)   

        return Response(serializer.data)

    def RecursiveGet(self, org_id, result_list):
        org_list = Organization.objects.filter(parent_id=org_id ) 
        for i in org_list:
            o2u_list=OrganizationToUser.objects.filter(org=i.id)
            for ii in o2u_list: 
                result_list.append({'base_info':ii.user,\
                                          'org':ii.org, \
                                         'role':ii.role, \
                                     'org2user':ii})
            self.RecursiveGet(i.id, result_list)
             

    def post(self, request, *args, **kwargs):
        q = request.data
        user_name = q['user_name']
        email = q['email']
        mobile_number = q['mobile_number'] 
        id_number = q['id_number']
        org_id = int(q['org_id'])
        job_title = q['job_title']
        job_type = int(q['job_type'])
        role_id = int(q['role_id'])
        domain_id = int(q['domain_id'])


        user_id = None
        try:
            user_id = q['user_id']
        except KeyError:
            pass
        user = None 

        if user_id is not None: 
            user = User.objects.get(id=user_id)
        else:
            import uuid
            uid = str(uuid.uuid4())[:-6]
            password = 'cjxd123'
            user = User.objects.create_user(uid, email, password)
        role = Role.objects.get(role_id=role_id) 
        org = Organization.objects.get(id=org_id)
        
        base_info = UserBaseInfo()
        base_info.user = user
        base_info.email = email
        base_info.name = user_name 
        base_info.id_number = id_number 
        base_info.domain_id = domain_id
        if mobile_number != '':
            base_info.mobile_number = mobile_number
        base_info.save()

        org2user = OrganizationToUser()
        org2user.user = base_info
        org2user.org = org
        org2user.role = role
        org2user.job_type = job_type
        org2user.job_title = job_title
        org2user.save()
        
        serializer = OrgUserSerializer({'base_info':base_info,\
                                        'org':org, \
                                        'role':role, \
                                        'org2user':org2user})
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        pk = int(request.path.split('/')[2])
        try: 
            i = User.objects.get(id=pk)
            i.delete()
            return Response('ok')
        except Exception:
            return Response('error')

    
    def put(self, request, *args, **kwargs):
        pk = int(request.path.split('/')[2])
        q = request.data
        user_name = q['user_name']
        email = q['email']
        mobile_number = q['mobile_number'] 
        id_number = q['id_number']
        org_id = int(q['org_id'])
        old_org_id = int(q['old_org_id'])
        job_title = q['job_title']
        job_type = q['job_type']
        role_id = int(q['role_id'])
      
        user_id = pk 

        user = User.objects.get(id=user_id)
        role = Role.objects.get(role_id=role_id) 
        org = Organization.objects.get(id=org_id)
        
        base_info = UserBaseInfo.objects.get(user_id=user_id)
        base_info.user = user
        base_info.email = email
        base_info.name = user_name 
        base_info.id_number = id_number 
        if mobile_number != '':
            base_info.mobile_number = mobile_number
        base_info.save()
     
        org2user = None 
        if org_id == old_org_id:  
            org2user = OrganizationToUser.objects.get(user_id=user_id, org_id=org_id ) 
        else:
            org2user = OrganizationToUser.objects.get(user_id=user_id, org_id=old_org_id ) 
        org2user.org = org
        org2user.role = role
        org2user.job_type = job_type
        org2user.job_title = job_title
        org2user.save()
        
        serializer = OrgUserSerializer({'base_info':base_info,\
                                        'org':org, \
                                        'role':role, \
                                        'org2user':org2user})
        return Response(serializer.data)





class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        ''' create a new user '''
        data = request.data
        
        # random generate uuid, max length 30 char
        import uuid
        username = str(uuid.uuid4())[:-6]
        email = data['email']
        password = data['password']
        try:
            user = User.objects.create_user(username, email, password)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except Exception, e:
            return Response(str(e), status=500)    
    

 
class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


    def list(self, request, *args, **kwargs):
        q = request.query_params 
        if len(q) == 0:
            return super(OrganizationViewSet, self).list(request, *args, **kwargs)
        else:
            org_id = q['org_id']
            org = Organization.objects.get(id=org_id)
            result = [{'text':org.short_name, 'org_id':org_id, 'nodes':[], 'short_name': org.short_name, }, ]
        
            self.RecursiveQuery(int(org_id), result[0]['nodes'])
            data = json.dumps(result)
            from django.http import HttpResponse
            return Response(data)

    def RecursiveQuery(self, org_id, result):
        res = Organization.objects.filter(parent_id=org_id)
        for i in res:
            item = {'text': i.short_name, \
                  'org_id':i.id, \
              'short_name':i.short_name}
            item['nodes'] = [] 
            result.append(item) 
            self.RecursiveQuery(i.id, item['nodes'])  


    def update(self, request, *args, **kwargs):
        org_id = int(kwargs['pk'])
        
        data = request.data
        name = data['name'] 
        short_name = data['short_name']
        parent_id = data['parent_id']
        try: 
            org = Organization.objects.get(id=org_id)
        except ObjectDoesNotExist:
            raise Http404
        org.name = name
        org.short_name = short_name
        new_parent_org = Organization.objects.get(id=parent_id)
        old_parent_org = Organization.objects.get(id=org.parent_id)
        org.org_id_seq = org.org_id_seq.replace(\
                               old_parent_org.org_id_seq, \
                               new_parent_org.org_id_seq)
        org.parent_id = parent_id 
        org.save()
        return Response("ok")


 
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
        #UserBaseInfo.objects.filter(org_id=org_id).delete()


        for i in res:
            # user exist check
            ret = self.RecursiveDestroy(i.id)
            i.delete()
        return ret





class OrganizationInfoViewSet(viewsets.ModelViewSet):
    queryset = OrganizationInfo.objects.all()
    serializer_class = OrganizationInfoSerializer




