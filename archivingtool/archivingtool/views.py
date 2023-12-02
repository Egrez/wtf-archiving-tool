from django.shortcuts import render, redirect

from django.urls import reverse

from .forms import PostUrlForm

import asyncio

from archivers import facebook_scraper, tiktok_scraper, youtube_scraper

def home(request):
	
	if request.method == "POST":
		# Create a form instance and populate it with data from the request (binding):
		form = PostUrlForm(data=request.POST)

		if form.is_valid():
			url = form.cleaned_data['url'].strip()
			if "facebook" in url:
				scraped_data =facebook_scraper.scrape(url)
			elif "tiktok" in url:
				scraped_data = asyncio.run(tiktok_scraper.scrape(url))
			elif "youtube" in url:
				scraped_data = youtube_scraper.scrape(url)

			print(scraped_data)
			

	else:
		form = PostUrlForm

	context = {
		'form' : form,
	}

	return render(request, "index.html", context)