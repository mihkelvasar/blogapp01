# Blogapp 01
This is the basic app for a possible future personal home page and a business
page.
It was originally written in Python 3.11 and Django 4.2 using sqlite, but any further development will be done
on Python 3.12 and Django 5.

## What is this?
Originally this started as a homework assignment of SDA Academy's Python from Scratch course
as the next logical step from the polls app in Django tutorial.  
Later, I developed an idea to turn it into a personal personal and personal business home page.  
It has been designed for the use of a single user, but can be extended to multiple users if needed.  

## What does it do?
The app is supposed to have two main functional aspects:  
1. Personal blog
- A personal home page with a blog  
- a comment system  
- post sorting by tags  
- comment editing and moderation  
- There are plans to also  
  - add a gallery system to upload and display images as singles and as galleries  
  - link images and galleries with blog posts  
  - add, edit and delete tags from frontend, instead of backend  
  - blog posts can have no tags as well  
  - cool ui with black and deep red colors
  - lots of minor bugs, stupid redirects, field resizes, etc  
2. Business home page section
- reuses the gallery system to create image galleries of different photography types and styles  
- generally bright UI with whites and grays  

Current functionality:  
1. login/logout for a single user.
2. blog post drafting/publishing/unpublishing/editing/deleting
3. Commenting for both logged in and anonymous users
4. tagging posts upon creation and when editing
5. basic page structure with httpResponses for missing pages

## But why?
This is aimed to be a learning experience but also something practical and of use to myself.  

On the learning side:
* I get to build new features in Django  
* I get to build unoptimized database queries and later optimize it  
* Build a UI either from scratch or with a framework
* build towards hosting it on a server (either SaaS or my own)  

On the practical side:
* I am currently paying a lot of money for a simple web page modified with a nocode UI framework.  
* I have a lot of images to share and organize into galleries  
* I want to link blog posts to galleries but not the other way around

## What's next?
This project is currently dormant.  

This was my main on and off project until recently until I realized that I don't want to be 
a Django equivalent of a React-Andy. Knowing the language and knowing a framework are two 
very different things. So I decided to pause this, and do some elementary pure Python projects.  
Or do projects in which I would build similar functionality to what I would do with a framework, 
but without a framework. For example database interactions or applications. Or algorithms and data structures.

## Updates
I finally got a handle on Markdown to some extent, so, thus a new and better ReadMe
