from django import template
from urllib.parse import quote_plus
register = template.Library()
import code

@register.filter
def urlify(url):
  
  if isinstance(url, dict) and len(url) > 0:
    result = ''
    for i, (k,v) in enumerate(url.items()):
      if k == "page":
        continue
      if v:
        # code.interact(local=dict(globals(),**locals()))
        if i == len(url) - 1 :
          result += "{0}={1}".format(k,quote_plus(v))
        else:
          result += "{0}={1}&".format(k,quote_plus(v))
    return result

  return quote_plus(url)








# from django import template
# from urllib.parse import quote_plus
# register = template.Library()

# @register.filter
# def urlify(url):
#   if isinstance(url, dict):
#     url = ''
#     for k,v in eurl.itmes():
#       if v:
#         url += "{0}={1}".format(k,quote_plus(v))
#     return quote_plus(url)

#   return quote_plus(url)