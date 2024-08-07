# Django Message Project

## What is Chatting App?

tweetapp is twitter's clone. in my prject, you can;
* send Message
* send Reply
* soft Delete Message
* contacts
* authentication
* profile

> **Note** : I use SQLite

## libraries

### Django
[Django Documents](https://docs.djangoproject.com/en/5.0/)

~~~
pip install Django
~~~

### Django-channels
[Django Channels Documents](https://pypi.org/project/django-channels/)

~~~
pip install django-channels
~~~

### pillow
[Pillow Documents](https://pypi.org/project/pillow/)

~~~
pip install pillow
~~~

## Send Message

### Message Models

* message (Charfield)
* title (Charfield)
* sender (User)
* receiver (User)
* createdAt (DateTimeField)
* deletedAt (DateTimeField)
* readStatus (BooleanField)

### Description

You can send message. But you need to fill this blanks:
* Receiver Username
* Title
* Message

![image](https://github.com/user-attachments/assets/aa1bb95d-7485-4a49-83e6-90637cade41e)

![image](https://github.com/user-attachments/assets/269f0115-d89e-42b4-8479-96235589f4ac)
  
After sending message, new table will create. if you look actions, you can see two actions:
* Reply
* Delete (soft)

> **Note** : When message is reply, reply icon changes info button

> **Note** : When readStatus = False, the message's background turns yellow. If you make Message readed, you can open InfoModal or ReplyModal  

![image](https://github.com/user-attachments/assets/0764abde-e751-430f-917f-c0de86be4f9d)


## Reply Message


You can reply message you need to fill this blank:
* Message

![image](https://github.com/user-attachments/assets/903c60d3-cc80-4509-a038-5142abadc7cd)

After sending tweet, you can see reply icon changes info button

![image](https://github.com/user-attachments/assets/99fb0738-b927-4c00-b818-dc278f791734)

When you click this icon, a modal appears on screen.

![image](https://github.com/user-attachments/assets/defce3fd-77aa-4d24-9bb2-cf6a7d4f0123)

It shows the information of the message.

> **Note** : reply Message is a regular message. only replyStatus = True

## Delete Message (soft delete)

I use Modal to show delete screen.

![image](https://github.com/user-attachments/assets/4b2ac19a-8cab-401d-a409-65de7db66e94)

Messages can delete. but they always saved in Database.

![image](https://github.com/user-attachments/assets/c7106a83-63c5-43b2-baf6-9ad30e4e4093)

## Contacts

This page shows who did you send message or who did send message to you

![image](https://github.com/user-attachments/assets/056055de-4847-4608-8e86-02db1a307348)

### profile

In profile, you can see your account information and change your profile photograph

![image](https://github.com/user-attachments/assets/0561849f-555f-4c80-a525-95d5c1e90d49)

## Authentication

Thats regular authentication system. you can log-in and sign-up.

![image](https://github.com/user-attachments/assets/8fd39fd2-0a28-40b3-bbdc-3a047ce77a6e)

![image](https://github.com/user-attachments/assets/e33faf6f-e318-44e2-8760-f9fe6d69eb27)

I used error messages with bootstrap alerts.

![image](https://github.com/user-attachments/assets/26ae02ce-3b1b-4637-b2d0-df4bfaa45c19)

Log-out

![image](https://github.com/user-attachments/assets/d26bc3ef-c65b-477e-bda4-a95f81787fa8)
