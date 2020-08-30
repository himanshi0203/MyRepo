# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CompanyDetails(models.Model):
    
    description = models.TextField(null=True)
    title = models.CharField(null=True, max_length=200)
    url = models.URLField(null=True)
    company_logo = models.URLField(null=True)
    company = models.CharField(null=True, max_length=200)
    id = models.CharField(max_length=200, primary_key=True)
    company_url = models.URLField(null=True)
    how_to_apply = models.TextField(null=True)
    location = models.TextField(null=True)
    type = models.CharField(null=True, max_length=200)
    created_at = models.CharField(null=True, max_length=100)

    class Meta:
        pass




#    {"description":"<p>COMPANY DESCRIPTION:\nA boutique digital marketing firm specializing in data driven campaign management. As a very efficient and small company we hold personal responsibility in the highest regard.</p>\n<p>JOB DESCRIPTION:\nOur Agency is looking for an extraordinarily skilled person in php, HTML, CSS, Node.js, TypeScript, MySQL, Wordpress &amp; customizing WP plugins, Google Cloud Platform, and CloudFlare.</p>\n<p>ABOUT THE ROLE:\nWe are actively seeking a Mid-Level Programmer who can work from home with extraordinary efficiency. You must be able to work independently, self-motivate yourself and be creative and ambitious enough to sometimes develop your own projects.</p>\n<p>EXPERIENCE:</p>\n<ul>\n<li>Developing code, systems and tools needed to maximize and streamline our business. You\u2019ll be working on sales web pages, landing pages, tracking visitor behavior, and more. We use php with App Engine on Google Cloud Platform to serve many landing pages, occasionally use ClickFunnels, and use CloudFlare caching and workers to speed things up.</li>\n<li>Adding integrations to other applications, ensuring that our data flow is efficient and secure. Developing tools that combine data (pageviews, clicks, conversions, revenue, etc) from different sources (3rd party APIs, databases, Google Analytics) into consolidated reports, as per our data analyst\u2019s needs. Finding or building new tools to enhance our marketing initiatives performance by automating or streamlining our processes. For new tools, you will be able to suggest which programming language to use based on your preferences.</li>\n<li>Recommending improvements to existing systems/tools for efficiency in design and maintaining quality control. Our tools include integrations with 3rd party SASS providers (Brax, ThriveTracker), an internal marketing dashboard and tracking and monitoring systems.</li>\n<li>Any other technical/developing needs of the business. Such as brainstorming and building new tools to automate tasks or streamline workflows. Also, diagnosing and fixing any bugs or problems that arise in our existing proprietary tools (many written in node.js).</li>\n<li>A small part of the job includes maintaining an image gallery based Wordpress site hosted on Kinsta.</li>\n</ul>\n<p>QUALIFICATIONS:</p>\n<ul>\n<li>Prior Programming experience with internet marketing</li>\n<li>Familiarity with best practices for software development and/or web development.</li>\n<li>Creative problem solver.</li>\n<li>Experience in php, HTML, CSS, Node.js, TypeScript, MySQL, Wordpress &amp; customizing WP plugins, Google Cloud Platform, and CloudFlare.</li>\n<li>Expert experience in GIT or other source management systems.</li>\n<li>Some experience in Wordpress custom themes and plugins (not required, but would be nice)</li>\n<li>Intrinsically self motivated with the ability to work on multiple projects relating to different topics at once.</li>\n<li>Team player with excellent communication skills.</li>\n</ul>\n<p>WE OFFER:</p>\n<ul>\n<li>Flexibility: Flexibility on work hours</li>\n<li>Great Benefits: Health, Dental, Vision</li>\n<li>Team: Work with a fun, lively and intelligent group of individuals that are DOERS, not watchers.</li>\n</ul>\n<p>Must be great at working in small teams and have very good communications skills.</p>\n<p>Job Type: Full Time\nPay: TBD</p>\n<p>Interview Process: You will have 2 rounds of interviews and then, if selected, you\u2019ll be hired for a 1-3 month trial.</p>\n",
#    "title":"Mid-Level Programmer",
#    "url":"https://jobs.github.com/positions/016883f3-59f5-4ccc-a35a-2e89e4ad95a9",
#    "company_logo":"https://jobs.github.com/rails/active_storage/blobs/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBdUdJIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--f2c4af15f0575645ccd561a2b21a4d8b4ff30ee2/CCM%20Logo%20Final.png",
#    "company":"Convert Cold Media LLC ",
#    "id":"016883f3-59f5-4ccc-a35a-2e89e4ad95a9",
#    "company_url":"https://convertcoldmedia.com",
#    "how_to_apply":"<p>You can email your resume to <a href=\"mailto:julie@convertcoldmedia.com\">julie@convertcoldmedia.com</a>. Please include the best way to contact you. Thanks!</p>\n",
#    "location":"Austin, TX",
#    "type":"Full Time",
#    "created_at":"Fri Aug 28 17:12:26 UTC 2020"
# }