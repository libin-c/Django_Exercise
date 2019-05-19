



#定义中间件 :处理请求对象之前 处理请求对象之后
def simple_middleware(get_response):
    # 此处编写的代码仅在Django第一次配置和初始化的时候执行一次。
    print('init----dbug---调用两次')
    def middleware(request):
        # 此处编写的代码会在每个请求处理视图前被调用。
        print("处理请求对象之后---咻咻怪111")

        #检验ip,校验登陆
        response = get_response(request)

        # 此处编写的代码会在每个请求处理视图之后被调用。
        print("处理请求对象之后---嗅嗅怪111")

        return response

    return middleware



def simple_middleware2(get_response):
    # 此处编写的代码仅在Django第一次配置和初始化的时候执行一次。
    print('init----dbug---调用两次')
    def middleware(request):
        # 此处编写的代码会在每个请求处理视图前被调用。
        print("处理请求对象之后---皮皮怪222")

        #检验ip,校验登陆
        response = get_response(request)

        # 此处编写的代码会在每个请求处理视图之后被调用。
        print("处理请求对象之后---猪皮怪222")

        return response

    return middleware


def simple_middleware3(get_response):
    # 此处编写的代码仅在Django第一次配置和初始化的时候执行一次。
    print('init----dbug---调用两次')
    def middleware(request):
        # 此处编写的代码会在每个请求处理视图前被调用。
        print("处理请求对象之后---蔡徐坤333")

        #检验ip,校验登陆
        response = get_response(request)

        # 此处编写的代码会在每个请求处理视图之后被调用。
        print("处理请求对象之后---菜虚鲲333")

        return response

    return middleware