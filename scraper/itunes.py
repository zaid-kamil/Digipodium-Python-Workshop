# -*- coding: utf-8 -*-
import scrapy


class ItunesSpider(scrapy.Spider):
	name = 'itunes'
	allowed_domains = ['www.apple.com']
	start_urls = ['http://www.apple.com/in/itunes/charts/songs/',
	'https://www.apple.com/in/itunes/charts/albums/',
	'https://www.apple.com/in/itunes/charts/movies/',
	'https://www.apple.com/in/itunes/charts/free-apps/',
	'https://www.apple.com/in/itunes/charts/paid-apps/',
	'https://www.apple.com/in/itunes/charts/music-videos/',
	]

	def parse(self, response):
		area = response.css('div.section-content')
		list_items =  area.css('li')
		print(len(list_items))
		print('--'*15)
		for item in list_items:
			yield { 
			'title': item.css('h3 a::text').extract_first(), #string
			'creator' : item.css('hcreator4 a::text').extract_first(), #string
			'rank' : item.css('strong::text').extract_first(), #string
			'link' : item.css('h3 a::attr(href)').extract_first(),
			}

           
