import re

result = re.match(r'^weather/(?P<city>\w*)/(?P<year>\d{4})/$', "weather/beijing/2008/")

print(result.group('city'))