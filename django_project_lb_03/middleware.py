

def simple_middleware(get_response):
    # 此处编写的代码仅在Django第一次配置和初始化的时候执行一次。
    print('init 被调用')

    def middleware(request):
        # 此处编写的代码会在每个请求处理视图前被调用。
        print('before request 第一次被调用')

        response = get_response(request)

        # 此处编写的代码会在每个请求处理视图之后被调用。
        print('after response 第一次被调用')

        return response

    return middleware

def simple_middleware_2(get_response):
    # 此处编写的代码仅在Django第一次配置和初始化的时候执行一次。
    print('init 被调用')

    def middleware(request):
        # 此处编写的代码会在每个请求处理视图前被调用。
        print('before request 第二次被调用')

        response = get_response(request)

        # 此处编写的代码会在每个请求处理视图之后被调用。
        print('after response 第二次被调用')

        return response

    return middleware