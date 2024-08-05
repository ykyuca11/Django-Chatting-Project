from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render ,redirect, get_object_or_404,HttpResponse
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.contrib.auth.models import User
from .models import Message , UserProfile
from . import models
from datetime import datetime





# Create your views here.

@login_required
def profile(request):
    # UserProfile'ı get_or_create ile al, yoksa oluştur
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST' and 'profile_photo' in request.FILES:
        user_profile.profile_photo = request.FILES['profile_photo']
        user_profile.save()
        messages.success(request, "Profil fotoğrafı başarıyla güncellendi!")
        return redirect('profile')
    
    return render(request, 'core/profile.html', {'profile': user_profile})


def signup(request):
    if request.method == "POST":
        yasaklikarakterler = "!'^+%&/()=?_-*}][{½$#£><|`,."
        form = SignUpForm(request.POST)
        username = request.POST.get("username")

        if " " in username:
            messages.error(request, "Kullanıcı adında boşluk olamaz!")
        elif len(username) >= 50:
            messages.error(request, "Kullanıcı adın 50'den az karakter ile oluşturulmalıdır!")
        elif len(username) <= 3:
            messages.error(request, "Kullanıcı adın 3'den fazla karakter ile oluşturulmalıdır!")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Başka bir kullanıcı bu ismi almış! Başka bir isim dene!")
        elif any(char in yasaklikarakterler for char in username):
            messages.error(request, "Kullanıcı adında özel karakter olamaz!")
        elif form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
            login(request, user)
            return redirect("contacts")
        
            
    else:
        messages.error(request, "Lütfen bütün boşlukları doldurun!")
        form = SignUpForm()

    return render(request, 'core/signup.html', {"form": form})
def sendMessage(request):

    if not request.user.is_authenticated:
        # Redirect to login page or handle the case where the user is not logged in
        return redirect('login')
    # Kullanıcının aldığı mesajları getir
    allMessages = Message.objects.filter(sender=request.user) | Message.objects.filter(receiver=request.user)

    if request.method == "POST":
        message_content = request.POST.get("sendMessage")
        receiver_username = request.POST.get("receiver")
        message_heading = request.POST.get("headingMessage")
        
        

        



        try:
            receiver_user = User.objects.get(username=receiver_username)
            sent_message = Message.objects.create(message=message_content, sender=request.user, receiver=receiver_user, replyStatus=False, title=message_heading)
            sent_message.save()  # Mesajı kaydetmeyi unutmayın

            return redirect('contacts')  # Başarılı gönderim sonrası istenirse başka bir sayfaya yönlendirme
        except User.DoesNotExist:
           return render(request, 'core/chatting.html', {'messages': allMessages})
        except TypeError:
            return render(request, 'core/chatting.html', {'messages': allMessages})

            

    return render(request, 'core/chatting.html', {'messages': allMessages})



@login_required
def reply_message(request):
    if request.method == "POST":
        message_id = request.POST.get("id")
        reply_content = request.POST.get("replyMessage")

        # Mesajın boş olup olmadığını kontrol et
        if not reply_content:
            print("Yanıt mesajı boş olamaz!")
            return redirect('contacts')

        # Orijinal mesajı al
        try:
            original_message = get_object_or_404(Message, id=message_id)
        except Message.DoesNotExist:
            print("Orijinal mesaj bulunamadı!")
            return redirect('contacts')

        # Yeni yanıt mesajını oluştur
        reply_message = Message(
            message = reply_content,
            title = original_message.title,
            sender = request.user,
            receiver = original_message.sender,
            replyStatus = True,
        )
        reply_message.save()

        print("Yanıt mesajı başarıyla gönderildi!")
        return redirect('contacts')
    else:
        return redirect('contacts')
    


def contacts(request):
    current_user = request.user
    sent_messages = Message.objects.filter(sender=current_user).values_list('receiver_id', flat=True)
    received_messages = Message.objects.filter(receiver=current_user).values_list('sender_id', flat=True)
    
    user_ids = set(sent_messages).union(set(received_messages))
    users = User.objects.filter(id__in=user_ids)
    
    return render(request, 'core/contacts.html', {'users': users})


@login_required
def softDelete(request, id):
    msg = get_object_or_404(Message, id=id)
    msg.deletedAt = datetime.now()
    msg.save()


    return redirect('contacts')

def update_read_status(request, id):
    if request.user.is_authenticated:
        message = get_object_or_404(Message, id=id)
        message.readStatus = True
        message.save()
        return redirect('contacts')
    else:
        return HttpResponse('Unauthorized', status=401)