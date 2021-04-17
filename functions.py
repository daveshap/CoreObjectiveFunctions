import requests
import json
from subprocess import Popen


def query_gpt3(prompt):
    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt,
        temperature=0.5,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.3,
        presence_penalty=0.3,
        stop=['<<END>>', 'CONTEXT:', 'ACTION:', 'INSTRUCTIONS:'])
    return response['choices'][0]['text']


def read_file(filename):
    with open(filename, 'r') as infile:
        text = infile.read()
    return text


def write_json(filename, data):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent=1)


def nexus_get(nexus_api='http://127.0.0.1:9999/', keyword=None, start=None, end=None, mid=None, key=None, sid=None, irt=None, ctx=None, metadata=None):
    urlquery = dict()
    if keyword:
        urlquery['keyword'] = keyword
    if start:
        urlquery['start'] = start
    if end:
        urlquery['end'] = end
    if mid:
        urlquery['mid'] = mid
    if key:
        urlquery['key'] = key
    if ctx:
        urlquery['ctx'] = ctx
    if sid:
        urlquery['sid'] = sid
    if irt:
        urlquery['irt'] = irt
    if metadata:
        urlquery['metadata'] = True
    response = requests.request(method='GET', url=nexus_api, params=urlquery)
    return response.json()


def nexus_post(payload, nexus_api='http://127.0.0.1:9999/'):
    return requests.request(method='POST', url=nexus_api, json=payload)


def message_table(message):
    result = '''<table><tr><th style="width:40px">Key</th><td style="width:200px">%s</td><td rowspan="0">%s</td></tr>
<tr><th style="width:40px">SID</th><td style="width:200px">%s</td></tr>
<tr><th style="width:40px">Time</th><td style="width:200px">%s</td></tr>
<tr><th style="width:40px">MID</th><td style="width:200px">%s</td></tr>
<tr><th style="width:40px">IRT</th><td style="width:200px">%s</td></tr>
<tr><th style="width:40px">CTX</th><td style="width:200px">%s</td></tr>
</table><br><br>'''  % (message['key'], message['msg'], message['sid'], message['time'], message['mid'], message['irt'], message['ctx'])
    return result


def service_table(services):
    keys = sorted(list(services.keys()))
    html = '<table style="width:400px"><tr><th>File</th><th style="width:70px">Status</th><th style="width:70px">Control</th></tr>\n'
    for key in keys:
        if services[key]:  # Popen object exists, status is running and control should be STOP
            status = '<font color="green">RUNNING</font>'
            button = '<a href="/microservices?service=%s&action=stop">HALT</a>' % key
        else:  # Popen doesn't exist, option is to start
            status = '<font color="red">STOPPED</font>'
            button = '<a href="/microservices?service=%s&action=start">START</a>' % key
        html += '<tr><td>%s</td><td>%s</td><td>%s</td></tr>\n' % (key, status, button)
    html += '</table>\n'
    return html


def stream_table(stream):
    html = '''<table><tr>
<th>Key</th>
<th>Message</th>
<th>SID</th>
<th>Time</th>
<th>MID</th>
<th>IRT</th>
<th>CTX</th></tr>
'''
    for message in stream:
        html += '''<tr><td nowrap>%s</td><td>%s</td><td nowrap>%s</td><td nowrap>%s</td><td nowrap>%s</td><td nowrap>%s</td><td nowrap>%s</td>
</tr>''' % (message['key'], message['msg'], message['sid'], message['time'], message['mid'], message['irt'], message['ctx'])
    html += '</table>'
    return html


def kill_service(microservices, filename):
    try:
        obj = microservices[filename]
        obj.kill()
        microservices[filename] = None
    except Exception as oops:
        print('ERROR in KILL_SERVICE:', oops)


def start_service(microservices, filename):
    try:
        obj = Popen('python %s' % filename)
        microservices[filename] = obj
    except Exception as oops:
        print('ERROR in START_SERVICE:', oops)        


#def filter_stream(stream, seen, key):
#    result = [i for i in stream if key in i['key']]
#    result = [i for i in stream if i['mid'] not in seen]
#    return result

