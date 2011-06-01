# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect

class MissingRedirect(object):
    def process_response(self, request, response):
        if response.status_code == 404:
            return HttpResponseRedirect('/')

        return response

