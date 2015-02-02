# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422858573.0773983
_enable_loop = True
_template_filename = '/usr/lib/python3.4/site-packages/nikola/data/themes/bootstrap3/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_feedlinks', 'late_load_js', 'html_headstart', 'html_navigation_links', 'html_translations', 'html_stylesheets']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        rss_link = context.get('rss_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in translations:
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        colorbox_locales = context.get('colorbox_locales', UNDEFINED)
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>\n            <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>\n            <script src="/assets/js/all.js"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/all-nocdn.js"></script>\n')
        else:
            if use_cdn:
                __M_writer('            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>\n            <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/jquery.min.js"></script>\n            <script src="/assets/js/bootstrap.min.js"></script>\n            <script src="/assets/js/moment-with-locales.min.js"></script>\n            <script src="/assets/js/fancydates.js"></script>\n')
            __M_writer('        <script src="/assets/js/jquery.colorbox-min.js"></script>\n')
        if colorbox_locales[lang]:
            __M_writer('        <script src="/assets/js/colorbox-i18n/jquery.colorbox-')
            __M_writer(str(colorbox_locales[lang]))
            __M_writer('.js"></script>\n')
        __M_writer('    ')
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        twitter_card = context.get('twitter_card', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        url_replacer = context.get('url_replacer', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        title = context.get('title', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        description = context.get('description', UNDEFINED)
        striphtml = context.get('striphtml', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html\n')
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']) or (comment_system == 'facebook'):
            __M_writer("prefix='")
            if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
                __M_writer('og: http://ogp.me/ns# ')
            if use_open_graph:
                __M_writer('article: http://ogp.me/ns/article# ')
            if comment_system == 'facebook':
                __M_writer('fb: http://ogp.me/ns/fb# ')
            __M_writer("'")
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n    <head>\n    <meta charset="utf-8">\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(str(description))
            __M_writer('">\n')
        __M_writer('    <meta name="viewport" content="width=device-width, initial-scale=1">\n    <title>')
        __M_writer(striphtml(str(title)))
        __M_writer(' | ')
        __M_writer(striphtml(str(blog_title)))
        __M_writer('</title>\n\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n')
        if permalink:
            __M_writer('      <link rel="canonical" href="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
        __M_writer('\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if prevlink:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\n')
        if nextlink:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\n')
        __M_writer('\n    ')
        __M_writer(str(mathjax_config))
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang)))
            __M_writer('"></script><![endif]-->\n')
        __M_writer('\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        navigation_links = context.get('navigation_links', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        tuple = context.get('tuple', UNDEFINED)
        rel_link = context.get('rel_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        for url, text in navigation_links[lang]:
            if isinstance(url, tuple):
                __M_writer('            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">')
                __M_writer(str(text))
                __M_writer('<b class="caret"></b></a>\n            <ul class="dropdown-menu">\n')
                for suburl, text in url:
                    if rel_link(permalink, suburl) == "#":
                        __M_writer('                    <li class="active"><a href="')
                        __M_writer(str(permalink))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('</a>\n')
                    else:
                        __M_writer('                    <li><a href="')
                        __M_writer(str(suburl))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('</a>\n')
                __M_writer('            </ul>\n')
            else:
                if rel_link(permalink, url) == "#":
                    __M_writer('                <li class="active"><a href="')
                    __M_writer(str(permalink))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a>\n')
                else:
                    __M_writer('                <li><a href="')
                    __M_writer(str(url))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        for langname in translations.keys():
            if langname != lang:
                __M_writer('            <li><a href="')
                __M_writer(str(_link("index", None, langname)))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        notes = context.get('notes', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        annotations = context.get('annotations', UNDEFINED)
        post = context.get('post', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet">\n            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
            else:
                __M_writer('            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            if use_cdn:
                __M_writer('            <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet">\n')
            else:
                __M_writer('            <link href="/assets/css/bootstrap.min.css" rel="stylesheet" type="text/css">\n')
            __M_writer('        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/colorbox.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if annotations and post and not post.meta('noannotations'):
            __M_writer('        ')
            __M_writer(str(notes.css()))
            __M_writer('\n')
        elif not annotations and post and post.meta('annotations'):
            __M_writer('        ')
            __M_writer(str(notes.css()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"15": 0, "20": 2, "21": 65, "22": 92, "23": 122, "24": 145, "25": 159, "26": 167, "32": 147, "41": 147, "42": 148, "43": 149, "44": 149, "45": 149, "46": 150, "47": 151, "48": 152, "49": 153, "50": 153, "51": 153, "52": 153, "53": 153, "54": 155, "55": 156, "56": 156, "57": 156, "63": 67, "72": 67, "73": 68, "74": 69, "75": 70, "76": 73, "77": 74, "78": 76, "79": 77, "80": 78, "81": 80, "82": 81, "83": 86, "84": 88, "85": 89, "86": 89, "87": 89, "88": 91, "89": 91, "90": 91, "96": 3, "123": 3, "124": 7, "125": 8, "126": 9, "127": 10, "128": 12, "129": 13, "130": 15, "131": 16, "132": 18, "133": 21, "134": 22, "135": 25, "136": 25, "137": 25, "138": 28, "139": 29, "140": 29, "141": 29, "142": 31, "143": 32, "144": 32, "145": 32, "146": 32, "147": 34, "148": 34, "149": 35, "150": 35, "151": 36, "152": 37, "153": 37, "154": 37, "155": 39, "156": 40, "157": 41, "158": 42, "159": 42, "160": 42, "161": 42, "162": 42, "163": 42, "164": 42, "165": 45, "166": 46, "167": 47, "168": 47, "169": 47, "170": 49, "171": 50, "172": 51, "173": 51, "174": 51, "175": 53, "176": 54, "177": 54, "178": 54, "179": 56, "180": 57, "181": 57, "182": 58, "183": 59, "184": 60, "185": 61, "186": 61, "187": 61, "188": 63, "189": 64, "190": 64, "196": 124, "206": 124, "207": 125, "208": 126, "209": 127, "210": 127, "211": 127, "212": 129, "213": 130, "214": 131, "215": 131, "216": 131, "217": 131, "218": 131, "219": 132, "220": 133, "221": 133, "222": 133, "223": 133, "224": 133, "225": 136, "226": 137, "227": 138, "228": 139, "229": 139, "230": 139, "231": 139, "232": 139, "233": 140, "234": 141, "235": 141, "236": 141, "237": 141, "238": 141, "244": 161, "252": 161, "253": 162, "254": 163, "255": 164, "256": 164, "257": 164, "258": 164, "259": 164, "260": 164, "261": 164, "267": 95, "277": 95, "278": 96, "279": 97, "280": 98, "281": 100, "282": 101, "283": 103, "284": 104, "285": 105, "286": 106, "287": 107, "288": 109, "289": 113, "290": 114, "291": 117, "292": 118, "293": 118, "294": 118, "295": 119, "296": 120, "297": 120, "298": 120, "304": 298}, "source_encoding": "utf-8", "uri": "base_helper.tmpl", "filename": "/usr/lib/python3.4/site-packages/nikola/data/themes/bootstrap3/templates/base_helper.tmpl"}
__M_END_METADATA
"""
