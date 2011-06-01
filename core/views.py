# -*- coding: utf-8 -*-

from django.http import Http404
from django.template import RequestContext

from models import Chapter, Paragraph


def render_to_response(request, template_name, context_dict={}):
    from django.shortcuts import render_to_response as _render_to_response
    context = RequestContext(request, context_dict)
    return _render_to_response(template_name, context_instance=context)


def chapter(request, chapter_id):
    try:
        chapter_id = int(chapter_id)
    except ValueError:
        chapter_id = 1

    return render_to_response(request, 'book/chapter.html', {'current_chapter': chapter_id,
                                                        'paragraphs': Paragraph.objects.filter(chapter=chapter_id),
                                                        'chapter': Chapter.objects.get(pk=chapter_id),
                                                        })


def paragraph(request, chapter_id, paragraph_id):
    try:
        chapter_id = int(chapter_id)
        paragraph_id = int(paragraph_id)
    except ValueError:
        raise Http404

    try:
        prev = Paragraph.objects.filter(pk__lt=paragraph_id).reverse()[0]
    except IndexError:
        prev = None

    try:
        next = Paragraph.objects.filter(pk__gt=paragraph_id)[0]
    except IndexError:
        next = None

    return render_to_response(request, 'book/paragraph.html',
                              {'current_chapter': chapter_id,
                               'paragraph': Paragraph.objects.get(pk=paragraph_id),
                               'prev': prev,
                               'next': next,
                              })
