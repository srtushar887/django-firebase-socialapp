from django.shortcuts import render, redirect

# Create your views here.



import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth, firestore



cred = credentials.Certificate("social-a44c3-firebase-adminsdk-va99i-a207695022.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def filrebaseusers(request):
    if request.user.is_authenticated:
        context = {
            'users' : auth.list_users().iterate_all()
        }

        return render(request, 'dashboard/firebaseUsers.html',context)
    else:
        return render(request,'account/login.html')

def deleteusers(request,uid):
    if request.user.is_authenticated:
        auth.delete_user(uid)
    return redirect('filrebaseusers')




docfile = db.collection('post')

def userposts(request):
    if request.user.is_authenticated:
        getData = docfile.get()
        case_list = []
        for i in getData:
            stored = i.to_dict()
            stored['docid']=i.id
            case_list.append(stored)
        return render (request, "dashboard/firbaseUserPosts.html", {"data": case_list})



likes = db.collection('user_post_like')
comments = db.collection('user_comment')

def postview(request,post_id):
    if request.user.is_authenticated:
        getData = docfile.document(post_id).get()
        postdetail = getData.to_dict()
        like_list = []
        comment_list = []
        get_likes = likes.get()
        get_comments=comments.get()
        for i in get_likes:
            like = i.to_dict()
            if like['id']==postdetail['id']:
                like_list.append(like)

        for i in get_comments:
            comment = i.to_dict()
        if comment['id']==postdetail['id']:
            comment_list.append(comment)
        
        return render (request, "dashboard/postdetails.html", {"data": postdetail,"likes":len(like_list),"commets":comment_list})





del_post = db.collection('post')
del_comment = db.collection('user_comment')
docfile1 = db.collection('post')
def postdelete(request ):
    if request.user.is_authenticated:
        if request.method == 'POST':
            postid = request.POST['postdeleteid']
            getData = docfile1.document(postid).get()
            getData1  = getData.to_dict() 

            getcomment = del_comment.get()
            comar = []
            for i in getcomment:
                comment = i.to_dict()
                if comment['id'] == getData1['id']:
                    comar.append(comment)
                    i.reference.delete()
                    
                    
            getData.reference.delete()

            # print(getData1)
            return redirect('userposts')


docfilecategory = db.collection('categories')
def category(request):
    if request.user.is_authenticated:
        getData = docfilecategory.get()
        case_list = []
        for i in getData:
            stored = i.to_dict()
            stored['docid']=i.id
            case_list.append(stored)
        return render(request,'dashboard/category.html',{"data": case_list})
    else:
        return redirect('login')

save_cat = db.collection('categories')
def categorysave(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            cat = request.POST['category_name']
            data = {
                'category_name' : cat,
            }
            db.collection(u'categories').document().set(data)
    
            return redirect('category')
    else:
        return redirect('login')

update_cat = db.collection('categories')
def updatecategory(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            cat = request.POST['category_name']
            catupid = request.POST['catdeleteid']
            data = {
                'category_name' : cat,
            }
            db.collection(u'categories').document(catupid).update(data)
    
            return redirect('category')
    else:
        return redirect('login')


delete_cat = db.collection('categories')
def deletecategory(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            catdelid = request.POST['catdeleteid']
            getData = delete_cat.document(catdelid).get()
            getData.reference.delete()
            return redirect('category')
    else:
        return redirect('login')


docfilereport = db.collection('report')
def videoreport(request):
    if request.user.is_authenticated:
        getData = docfilereport.get()
        case_list1 = []
        for i in getData:
            stored = i.to_dict()
            stored['docid']=i.id
            case_list1.append(stored)
            return render(request,'dashboard/report.html',{"data": case_list1})
            
    else:
        return redirect('login')

delete_report = db.collection('categories')
def deletereport(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            reportdelid = request.POST['reportdeleteid']
            getData = delete_report.document(reportdelid).get()
            getData.reference.delete()
            return redirect('videoreport')
    else:
        return redirect('login')
            
