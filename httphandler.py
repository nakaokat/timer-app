# -*- coding: utf-8 -*-
__author__ = 'nakaokataiki'

def get_htmltemplate():
    """
    レスポンスとして返すHTMLのうち、定形部分を返す。
    """
    html_body = u"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>{title}</title>
            <meta http-equiv="content-type" content="text/html;charset=utf-8">
            <link rel="stylesheet" href="css/default.css">
            <link rel="stylesheet" href="css/bootstrap.css">
            <script type="text/javascript">{script}</script>
        </head>
        <body>
        <div>
            <div class="container">
                <div class="row">
                    <div class="head">
                    <h1>{title}</h1>
                    </div>
                </div>
                <div class="row">
                    <div class ="span12">
                        <div id="timer">
                        <div id="timer-inner">
                        {body}
                        </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        </body>
    </html>"""
    return html_body