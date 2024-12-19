from django.http import HttpResponse
from django.shortcuts import render
from .models import app
import gridfs
from db_connection import db
import base64



# Create your views here.

def home(request):
    name,email,fs,phone,register,coll,address,fss="","","","","",{},"",""

    if 're' in request.POST:
        name=request.POST['n']
        email=request.POST['e']
        phone=request.POST['p']
        address=request.POST['ad']
        register=int(request.POST['r'])
        file=request.FILES.get('img')
        if file:
                fs=gridfs.GridFS(db)
                fss=fs.put(file,filename=file.name)
        cnt=app.aggregate([{"$count":'count'}])
        c=0
        for i in cnt:
             c=i['count']
             break
        coll={"name":name,"email":email,"phone":phone,"address":address,'img':file.name,'img':fss,"register":register}  
        app.insert_one(coll)
    elif 'fet' in request.POST:
         register=int(request.POST['r'])
         if register:
            coll=app.find_one({'register':register})
            fs=gridfs.GridFS(db)
            fl=fs.get(coll['img'])
            image_data=fl.read()
            encoded_data = base64.b64encode(image_data).decode('utf-8')
            coll['img']=f"data:image/{fl.content_type};base64,{encoded_data}"
            print(app.find_one({"register":register}))
         
       
    return render(request,"regi/index.html",{"coll":coll})



