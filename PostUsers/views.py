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
        print(comment_list)
        return render (request, "dashboard/postdetails.html", {"data": postdetail,"likes":len(like_list),"commets":comment_list})