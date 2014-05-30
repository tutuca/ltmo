from asyncio import coroutine, get_event_loop
from markdown import markdown
from leaks.mdx_urlize import makeExtension as make_urlize
from leaks.mdx_video import makeExtension as make_video

def guess_mimetype(data):
    #return mimetype
    pass

@coroutine
def process_text(instance):
    instance.rendered = markdown(
        instance.description, 
        [make_urlize(), make_video(), 'codehilite']
    )

@coroutine
def create_attachment(url):
    return ''

@coroutine
def start(instance):
    print("printed from coroutine")
