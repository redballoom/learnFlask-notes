# -*- coding:utf-8 -*-
# @Author:🎈RedBalloon
# @Time:2022/11/2-18:40
# @File:11-请求和响应01.py


"""
请求（request）和 响应（response）
1.了解 HTTP协议
2，请求对象 - request
就是网页的请求头
request - 请求对象，封装了所有与请求相关的信息，如：请求头，请求的数据，请求的路径...
在Flask中， 请求信息被封装到request对象中

2-1.request中常用的成员对象。
    2-1-1.scheme : 获取请求方案（协议）
    2-1-2.method : 获取当前请求的请求方式
    2-1-3.request.args : 获取使用get请求方式提交的数据
    2-1-4.request.form : 获取使用post请求方式提交的数据
    2-1-5.request.values : 获取get和post请求方式提交的数据（通用）
    2-1-6.request.cookies : 获取cookies中的信息
    2-1-7.request.headers : 获取请求消息头的信息
    2-1-8.request.path : 获取请求的url地址
    2-1-9.request.files : 获取用户上传的文件


['__annotations__', '__class__', '__delattr__', '__dict__', '__dir__',
'__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__',
 '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
 '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
 '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
'_cached_json', '_get_file_stream', '_get_stream_for_parsing', '_load_form_data', '_parse_content_type',
'accept_charsets', 'accept_encodings', 'accept_languages', 'accept_mimetypes',
 'access_control_request_headers', 'access_control_request_method', 'access_route',
 'application', 'args', 'authorization', 'base_url', 'blueprint', 'blueprints', 'cache_control', 'charset', 'close',
 'content_encoding', 'content_length', 'content_md5', 'content_type', 'cookies',
 'data', 'date', 'dict_storage_class', 'encoding_errors', 'endpoint', 'environ', 'files', 'form',
 'form_data_parser_class', 'from_values', 'full_path', 'get_data', 'get_json', 'headers', 'host',
 'host_url', 'if_match', 'if_modified_since', 'if_none_match', 'if_range', 'if_unmodified_since', 'input_stream',
'is_json', 'is_multiprocess', 'is_multithread', 'is_run_once', 'is_secure', 'json', 'json_module',
'list_storage_class', 'make_form_data_parser', 'max_content_length', 'max_form_memory_size',
 'max_forwards', 'method', 'mimetype', 'mimetype_params', 'on_json_loading_failed', 'origin',
'parameter_storage_class', 'path', 'pragma', 'query_string', 'range', 'referrer', 'remote_addr', 'remote_user',
'root_path', 'root_url', 'routing_exception', 'scheme', 'script_root', 'server', 'shallow', 'stream',
'trusted_hosts', 'url', 'url_charset', 'url_root', 'url_rule', 'user_agent', 'user_agent_class', 'values',
'view_args', 'want_form_data_parsed']
"""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/request')
def rq_views():
    # print(dir(request))
    # 将request中的内容打印到终端

    # 1.获取请求方案（协议）
    scheme = request.scheme
    # 2.获取请求方式（method）
    method = request.method
    # 3获取get请求方式提交的数据
    get_args = request.args
    # 4.获取post请求方式提交的数据
    post_form = request.form
    # 5.获取任意请求方式提交的数据
    values = request.values
    return render_template('sss.html', params=locals())


if __name__ == '__main__':
    app.run(debug=True)