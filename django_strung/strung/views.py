from django.shortcuts import render

def base(request):
  return render(request, 'strung/base.html')

def music_feed(request):
  return render(request, 'strung/music_feed.html')

def discover(request):
  return render(request, 'strung/discover.html')