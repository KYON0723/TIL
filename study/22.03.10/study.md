# Create

```python
# 1
post = Post()
post.title = 'a'
post.content = 'b'
post.save()

# 2 
post = Post(title='가', content='나')
post.save()


# 3
post.objects.create(title='1', content='2')

```

> 위 3가지 방법으로 가능함
