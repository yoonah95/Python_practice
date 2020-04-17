



import string
t = string.Template('$page:$title')
print(t.substitute({'page':2,'title':'The Best of Times'}))



t = string.Template('$page:$title')
print(t.safe_subtitute({'page':3}))

t = string.Template('$page: $title $$')
print(t.subtitute({'page':2,'title':'The Best'})



